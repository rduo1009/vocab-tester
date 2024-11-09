from __future__ import annotations

from typing import Any

from ._dill import _locate_object as at  # type: ignore
from ._dill import _proxy_helper as reference  # type: ignore

__all__ = ["parent", "reference", "at", "parents", "children"]

def parent(obj: object, objtype: type, ignore: tuple = ()) -> Any: ...  # type: ignore
def parents(
    obj: object,
    objtype: type,
    depth: int = 1,
    ignore: tuple = (),  # type: ignore
) -> Any: ...
def children(
    obj: object,
    objtype: type,
    depth: int = 1,
    ignore: tuple = (),  # type: ignore
) -> Any: ...

refobject = at
