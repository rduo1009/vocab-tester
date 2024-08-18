from _typeshed import Incomplete

HAS_NUMPY: bool
getrefcount: Incomplete
memo: Incomplete
id_to_obj: Incomplete
builtins_types: Incomplete
dont_memo: Incomplete

def get_attrs(obj): ...
def get_seq(obj, cache=...): ...
def memorise(obj, force: bool = False) -> None: ...
def release_gone() -> None: ...
def whats_changed(
    obj,
    seen: Incomplete | None = None,
    simple: bool = False,
    first: bool = True,
): ...
def has_changed(*args, **kwds): ...

__import__ = __import__
