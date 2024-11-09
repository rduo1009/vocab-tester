from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.tokenize import *

TITLE: Incomplete
FEATURES: Incomplete
NOTES: Incomplete
SENT: Incomplete

class Review:
    title: Incomplete
    review_lines: Incomplete
    def __init__(
        self,
        title: Incomplete | None = None,
        review_lines: Incomplete | None = None,
    ) -> None: ...
    def add_line(self, review_line: Incomplete) -> None: ...
    def features(self) -> Incomplete: ...
    def sents(self) -> Incomplete: ...

class ReviewLine:
    sent: Incomplete
    features: Incomplete
    notes: Incomplete
    def __init__(
        self,
        sent: Incomplete,
        features: Incomplete | None = None,
        notes: Incomplete | None = None,
    ) -> None: ...

class ReviewsCorpusReader(CorpusReader):
    CorpusView = StreamBackedCorpusView
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        word_tokenizer: Incomplete = ...,
        encoding: str = "utf8",
    ) -> None: ...
    def features(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def reviews(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
