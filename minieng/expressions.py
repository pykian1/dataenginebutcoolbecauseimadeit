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
def sub(a, b): return FnCall("sub", (a, b))
def mul(a, b): return FnCall("mul", (a, b))
def eq(a, b): return FnCall("eq", (a, b))
def gt(a, b): return FnCall("gt", (a, b))
def lt(a, b): return FnCall("lt", (a, b))
def ge(a, b): return FnCall("ge", (a, b))
def le(a, b): return FnCall("le", (a, b))
def and_(a, b): return FnCall("and", (a, b))
def or_(a, b): return FnCall("or", (a, b))


