from minidaft.plan import Source, Filter, Project, Limit
from minidaft.expressions import col, lit, FnCall

def test_plan():
    source = Source(path="orders.parquet")
    filt = Filter(children=[source], predicate=FnCall("test", (col("amount"), lit(100))))
    proj = Project(children=[filt], columns=[col("a")])
    plan = Limit(children=[proj], n=10)

    output = plan.explain()
    

    assert "Limit(n=10)" in output
    assert "Project" in output
    assert "Filter" in output
    assert "Source(path='orders.parquet')" in output
    

    assert output.index("Limit") < output.index("Project")
    assert output.index("Project") < output.index("Filter")
    assert output.index("Filter") < output.index("Source")