from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.timit import read_timit_block as read_timit_block
from nltk.corpus.reader.util import *
from nltk.tag import map_tag as map_tag
from nltk.tag import str2tuple as str2tuple
from nltk.tokenize import *

class TaggedCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        sep: str = "/",
        word_tokenizer: Incomplete = ...,
        sent_tokenizer: Incomplete = ...,
        para_block_reader: Incomplete = ...,
        encoding: str = "utf8",
        tagset: Incomplete | None = None,
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def paras(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_paras(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...

class CategorizedTaggedCorpusReader(
    CategorizedCorpusReader, TaggedCorpusReader
):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def tagged_paras(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...

class TaggedCorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        corpus_file: Incomplete,
        encoding: Incomplete,
        tagged: Incomplete,
        group_by_sent: Incomplete,
        group_by_para: Incomplete,
        sep: Incomplete,
        word_tokenizer: Incomplete,
        sent_tokenizer: Incomplete,
        para_block_reader: Incomplete,
        tag_mapping_function: Incomplete | None = None,
    ) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...

class MacMorphoCorpusReader(TaggedCorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        encoding: str = "utf8",
        tagset: Incomplete | None = None,
    ) -> None: ...

class TimitTaggedCorpusReader(TaggedCorpusReader):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def paras(self) -> None: ...
    def tagged_paras(self) -> None: ...
