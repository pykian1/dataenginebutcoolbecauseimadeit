from dataclasses import replace
from typing import Callable, List

from minidaft.plan import LogicalPlan, Filter, Project
from minidaft.io.parquet import ParquetScan
from minidaft.expressions import Expr, Col, Lit, FnCall, and_

Rule = Callable[[LogicalPlan], LogicalPlan]


def optimize(plan: LogicalPlan, rules: List[Rule]) -> LogicalPlan:
    """Apply rules until a fixed point. Returns a *new* plan tree;
    never mutates in place."""
    current = plan
    while True:
        new = current
        for rule in rules:
            new = rule(new)
        if new == current:
            return new
        current = new


def _map_children(node: LogicalPlan, fn: Rule) -> LogicalPlan:
    """Apply fn to every child, returning a new node only if something changed.
    Walks children first so rules can be written bottom-up."""
    if not node.children:
        return node
    new_children = [fn(c) for c in node.children]
    if new_children == node.children:
        return node
    return replace(node, children=new_children)


def predicate_pushdown(plan: LogicalPlan) -> LogicalPlan:
    """Push Filter below Project when safe.

    Filter(Project(child, cols), p) -> Project(Filter(child, p), cols)
    """
    plan = _map_children(plan, predicate_pushdown)
    if (
        isinstance(plan, Filter)
        and len(plan.children) == 1
        and isinstance(plan.children[0], Project)
    ):
        proj = plan.children[0]
        # Day 6: refuse to push through a Project containing an expensive expr.
        if any(_is_expensive(c) for c in proj.columns):
            return plan
        new_filter = replace(plan, children=proj.children)
        return replace(proj, children=[new_filter])
    return plan


def projection_pushdown(plan: LogicalPlan) -> LogicalPlan:
    """Push the column list of a Project down into a ParquetScan's pushdowns."""
    plan = _map_children(plan, projection_pushdown)
    if (
        isinstance(plan, Project)
        and len(plan.children) == 1
        and isinstance(plan.children[0], ParquetScan)
    ):
        scan = plan.children[0]
        col_names = [c.value for c in plan.columns if isinstance(c, Col)]
        new_pushdowns = replace(scan.pushdowns, columns=col_names)
        new_scan = replace(scan, pushdowns=new_pushdowns)
        return replace(plan, children=[new_scan])
    return plan


def filter_combine(plan: LogicalPlan) -> LogicalPlan:
    """Filter(Filter(x, p), q) -> Filter(x, p AND q)."""
    plan = _map_children(plan, filter_combine)
    if (
        isinstance(plan, Filter)
        and len(plan.children) == 1
        and isinstance(plan.children[0], Filter)
    ):
        inner = plan.children[0]
        combined = and_(inner.predicate, plan.predicate)
        return replace(plan, predicate=combined, children=inner.children)
    return plan


def const_fold(plan: LogicalPlan) -> LogicalPlan:
    """Fold constant expressions inside a plan: Lit(2) + Lit(3) -> Lit(5)."""
    plan = _map_children(plan, const_fold)
    if isinstance(plan, Filter) and plan.predicate is not None:
        return replace(plan, predicate=_fold_expr(plan.predicate))
    if isinstance(plan, Project):
        return replace(plan, columns=[_fold_expr(c) for c in plan.columns])
    return plan


# --- expression helpers -------------------------------------------------

# Pure binary ops we can evaluate at plan time when both operands are literals.
_FOLDABLE = {
    "add": lambda a, b: a + b,
    "eq": lambda a, b: a == b,
    "and": lambda a, b: a and b,
}


def _fold_expr(expr: Expr) -> Expr:
    """Recursively fold an expression tree's constant subtrees."""
    if isinstance(expr, FnCall):
        args = tuple(_fold_expr(a) for a in expr.args)
        if (
            not expr.is_expensive
            and expr.name in _FOLDABLE
            and all(isinstance(a, Lit) for a in args)
        ):
            return Lit(_FOLDABLE[expr.name](*[a.value for a in args]))
        return FnCall(expr.name, args, expr.is_expensive)
    return expr


def _is_expensive(expr: Expr) -> bool:
    """True if any node in the expression tree is flagged is_expensive."""
    if isinstance(expr, FnCall):
        return expr.is_expensive or any(_is_expensive(a) for a in expr.args)
    return False
