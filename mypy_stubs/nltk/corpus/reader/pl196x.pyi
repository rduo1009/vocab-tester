from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.xmldocs import XMLCorpusReader as XMLCorpusReader

PARA: Incomplete
SENT: Incomplete
TAGGEDWORD: Incomplete
WORD: Incomplete
TYPE: Incomplete
ANA: Incomplete
TEXTID: Incomplete

class TEICorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        corpus_file: Incomplete,
        tagged: Incomplete,
        group_by_sent: Incomplete,
        group_by_para: Incomplete,
        tagset: Incomplete | None = None,
        head_len: int = 0,
        textids: Incomplete | None = None,
    ) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...

class Pl196xCorpusReader(CategorizedCorpusReader, XMLCorpusReader):
    head_len: int
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def decode_tag(self, tag: Incomplete) -> Incomplete: ...
    def textids(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def words(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        textids: Incomplete | None = None,
    ) -> Incomplete: ...
    def sents(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        textids: Incomplete | None = None,
    ) -> Incomplete: ...
    def paras(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        textids: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        textids: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        textids: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_paras(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        textids: Incomplete | None = None,
    ) -> Incomplete: ...
    def xml(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
