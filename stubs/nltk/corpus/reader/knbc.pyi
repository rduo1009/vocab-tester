from _typeshed import Incomplete

from nltk.corpus.reader.api import (
    CorpusReader as CorpusReader,
)
from nltk.corpus.reader.api import (
    SyntaxCorpusReader as SyntaxCorpusReader,
)
from nltk.corpus.reader.util import (
    FileSystemPathPointer as FileSystemPathPointer,
)
from nltk.corpus.reader.util import (
    find_corpus_fileids as find_corpus_fileids,
)
from nltk.corpus.reader.util import (
    read_blankline_block as read_blankline_block,
)
from nltk.parse import DependencyGraph as DependencyGraph

class KNBCorpusReader(SyntaxCorpusReader):
    morphs2str: Incomplete
    def __init__(
        self,
        root: Incomplete,
        fileids: Incomplete,
        encoding: str = "utf8",
        morphs2str: Incomplete = ...,
    ) -> None: ...

def demo() -> Incomplete: ...
def test() -> None: ...
