from _typeshed import Incomplete

from nltk.corpus.reader.plaintext import (
    PlaintextCorpusReader as PlaintextCorpusReader,
)
from nltk.corpus.reader.util import find_corpus_fileids as find_corpus_fileids

class UdhrCorpusReader(PlaintextCorpusReader):
    ENCODINGS: Incomplete
    SKIP: Incomplete
    def __init__(self, root: str = "udhr") -> None: ...
