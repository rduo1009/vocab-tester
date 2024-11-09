from _typeshed import Incomplete

from nltk.corpus.reader import util as util
from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *

class ChasenCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        encoding: str = "utf8",
        sent_splitter: Incomplete | None = None,
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_words(
        self, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_sents(
        self, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def paras(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_paras(
        self, fileids: Incomplete | None = None
    ) -> Incomplete: ...

class ChasenCorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        corpus_file: Incomplete,
        encoding: Incomplete,
        tagged: Incomplete,
        group_by_sent: Incomplete,
        group_by_para: Incomplete,
        sent_splitter: Incomplete | None = None,
    ) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...

def demo() -> None: ...
def test() -> None: ...
