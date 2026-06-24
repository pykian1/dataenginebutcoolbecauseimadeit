from minidaft.plan import Source, Filter, Project, Limit
from minidaft.io.parquet import ParquetScan, Pushdowns
from minidaft.expressions import col, lit, add, eq, and_, Lit, FnCall
from minidaft.optimizer import (
    optimize,
    predicate_pushdown,
    projection_pushdown,
    filter_combine,
    const_fold,
)


def test_predicate_pushdown_through_project():
    # Filter(Project(Source, [x, y]), x > 3) -> Project(Filter(Source, x > 3), [x, y])
    source = Source(path="orders.parquet")
    proj = Project(children=[source], columns=[col("x"), col("y")])
    pred = eq(col("x"), lit(3))
    plan = Filter(children=[proj], predicate=pred)

    out = predicate_pushdown(plan)

    assert isinstance(out, Project)
    assert out.columns == [col("x"), col("y")]
    inner = out.children[0]
    assert isinstance(inner, Filter)
    assert inner.predicate == pred
    assert isinstance(inner.children[0], Source)


def test_filter_combine():
    # Filter(Filter(Source, p), q) -> Filter(Source, p AND q)
    source = Source(path="orders.parquet")
    p = eq(col("x"), lit(1))
    q = eq(col("y"), lit(2))
    plan = Filter(children=[Filter(children=[source], predicate=p)], predicate=q)

    out = filter_combine(plan)

    assert isinstance(out, Filter)
    assert out.predicate == and_(p, q)
    assert isinstance(out.children[0], Source)


def test_const_fold():
    # Lit(2) + Lit(3) -> Lit(5), folded inside a Project's columns.
    plan = Project(children=[Source(path="p")], columns=[add(lit(2), lit(3))])

    out = const_fold(plan)

    assert out.columns == [Lit(5)]


def test_projection_pushdown_into_scan():
    scan = ParquetScan(path="p.parquet", pushdowns=Pushdowns())
    plan = Project(children=[scan], columns=[col("x"), col("y")])

    out = projection_pushdown(plan)

    assert isinstance(out, Project)
    new_scan = out.children[0]
    assert isinstance(new_scan, ParquetScan)
    assert new_scan.pushdowns.columns == ["x", "y"]
    # original scan untouched (rules return new trees)
    assert scan.pushdowns.columns is None


def test_optimize_reaches_fixed_point():
    # Two stacked filters above a project above a scan; run the whole rule set.
    scan = ParquetScan(path="p.parquet", pushdowns=Pushdowns())
    proj = Project(children=[scan], columns=[col("x")])
    p = eq(col("x"), lit(1))
    q = eq(col("x"), lit(2))
    plan = Filter(
        children=[Filter(children=[proj], predicate=p)],
        predicate=q,
    )

    # projection_pushdown first: it only fires while the Project sits directly
    # over the scan, before predicate_pushdown slides the filters in between.
    rules = [projection_pushdown, predicate_pushdown, filter_combine, const_fold]
    out = optimize(plan, rules)

    # Filters combined and pushed below the projection.
    assert isinstance(out, Project)
    filt = out.children[0]
    assert isinstance(filt, Filter)
    assert filt.predicate == and_(p, q)
    new_scan = filt.children[0]
    assert isinstance(new_scan, ParquetScan)
    assert new_scan.pushdowns.columns == ["x"]

    # optimize is idempotent: running again changes nothing.
    assert optimize(out, rules) == out
