from collections.abc import Generator

from _typeshed import Incomplete

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
from nltk.parse.chart import (
    FilteredBottomUpPredictCombineRule as FilteredBottomUpPredictCombineRule,
)
from nltk.parse.chart import (
    FilteredSingleEdgeFundamentalRule as FilteredSingleEdgeFundamentalRule,
)
from nltk.parse.chart import LeafEdge as LeafEdge
from nltk.parse.chart import LeafInitRule as LeafInitRule
from nltk.parse.chart import (
    SingleEdgeFundamentalRule as SingleEdgeFundamentalRule,
)
from nltk.parse.chart import TopDownInitRule as TopDownInitRule
from nltk.parse.featurechart import (
    FeatureBottomUpPredictCombineRule as FeatureBottomUpPredictCombineRule,
)
from nltk.parse.featurechart import (
    FeatureBottomUpPredictRule as FeatureBottomUpPredictRule,
)
from nltk.parse.featurechart import FeatureChart as FeatureChart
from nltk.parse.featurechart import FeatureChartParser as FeatureChartParser
from nltk.parse.featurechart import (
    FeatureEmptyPredictRule as FeatureEmptyPredictRule,
)
from nltk.parse.featurechart import (
    FeatureSingleEdgeFundamentalRule as FeatureSingleEdgeFundamentalRule,
)
from nltk.parse.featurechart import (
    FeatureTopDownInitRule as FeatureTopDownInitRule,
)
from nltk.parse.featurechart import (
    FeatureTopDownPredictRule as FeatureTopDownPredictRule,
)

class IncrementalChart(Chart):
    def initialize(self) -> None: ...
    def edges(self) -> Incomplete: ...
    def iteredges(self) -> Incomplete: ...
    def select(
        self, end: Incomplete, **restrictions: Incomplete
    ) -> Incomplete: ...

class FeatureIncrementalChart(IncrementalChart, FeatureChart):
    def select(
        self, end: Incomplete, **restrictions: Incomplete
    ) -> Incomplete: ...

class CompleteFundamentalRule(SingleEdgeFundamentalRule): ...

class CompleterRule(CompleteFundamentalRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class ScannerRule(CompleteFundamentalRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class PredictorRule(CachedTopDownPredictRule): ...

class FilteredCompleteFundamentalRule(FilteredSingleEdgeFundamentalRule):
    def apply(
        self, chart: Incomplete, grammar: Incomplete, edge: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class FeatureCompleteFundamentalRule(FeatureSingleEdgeFundamentalRule): ...
class FeatureCompleterRule(CompleterRule): ...
class FeatureScannerRule(ScannerRule): ...
class FeaturePredictorRule(FeatureTopDownPredictRule): ...

EARLEY_STRATEGY: Incomplete
TD_INCREMENTAL_STRATEGY: Incomplete
BU_INCREMENTAL_STRATEGY: Incomplete
BU_LC_INCREMENTAL_STRATEGY: Incomplete
LC_INCREMENTAL_STRATEGY: Incomplete

class IncrementalChartParser(ChartParser):
    def __init__(
        self,
        grammar: Incomplete,
        strategy: Incomplete = ...,
        trace: int = 0,
        trace_chart_width: int = 50,
        chart_class: Incomplete = ...,
    ) -> None: ...
    def chart_parse(
        self, tokens: Incomplete, trace: Incomplete | None = None
    ) -> Incomplete: ...

class EarleyChartParser(IncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class IncrementalTopDownChartParser(IncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class IncrementalBottomUpChartParser(IncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class IncrementalBottomUpLeftCornerChartParser(IncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class IncrementalLeftCornerChartParser(IncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

EARLEY_FEATURE_STRATEGY: Incomplete
TD_INCREMENTAL_FEATURE_STRATEGY: Incomplete
BU_INCREMENTAL_FEATURE_STRATEGY: Incomplete
BU_LC_INCREMENTAL_FEATURE_STRATEGY: Incomplete

class FeatureIncrementalChartParser(
    IncrementalChartParser, FeatureChartParser
):
    def __init__(
        self,
        grammar: Incomplete,
        strategy: Incomplete = ...,
        trace_chart_width: int = 20,
        chart_class: Incomplete = ...,
        **parser_args: Incomplete,
    ) -> None: ...

class FeatureEarleyChartParser(FeatureIncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class FeatureIncrementalTopDownChartParser(FeatureIncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class FeatureIncrementalBottomUpChartParser(FeatureIncrementalChartParser):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

class FeatureIncrementalBottomUpLeftCornerChartParser(
    FeatureIncrementalChartParser
):
    def __init__(
        self, grammar: Incomplete, **parser_args: Incomplete
    ) -> None: ...

def demo(
    print_times: bool = True,
    print_grammar: bool = False,
    print_trees: bool = True,
    trace: int = 2,
    sent: str = "I saw John with a dog with my cookie",
    numparses: int = 5,
) -> None: ...
