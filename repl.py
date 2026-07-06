from minieng.plan import Source, Filter, Project, Limit
from minieng.expressions import col, lit, FnCall


source = Source(path="orders.parquet")
filt = Filter(children=[source], predicate=FnCall("gt", (col("amount"), lit(100))))
proj = Project(children=[filt], columns=[col("customer_id")])
plan = Limit(children=[proj], n=10)

print(plan.explain())


