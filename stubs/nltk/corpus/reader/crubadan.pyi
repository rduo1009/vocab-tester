from _typeshed import Incomplete

from nltk.corpus.reader import CorpusReader as CorpusReader
from nltk.data import ZipFilePathPointer as ZipFilePathPointer
from nltk.probability import FreqDist as FreqDist

class CrubadanCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        encoding: str = "utf8",
        tagset: Incomplete | None = None,
    ) -> None: ...
    def lang_freq(self, lang: Incomplete) -> Incomplete: ...
    def langs(self) -> Incomplete: ...
    def iso_to_crubadan(self, lang: Incomplete) -> Incomplete: ...
    def crubadan_to_iso(self, lang: Incomplete) -> Incomplete: ...
