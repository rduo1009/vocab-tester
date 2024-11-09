from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *

class StringCategoryCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        delimiter: str = " ",
        encoding: str = "utf8",
    ) -> None: ...
    def tuples(self, fileids: Incomplete | None = None) -> Incomplete: ...
