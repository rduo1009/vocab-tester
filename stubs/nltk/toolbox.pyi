from collections.abc import Generator

from _typeshed import Incomplete

from nltk.data import PathPointer as PathPointer
from nltk.data import find as find

class StandardFormat:
    def __init__(
        self,
        filename: Incomplete | None = None,
        encoding: Incomplete | None = None,
    ) -> None: ...
    def open(self, sfm_file: Incomplete) -> None: ...
    def open_string(self, s: Incomplete) -> None: ...
    line_num: int
    def raw_fields(self) -> Generator[Incomplete, None, None]: ...
    def fields(
        self,
        strip: bool = True,
        unwrap: bool = True,
        encoding: Incomplete | None = None,
        errors: str = "strict",
        unicode_fields: Incomplete | None = None,
    ) -> Generator[Incomplete, None, None]: ...
    def close(self) -> None: ...

class ToolboxData(StandardFormat):
    def parse(
        self, grammar: Incomplete | None = None, **kwargs: Incomplete
    ) -> Incomplete: ...

def to_sfm_string(
    tree: Incomplete,
    encoding: Incomplete | None = None,
    errors: str = "strict",
    unicode_fields: Incomplete | None = None,
) -> Incomplete: ...

class ToolboxSettings(StandardFormat):
    def __init__(self) -> None: ...
    def parse(
        self,
        encoding: Incomplete | None = None,
        errors: str = "strict",
        **kwargs: Incomplete,
    ) -> Incomplete: ...

def to_settings_string(
    tree: Incomplete,
    encoding: Incomplete | None = None,
    errors: str = "strict",
    unicode_fields: Incomplete | None = None,
) -> Incomplete: ...
def remove_blanks(elem: Incomplete) -> None: ...
def add_default_fields(
    elem: Incomplete, default_fields: Incomplete
) -> None: ...
def sort_fields(elem: Incomplete, field_orders: Incomplete) -> None: ...
def add_blank_lines(
    tree: Incomplete, blanks_before: Incomplete, blanks_between: Incomplete
) -> None: ...
def demo() -> None: ...
