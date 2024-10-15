from _typeshed import Incomplete

from nltk.corpus.reader.api import CorpusReader as CorpusReader
from nltk.corpus.reader.util import (
    StreamBackedCorpusView as StreamBackedCorpusView,
)
from nltk.corpus.reader.util import (
    ZipFilePathPointer as ZipFilePathPointer,
)
from nltk.corpus.reader.util import (
    concat as concat,
)
from nltk.tokenize import TweetTokenizer as TweetTokenizer

class TwitterCorpusReader(CorpusReader):
    CorpusView = StreamBackedCorpusView
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete | None = None,
        word_tokenizer: Incomplete = ...,
        encoding: str = "utf8",
    ) -> None: ...
    def docs(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def strings(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tokenized(self, fileids: Incomplete | None = None) -> Incomplete: ...
