from collections.abc import Generator

from _typeshed import Incomplete

from nltk.data import load as load
from nltk.grammar import (
    CFG as CFG,
)
from nltk.grammar import (
    PCFG as PCFG,
)
from nltk.grammar import (
    FeatureGrammar as FeatureGrammar,
)
from nltk.parse.chart import Chart as Chart
from nltk.parse.chart import ChartParser as ChartParser
from nltk.parse.featurechart import (
    FeatureChart as FeatureChart,
)
from nltk.parse.featurechart import (
    FeatureChartParser as FeatureChartParser,
)
from nltk.parse.pchart import InsideChartParser as InsideChartParser

def load_parser(
    grammar_url: Incomplete,
    trace: int = 0,
    parser: Incomplete | None = None,
    chart_class: Incomplete | None = None,
    beam_size: int = 0,
    **load_args: Incomplete,
) -> Incomplete: ...
def taggedsent_to_conll(
    sentence: Incomplete,
) -> Generator[Incomplete, None, None]: ...
def taggedsents_to_conll(
    sentences: Incomplete,
) -> Generator[Incomplete, Incomplete, None]: ...

class TestGrammar:
    test_grammar: Incomplete
    cp: Incomplete
    suite: Incomplete
    def __init__(
        self,
        grammar: Incomplete,
        suite: Incomplete,
        accept: Incomplete | None = None,
        reject: Incomplete | None = None,
    ) -> None: ...
    def run(self, show_trees: bool = False) -> None: ...

def extract_test_sentences(
    string: Incomplete,
    comment_chars: str = "#%;",
    encoding: Incomplete | None = None,
) -> Incomplete: ...
