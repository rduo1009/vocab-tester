from typing import (
    Callable,
    Optional,
)

from nltk.corpus.reader.util import StreamBackedCorpusView
from nltk.corpus.util import LazyCorpusLoader
from nltk.data import ZipFilePathPointer

class NombankCorpusReader:
    def __init__(
        self,
        root: ZipFilePathPointer,
        nomfile: str,
        framefiles: str = ...,
        nounsfile: Optional[str] = ...,
        parse_fileid_xform: Optional[Callable] = ...,
        parse_corpus: Optional[LazyCorpusLoader] = ...,
        encoding: str = ...,
    ): ...
    def nouns(self) -> StreamBackedCorpusView: ...
