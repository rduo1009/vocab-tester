from _typeshed import Incomplete

from nltk.decorators import decorator as decorator
from nltk.sem.logic import (
    AbstractVariableExpression as AbstractVariableExpression,
)
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
    EqualityExpression as EqualityExpression,
)
from nltk.sem.logic import (
    ExistsExpression as ExistsExpression,
)
from nltk.sem.logic import (
    Expression as Expression,
)
from nltk.sem.logic import (
    IffExpression as IffExpression,
)
from nltk.sem.logic import (
    ImpExpression as ImpExpression,
)
from nltk.sem.logic import (
    IndividualVariableExpression as IndividualVariableExpression,
)
from nltk.sem.logic import (
    IotaExpression as IotaExpression,
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
from nltk.sem.logic import (
    Variable as Variable,
)
from nltk.sem.logic import (
    is_indvar as is_indvar,
)

class Error(Exception): ...
class Undefined(Error): ...

def trace(
    f: Incomplete, *args: Incomplete, **kw: Incomplete
) -> Incomplete: ...
def is_rel(s: Incomplete) -> Incomplete: ...
def set2rel(s: Incomplete) -> Incomplete: ...
def arity(rel: Incomplete) -> Incomplete: ...

class Valuation(dict):
    def __init__(self, xs: Incomplete) -> None: ...
    def __getitem__(self, key: Incomplete) -> Incomplete: ...
    @property
    def domain(self) -> Incomplete: ...
    @property
    def symbols(self) -> Incomplete: ...
    @classmethod
    def fromstring(cls: Incomplete, s: Incomplete) -> Incomplete: ...

def read_valuation(
    s: Incomplete, encoding: Incomplete | None = None
) -> Incomplete: ...

class Assignment(dict):
    domain: Incomplete
    variant: Incomplete
    def __init__(
        self, domain: Incomplete, assign: Incomplete | None = None
    ) -> None: ...
    def __getitem__(self, key: Incomplete) -> Incomplete: ...
    def copy(self) -> Incomplete: ...
    def purge(self, var: Incomplete | None = None) -> None: ...
    def add(self, var: Incomplete, val: Incomplete) -> Incomplete: ...

class Model:
    domain: Incomplete
    valuation: Incomplete
    def __init__(self, domain: Incomplete, valuation: Incomplete) -> None: ...
    def evaluate(
        self, expr: Incomplete, g: Incomplete, trace: Incomplete | None = None
    ) -> Incomplete: ...
    def satisfy(
        self,
        parsed: Incomplete,
        g: Incomplete,
        trace: Incomplete | None = None,
    ) -> Incomplete: ...
    def i(
        self, parsed: Incomplete, g: Incomplete, trace: bool = False
    ) -> Incomplete: ...
    def satisfiers(
        self,
        parsed: Incomplete,
        varex: Incomplete,
        g: Incomplete,
        trace: Incomplete | None = None,
        nesting: int = 0,
    ) -> Incomplete: ...

mult: int

def propdemo(trace: Incomplete | None = None) -> None: ...
def folmodel(quiet: bool = False, trace: Incomplete | None = None) -> None: ...
def foldemo(trace: Incomplete | None = None) -> None: ...
def satdemo(trace: Incomplete | None = None) -> None: ...
def demo(num: int = 0, trace: Incomplete | None = None) -> None: ...
