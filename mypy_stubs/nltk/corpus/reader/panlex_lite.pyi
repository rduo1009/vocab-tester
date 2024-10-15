from _typeshed import Incomplete

from nltk.corpus.reader.api import CorpusReader as CorpusReader

class PanLexLiteCorpusReader(CorpusReader):
    MEANING_Q: str
    TRANSLATION_Q: str
    def __init__(self, root: Incomplete) -> None: ...
    def language_varieties(
        self, lc: Incomplete | None = None
    ) -> Incomplete: ...
    def meanings(
        self, expr_uid: Incomplete, expr_tt: Incomplete
    ) -> Incomplete: ...
    def translations(
        self, from_uid: Incomplete, from_tt: Incomplete, to_uid: Incomplete
    ) -> Incomplete: ...

class Meaning(dict):
    def __init__(self, mn: Incomplete, attr: Incomplete) -> None: ...
    def id(self) -> Incomplete: ...
    def quality(self) -> Incomplete: ...
    def source(self) -> Incomplete: ...
    def source_group(self) -> Incomplete: ...
    def expressions(self) -> Incomplete: ...
