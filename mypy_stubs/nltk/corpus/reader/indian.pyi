from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.tag import map_tag as map_tag
from nltk.tag import str2tuple as str2tuple

class IndianCorpusReader(CorpusReader):
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_words(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def tagged_sents(
        self,
        fileids: Incomplete | None = None,
        tagset: Incomplete | None = None,
    ) -> Incomplete: ...

class IndianCorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        corpus_file: Incomplete,
        encoding: Incomplete,
        tagged: Incomplete,
        group_by_sent: Incomplete,
        tag_mapping_function: Incomplete | None = None,
    ) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...
