from __future__ import annotations

import typing
from pickle import (
    DEFAULT_PROTOCOL as DEFAULT_PROTOCOL,
)
from pickle import (
    HIGHEST_PROTOCOL as HIGHEST_PROTOCOL,
)
from pickle import (
    PickleError as PickleError,
)
from pickle import (
    PicklingError as PicklingError,
)
from pickle import (
    Unpickler as StockUnpickler,
)
from pickle import (
    UnpicklingError as UnpicklingError,
)
from pickle import (
    _Pickler as StockPickler,
)
from typing import Any, Callable

from _typeshed import Incomplete

from .logger import adapter as logger

__all__ = [
    "dump",
    "dumps",
    "load",
    "loads",
    "copy",
    "Pickler",
    "Unpickler",
    "register",
    "pickle",
    "pickles",
    "check",
    "DEFAULT_PROTOCOL",
    "HIGHEST_PROTOCOL",
    "HANDLE_FMODE",
    "CONTENTS_FMODE",
    "FILE_FMODE",
    "PickleError",
    "PickleWarning",
    "PicklingError",
    "PicklingWarning",
    "UnpicklingError",
    "UnpicklingWarning",
]

log = logger
BufferType = memoryview
ClassType = type
SliceType = slice
TypeType = type
XRangeType = range
try:
    IS_IPYTHON = __IPYTHON__  # type: ignore
except NameError:
    IS_IPYTHON = False

class Sentinel:
    name: str
    __module__: Incomplete
    def __init__(
        self, name: str, module_name: Incomplete | None = None
    ) -> None: ...
    def __copy__(self) -> "Sentinel": ...
    def __deepcopy__(self, memo: Incomplete) -> "Sentinel": ...
    def __reduce__(self) -> str: ...
    def __reduce_ex__(self, protocol: Incomplete) -> str: ...

HANDLE_FMODE: int
CONTENTS_FMODE: int
FILE_FMODE: int

def copy(obj: object, *args: Any, **kwds: Any) -> Incomplete: ...
def dump(
    obj: object,
    file: Incomplete,
    protocol: Incomplete | None = None,
    byref: Incomplete | None = None,
    fmode: Incomplete | None = None,
    recurse: Incomplete | None = None,
    **kwds: Incomplete,
) -> None: ...
def dumps(
    obj: object,
    protocol: Incomplete | None = None,
    byref: Incomplete | None = None,
    fmode: Incomplete | None = None,
    recurse: Incomplete | None = None,
    **kwds: Incomplete,
) -> Incomplete: ...
def load(
    file: Incomplete, ignore: Incomplete | None = None, **kwds: Any
) -> Unpickler: ...
def loads(
    str: str | bytes, ignore: Incomplete | None = None, **kwds: Any
) -> Unpickler: ...

class MetaCatchingDict(dict):  # type: ignore
    def get(
        self, key: Incomplete, default: Incomplete | None = None
    ) -> Incomplete: ...
    def __missing__(self, key: Incomplete) -> Incomplete: ...

class PickleWarning(Warning, PickleError): ...
class PicklingWarning(PickleWarning, PicklingError): ...
class UnpicklingWarning(PickleWarning, UnpicklingError): ...

class Pickler(StockPickler):
    dispatch: dict[type, Callable[[Pickler, typing.Any], None]]  # type: ignore
    settings: dict[str, Any]
    def __init__(
        self, file: Incomplete, *args: Incomplete, **kwds: Incomplete
    ) -> None: ...
    def save(
        self, obj: Incomplete, save_persistent_id: bool = True
    ) -> None: ...
    def dump(self, obj: Incomplete) -> None: ...

class Unpickler(StockUnpickler):
    settings: dict[str, Any]
    def find_class(
        self, module: Incomplete, name: Incomplete
    ) -> Incomplete: ...
    def __init__(self, *args: Incomplete, **kwds: Incomplete) -> None: ...
    def load(self) -> Incomplete: ...

def pickle(t: Incomplete, func: Incomplete) -> None: ...
def register(t: Incomplete) -> Callable: ...  # type: ignore

class match:
    value: Incomplete
    def __init__(self, value: Incomplete) -> None: ...
    def __enter__(self) -> "match": ...
    def __exit__(self, *exc_info: Incomplete) -> bool: ...
    args: Incomplete
    def case(self, args: Any) -> bool: ...
    @property
    def fields(self) -> dict: ...  # type: ignore
    def __getattr__(self, item: Any) -> Any: ...

CODE_VERSION: tuple[int, ...]

# class _itemgetter_helper:
#     items: Incomplete
#     def __init__(self) -> None: ...
#     def __getitem__(self, item) -> None: ...
#
# class _attrgetter_helper:
#     attrs: Incomplete
#     index: Incomplete
#     def __init__(self, attrs, index: Incomplete | None = None) -> None: ...
#     def __getattribute__(self, attr): ...
#
# class _dictproxy_helper(dict):
#     def __ror__(self, a): ...

def pickles(
    obj: object, exact: bool = False, safe: bool = False, **kwds: Any
) -> bool | Incomplete: ...
def check(obj: object, *args: Any, **kwds: Any) -> None: ...
