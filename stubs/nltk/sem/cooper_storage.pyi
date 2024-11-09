from _typeshed import Incomplete

from nltk.parse import load_parser as load_parser
from nltk.parse.featurechart import (
    InstantiateVarsChart as InstantiateVarsChart,
)
from nltk.sem.logic import (
    ApplicationExpression as ApplicationExpression,
)
from nltk.sem.logic import (
    LambdaExpression as LambdaExpression,
)
from nltk.sem.logic import (
    Variable as Variable,
)

class CooperStore:
    featstruct: Incomplete
    readings: Incomplete
    core: Incomplete
    store: Incomplete
    def __init__(self, featstruct: Incomplete) -> None: ...
    def s_retrieve(self, trace: bool = False) -> None: ...

def parse_with_bindops(
    sentence: Incomplete, grammar: Incomplete | None = None, trace: int = 0
) -> Incomplete: ...
def demo() -> None: ...
