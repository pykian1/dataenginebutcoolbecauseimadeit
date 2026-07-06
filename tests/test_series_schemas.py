import pytest

import pandas as pd
import pyarrow as pa
from minieng.series import Series
from minieng.schema import Schema
from minieng.dtypes import LogicalType


def test_roundtrip_pandas():
    df = pd.DataFrame({
        "name": ["Arshiya", "Kian", "Ali", "Aidan"],
        "age": [22, 21, 22, 22],
        "is_student": [True, True, True, False],
        "bluff_frequency": [.1, .5, .1, .1],
        "merged_range": [True, False, True, True]
    })

    table = pa.Table.from_pandas(df)
    series_list = [ # Hit error, pandas returns large string; will loose validation
        Series(name="name", dtype=LogicalType.STRING, array=table.column("name").combine_chunks()),
        Series(name="age", dtype=LogicalType.INT64, array=table.column("age").combine_chunks()),
        Series(name="is_student", dtype=LogicalType.BOOL, array=table.column("is_student").combine_chunks()),
        Series(name="bluff_frequency", dtype=LogicalType.FLOAT64, array=table.column("bluff_frequency").combine_chunks()),
        Series(name="merged_range", dtype=LogicalType.BOOL, array=table.column("merged_range").combine_chunks())
    
    ]
    
    result = pa.table({s.name: s.array for s in series_list}).to_pandas()
    pd.testing.assert_frame_equal(result, df)

    def test_wrong_type_raises():

        string_array = pa.array(["a", "b", "c"], type=pa.string())

        with pytest.raises(TypeError):
            Series(name="oops", dtype=LogicalType.INT64, array=string_array)

    def test_schema_equality():
        s1 = Schema(fields=(("name", LogicalType.STRING), ("age", LogicalType.INT64)))
        s2 = Schema(fields=(("name", LogicalType.STRING), ("age", LogicalType.INT64)))

        assert s1 == s2, s1 is not s2
