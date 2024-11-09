from _typeshed import Incomplete

from nltk.inference.api import (
    BaseProverCommand as BaseProverCommand,
)
from nltk.inference.api import (
    Prover as Prover,
)
from nltk.internals import Counter as Counter
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
    FunctionVariableExpression as FunctionVariableExpression,
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
from nltk.sem.logic import (
    Variable as Variable,
)
from nltk.sem.logic import (
    VariableExpression as VariableExpression,
)
from nltk.sem.logic import (
    unique_variable as unique_variable,
)

class ProverParseError(Exception): ...

class TableauProver(Prover):
    @staticmethod
    def is_atom(e: Incomplete) -> Incomplete: ...

class TableauProverCommand(BaseProverCommand):
    def __init__(
        self,
        goal: Incomplete | None = None,
        assumptions: Incomplete | None = None,
        prover: Incomplete | None = None,
    ) -> None: ...

class Agenda:
    sets: Incomplete
    def __init__(self) -> None: ...
    def clone(self) -> Incomplete: ...
    def __getitem__(self, index: Incomplete) -> Incomplete: ...
    def put(
        self, expression: Incomplete, context: Incomplete | None = None
    ) -> None: ...
    def put_all(self, expressions: Incomplete) -> None: ...
    def put_atoms(self, atoms: Incomplete) -> None: ...
    def pop_first(self) -> Incomplete: ...
    def replace_all(self, old: Incomplete, new: Incomplete) -> None: ...
    def mark_alls_fresh(self) -> None: ...
    def mark_neqs_fresh(self) -> None: ...

class Debug:
    verbose: Incomplete
    indent: Incomplete
    lines: Incomplete
    def __init__(
        self,
        verbose: Incomplete,
        indent: int = 0,
        lines: Incomplete | None = None,
    ) -> None: ...
    def __add__(self, increment: Incomplete) -> Incomplete: ...
    def line(self, data: Incomplete, indent: int = 0) -> None: ...

class Categories:
    ATOM: int
    PROP: int
    N_ATOM: int
    N_PROP: int
    APP: int
    N_APP: int
    N_EQ: int
    D_NEG: int
    N_ALL: int
    N_EXISTS: int
    AND: int
    N_OR: int
    N_IMP: int
    OR: int
    IMP: int
    N_AND: int
    IFF: int
    N_IFF: int
    EQ: int
    EXISTS: int
    ALL: int

def testTableauProver() -> None: ...
def testHigherOrderTableauProver() -> None: ...
def tableau_test(
    c: Incomplete, ps: Incomplete | None = None, verbose: bool = False
) -> None: ...
def demo() -> None: ...
