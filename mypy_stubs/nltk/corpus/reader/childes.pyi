from _typeshed import Incomplete

from nltk.corpus.reader.util import concat as concat
from nltk.corpus.reader.xmldocs import (
    ElementTree as ElementTree,
)
from nltk.corpus.reader.xmldocs import (
    XMLCorpusReader as XMLCorpusReader,
)
from nltk.util import (
    LazyConcatenation as LazyConcatenation,
)
from nltk.util import (
    LazyMap as LazyMap,
)
from nltk.util import (
    flatten as flatten,
)

__docformat__: str
NS: str

class CHILDESCorpusReader(XMLCorpusReader):
    def __init__(
        self, root: Incomplete, fileids: Incomplete, lazy: bool = True
    ) -> None: ...
    def words(
        self,
        fileids: Incomplete | None = None,
        speaker: str = "ALL",
        stem: bool = False,
        relation: bool = False,
        strip_space: bool = True,
        replace: bool = False,
    ) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        speaker: str = "ALL",
        stem: bool = False,
        relation: bool = False,
        strip_space: bool = True,
        replace: bool = False,
    ) -> Incomplete: ...
    def sents(
        self,
        fileids: Incomplete | None = None,
        speaker: str = "ALL",
        stem: bool = False,
        relation: Incomplete | None = None,
        strip_space: bool = True,
        replace: bool = False,
    ) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        speaker: str = "ALL",
        stem: bool = False,
        relation: Incomplete | None = None,
        strip_space: bool = True,
        replace: bool = False,
    ) -> Incomplete: ...
    def corpus(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def participants(
        self, fileids: Incomplete | None = None
    ) -> Incomplete: ...
    def age(
        self,
        fileids: Incomplete | None = None,
        speaker: str = "CHI",
        month: bool = False,
    ) -> Incomplete: ...
    def convert_age(self, age_year: Incomplete) -> Incomplete: ...
    def MLU(
        self, fileids: Incomplete | None = None, speaker: str = "CHI"
    ) -> Incomplete: ...
    childes_url_base: str
    def webview_file(
        self, fileid: Incomplete, urlbase: Incomplete | None = None
    ) -> None: ...

def demo(corpus_root: Incomplete | None = None) -> None: ...
