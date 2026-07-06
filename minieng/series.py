from dataclasses import dataclass
import pyarrow as pa
from minieng.dtypes import LogicalType
#mapping from dtype -> arrow 
LOGICAL_TO_ARROW = {
    LogicalType.INT64: pa.int64(),
    LogicalType.FLOAT64: pa.float64(),
    LogicalType.STRING: {pa.string(), pa.large_string()}, # changed for test validation, pandas returns large_string
    LogicalType.BOOL: pa.bool_(),
    LogicalType.BINARY: {pa.binary(), pa.large_binary()} 
}

@dataclass
class Series:
    name: str
    dtype: LogicalType
    array: pa.array

    def __post_init__(self): # validation 
        expected = LOGICAL_TO_ARROW[self.dtype]
        if isinstance(expected, set):
            if self.array.type not in expected:
                raise TypeError(f"Array type {self.array.type} doesnt match LogicalType")
        elif expected != self.array.type:
            raise TypeError(f"Array type {self.array.type} doesnt match LogicalType") 
    
    def __len__(self) -> int: # number of elements in array
        return len(self.array)
    