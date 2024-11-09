from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.xmldocs import *
from nltk.internals import ElementWrapper as ElementWrapper
from nltk.tag import map_tag as map_tag
from nltk.util import LazyConcatenation as LazyConcatenation

class NPSChatCorpusReader(XMLCorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        wrap_etree: bool = False,
        tagset: Incomplete | None = None,
    ) -> None: ...
    def xml_posts(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def posts(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_posts(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
