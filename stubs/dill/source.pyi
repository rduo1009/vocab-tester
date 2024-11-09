from __future__ import annotations

from typing import Any, Callable, List, Tuple

from _typeshed import Incomplete

__all__ = [
    "findsource",
    "getsourcelines",
    "getsource",
    "indent",
    "outdent",
    "_wrap",
    "dumpsource",
    "getname",
    "_namespace",
    "getimport",
    "_importable",
    "importable",
    "isdynamic",
    "isfrommain",
]

def isfrommain(obj: Any) -> bool: ...
def isdynamic(obj: Any) -> bool: ...
def findsource(object: Any) -> Tuple[List[str], int]: ...
def getsourcelines(
    object: Any, lstrip: bool = False, enclosing: bool = False
) -> Tuple[List[str], int]: ...
def getsource(
    object: Any,
    alias: str = "",
    lstrip: bool = False,
    enclosing: bool = False,
    force: bool = False,
    builtin: bool = False,
) -> str: ...
def indent(code: str, spaces: int = 4) -> str: ...
def outdent(
    code: str, spaces: Incomplete | None = None, all: bool = True
) -> str: ...
def _wrap(f: Callable) -> Callable: ...  # type: ignore
def dumpsource(
    object: Any, alias: str = "", new: bool = False, enclose: bool = True
) -> str: ...
def getname(obj: Any, force: bool = False, fqn: bool = False) -> str: ...
def _namespace(obj: Any) -> str: ...
def getimport(
    obj: Any,
    alias: str = "",
    verify: bool = True,
    builtin: bool = False,
    enclosing: bool = False,
) -> str: ...
def _importable(
    obj: Any,
    alias: str = "",
    source: Incomplete | None = None,
    enclosing: bool = False,
    force: bool = True,
    builtin: bool = True,
    lstrip: bool = True,
) -> str: ...
def importable(
    obj: Any,
    alias: str = "",
    source: Incomplete | None = None,
    builtin: bool = True,
) -> str: ...

# getblocks_from_history = getblocks
