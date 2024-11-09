from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.xmldocs import (
    XMLCorpusReader as XMLCorpusReader,
)
from nltk.corpus.reader.xmldocs import (
    XMLCorpusView as XMLCorpusView,
)
from nltk.tree import Tree as Tree

__docformat__: str

class SemcorCorpusReader(XMLCorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        wordnet: Incomplete,
        lazy: bool = True,
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def chunks(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_chunks(
        self, fileids: Incomplete | None = None, tag: Incomplete = ...
    ) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def chunk_sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_sents(
        self, fileids: Incomplete | None = None, tag: Incomplete = ...
    ) -> Incomplete: ...

class SemcorSentence(list):
    num: Incomplete
    def __init__(self, num: Incomplete, items: Incomplete) -> None: ...

class SemcorWordView(XMLCorpusView):
    def __init__(
        self,
        fileid: Incomplete,
        unit: Incomplete,
        bracket_sent: Incomplete,
        pos_tag: Incomplete,
        sem_tag: Incomplete,
        wordnet: Incomplete,
    ) -> None: ...
    def handle_elt(
        self, elt: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def handle_word(self, elt: Incomplete) -> Incomplete: ...
    def handle_sent(self, elt: Incomplete) -> Incomplete: ...
