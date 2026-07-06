"""Day 5 --- the DataFrame facade.

A builder-pattern front end. Each of ``where`` / ``select`` / ``limit`` returns a
*new* DataFrame with one more node stacked on top of the LogicalPlan --- nothing
runs yet. ``collect()`` is the only method that does work: it optimizes the plan,
compiles it to a physical executor tree, pulls every batch, and returns a Table.

    DataFrame(parquet).where(price > 100).select(name).limit(10).collect()
"""

from typing import List, Optional

import pyarrow as pa
import pyarrow.parquet  # noqa: F401  (registers pa.parquet used by ParquetScan)

from minieng.expressions import Expr, Col
from minieng.plan import LogicalPlan, Filter, Project, Limit
from minieng.io.parquet import ParquetScan, Pushdowns
from minieng.optimizer import (
    optimize,
    projection_pushdown,
    predicate_pushdown,
    filter_combine,
    const_fold,
)
from minieng.exec.pull import build_exec, find_scan

# projection_pushdown runs first: it only fires while a Project sits directly
# over the scan, before predicate_pushdown can slide a Filter in between.
_RULES = [projection_pushdown, predicate_pushdown, filter_combine, const_fold]


class DataFrame:
    def __init__(self, source, plan: Optional[LogicalPlan] = None):
        if plan is not None:
            self._plan = plan
        elif isinstance(source, LogicalPlan):
            self._plan = source
        else:  # a path string -> a Parquet scan leaf
            self._plan = ParquetScan(path=str(source), pushdowns=Pushdowns())
        # Populated by collect(), for inspection (.explain_physical(), counters).
        self._physical = None

    # --- builder methods: each returns a new DataFrame -------------------

    def where(self, predicate: Expr) -> "DataFrame":
        return DataFrame(None, Filter(children=[self._plan], predicate=predicate))

    def select(self, *exprs) -> "DataFrame":
        columns: List[Expr] = list(exprs)
        return DataFrame(None, Project(children=[self._plan], columns=columns))

    def limit(self, n: int) -> "DataFrame":
        return DataFrame(None, Limit(children=[self._plan], n=n))

    # --- execution ------------------------------------------------------

    def collect(self) -> pa.Table:
        """Optimize, compile to executors, pull all batches, return a Table.

        Rebuilds the executor tree on every call, since generators are one-shot.
        """
        optimized = optimize(self._plan, _RULES)
        root = build_exec(optimized)
        self._physical = root

        root.open()
        try:
            batches = list(root)
        finally:
            root.close()

        if not batches:
            return pa.table({})
        return pa.Table.from_batches(batches)

    # --- introspection --------------------------------------------------

    def explain(self) -> str:
        """The logical plan (what to do)."""
        return self._plan.explain()

    def explain_physical(self) -> str:
        """The physical executor tree (how it will run). Requires a collect() first."""
        if self._physical is None:
            self._physical = build_exec(optimize(self._plan, _RULES))
        return self._physical.explain()

    def _scan_exec(self):
        """The leaf ScanExec of the last collect() --- exposes the read counter."""
        return find_scan(self._physical) if self._physical is not None else None
