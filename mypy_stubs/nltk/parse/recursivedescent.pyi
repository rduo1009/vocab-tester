from _typeshed import Incomplete

from nltk.grammar import Nonterminal as Nonterminal
from nltk.parse.api import ParserI as ParserI
from nltk.tree import ImmutableTree as ImmutableTree
from nltk.tree import Tree as Tree

class RecursiveDescentParser(ParserI):
    def __init__(self, grammar: Incomplete, trace: int = 0) -> None: ...
    def grammar(self) -> Incomplete: ...
    def parse(self, tokens: Incomplete) -> Incomplete: ...
    def trace(self, trace: int = 2) -> None: ...

class SteppingRecursiveDescentParser(RecursiveDescentParser):
    def __init__(self, grammar: Incomplete, trace: int = 0) -> None: ...
    def parse(self, tokens: Incomplete) -> Incomplete: ...
    def initialize(self, tokens: Incomplete) -> None: ...
    def remaining_text(self) -> Incomplete: ...
    def frontier(self) -> Incomplete: ...
    def tree(self) -> Incomplete: ...
    def step(self) -> Incomplete: ...
    def expand(self, production: Incomplete | None = None) -> Incomplete: ...
    def match(self) -> Incomplete: ...
    def backtrack(self) -> Incomplete: ...
    def expandable_productions(self) -> Incomplete: ...
    def untried_expandable_productions(self) -> Incomplete: ...
    def untried_match(self) -> Incomplete: ...
    def currently_complete(self) -> Incomplete: ...
    def parses(self) -> Incomplete: ...
    def set_grammar(self, grammar: Incomplete) -> None: ...

def demo() -> None: ...
