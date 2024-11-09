from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.xmldocs import *

def norm(value_strin: Incomplete) -> Incomplete: ...

class RTEPair:
    challenge: Incomplete
    id: Incomplete
    gid: Incomplete
    text: Incomplete
    hyp: Incomplete
    value: Incomplete
    task: Incomplete
    length: Incomplete
    def __init__(
        self,
        pair: Incomplete,
        challenge: Incomplete | None = None,
        id: Incomplete | None = None,
        text: Incomplete | None = None,
        hyp: Incomplete | None = None,
        value: Incomplete | None = None,
        task: Incomplete | None = None,
        length: Incomplete | None = None,
    ) -> None: ...

class RTECorpusReader(XMLCorpusReader):
    def pairs(self, fileids: Incomplete) -> Incomplete: ...
