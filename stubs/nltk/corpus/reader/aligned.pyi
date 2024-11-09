from _typeshed import Incomplete

from nltk.corpus.reader.api import CorpusReader as CorpusReader
from nltk.corpus.reader.util import (
    StreamBackedCorpusView as StreamBackedCorpusView,
)
from nltk.corpus.reader.util import (
    concat as concat,
)
from nltk.corpus.reader.util import (
    read_alignedsent_block as read_alignedsent_block,
)
from nltk.tokenize import (
    RegexpTokenizer as RegexpTokenizer,
)
from nltk.tokenize import (
    WhitespaceTokenizer as WhitespaceTokenizer,
)
from nltk.translate import AlignedSent as AlignedSent
from nltk.translate import Alignment as Alignment

class AlignedCorpusReader(CorpusReader):
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        sep: str = "/",
        word_tokenizer: Incomplete = ...,
        sent_tokenizer: Incomplete = ...,
        alignedsent_block_reader: Incomplete = ...,
        encoding: str = "latin1",
    ) -> None: ...
    def words(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def sents(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def aligned_sents(
        self, fileids: Incomplete | None = None
    ) -> Incomplete: ...

class AlignedSentCorpusView(StreamBackedCorpusView):
    def __init__(
        self,
        corpus_file: Incomplete,
        encoding: Incomplete,
        aligned: Incomplete,
        group_by_sent: Incomplete,
        word_tokenizer: Incomplete,
        sent_tokenizer: Incomplete,
        alignedsent_block_reader: Incomplete,
    ) -> None: ...
    def read_block(self, stream: Incomplete) -> Incomplete: ...
