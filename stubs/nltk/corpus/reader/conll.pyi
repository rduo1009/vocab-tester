from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tag import map_tag as map_tag
from nltk.tree import Tree as Tree
from nltk.util import (
    LazyConcatenation as LazyConcatenation,
)
from nltk.util import (
    LazyMap as LazyMap,
)

class ConllCorpusReader(CorpusReader):
    WORDS: str
    POS: str
    TREE: str
    CHUNK: str
    NE: str
    SRL: str
    IGNORE: str
    COLUMN_TYPES: Incomplete
    sep: Incomplete
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        columntypes: Incomplete,
        chunk_types: Incomplete | None = None,
        root_label: str = "S",
        pos_in_tree: bool = False,
        srl_includes_roleset: bool = True,
        encoding: str = "utf8",
        tree_class: Incomplete = ...,
        tagset: Incomplete | None = None,
        separator: Incomplete | None = None,
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
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
    def chunked_words(
        self,
        fileids: Incomplete | None = None,
        chunk_types: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def chunked_sents(
        self,
        fileids: Incomplete | None = None,
        chunk_types: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def parsed_sents(
        self,
        fileids: Incomplete | None = None,
        pos_in_tree: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def srl_spans(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def srl_instances(
        self,
        fileids: Incomplete | None = None,
        pos_in_tree: Incomplete | None = None,
        flatten: bool = True,
    ) -> Incomplete: ...
    def iob_words(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def iob_sents(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...

class ConllSRLInstance:
    verb: Incomplete
    verb_head: Incomplete
    verb_stem: Incomplete
    roleset: Incomplete
    arguments: Incomplete
    tagged_spans: Incomplete
    tree: Incomplete
    words: Incomplete
    def __init__(
        self,
        tree: Incomplete,
        verb_head: Incomplete,
        verb_stem: Incomplete,
        roleset: Incomplete,
        tagged_spans: Incomplete,
    ) -> None: ...
    def pprint(self) -> Incomplete: ...

class ConllSRLInstanceList(list):
    tree: Incomplete
    def __init__(
        self, tree: Incomplete, instances: Incomplete = ()
    ) -> None: ...
    def pprint(self, include_tree: bool = False) -> Incomplete: ...

class ConllChunkCorpusReader(ConllCorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        chunk_types: Incomplete,
        encoding: str = "utf8",
        tagset: Incomplete | None = None,
        separator: Incomplete | None = None,
    ) -> None: ...
