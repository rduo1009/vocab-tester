from collections.abc import Generator

from _typeshed import Incomplete

from nltk.grammar import PCFG as PCFG
from nltk.grammar import Nonterminal as Nonterminal
from nltk.parse.api import ParserI as ParserI
from nltk.parse.chart import (
    AbstractChartRule as AbstractChartRule,
)
from nltk.parse.chart import (
    Chart as Chart,
)
from nltk.parse.chart import (
    LeafEdge as LeafEdge,
)
from nltk.parse.chart import (
    TreeEdge as TreeEdge,
)
from nltk.tree import ProbabilisticTree as ProbabilisticTree
from nltk.tree import Tree as Tree

class ProbabilisticLeafEdge(LeafEdge):
    def prob(self) -> Incomplete: ...

class ProbabilisticTreeEdge(TreeEdge):
    def __init__(
        self, prob: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def prob(self) -> Incomplete: ...
    @staticmethod
    def from_production(
        production: Incomplete, index: Incomplete, p: Incomplete
    ) -> Incomplete: ...

class ProbabilisticBottomUpInitRule(AbstractChartRule):
    NUM_EDGES: int
    def apply(
        self, chart: Incomplete, grammar: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class ProbabilisticBottomUpPredictRule(AbstractChartRule):
    NUM_EDGES: int
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class ProbabilisticFundamentalRule(AbstractChartRule):
    NUM_EDGES: int
    def apply(
        self,
        chart: Incomplete,
        grammar: Incomplete,
        left_edge: Incomplete,
        right_edge: Incomplete,
    ) -> Generator[Incomplete, None, None]: ...

class SingleEdgeProbabilisticFundamentalRule(AbstractChartRule):
    NUM_EDGES: int
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge1: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class BottomUpProbabilisticChartParser(ParserI):
    beam_size: Incomplete
    def __init__(
        self, grammar: Incomplete, beam_size: int = 0, trace: int = 0
    ) -> None: ...
    def grammar(self) -> Incomplete: ...
    def trace(self, trace: int = 2) -> None: ...
    def parse(self, tokens: Incomplete) -> Incomplete: ...
    def sort_queue(self, queue: Incomplete, chart: Incomplete) -> None: ...

class InsideChartParser(BottomUpProbabilisticChartParser):
    def sort_queue(
        self, queue: Incomplete, chart: Incomplete
    ) -> Incomplete: ...

class RandomChartParser(BottomUpProbabilisticChartParser):
    def sort_queue(self, queue: Incomplete, chart: Incomplete) -> None: ...

class UnsortedChartParser(BottomUpProbabilisticChartParser):
    def sort_queue(self, queue: Incomplete, chart: Incomplete) -> None: ...

class LongestChartParser(BottomUpProbabilisticChartParser):
    def sort_queue(
        self, queue: Incomplete, chart: Incomplete
    ) -> Incomplete: ...

def demo(
    choice: Incomplete | None = None,
    draw_parses: Incomplete | None = None,
    print_parses: Incomplete | None = None,
) -> Incomplete: ...
