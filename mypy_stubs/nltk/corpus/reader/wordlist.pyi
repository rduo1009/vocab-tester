from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tokenize import line_tokenize as line_tokenize

class WordListCorpusReader(CorpusReader):
    def words(
        self,
        fileids: Incomplete | None = None,
        ignore_lines_startswith: str = "\n",
    ) -> Incomplete: ...

class SwadeshCorpusReader(WordListCorpusReader):
    def entries(self, fileids: Incomplete | None = None) -> Incomplete: ...

class NonbreakingPrefixesCorpusReader(WordListCorpusReader):
    available_langs: Incomplete
    def words(
        self,
        lang: Incomplete | None = None,
        fileids: Incomplete | None = None,
        ignore_lines_startswith: str = "#",
    ) -> Incomplete: ...

class UnicharsCorpusReader(WordListCorpusReader):
    available_categories: Incomplete
    def chars(
        self,
        category: Incomplete | None = None,
        fileids: Incomplete | None = None,
    ) -> Incomplete: ...

class MWAPPDBCorpusReader(WordListCorpusReader):
    mwa_ppdb_xxxl_file: str
    def entries(self, fileids: Incomplete = ...) -> Incomplete: ...
