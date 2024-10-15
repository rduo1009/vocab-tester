from _typeshed import Incomplete

from nltk.draw.tree import (
    TreeSegmentWidget as TreeSegmentWidget,
)
from nltk.draw.tree import (
    tree_to_treesegment as tree_to_treesegment,
)
from nltk.draw.util import (
    CanvasFrame as CanvasFrame,
)
from nltk.draw.util import (
    ColorizedList as ColorizedList,
)
from nltk.draw.util import (
    ShowText as ShowText,
)
from nltk.draw.util import (
    SymbolWidget as SymbolWidget,
)
from nltk.draw.util import (
    TextWidget as TextWidget,
)
from nltk.grammar import (
    CFG as CFG,
)
from nltk.grammar import (
    Nonterminal as Nonterminal,
)
from nltk.grammar import (
    nonterminals as nonterminals,
)
from nltk.tree import Tree as Tree

class ProductionList(ColorizedList):
    ARROW: Incomplete

class CFGEditor:
    ARROW: Incomplete
    def __init__(
        self,
        parent: Incomplete,
        cfg: Incomplete | None = None,
        set_cfg_callback: Incomplete | None = None,
    ) -> None: ...

class CFGDemo:
    def __init__(self, grammar: Incomplete, text: Incomplete) -> None: ...
    def reset_workspace(self) -> None: ...
    def workspace_markprod(self, production: Incomplete) -> None: ...
    def destroy(self, *args: Incomplete) -> None: ...
    def mainloop(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

def demo2() -> None: ...
def demo() -> None: ...
def demo3() -> None: ...
