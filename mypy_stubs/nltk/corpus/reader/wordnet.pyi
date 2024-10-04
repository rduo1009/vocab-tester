from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

from _typeshed import Incomplete

from nltk.corpus.reader import CorpusReader as CorpusReader
from nltk.corpus.util import LazyCorpusLoader
from nltk.data import (
    SeekableUnicodeStreamReader,
    ZipFilePathPointer,
)

class Lemma:
    def __init__(
        self,
        wordnet_corpus_reader: WordNetCorpusReader,
        synset: Synset,
        name: str,
        lexname_index: int,
        lex_id: int,
        syntactic_marker: None,
    ) -> None: ...
    def name(self) -> str: ...

class Synset:
    def __init__(self, wordnet_corpus_reader: WordNetCorpusReader) -> None: ...
    def lemmas(self, lang: str = ...) -> List[Lemma]: ...

class WordNetCorpusReader:
    def __init__(
        self, root: ZipFilePathPointer, omw_reader: LazyCorpusLoader
    ) -> None: ...
    def _data_file(self, pos: str) -> SeekableUnicodeStreamReader: ...
    def _load_exception_map(self) -> Incomplete: ...
    def _load_lemma_pos_offset_map(self) -> Incomplete: ...
    def _morphy(
        self, form: str, pos: str, check_exceptions: bool = ...
    ) -> List[Union[str, Any]]: ...
    def _synset_from_pos_and_line(
        self, pos: str, data_file_line: str
    ) -> Synset: ...
    def get_version(self) -> str: ...
    def index_sense(self, version: Optional[str] = ...) -> Dict[str, str]: ...
    def map_to_many(self, version: str = ...) -> Dict[str, List[str]]: ...
    def map_to_one(self, version: str = ...) -> Dict[str, str]: ...
    def map_wn(self, version: str = ...) -> Dict[str, str]: ...
    def synset_from_pos_and_offset(self, pos: str, offset: int) -> Synset: ...
    def synsets(
        self,
        lemma: str,
        pos: None = ...,
        lang: str = ...,
        check_exceptions: bool = ...,
    ) -> List[Synset]: ...

class WordNetICCorpusReader(CorpusReader):
    def __init__(self, root: Incomplete, fileids: Incomplete) -> None: ...
    def ic(self, icfile: Incomplete) -> Incomplete: ...
