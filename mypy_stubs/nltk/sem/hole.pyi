from _typeshed import Incomplete

from nltk.parse import load_parser as load_parser
from nltk.sem.logic import (
    AllExpression as AllExpression,
)
from nltk.sem.logic import (
    AndExpression as AndExpression,
)
from nltk.sem.logic import (
    ApplicationExpression as ApplicationExpression,
)
from nltk.sem.logic import (
    ExistsExpression as ExistsExpression,
)
from nltk.sem.logic import (
    IffExpression as IffExpression,
)
from nltk.sem.logic import (
    ImpExpression as ImpExpression,
)
from nltk.sem.logic import (
    LambdaExpression as LambdaExpression,
)
from nltk.sem.logic import (
    NegatedExpression as NegatedExpression,
)
from nltk.sem.logic import (
    OrExpression as OrExpression,
)
from nltk.sem.skolemize import skolemize as skolemize

class Constants:
    ALL: str
    EXISTS: str
    NOT: str
    AND: str
    OR: str
    IMP: str
    IFF: str
    PRED: str
    LEQ: str
    HOLE: str
    LABEL: str
    MAP: Incomplete

class HoleSemantics:
    holes: Incomplete
    labels: Incomplete
    fragments: Incomplete
    constraints: Incomplete
    top_most_labels: Incomplete
    top_hole: Incomplete
    def __init__(self, usr: Incomplete) -> None: ...
    def is_node(self, x: Incomplete) -> Incomplete: ...
    def pluggings(self) -> Incomplete: ...
    def formula_tree(self, plugging: Incomplete) -> Incomplete: ...

class Constraint:
    lhs: Incomplete
    rhs: Incomplete
    def __init__(self, lhs: Incomplete, rhs: Incomplete) -> None: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...

def hole_readings(
    sentence: Incomplete,
    grammar_filename: Incomplete | None = None,
    verbose: bool = False,
) -> Incomplete: ...
