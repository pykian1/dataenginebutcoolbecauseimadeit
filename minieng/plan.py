from dataclasses import dataclass, field
from .expressions import Expr, Col, Lit, FnCall
from typing import Optional, List, Tuple


@dataclass
class LogicalPlan:
    children: List["LogicalPlan"] = field(default_factory=list)

    def explain(self, depth: int = 0) -> str:
        indent = "  " * depth
        line = f"{indent}{self._describe()}"
        child_lines = [c.explain(depth + 1) for c in self.children]
        return "\n".join([line] + child_lines)
    
    def _describe(self) -> str: 
        return self.__class__.__name__


@dataclass
class Source(LogicalPlan):
    path: str = ""
    def _describe(self):
        return f"Source(path={self.path!r})"

@dataclass
class Filter(LogicalPlan):
    predicate: Expr = None
    def _describe(self): 
        return f"Filter(predicate={self.predicate!r})"


@dataclass
class Project(LogicalPlan):
    columns: List[Expr] = field(default_factory=list)
    def _describe(self): 
        return f"Project(columns={self.columns})"

@dataclass
class Limit(LogicalPlan):
    n: int = 0
    def _describe(self): 
        return f"Limit(n={self.n})"




"""
plan ──────► Limit(n=10, children=[─┐])
                                      │
   proj ─────► Project(columns=[...], children=[─┐])
                  ▲                              │
                  └──────────────────────────────┘
                            (same object)
   filt ─────► Filter(predicate=..., children=[─┐])
                  ▲                             │
                  └─────────────────────────────┘
   source ───► Source(path="orders.parquet", children=[])
                  ▲                          
                  └─── (also reachable via filt.children[0])
                  
                  
"""