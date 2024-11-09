from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tokenize import *

class PlaintextCorpusReader(CorpusReader):
    CorpusView = StreamBackedCorpusView
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        word_tokenizer: Incomplete = ...,
        sent_tokenizer: Incomplete | None = None,
        para_block_reader: Incomplete = ...,
        encoding: str = "utf8",
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def paras(self, fileids: Incomplete | None = None) -> Incomplete: ...

class CategorizedPlaintextCorpusReader(
    CategorizedCorpusReader, PlaintextCorpusReader
):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class PortugueseCategorizedPlaintextCorpusReader(
    CategorizedPlaintextCorpusReader
):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class EuroparlCorpusReader(PlaintextCorpusReader):
    def chapters(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def paras(self, fileids: Incomplete | None = None) -> None: ...
