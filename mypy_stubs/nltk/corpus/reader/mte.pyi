from functools import reduce as reduce

from _typeshed import Incomplete

from nltk.corpus.reader import (
    TaggedCorpusReader as TaggedCorpusReader,
)
from nltk.corpus.reader import (
    concat as concat,
)
from nltk.corpus.reader.xmldocs import XMLCorpusView as XMLCorpusView

def xpath(
    root: Incomplete, path: Incomplete, ns: Incomplete
) -> Incomplete: ...

class MTECorpusView(XMLCorpusView):
    def __init__(
        self,
        fileid: Incomplete,
        tagspec: Incomplete,
        elt_handler: Incomplete | None = None,
    ) -> None: ...
    def read_block(
        self,
        stream: Incomplete,
        tagspec: Incomplete | None = None,
        elt_handler: Incomplete | None = None,
    ) -> Incomplete: ...

class MTEFileReader:
    ns: Incomplete
    tag_ns: str
    xml_ns: str
    word_path: str
    sent_path: str
    para_path: str
    def __init__(self, file_path: Incomplete) -> None: ...
    def words(self) -> Incomplete: ...
    def sents(self) -> Incomplete: ...
    def paras(self) -> Incomplete: ...
    def lemma_words(self) -> Incomplete: ...
    def tagged_words(
        self, tagset: Incomplete, tags: Incomplete
    ) -> Incomplete: ...
    def lemma_sents(self) -> Incomplete: ...
    def tagged_sents(
        self, tagset: Incomplete, tags: Incomplete
    ) -> Incomplete: ...
    def lemma_paras(self) -> Incomplete: ...
    def tagged_paras(
        self, tagset: Incomplete, tags: Incomplete
    ) -> Incomplete: ...

class MTETagConverter:
    mapping_msd_universal: Incomplete
    @staticmethod
    def msd_to_universal(tag: Incomplete) -> Incomplete: ...

class MTECorpusReader(TaggedCorpusReader):
    def __init__(
        self,
        root: Incomplete | None = None,
        fileids: Incomplete | None = None,
        encoding: str = "utf8",
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def paras(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def lemma_words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        tagset: str = "msd",
        tags: str = "",
    ) -> Incomplete: ...
    def lemma_sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        tagset: str = "msd",
        tags: str = "",
    ) -> Incomplete: ...
    def lemma_paras(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_paras(
        self,
        fileids: Incomplete | None = None,
        tagset: str = "msd",
        tags: str = "",
    ) -> Incomplete: ...
