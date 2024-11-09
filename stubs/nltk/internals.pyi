from abc import ABC
from typing import (
    Callable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

from _typeshed import Incomplete

from nltk.corpus.reader.util import (
    ConcatenatedCorpusView,
    StreamBackedCorpusView,
)
from nltk.parse.api import ParserI
from nltk.parse.corenlp import (
    CoreNLPDependencyParser,
    CoreNLPParser,
    GenericCoreNLPParser,
)
from nltk.tag.api import TaggerI
from nltk.tokenize.api import TokenizerI

def _add_epytext_field(
    obj: Callable, field: str, message: str
) -> Incomplete: ...
def _decode_stdoutdata(stdoutdata: bytes) -> str: ...
def _mro(
    cls: Union[Type[CoreNLPParser], Type[CoreNLPDependencyParser]],
) -> Union[
    Tuple[
        Type[CoreNLPParser],
        Type[GenericCoreNLPParser],
        Type[ParserI],
        Type[TokenizerI],
        Type[ABC],
        Type[TaggerI],
        Type[object],
    ],
    Tuple[
        Type[CoreNLPDependencyParser],
        Type[GenericCoreNLPParser],
        Type[ParserI],
        Type[TokenizerI],
        Type[ABC],
        Type[TaggerI],
        Type[object],
    ],
]: ...
def deprecated(message: str) -> Callable: ...  # type: ignore[type-arg]
def find_binary(
    name: str,
    path_to_bin: None = ...,
    env_vars: List[str] = ...,
    searchpath: Tuple[()] = ...,
    binary_names: Optional[List[str]] = ...,
    url: Optional[str] = ...,
    verbose: bool = ...,
) -> Incomplete: ...
def find_binary_iter(
    name: str,
    path_to_bin: Incomplete | None = None,
    env_vars: Incomplete = (),
    searchpath: Tuple[()] = (),
    binary_names: Optional[List[str]] = None,
    url: Optional[str] = None,
    verbose: bool = False,
) -> Incomplete: ...
def find_file_iter(
    filename: str,
    env_vars: List[str] = ...,
    searchpath: Tuple[()] = (),
    file_names: Optional[List[str]] = ...,
    url: Optional[str] = ...,
    verbose: bool = False,
    finding_dir: bool = False,
) -> Incomplete: ...
def find_jar(
    name_pattern: str,
    path_to_jar: None = ...,
    env_vars: Tuple[str] = ...,
    searchpath: Tuple[()] = ...,
    url: Optional[str] = ...,
    verbose: bool = ...,
    is_regex: bool = ...,
) -> Incomplete: ...
def find_jar_iter(
    name_pattern: str,
    path_to_jar: None = ...,
    env_vars: Tuple[str] = ...,
    searchpath: Tuple[()] = ...,
    url: Optional[str] = ...,
    verbose: bool = ...,
    is_regex: bool = ...,
) -> Incomplete: ...
def is_writable(path: str) -> Incomplete: ...
def overridden(method: Callable) -> bool: ...
def slice_bounds(
    sequence: Union[ConcatenatedCorpusView, StreamBackedCorpusView],
    slice_obj: slice,
    allow_step: bool = ...,
) -> Tuple[int, int]: ...

class Counter:
    def __init__(self, initial_value: int = 0) -> None: ...
    def get(self) -> Incomplete: ...

def config_java(
    bin: Incomplete | None = None,
    options: Incomplete | None = None,
    verbose: bool = False,
) -> None: ...
def java(
    cmd: Incomplete,
    classpath: Incomplete | None = None,
    stdin: Incomplete | None = None,
    stdout: Incomplete | None = None,
    stderr: Incomplete | None = None,
    blocking: bool = True,
) -> Incomplete: ...

class ReadError(ValueError):
    expected: Incomplete
    position: Incomplete
    def __init__(self, expected: Incomplete, position: Incomplete) -> None: ...

def read_str(s: Incomplete, start_position: Incomplete) -> Incomplete: ...
def read_int(s: Incomplete, start_position: Incomplete) -> Incomplete: ...
def read_number(s: Incomplete, start_position: Incomplete) -> Incomplete: ...

class Deprecated:
    def __new__(
        cls: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...

def find_file(
    filename: Incomplete,
    env_vars: Incomplete = (),
    searchpath: Incomplete = (),
    file_names: Incomplete | None = None,
    url: Incomplete | None = None,
    verbose: bool = False,
) -> Incomplete: ...
def find_dir(
    filename: Incomplete,
    env_vars: Incomplete = (),
    searchpath: Incomplete = (),
    file_names: Incomplete | None = None,
    url: Incomplete | None = None,
    verbose: bool = False,
) -> Incomplete: ...
def find_jars_within_path(path_to_jars: Incomplete) -> Incomplete: ...
def import_from_stdlib(module: Incomplete) -> Incomplete: ...

class ElementWrapper:
    def __new__(cls: Incomplete, etree: Incomplete) -> Incomplete: ...
    def __init__(self, etree: Incomplete) -> None: ...
    def unwrap(self) -> Incomplete: ...
    def __getattr__(self, attrib: Incomplete) -> Incomplete: ...
    def __setattr__(
        self, attr: Incomplete, value: Incomplete
    ) -> Incomplete: ...
    def __delattr__(self, attr: Incomplete) -> Incomplete: ...
    def __setitem__(self, index: Incomplete, element: Incomplete) -> None: ...
    def __delitem__(self, index: Incomplete) -> None: ...
    def __setslice__(
        self, start: Incomplete, stop: Incomplete, elements: Incomplete
    ) -> None: ...
    def __delslice__(self, start: Incomplete, stop: Incomplete) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: Incomplete) -> Incomplete: ...
    def __getslice__(
        self, start: Incomplete, stop: Incomplete
    ) -> Incomplete: ...
    def getchildren(self) -> Incomplete: ...
    def getiterator(self, tag: Incomplete | None = None) -> Incomplete: ...
    def makeelement(
        self, tag: Incomplete, attrib: Incomplete
    ) -> Incomplete: ...
    def find(self, path: Incomplete) -> Incomplete: ...
    def findall(self, path: Incomplete) -> Incomplete: ...

def raise_unorderable_types(
    ordering: Incomplete, a: Incomplete, b: Incomplete
) -> None: ...
