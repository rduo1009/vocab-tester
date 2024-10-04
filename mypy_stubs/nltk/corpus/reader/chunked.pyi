from _typeshed import Incomplete

from nltk.chunk import tagstr2tree as tagstr2tree
from nltk.corpus.reader.api import *
from nltk.corpus.reader.bracket_parse import (
    BracketParseCorpusReader as BracketParseCorpusReader,
)
from nltk.corpus.reader.util import *
from nltk.tokenize import *
from nltk.tree import Tree as Tree

class ChunkedCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        extension: str = "",
        str2chunktree: Incomplete = ...,
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
    def chunked_words(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def chunked_sents(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def chunked_paras(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...

class ChunkedCorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        fileid: Incomplete,
        encoding: Incomplete,
        tagged: Incomplete,
        group_by_sent: Incomplete,
        group_by_para: Incomplete,
        chunked: Incomplete,
        str2chunktree: Incomplete,
        sent_tokenizer: Incomplete,
        para_block_reader: Incomplete,
        source_tagset: Incomplete | None = None,
        target_tagset: Incomplete | None = None,
    ) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...
