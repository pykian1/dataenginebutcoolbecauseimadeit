from dataclasses import dataclass
from typing import Any, List

@dataclass(frozen=True)
class Expr: pass
@dataclass(frozen=True)
class Col(Expr): 
    value: Any
@dataclass(frozen=True)
class Lit(Expr):
    value: Any
@dataclass(frozen=True)
class FnCall(Expr):
    name: str
    args: tuple
    is_expensive: bool = False

def col(n): return Col(n)
def lit(v): return Lit(v)
def add(a, b): return FnCall("add", (a, b))
def eq(a, b): return FnCall("eq", (a, b))
def and_(a, b): return FnCall("and", (a, b))


