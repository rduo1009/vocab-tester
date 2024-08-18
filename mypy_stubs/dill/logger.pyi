import contextlib
import logging
from logging import (
    Logger,
    StreamHandler,
)
from os import PathLike
from typing import (
    Any,
    Optional,
    TextIO,
    Union,
)

from _typeshed import Incomplete
from dill._dill import Pickler

__all__ = ["adapter", "logger", "trace"]

class TraceAdapter:
    def __init__(self, logger: Logger) -> None: ...
    def addHandler(self, handler: StreamHandler) -> None: ...  # type: ignore
    def trace(
        self, pickler: Pickler, msg: str, *args: Any, **kwargs: Any
    ) -> None | TraceManager: ...
    def trace_setup(self, pickler: Pickler) -> None: ...
    def process(self, msg: Any, kwargs: Any) -> tuple[Any, Any]: ...
    def removeHandler(self, handler: Any) -> None: ...

class TraceFormatter(logging.Formatter):
    is_utf8: bool
    def __init__(
        self, *args: Any, handler: Incomplete = ..., **kwargs: Any
    ): ...
    def format(self, record: Incomplete) -> Incomplete: ...

logger: Incomplete
adapter: Incomplete

def trace(
    arg: Optional[Union[bool, TextIO, str, PathLike]] = ...,  # type: ignore
    *,
    mode: str = ...,
) -> None: ...

class TraceManager(contextlib.AbstractContextManager):  # type: ignore
    file: Any
    mode: Any
    redirect: bool
    file_is_stream: bool
    def __init__(self, file: Any, mode: Any) -> None: ...
    handler: logging.StreamHandler | logging.FileHandler  # type: ignore
    old_level: Incomplete
    def __enter__(self) -> Incomplete: ...
    def __exit__(self, *exc_info: Incomplete) -> None: ...
