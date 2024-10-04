from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.tokenize import *

class ProsConsCorpusReader(CategorizedCorpusReader, CorpusReader):
    CorpusView = StreamBackedCorpusView
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        word_tokenizer: Incomplete = ...,
        encoding: str = "utf8",
        **kwargs: Incomplete,
    ) -> None: ...
    def sents(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def words(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
