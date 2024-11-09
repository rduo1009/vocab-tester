from functools import reduce as reduce

from _typeshed import Incomplete

from nltk.corpus.reader import TaggedCorpusReader as TaggedCorpusReader
from nltk.corpus.reader import concat as concat
from nltk.corpus.reader.xmldocs import XMLCorpusView as XMLCorpusView

def xpath(
    root: Incomplete, path: Incomplete, ns: Incomplete
) -> Incomplete: ...

class MTECorpusView(XMLCorpusView):
    def __init__(
        self: Incomplete,
        fileid: Incomplete,
        tagspec: Incomplete,
        elt_handler: Incomplete | None = None,
    ) -> None: ...
    def read_block(
        self: Incomplete,
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

    def __init__(self: Incomplete, file_path: Incomplete) -> None: ...
    def words(self: Incomplete) -> Incomplete: ...
    def sents(self: Incomplete) -> Incomplete: ...
    def paras(self: Incomplete) -> Incomplete: ...
    def lemma_words(self: Incomplete) -> Incomplete: ...
    def tagged_words(
        self: Incomplete, tagset: Incomplete, tags: Incomplete
    ) -> Incomplete: ...
    def lemma_sents(self: Incomplete) -> Incomplete: ...
    def tagged_sents(
        self: Incomplete, tagset: Incomplete, tags: Incomplete
    ) -> Incomplete: ...
    def lemma_paras(self: Incomplete) -> Incomplete: ...
    def tagged_paras(
        self: Incomplete, tagset: Incomplete, tags: Incomplete
    ) -> Incomplete: ...

class MTETagConverter:
    mapping_msd_universal: Incomplete

    @staticmethod
    def msd_to_universal(tag: Incomplete) -> Incomplete: ...

class MTECorpusReader(TaggedCorpusReader):
    def __init__(
        self: Incomplete,
        root: Incomplete | None = None,
        fileids: Incomplete | None = None,
        encoding: str = "utf8",
    ) -> None: ...
    def words(
        self: Incomplete, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def sents(
        self: Incomplete, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def paras(
        self: Incomplete, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def lemma_words(
        self: Incomplete, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def tagged_words(
        self: Incomplete,
        fileids: Incomplete | None = None,
        tagset: str = "msd",
        tags: str = "",
    ) -> Incomplete: ...
    def lemma_sents(
        self: Incomplete, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def tagged_sents(
        self: Incomplete,
        fileids: Incomplete | None = None,
        tagset: str = "msd",
        tags: str = "",
    ) -> Incomplete: ...
    def lemma_paras(
        self: Incomplete, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def tagged_paras(
        self: Incomplete,
        fileids: Incomplete | None = None,
        tagset: str = "msd",
        tags: str = "",
    ) -> Incomplete: ...
