from _typeshed import Incomplete

from nltk.inference.api import (
    BaseProverCommand as BaseProverCommand,
)
from nltk.inference.api import (
    Prover as Prover,
)
from nltk.sem import skolemize as skolemize
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
    Expression as Expression,
)
from nltk.sem.logic import (
    IndividualVariableExpression as IndividualVariableExpression,
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
    VariableExpression as VariableExpression,
)
from nltk.sem.logic import (
    is_indvar as is_indvar,
)
from nltk.sem.logic import (
    unique_variable as unique_variable,
)

class ProverParseError(Exception): ...

class ResolutionProver(Prover):
    ANSWER_KEY: str

class ResolutionProverCommand(BaseProverCommand):
    def __init__(
        self,
        goal: Incomplete | None = None,
        assumptions: Incomplete | None = None,
        prover: Incomplete | None = None,
    ) -> None: ...
    def prove(self, verbose: bool = False) -> Incomplete: ...
    def find_answers(self, verbose: bool = False) -> Incomplete: ...

class Clause(list):
    def __init__(self, data: Incomplete) -> None: ...
    def unify(
        self,
        other: Incomplete,
        bindings: Incomplete | None = None,
        used: Incomplete | None = None,
        skipped: Incomplete | None = None,
        debug: bool = False,
    ) -> Incomplete: ...
    def isSubsetOf(self, other: Incomplete) -> Incomplete: ...
    def subsumes(self, other: Incomplete) -> Incomplete: ...
    def __getslice__(
        self, start: Incomplete, end: Incomplete
    ) -> Incomplete: ...
    def __sub__(self, other: Incomplete) -> Incomplete: ...
    def __add__(self, other: Incomplete) -> Incomplete: ...
    def is_tautology(self) -> Incomplete: ...
    def free(self) -> Incomplete: ...
    def replace(
        self, variable: Incomplete, expression: Incomplete
    ) -> Incomplete: ...
    def substitute_bindings(self, bindings: Incomplete) -> Incomplete: ...

def clausify(expression: Incomplete) -> Incomplete: ...

class BindingDict:
    d: Incomplete
    def __init__(self, binding_list: Incomplete | None = None) -> None: ...
    def __setitem__(
        self, variable: Incomplete, binding: Incomplete
    ) -> None: ...
    def __getitem__(self, variable: Incomplete) -> Incomplete: ...
    def __contains__(self, item: Incomplete) -> bool: ...
    def __add__(self, other: Incomplete) -> Incomplete: ...
    def __len__(self) -> int: ...

def most_general_unification(
    a: Incomplete, b: Incomplete, bindings: Incomplete | None = None
) -> Incomplete: ...

class BindingException(Exception):
    def __init__(self, arg: Incomplete) -> None: ...

class UnificationException(Exception):
    def __init__(self, a: Incomplete, b: Incomplete) -> None: ...

class DebugObject:
    enabled: Incomplete
    indent: Incomplete
    def __init__(self, enabled: bool = True, indent: int = 0) -> None: ...
    def __add__(self, i: Incomplete) -> Incomplete: ...
    def line(self, line: Incomplete) -> None: ...

def testResolutionProver() -> None: ...
def resolution_test(e: Incomplete) -> None: ...
def test_clausify() -> None: ...
def demo() -> None: ...
