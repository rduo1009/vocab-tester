from _typeshed import Incomplete

from nltk.corpus.reader.util import concat as concat
from nltk.corpus.reader.xmldocs import (
    ElementTree as ElementTree,
)
from nltk.corpus.reader.xmldocs import (
    XMLCorpusReader as XMLCorpusReader,
)
from nltk.corpus.reader.xmldocs import (
    XMLCorpusView as XMLCorpusView,
)

class BNCCorpusReader(XMLCorpusReader):
    def __init__(
        self, root: Incomplete, fileids: Incomplete, lazy: bool = True
    ) -> None: ...
    def words(
        self,
        fileids: Incomplete | None = None,
        strip_space: bool = True,
        stem: bool = False,
    ) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        c5: bool = False,
        strip_space: bool = True,
        stem: bool = False,
    ) -> Incomplete: ...
    def sents(
        self,
        fileids: Incomplete | None = None,
        strip_space: bool = True,
        stem: bool = False,
    ) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        c5: bool = False,
        strip_space: bool = True,
        stem: bool = False,
    ) -> Incomplete: ...

class BNCSentence(list):
    num: Incomplete
    def __init__(self, num: Incomplete, items: Incomplete) -> None: ...

class BNCWordView(XMLCorpusView):
    tags_to_ignore: Incomplete
    title: Incomplete
    author: Incomplete
    editor: Incomplete
    resps: Incomplete
    def __init__(
        self,
        fileid: Incomplete,
        sent: Incomplete,
        tag: Incomplete,
        strip_space: Incomplete,
        stem: Incomplete,
    ) -> None: ...
    def handle_header(self, elt: Incomplete, context: Incomplete) -> None: ...
    def handle_elt(
        self, elt: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def handle_word(self, elt: Incomplete) -> Incomplete: ...
    def handle_sent(self, elt: Incomplete) -> Incomplete: ...
