from collections.abc import Generator

from _typeshed import Incomplete

from nltk.draw import CFGEditor as CFGEditor
from nltk.draw import TreeSegmentWidget as TreeSegmentWidget
from nltk.draw import tree_to_treesegment as tree_to_treesegment
from nltk.draw.util import CanvasFrame as CanvasFrame
from nltk.draw.util import ColorizedList as ColorizedList
from nltk.draw.util import EntryDialog as EntryDialog
from nltk.draw.util import MutableOptionMenu as MutableOptionMenu
from nltk.draw.util import ShowText as ShowText
from nltk.draw.util import SymbolWidget as SymbolWidget
from nltk.grammar import CFG as CFG
from nltk.grammar import Nonterminal as Nonterminal
from nltk.parse.chart import (
    BottomUpPredictCombineRule as BottomUpPredictCombineRule,
)
from nltk.parse.chart import BottomUpPredictRule as BottomUpPredictRule
from nltk.parse.chart import Chart as Chart
from nltk.parse.chart import LeafEdge as LeafEdge
from nltk.parse.chart import LeafInitRule as LeafInitRule
from nltk.parse.chart import (
    SingleEdgeFundamentalRule as SingleEdgeFundamentalRule,
)
from nltk.parse.chart import SteppingChartParser as SteppingChartParser
from nltk.parse.chart import TopDownInitRule as TopDownInitRule
from nltk.parse.chart import TopDownPredictRule as TopDownPredictRule
from nltk.parse.chart import TreeEdge as TreeEdge
from nltk.tree import Tree as Tree
from nltk.util import in_idle as in_idle

class EdgeList(ColorizedList):
    ARROW: Incomplete

