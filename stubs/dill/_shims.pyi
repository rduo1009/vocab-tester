from __future__ import annotations

from typing import Any, Callable

from _typeshed import Incomplete

class Reduce:
    reduction: tuple[Any, ...]
    def __new__(
        cls: object, *reduction: tuple[Any, ...], **kwargs: dict[str, bool]
    ) -> "Reduce": ...
    def __copy__(self) -> "Reduce": ...
    def __deepcopy__(self, memo: Any) -> "Reduce": ...
    def __reduce__(self) -> tuple[Any, ...]: ...
    def __reduce_ex__(self, protocol: Any) -> tuple[Any, ...]: ...

class _CallableReduce(Reduce):
    def __call__(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...

def Getattr(
    object: object, name: str, default: Incomplete = ...
) -> Reduce: ...
def move_to(
    module: Incomplete, name: Incomplete | None = None
) -> Callable: ...  # type: ignore
def register_shim(name: Incomplete, default: Incomplete) -> Reduce: ...