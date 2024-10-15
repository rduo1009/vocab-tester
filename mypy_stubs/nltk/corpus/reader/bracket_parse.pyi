from typing import (
    List,
    Optional,
    Tuple,
)

from _typeshed import Incomplete

from nltk.data import (
    FileSystemPathPointer,
    SeekableUnicodeStreamReader,
)

class BracketParseCorpusReader:
    def __init__(
        self,
        root: FileSystemPathPointer,
        fileids: str,
        comment_char: Optional[str] = ...,
        detect_blocks: str = ...,
        encoding: str = ...,
        tagset: Optional[str] = ...,
    ) -> Incomplete: ...
    def _normalize(self, t: str) -> str: ...
    def _read_block(
        self, stream: SeekableUnicodeStreamReader
    ) -> List[str]: ...
    def _tag(self, t: str, tagset: None = ...) -> List[Tuple[str, str]]: ...
    def _word(self, t: str) -> List[str]: ...

class CategorizedBracketParseCorpusReader:
    def __init__(
        self, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Optional[str] = ...,
        categories: None = ...,
        tagset: None = ...,
    ) -> Incomplete: ...

class AlpinoCorpusReader(BracketParseCorpusReader):
    def __init__(
        self,
        root: Incomplete,
        encoding: str = "ISO-8859-1",
        tagset: Incomplete | None = None,
    ) -> None: ...
