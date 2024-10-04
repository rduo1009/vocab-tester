from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tokenize import *

class SensevalInstance:
    word: Incomplete
    senses: Incomplete
    position: Incomplete
    context: Incomplete
    def __init__(
        self,
        word: Incomplete,
        position: Incomplete,
        context: Incomplete,
        senses: Incomplete,
    ) -> None: ...

class SensevalCorpusReader(CorpusReader):
    def instances(self, fileids: Incomplete | None = None) -> Incomplete: ...

class SensevalCorpusView(StreamBackedCorpusView):
    def __init__(self, fileid: Incomplete, encoding: Incomplete) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...
