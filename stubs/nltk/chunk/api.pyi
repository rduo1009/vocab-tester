from _typeshed import Incomplete

from nltk.chunk.util import ChunkScore as ChunkScore
from nltk.internals import deprecated as deprecated
from nltk.parse import ParserI as ParserI

class ChunkParserI(ParserI):
    def parse(self, tokens: Incomplete) -> None: ...
    def evaluate(self, gold: Incomplete) -> Incomplete: ...
    def accuracy(self, gold: Incomplete) -> Incomplete: ...
