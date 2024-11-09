from _typeshed import Incomplete

from nltk.corpus.reader import WordListCorpusReader as WordListCorpusReader
from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import StreamBackedCorpusView

class IgnoreReadmeCorpusView(StreamBackedCorpusView):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class OpinionLexiconCorpusReader(WordListCorpusReader):
    CorpusView = IgnoreReadmeCorpusView
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def positive(self) -> Incomplete: ...
    def negative(self) -> Incomplete: ...
