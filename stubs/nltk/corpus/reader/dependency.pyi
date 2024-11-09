from typing import (
    Callable,
    List,
    Optional,
    Tuple,
    Union,
)

from nltk.data import (
    SeekableUnicodeStreamReader,
    ZipFilePathPointer,
)
from nltk.parse.dependencygraph import DependencyGraph
from nltk.tokenize.regexp import RegexpTokenizer
from nltk.tokenize.simple import TabTokenizer

class DependencyCorpusReader:
    def __init__(
        self,
        root: ZipFilePathPointer,
        fileids: str,
        encoding: List[Tuple[str, str]] = ...,
        word_tokenizer: TabTokenizer = ...,
        sent_tokenizer: RegexpTokenizer = ...,
        para_block_reader: Callable = ...,  # type: ignore[type-arg]
    ): ...
    def parsed_sents(
        self, fileids: Optional[str] = ...
    ) -> List[DependencyGraph]: ...
    def sents(self, fileids: Optional[str] = ...) -> DependencyCorpusView: ...

class DependencyCorpusView:
    def __init__(
        self,
        corpus_file: ZipFilePathPointer,
        tagged: bool,
        group_by_sent: bool,
        dependencies: bool,
        chunk_types: None = ...,
        encoding: str = ...,
    ): ...
    def read_block(
        self, stream: SeekableUnicodeStreamReader
    ) -> List[Union[str, List[str]]]: ...
