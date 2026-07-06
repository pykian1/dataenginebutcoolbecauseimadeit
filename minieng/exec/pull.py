"""Day 5 --- Pull-based Volcano executor.

Every operator is an iterator of ``pa.RecordBatch``. The root of the tree is
pulled (via ``for batch in exec``); each operator in turn pulls from its child.
Nothing is computed until the consumer asks --- this is the "coffee shop with one
barista" model (Graefe 1994, the Volcano iterator).

    consumer  --pull-->  Limit  --pull-->  Project  --pull-->  Filter  --pull-->  Scan
      (control flow goes DOWN the tree; data batches flow back UP)
"""

from typing import Iterator, List, Optional

import pyarrow as pa
import pyarrow.compute as pc

from minieng.expressions import Expr, Col, Lit, FnCall
from minieng.plan import LogicalPlan, Filter, Project, Limit
from minieng.io.parquet import ParquetScan


# --- expression evaluation ------------------------------------------------
#
# An expression is a little tree (Col / Lit / FnCall). To run it we walk the
# tree and, at each node, produce a pyarrow value for the given batch:
#   Col   -> that column's array out of the batch
#   Lit   -> a constant scalar
#   FnCall-> apply the matching pyarrow.compute function to its evaluated args
# A predicate is just an expression that happens to evaluate to a boolean array.

_FUNCS = {
    "add": pc.add,
    "sub": pc.subtract,
    "mul": pc.multiply,
    "eq": pc.equal,
    "gt": pc.greater,
    "lt": pc.less,
    "ge": pc.greater_equal,
    "le": pc.less_equal,
    "and": pc.and_,
    "or": pc.or_,
}


def eval_expr(expr: Expr, batch: pa.RecordBatch):
    """Recursively evaluate one expression against a batch -> pa.Array/Scalar."""
    if isinstance(expr, Col):
        return batch.column(batch.schema.get_field_index(expr.value))
    if isinstance(expr, Lit):
        return pa.scalar(expr.value)
    if isinstance(expr, FnCall):
        fn = _FUNCS.get(expr.name)
        if fn is None:
            raise NotImplementedError(f"no executor for function {expr.name!r}")
        args = [eval_expr(a, batch) for a in expr.args]
        return fn(*args)
    raise TypeError(f"cannot evaluate expression node: {expr!r}")


def _as_array(value, length: int) -> pa.Array:
    """A Project can select a bare literal; broadcast a scalar to a full column."""
    if isinstance(value, pa.Scalar):
        return pa.array([value.as_py()] * length, type=value.type)
    if isinstance(value, pa.ChunkedArray):
        return value.combine_chunks()
    return value


def _output_name(expr: Expr, idx: int) -> str:
    if isinstance(expr, Col):
        return expr.value
    return f"col{idx}"


# --- operators ------------------------------------------------------------


class Executor:
    """Volcano-style operator. Each one is an iterator of RecordBatch.

    open()/close() walk the tree so leaves can grab (and later release) file
    handles; __iter__ is where the actual pulling happens.
    """

    child: Optional["Executor"] = None

    def open(self) -> None:
        if self.child is not None:
            self.child.open()

    def close(self) -> None:
        if self.child is not None:
            self.child.close()

    def __iter__(self) -> Iterator[pa.RecordBatch]:
        raise NotImplementedError

    # Mirror of LogicalPlan.explain(): print the *physical* executor tree.
    def explain(self, depth: int = 0) -> str:
        indent = "  " * depth
        line = f"{indent}{self._describe()}"
        child_lines = [self.child.explain(depth + 1)] if self.child is not None else []
        return "\n".join([line] + child_lines)

    def _describe(self) -> str:
        return self.__class__.__name__


class ScanExec(Executor):
    """Leaf operator: streams RecordBatches straight out of a ParquetScan.

    ParquetScan already knows how to skip row groups / columns / stop at a limit
    (the Day 3 pushdowns), so the executor just forwards its batches.
    """

    def __init__(self, scan: ParquetScan):
        self.scan = scan

    def __iter__(self) -> Iterator[pa.RecordBatch]:
        yield from self.scan.execute()

    def _describe(self) -> str:
        return f"ScanExec(path={self.scan.path!r})"


class FilterExec(Executor):
    """Wraps a child; yields each batch with the predicate applied (rows dropped)."""

    def __init__(self, child: Executor, predicate: Expr):
        self.child = child
        self.predicate = predicate

    def __iter__(self) -> Iterator[pa.RecordBatch]:
        for batch in self.child:
            mask = eval_expr(self.predicate, batch)
            out = pc.filter(batch, mask)
            if out.num_rows:
                yield out

    def _describe(self) -> str:
        return f"FilterExec(predicate={self.predicate!r})"


class ProjectExec(Executor):
    """Wraps a child; yields batches containing only the projected expressions."""

    def __init__(self, child: Executor, columns: List[Expr]):
        self.child = child
        self.columns = columns

    def __iter__(self) -> Iterator[pa.RecordBatch]:
        for batch in self.child:
            arrays = [
                _as_array(eval_expr(c, batch), batch.num_rows) for c in self.columns
            ]
            names = [_output_name(c, i) for i, c in enumerate(self.columns)]
            yield pa.RecordBatch.from_arrays(arrays, names=names)

    def _describe(self) -> str:
        return f"ProjectExec(columns={self.columns})"


class LimitExec(Executor):
    """Wraps a child; yields at most n rows total, then stops pulling.

    Because it simply *stops iterating* once it has n rows, the child's generator
    is never resumed --- so a Scan below it never reads the rest of the file.
    This is why Limit is efficient in the pull model with no special rule.
    """

    def __init__(self, child: Executor, n: int):
        self.child = child
        self.n = n

    def __iter__(self) -> Iterator[pa.RecordBatch]:
        if self.n <= 0:
            return
        emitted = 0
        for batch in self.child:
            remaining = self.n - emitted
            # Stop the instant this batch fills the quota: yield the slice and
            # return WITHOUT looping back to pull another batch from the child.
            # (Looping first would wake the scan for one extra row group.)
            if batch.num_rows >= remaining:
                yield batch.slice(0, remaining)
                return
            emitted += batch.num_rows
            yield batch

    def _describe(self) -> str:
        return f"LimitExec(n={self.n})"


# --- logical plan -> physical executor tree -------------------------------


def build_exec(node: LogicalPlan) -> Executor:
    """Translate an (optimized) LogicalPlan into a physical executor tree."""
    if isinstance(node, ParquetScan):
        return ScanExec(node)
    if isinstance(node, Filter):
        return FilterExec(build_exec(node.children[0]), node.predicate)
    if isinstance(node, Project):
        return ProjectExec(build_exec(node.children[0]), node.columns)
    if isinstance(node, Limit):
        return LimitExec(build_exec(node.children[0]), node.n)
    raise NotImplementedError(f"no executor for plan node {type(node).__name__}")


def find_scan(exec_node: Executor) -> Optional[ScanExec]:
    """Walk down to the leaf ScanExec (handy for inspecting the read counter)."""
    node: Optional[Executor] = exec_node
    while node is not None:
        if isinstance(node, ScanExec):
            return node
        node = node.child
    return None
