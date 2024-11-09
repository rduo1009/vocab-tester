from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.tokenize import *

STARS: Incomplete
COMPARISON: Incomplete
CLOSE_COMPARISON: Incomplete
GRAD_COMPARISON: Incomplete
NON_GRAD_COMPARISON: Incomplete
ENTITIES_FEATS: Incomplete
KEYWORD: Incomplete

class Comparison:
    text: Incomplete
    comp_type: Incomplete
    entity_1: Incomplete
    entity_2: Incomplete
    feature: Incomplete
    keyword: Incomplete
    def __init__(
        self,
        text: Incomplete | None = None,
        comp_type: Incomplete | None = None,
        entity_1: Incomplete | None = None,
        entity_2: Incomplete | None = None,
        feature: Incomplete | None = None,
        keyword: Incomplete | None = None,
    ) -> None: ...

class ComparativeSentencesCorpusReader(CorpusReader):
    CorpusView = StreamBackedCorpusView
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        word_tokenizer: Incomplete = ...,
        sent_tokenizer: Incomplete | None = None,
        encoding: str = "utf8",
    ) -> None: ...
    def comparisons(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def keywords(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def keywords_readme(self) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
