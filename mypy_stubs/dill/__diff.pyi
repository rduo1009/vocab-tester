from __future__ import annotations

from typing import Any

from _typeshed import Incomplete

HAS_NUMPY: bool
getrefcount: Incomplete
memo: dict  # type: ignore
id_to_obj: dict  # type: ignore
builtins_types: set[tuple[type, ...]]
dont_memo: set  # type: ignore

def get_attrs(obj: object) -> dict[str, Any]: ...
def get_seq(
    obj: object, cache: dict[type, bool] = ...
) -> object | list | None: ...  # type: ignore
def memorise(obj: object, force: bool = False) -> None: ...
def release_gone() -> None: ...
def whats_changed(
    obj: object,
    seen: Incomplete | None = None,
    simple: bool = False,
    first: bool = True,
) -> Incomplete: ...
def has_changed(*args: Incomplete, **kwds: Incomplete) -> Incomplete: ...

__import__ = __import__
