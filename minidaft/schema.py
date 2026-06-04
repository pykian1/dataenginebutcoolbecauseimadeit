from dataclasses import dataclass
from typing import Tuple
from minidaft.dtypes import LogicalType


@dataclass(frozen=True)
class Schema:
    fields: Tuple[Tuple[str,[LogicalType], ...]] 