class ChartMatrixView:
    def __init__(
        self,
        parent: Incomplete,
        chart: Incomplete,
        toplevel: bool = True,
        title: str = "Chart Matrix",
        show_numedges: bool = False,
    ) -> None: ...
    def destroy(self, *e: Incomplete) -> None: ...
    def set_chart(self, chart: Incomplete) -> None: ...
    def update(self) -> None: ...
    def activate(self) -> None: ...
    def inactivate(self) -> None: ...
    def add_callback(self, event: Incomplete, func: Incomplete) -> None: ...
    def remove_callback(
        self, event: Incomplete, func: Incomplete | None = None
    ) -> None: ...
    def select_cell(self, i: Incomplete, j: Incomplete) -> None: ...
    def deselect_cell(self) -> None: ...
    def view_edge(self, edge: Incomplete) -> None: ...
    def mark_edge(self, edge: Incomplete) -> None: ...
    def unmark_edge(self, edge: Incomplete | None = None) -> None: ...
    def markonly_edge(self, edge: Incomplete) -> None: ...
    def draw(self) -> None: ...
    def pack(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class ChartResultsView:
    def __init__(
        self,
        parent: Incomplete,
        chart: Incomplete,
        grammar: Incomplete,
        toplevel: bool = True,
    ) -> None: ...
    def update(self, edge: Incomplete | None = None) -> None: ...
    def print_all(self, *e: Incomplete) -> None: ...
    def print_selection(self, *e: Incomplete) -> None: ...
    def clear(self) -> None: ...
    def set_chart(self, chart: Incomplete) -> None: ...
    def set_grammar(self, grammar: Incomplete) -> None: ...
    def destroy(self, *e: Incomplete) -> None: ...
    def pack(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class ChartComparer:
    def __init__(self, *chart_filename: Incomplete) -> None: ...
    def destroy(self, *e: Incomplete) -> None: ...
    def mainloop(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    CHART_FILE_TYPES: Incomplete
    def save_chart_dialog(self, *args: Incomplete) -> None: ...
    def load_chart_dialog(self, *args: Incomplete) -> None: ...
    def load_chart(self, filename: Incomplete) -> None: ...
    def select_edge(self, edge: Incomplete) -> None: ...
    def select_cell(self, i: Incomplete, j: Incomplete) -> None: ...

class ChartView:
    def __init__(
        self,
        chart: Incomplete,
        root: Incomplete | None = None,
        **kw: Incomplete,
    ) -> None: ...
    def scroll_up(self, *e: Incomplete) -> None: ...
    def scroll_down(self, *e: Incomplete) -> None: ...
    def page_up(self, *e: Incomplete) -> None: ...
    def page_down(self, *e: Incomplete) -> None: ...
    def set_font_size(self, size: Incomplete) -> None: ...
    def get_font_size(self) -> Incomplete: ...
    def update(self, chart: Incomplete | None = None) -> None: ...
    def view_edge(self, edge: Incomplete) -> None: ...
    def mark_edge(self, edge: Incomplete, mark: str = "#0df") -> None: ...
    def unmark_edge(self, edge: Incomplete | None = None) -> None: ...
    def markonly_edge(self, edge: Incomplete, mark: str = "#0df") -> None: ...
    def erase_tree(self) -> None: ...
    def draw_tree(self, edge: Incomplete | None = None) -> None: ...
    def cycle_tree(self) -> None: ...
    def draw(self) -> None: ...
    def add_callback(self, event: Incomplete, func: Incomplete) -> None: ...
    def remove_callback(
        self, event: Incomplete, func: Incomplete | None = None
    ) -> None: ...

class EdgeRule:
    NUM_EDGES: Incomplete
    def __init__(self, edge: Incomplete) -> None: ...
    def apply(
        self, chart: Incomplete, grammar: Incomplete, *e: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class TopDownPredictEdgeRule(EdgeRule, TopDownPredictRule): ...  # type: ignore[misc]
class BottomUpEdgeRule(EdgeRule, BottomUpPredictRule): ...  # type: ignore[misc]
class BottomUpLeftCornerEdgeRule(EdgeRule, BottomUpPredictCombineRule): ...  # type: ignore[misc]
class FundamentalEdgeRule(EdgeRule, SingleEdgeFundamentalRule): ...  # type: ignore[misc]

class ChartParserApp:
    def __init__(
        self,
        grammar: Incomplete,
        tokens: Incomplete,
        title: str = "Chart Parser Application",
    ) -> None: ...
    def destroy(self, *args: Incomplete) -> None: ...
    def mainloop(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def help(self, *e: Incomplete) -> None: ...
    def about(self, *e: Incomplete) -> None: ...
    CHART_FILE_TYPES: Incomplete
    GRAMMAR_FILE_TYPES: Incomplete
    def load_chart(self, *args: Incomplete) -> None: ...
    def save_chart(self, *args: Incomplete) -> None: ...
    def load_grammar(self, *args: Incomplete) -> None: ...
    def save_grammar(self, *args: Incomplete) -> None: ...
    def reset(self, *args: Incomplete) -> None: ...
    def edit_grammar(self, *e: Incomplete) -> None: ...
    def set_grammar(self, grammar: Incomplete) -> None: ...
    def edit_sentence(self, *e: Incomplete) -> None: ...
    def set_sentence(self, sentence: Incomplete) -> None: ...
    def view_matrix(self, *e: Incomplete) -> None: ...
    def view_results(self, *e: Incomplete) -> None: ...
    def resize(self) -> None: ...
    def set_font_size(self, size: Incomplete) -> None: ...
    def get_font_size(self) -> Incomplete: ...
    def apply_strategy(
        self, strategy: Incomplete, edge_strategy: Incomplete | None = None
    ) -> None: ...
    def top_down_init(self, *e: Incomplete) -> None: ...
    def top_down_predict(self, *e: Incomplete) -> None: ...
    def bottom_up(self, *e: Incomplete) -> None: ...
    def bottom_up_leftcorner(self, *e: Incomplete) -> None: ...
    def fundamental(self, *e: Incomplete) -> None: ...
    def bottom_up_strategy(self, *e: Incomplete) -> None: ...
    def bottom_up_leftcorner_strategy(self, *e: Incomplete) -> None: ...
    def top_down_strategy(self, *e: Incomplete) -> None: ...

def app() -> None: ...
