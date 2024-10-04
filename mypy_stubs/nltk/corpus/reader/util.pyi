from typing import (
    Any,
    Callable,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.corpus.reader.dependency import DependencyCorpusView
from nltk.data import (
    FileSystemPathPointer,
    SeekableUnicodeStreamReader,
    ZipFilePathPointer,
)

def _path_from(parent: str, child: str) -> List[Any]: ...
def concat(
    docs: List[Union[StreamBackedCorpusView, DependencyCorpusView, Any]],
) -> Union[
    DependencyCorpusView, ConcatenatedCorpusView, StreamBackedCorpusView
]: ...
def find_corpus_fileids(
    root: Union[ZipFilePathPointer, FileSystemPathPointer], regexp: str
) -> List[Union[Any, str]]: ...
def read_blankline_block(stream: SeekableUnicodeStreamReader) -> List[str]: ...
def read_regexp_block(
    stream: SeekableUnicodeStreamReader, start_re: str, end_re: None = ...
) -> List[str]: ...

class ConcatenatedCorpusView:
    def __init__(self, corpus_views: List[StreamBackedCorpusView]) -> None: ...
    def iterate_from(
        self, start_tok: int
    ) -> Iterator[Union[str, List[Tuple[str, str]]]]: ...

class StreamBackedCorpusView:
    def __getitem__(self, i: Union[int, slice]) -> Union[str, List[str]]: ...
    def __init__(
        self,
        fileid: Union[ZipFilePathPointer, FileSystemPathPointer],
        block_reader: Optional[Callable] = ...,  # type: ignore[type-arg]
        startpos: int = ...,
        encoding: str = ...,
    ) -> None: ...
    def _open(self) -> Incomplete: ...
    def close(self) -> Incomplete: ...
    def iterate_from(self, start_tok: int) -> Iterator[str]: ...
