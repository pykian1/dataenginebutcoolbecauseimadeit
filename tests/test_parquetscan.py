import pyarrow as pa
import pyarrow.parquet as pq
import pytest
from minidaft.io.parquet import ParquetScan, Pushdowns

def make_fixture(tmp_path):
    #create parquet file w/ 10 row groups; rg_i contains row where x = [i*100, ...., i*100 + 99]

    path = tmp_path / "test.parquet"
    xs = list[int](range(1000))
    ys = [v* 2.0 for v in xs]
    table = pa.table({"x": xs, "y": ys})
    pq.write_table(table, path, row_group_size=100)
    return str(path)


def test_predicate_pushdown_row_count(tmp_path):
    #pred: x>= 300 and x<400 => rg_3 
    path = make_fixture(tmp_path) 
    scan = ParquetScan(
        path=path, 
        pushdowns=Pushdowns(predicate= lambda min, max: max>=300 and min<400, predicate_col="x"))

    batches = list(scan.execute())
    total_rows = sum(b.num_rows for b in batches)
    assert total_rows == 100 #rg_3
def test_predicate_pushdown_counter(tmp_path):
    path = make_fixture(tmp_path)
    scan = ParquetScan(path=path,
    pushdowns=Pushdowns(predicate= lambda min, max: max>=300 and min<400, predicate_col="x"))
    _ = list(scan.execute())

    assert scan._row_groups_read == 1 #rg_3

def test_projection_pushdown_schema(tmp_path):
    path = make_fixture(tmp_path)
    scan = ParquetScan(
        path=path,
        pushdowns=Pushdowns(columns=["x"]))
    batches = list(scan.execute())
    assert len(batches) == 10
    assert batches[0].schema.names == ["x"]
    assert batches[0].schema.field(0).name == "x"




