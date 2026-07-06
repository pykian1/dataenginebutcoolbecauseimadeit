import pyarrow as pa
from dataclasses import dataclass, field
from typing import Optional, Callable, List, Iterator
from minieng.plan import LogicalPlan


@dataclass(frozen=True)
class Pushdowns:

    predicate: Optional[Callable] = None #(min,max) -> bool
    columns: Optional[List[str]] = None #list of columns to read (None=All)
    limit: Optional[int] = None #max # of rows to read (None=All)
    predicate_col: Optional[str] = None #column to apply predicate to (None=All)

@dataclass
class ParquetScan(LogicalPlan):
    path: str = ""
    pushdowns: Pushdowns = field(default_factory=Pushdowns)
    _row_groups_read: int = field(default=0, repr=False)

    def execute(self) -> Iterator[pa.RecordBatch]:
        pf = pa.parquet.ParquetFile(self.path)
        md = pf.metadata
        emitted = 0 #of rowss emitted 

        for i in range(md.num_row_groups):
            if self.pushdowns.predicate and self.pushdowns.predicate_col:
                col_idx = pf.schema_arrow.get_field_index(self.pushdowns.predicate_col)
                stats = md.row_group(i).column(col_idx).statistics
                if stats and stats.has_min_max:
                    if not self.pushdowns.predicate(stats.min, stats.max):
                        continue

            table = pf.read_row_group(i, columns=self.pushdowns.columns)
            self._row_groups_read += 1
            for b in table.to_batches():
                if self.pushdowns.limit is not None:
                    remaining = self.pushdowns.limit - emitted
                    if remaining <= 0:
                        return
                    if b.num_rows > remaining:
                        b = b.slice(0, remaining)
                emitted += b.num_rows
                yield b

        