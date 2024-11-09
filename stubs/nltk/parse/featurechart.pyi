from collections.abc import Generator

from _typeshed import Incomplete

from nltk.featstruct import TYPE as TYPE
from nltk.featstruct import FeatStruct as FeatStruct
from nltk.featstruct import find_variables as find_variables
from nltk.featstruct import unify as unify
from nltk.grammar import CFG as CFG
from nltk.grammar import FeatStructNonterminal as FeatStructNonterminal
from nltk.grammar import Nonterminal as Nonterminal
from nltk.grammar import Production as Production
from nltk.grammar import is_nonterminal as is_nonterminal
from nltk.grammar import is_terminal as is_terminal
from nltk.parse.chart import (
    BottomUpPredictCombineRule as BottomUpPredictCombineRule,
)
from nltk.parse.chart import BottomUpPredictRule as BottomUpPredictRule
from nltk.parse.chart import (
    CachedTopDownPredictRule as CachedTopDownPredictRule,
)
from nltk.parse.chart import Chart as Chart
from nltk.parse.chart import ChartParser as ChartParser
from nltk.parse.chart import EdgeI as EdgeI
from nltk.parse.chart import EmptyPredictRule as EmptyPredictRule
from nltk.parse.chart import FundamentalRule as FundamentalRule
from nltk.parse.chart import LeafInitRule as LeafInitRule
from nltk.parse.chart import (
    SingleEdgeFundamentalRule as SingleEdgeFundamentalRule,
)
from nltk.parse.chart import TopDownInitRule as TopDownInitRule
from nltk.parse.chart import TreeEdge as TreeEdge
from nltk.sem import logic as logic
from nltk.tree import Tree as Tree

class FeatureTreeEdge(TreeEdge):
    def __init__(
        self,
        span: Incomplete,
        lhs: Incomplete,
        rhs: Incomplete,
        dot: int = 0,
        bindings: Incomplete | None = None,
    ) -> None: ...
    @staticmethod
    def from_production(
        production: Incomplete, index: Incomplete
    ) -> Incomplete: ...
    def move_dot_forward(
        self, new_end: Incomplete, bindings: Incomplete | None = None
    ) -> Incomplete: ...
    def next_with_bindings(self) -> Incomplete: ...
    def bindings(self) -> Incomplete: ...
    def variables(self) -> Incomplete: ...

class FeatureChart(Chart):
    def select(self, **restrictions: Incomplete) -> Incomplete: ...
    def parses(
        self, start: Incomplete, tree_class: Incomplete = ...
    ) -> Generator[Incomplete, Incomplete, None]: ...

class FeatureFundamentalRule(FundamentalRule):
    def apply(
        self,
        chart: Incomplete,
        grammar: Incomplete,
        left_edge: Incomplete,
        right_edge: Incomplete,
    ) -> Generator[Incomplete, None, None]: ...

class FeatureSingleEdgeFundamentalRule(SingleEdgeFundamentalRule): ...

class FeatureTopDownInitRule(TopDownInitRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class FeatureTopDownPredictRule(CachedTopDownPredictRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class FeatureBottomUpPredictRule(BottomUpPredictRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class FeatureBottomUpPredictCombineRule(BottomUpPredictCombineRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class FeatureEmptyPredictRule(EmptyPredictRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

TD_FEATURE_STRATEGY: Incomplete
BU_FEATURE_STRATEGY: Incomplete
BU_LC_FEATURE_STRATEGY: Incomplete

class FeatureChartParser(ChartParser):
    def __init__(
        self,
        grammar: Incomplete,
        strategy: Incomplete = ...,
        trace_chart_width: int = 20,
        chart_class: Incomplete = ...,
        **parser_args: Incomplete,
    ) -> None: ...

class FeatureTopDownChartParser(FeatureChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class FeatureBottomUpChartParser(FeatureChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class FeatureBottomUpLeftCornerChartParser(FeatureChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class InstantiateVarsChart(FeatureChart):
    def __init__(self, tokens: Incomplete) -> None: ...
    def initialize(self) -> None: ...
    def insert(
        self, edge: Incomplete, child_pointer_list: Incomplete
    ) -> Incomplete: ...
    def instantiate_edge(self, edge: Incomplete) -> None: ...
    def inst_vars(self, edge: Incomplete) -> Incomplete: ...

def demo_grammar() -> Incomplete: ...
def demo(
    print_times: bool = True,
    print_grammar: bool = True,
    print_trees: bool = True,
    print_sentence: bool = True,
    trace: int = 1,
    parser: Incomplete = ...,
    sent: str = "I saw John with a dog with my cookie",
) -> None: ...
def run_profile() -> None: ...
