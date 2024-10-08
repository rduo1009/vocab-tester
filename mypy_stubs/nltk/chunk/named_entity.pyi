from collections.abc import Generator

from _typeshed import Incomplete

from nltk.chunk.api import ChunkParserI as ChunkParserI
from nltk.chunk.util import ChunkScore as ChunkScore
from nltk.classify import MaxentClassifier as MaxentClassifier
from nltk.data import find as find
from nltk.tag import ClassifierBasedTagger as ClassifierBasedTagger
from nltk.tag import pos_tag as pos_tag
from nltk.tokenize import word_tokenize as word_tokenize
from nltk.tree import Tree as Tree

class NEChunkParserTagger(ClassifierBasedTagger):
    def __init__(
        self,
        train: Incomplete | None = None,
        classifier: Incomplete | None = None,
    ) -> None: ...

class NEChunkParser(ChunkParserI):
    def __init__(self, train: Incomplete) -> None: ...
    def parse(self, tokens: Incomplete) -> Incomplete: ...

def shape(word: Incomplete) -> Incomplete: ...
def simplify_pos(s: Incomplete) -> Incomplete: ...
def postag_tree(tree: Incomplete) -> Incomplete: ...
def load_ace_data(
    roots: Incomplete, fmt: str = "binary", skip_bnews: bool = True
) -> Generator[Incomplete, Incomplete, None]: ...
def load_ace_file(
    textfile: Incomplete, fmt: Incomplete
) -> Generator[Incomplete, None, Incomplete]: ...
def cmp_chunks(correct: Incomplete, guessed: Incomplete) -> None: ...

class Maxent_NE_Chunker(NEChunkParser):
    def __init__(self, fmt: str = "multiclass") -> None: ...
    def load_params(self) -> None: ...
    def save_params(self) -> None: ...

def build_model(fmt: str = "multiclass") -> Incomplete: ...
