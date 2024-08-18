from typing import Callable, Dict, MappingView, Type

from _typeshed import Incomplete

from .logger import trace as trace

__all__ = [
    "baditems",
    "badobjects",
    "badtypes",
    "code",
    "errors",
    "freevars",
    "getmodule",
    "globalvars",
    "nestedcode",
    "nestedglobals",
    "outermost",
    "referredglobals",
    "referrednested",
    "trace",
    "varnames",
]

def getmodule(
    object: object, _filename: Incomplete | None = None, force: bool = False
) -> Incomplete: ...
def outermost(func: Callable) -> Incomplete: ...  # type: ignore
def nestedcode(func: Callable, recurse: bool = True) -> list: ...  # type: ignore
def code(func: Callable) -> Incomplete: ...  # type: ignore
def referrednested(func: Callable, recurse: bool = True) -> list: ...  # type: ignore
def freevars(func: Callable) -> dict: ...  # type: ignore
def nestedglobals(func: Callable, recurse: bool = True) -> list: ...  # type: ignore
def referredglobals(
    func: Callable,  # type: ignore
    recurse: bool = True,
    builtin: bool = False,
) -> MappingView: ...
def globalvars(
    func: Callable,  # type: ignore
    recurse: bool = ...,
    builtin: bool = ...,
) -> Dict[str, Type[KeyError]]: ...
def varnames(func: Callable) -> tuple: ...  # type: ignore
def baditems(obj: object, exact: bool = False, safe: bool = False) -> list: ...  # type: ignore
def badobjects(
    obj: object, depth: int = 0, exact: bool = False, safe: bool = False
) -> dict: ...  # type: ignore
def badtypes(
    obj: object, depth: int = 0, exact: bool = False, safe: bool = False
) -> dict: ...  # type: ignore
def errors(
    obj: object, depth: int = 0, exact: bool = False, safe: bool = False
) -> Incomplete: ...
