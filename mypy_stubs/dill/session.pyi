from __future__ import annotations

import os

from _typeshed import Incomplete

from ._dill import ModuleType  # type: ignore

__all__ = [
    "dump_module",
    "load_module",
    "load_module_asdict",
    "dump_session",
    "load_session",
]

def dump_module(
    filename: str | os.PathLike | None = None,  # type: ignore
    module: ModuleType | str | None = None,
    refimported: bool = False,
    **kwds: Incomplete,
) -> None: ...
def dump_session(
    filename: Incomplete | None = None,
    main: Incomplete | None = None,
    byref: bool = False,
    **kwds: Incomplete,
) -> None: ...

class _PeekableReader:
    stream: Incomplete
    def __init__(self, stream: Incomplete) -> None: ...
    def read(self, n: Incomplete) -> Incomplete: ...
    def readline(self) -> Incomplete: ...
    def tell(self) -> Incomplete: ...
    def close(self) -> Incomplete: ...
    def peek(self, n: Incomplete) -> Incomplete: ...

def load_module(
    filename: str | os.PathLike | None = None,  # type: ignore
    module: ModuleType | str | None = None,
    **kwds: Incomplete,
) -> ModuleType | None: ...
def load_session(
    filename: Incomplete | None = None,
    main: Incomplete | None = None,
    **kwds: Incomplete,
) -> None: ...
def load_module_asdict(
    filename: str | os.PathLike | None = None,  # type: ignore
    update: bool = False,
    **kwds: Incomplete,
) -> dict: ...  # type: ignore
