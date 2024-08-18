from __future__ import annotations

from ._dill import _locate_object as at  # type: ignore
from ._dill import _proxy_helper as reference  # type: ignore

__all__ = ["parent", "reference", "at", "parents", "children"]

def parent(obj, objtype, ignore=()): ...
def parents(obj, objtype, depth: int = 1, ignore=()): ...
def children(obj, objtype, depth: int = 1, ignore=()): ...

refobject = at
