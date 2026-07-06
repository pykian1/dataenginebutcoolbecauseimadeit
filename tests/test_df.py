import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.compute as pc

from minieng.dataframe import DataFrame
from minieng.expressions import col, lit, gt


def make_fixture(tmp_path):
    # 1000 rows, 10 row groups of 100. price = 0..999, name = "name_i".
    path = tmp_path / "lineitem.parquet"
    prices = list(range(1000))
    names = [f"name_{i}" for i in prices]
    table = pa.table({"price": prices, "name": names})
    pq.write_table(table, path, row_group_size=100)
    return str(path)


def test_end_to_end_returns_10_rows(tmp_path):
    # DataFrame(parquet).where(price > 100).select(name).limit(10).collect()
    path = make_fixture(tmp_path)
    result = (
        DataFrame(path)
        .where(gt(col("price"), lit(100)))
        .select(col("name"))
        .limit(10)
        .collect()
    )

    assert result.num_rows == 10
    assert result.schema.names == ["name"]
    # price > 100 means the first surviving row is price == 101 -> "name_101".
    assert result.column("name").to_pylist() == [f"name_{i}" for i in range(101, 111)]


def test_limit_reads_early(tmp_path):
    # A counter on the Source proves we did not read the entire file.
    path = make_fixture(tmp_path)
    df = (
        DataFrame(path)
        .where(gt(col("price"), lit(100)))
        .select(col("name"))
        .limit(10)
    )
    df.collect()

    scan = df._scan_exec()
    assert scan is not None
    # Only row groups 0 (all filtered) and 1 (supplies the 10 rows) get touched.
    assert scan.scan._row_groups_read < 10
    assert scan.scan._row_groups_read == 2


def test_filter_matches_pyarrow_reference(tmp_path):
    path = make_fixture(tmp_path)

    result = DataFrame(path).where(gt(col("price"), lit(100))).collect()

    # pyarrow-only reference: read the whole table and filter with compute.
    ref = pq.read_table(path)
    ref = ref.filter(pc.greater(ref.column("price"), pa.scalar(100)))

    assert result.num_rows == ref.num_rows
    assert result.column("price").to_pylist() == ref.column("price").to_pylist()
    assert result.column("name").to_pylist() == ref.column("name").to_pylist()
