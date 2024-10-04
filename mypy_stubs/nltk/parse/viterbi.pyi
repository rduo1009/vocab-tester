from collections.abc import Generator

from _typeshed import Incomplete

from nltk.parse.api import ParserI as ParserI
from nltk.tree import ProbabilisticTree as ProbabilisticTree
from nltk.tree import Tree as Tree

class ViterbiParser(ParserI):
    def __init__(self, grammar: Incomplete, trace: int = 0) -> None: ...
    def grammar(self) -> Incomplete: ...
    def trace(self, trace: int = 2) -> None: ...
    def parse(
        self, tokens: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

def demo() -> Incomplete: ...
