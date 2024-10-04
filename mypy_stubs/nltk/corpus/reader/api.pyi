from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.corpus.reader.util import (
    ConcatenatedCorpusView,
)
from nltk.corpus.reader.util import (
    StreamBackedCorpusView as StreamBackedCorpusView,
)
from nltk.data import (
    FileSystemPathPointer,
    SeekableUnicodeStreamReader,
    ZipFilePathPointer,
)

class CategorizedCorpusReader:
    def __init__(self, kwargs: Dict[str, str]) -> Incomplete: ...
    def _init(self) -> Incomplete: ...
    def _resolve(
        self, fileids: Optional[str], categories: Optional[List[str]]
    ) -> str: ...
    def categories(self, fileids: None = ...) -> Incomplete: ...
    def fileids(
        self, categories: Optional[Union[List[str], str]] = ...
    ) -> List[Any]: ...
    def words(
        self,
        fileids: Optional[str] = ...,
        categories: Optional[List[str]] = ...,
    ) -> Incomplete: ...

class CorpusReader:
    def __init__(
        self,
        root: Union[ZipFilePathPointer, FileSystemPathPointer],
        fileids: Union[
            str,
            Tuple[str, ...],
        ],
        encoding: Union[str, List[Tuple[str, str]]] = ...,
        tagset: None = ...,
    ) -> Incomplete: ...
    def abspath(self, fileid: str) -> ZipFilePathPointer: ...
    def abspaths(
        self,
        fileids: Optional[str] = ...,
        include_encoding: bool = ...,
        include_fileid: bool = ...,
    ) -> List[
        Union[
            Tuple[FileSystemPathPointer, str],
            Tuple[ZipFilePathPointer, str],
            Any,
        ]
    ]: ...
    def encoding(self, file: str) -> str: ...
    def ensure_loaded(self) -> Incomplete: ...
    def fileids(self) -> List[Any]: ...
    def open(self, file: str) -> SeekableUnicodeStreamReader: ...

class SyntaxCorpusReader:
    def _read_sent_block(
        self, stream: SeekableUnicodeStreamReader
    ) -> List[List[str]]: ...
    def _read_tagged_sent_block(
        self, stream: SeekableUnicodeStreamReader, tagset: None = ...
    ) -> List[List[Tuple[str, str]]]: ...
    def _read_word_block(
        self, stream: SeekableUnicodeStreamReader
    ) -> List[str]: ...
    def tagged_sents(
        self, fileids: None = ..., tagset: None = ...
    ) -> ConcatenatedCorpusView: ...
    def tagged_words(
        self, fileids: Optional[str] = ..., tagset: None = ...
    ) -> Incomplete: ...
    def words(
        self, fileids: Optional[str] = ...
    ) -> Union[ConcatenatedCorpusView, StreamBackedCorpusView]: ...
