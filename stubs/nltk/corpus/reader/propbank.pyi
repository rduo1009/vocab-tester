from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.internals import raise_unorderable_types as raise_unorderable_types
from nltk.tree import Tree as Tree

class PropbankCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        propfile: Incomplete,
        framefiles: str = "",
        verbsfile: Incomplete | None = None,
        parse_fileid_xform: Incomplete | None = None,
        parse_corpus: Incomplete | None = None,
        encoding: str = "utf8",
    ) -> None: ...
    def instances(self, baseform: Incomplete | None = None) -> Incomplete: ...
    def lines(self) -> Incomplete: ...
    def roleset(self, roleset_id: Incomplete) -> Incomplete: ...
    def rolesets(self, baseform: Incomplete | None = None) -> Incomplete: ...
    def verbs(self) -> Incomplete: ...

class PropbankInstance:
    fileid: Incomplete
    sentnum: Incomplete
    wordnum: Incomplete
    tagger: Incomplete
    roleset: Incomplete
    inflection: Incomplete
    predicate: Incomplete
    arguments: Incomplete
    parse_corpus: Incomplete
    def __init__(
        self,
        fileid: Incomplete,
        sentnum: Incomplete,
        wordnum: Incomplete,
        tagger: Incomplete,
        roleset: Incomplete,
        inflection: Incomplete,
        predicate: Incomplete,
        arguments: Incomplete,
        parse_corpus: Incomplete | None = None,
    ) -> None: ...
    @property
    def baseform(self) -> Incomplete: ...
    @property
    def sensenumber(self) -> Incomplete: ...
    @property
    def predid(self) -> Incomplete: ...
    tree: Incomplete
    @staticmethod
    def parse(
        s: Incomplete,
        parse_fileid_xform: Incomplete | None = None,
        parse_corpus: Incomplete | None = None,
    ) -> Incomplete: ...

class PropbankPointer:
    def __init__(self) -> None: ...

class PropbankChainTreePointer(PropbankPointer):
    pieces: Incomplete
    def __init__(self, pieces: Incomplete) -> None: ...
    def select(self, tree: Incomplete) -> Incomplete: ...

class PropbankSplitTreePointer(PropbankPointer):
    pieces: Incomplete
    def __init__(self, pieces: Incomplete) -> None: ...
    def select(self, tree: Incomplete) -> Incomplete: ...

class PropbankTreePointer(PropbankPointer):
    wordnum: Incomplete
    height: Incomplete
    def __init__(self, wordnum: Incomplete, height: Incomplete) -> None: ...
    @staticmethod
    def parse(s: Incomplete) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def select(self, tree: Incomplete) -> Incomplete: ...
    def treepos(self, tree: Incomplete) -> Incomplete: ...

class PropbankInflection:
    INFINITIVE: str
    GERUND: str
    PARTICIPLE: str
    FINITE: str
    FUTURE: str
    PAST: str
    PRESENT: str
    PERFECT: str
    PROGRESSIVE: str
    PERFECT_AND_PROGRESSIVE: str
    THIRD_PERSON: str
    ACTIVE: str
    PASSIVE: str
    NONE: str
    form: Incomplete
    tense: Incomplete
    aspect: Incomplete
    person: Incomplete
    voice: Incomplete
    def __init__(
        self,
        form: str = "-",
        tense: str = "-",
        aspect: str = "-",
        person: str = "-",
        voice: str = "-",
    ) -> None: ...
    @staticmethod
    def parse(s: Incomplete) -> Incomplete: ...
