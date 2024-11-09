from _typeshed import Incomplete

from nltk.corpus.reader.api import CorpusReader as CorpusReader
from nltk.corpus.reader.util import *
from nltk.data import (
    SeekableUnicodeStreamReader as SeekableUnicodeStreamReader,
)
from nltk.internals import ElementWrapper as ElementWrapper
from nltk.tokenize import WordPunctTokenizer as WordPunctTokenizer

class XMLCorpusReader(CorpusReader):
    def __init__(
        self, root: Incomplete, fileids: Incomplete, wrap_etree: bool = False
    ) -> None: ...
    def xml(self, fileid: Incomplete | None = None) -> Incomplete: ...
    def words(self, fileid: Incomplete | None = None) -> Incomplete: ...

class XMLCorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        fileid: Incomplete,
        tagspec: Incomplete,
        elt_handler: Incomplete | None = None,
    ) -> None: ...
    def handle_elt(
        self, elt: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def read_block(
        self,
        stream: Incomplete,
        tagspec: Incomplete | None = None,
        elt_handler: Incomplete | None = None,
    ) -> Incomplete: ...
