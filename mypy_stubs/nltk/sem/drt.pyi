from _typeshed import Incomplete

from nltk.sem.logic import (
    APP as APP,
)
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
    BinaryExpression as BinaryExpression,
)
from nltk.sem.logic import (
    BooleanExpression as BooleanExpression,
)
from nltk.sem.logic import (
    ConstantExpression as ConstantExpression,
)
from nltk.sem.logic import (
    EqualityExpression as EqualityExpression,
)
from nltk.sem.logic import (
    EventVariableExpression as EventVariableExpression,
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
    ImpExpression as ImpExpression,
)
from nltk.sem.logic import (
    IndividualVariableExpression as IndividualVariableExpression,
)
from nltk.sem.logic import (
    LambdaExpression as LambdaExpression,
)
from nltk.sem.logic import (
    LogicParser as LogicParser,
)
from nltk.sem.logic import (
    NegatedExpression as NegatedExpression,
)
from nltk.sem.logic import (
    OrExpression as OrExpression,
)
from nltk.sem.logic import (
    Tokens as tokens,
)
from nltk.sem.logic import (
    Variable as Variable,
)
from nltk.sem.logic import (
    is_eventvar as is_eventvar,
)
from nltk.sem.logic import (
    is_funcvar as is_funcvar,
)
from nltk.sem.logic import (
    is_indvar as is_indvar,
)
from nltk.sem.logic import (
    unique_variable as unique_variable,
)
from nltk.util import in_idle as in_idle

class DrtTokens(tokens):
    DRS: str
    DRS_CONC: str
    PRONOUN: str
    OPEN_BRACKET: str
    CLOSE_BRACKET: str
    COLON: str
    PUNCT: Incomplete
    SYMBOLS: Incomplete
    TOKENS: Incomplete

class DrtParser(LogicParser):
    operator_precedence: Incomplete
    def __init__(self) -> None: ...
    def get_all_symbols(self) -> Incomplete: ...
    def isvariable(self, tok: Incomplete) -> Incomplete: ...
    def handle(self, tok: Incomplete, context: Incomplete) -> Incomplete: ...
    def make_NegatedExpression(self, expression: Incomplete) -> Incomplete: ...
    def handle_DRS(
        self, tok: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def handle_refs(self) -> Incomplete: ...
    def handle_conds(self, context: Incomplete) -> Incomplete: ...
    def handle_prop(
        self, tok: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def make_EqualityExpression(
        self, first: Incomplete, second: Incomplete
    ) -> Incomplete: ...
    def get_BooleanExpression_factory(self, tok: Incomplete) -> Incomplete: ...
    def make_BooleanExpression(
        self, factory: Incomplete, first: Incomplete, second: Incomplete
    ) -> Incomplete: ...
    def make_ApplicationExpression(
        self, function: Incomplete, argument: Incomplete
    ) -> Incomplete: ...
    def make_VariableExpression(self, name: Incomplete) -> Incomplete: ...
    def make_LambdaExpression(
        self, variables: Incomplete, term: Incomplete
    ) -> Incomplete: ...

class DrtExpression:
    @classmethod
    def fromstring(cls: Incomplete, s: Incomplete) -> Incomplete: ...
    def applyto(self, other: Incomplete) -> Incomplete: ...
    def __neg__(self) -> Incomplete: ...
    def __and__(self, other: Incomplete) -> Incomplete: ...
    def __or__(self, other: Incomplete) -> Incomplete: ...
    def __gt__(self, other: Incomplete) -> Incomplete: ...
    def equiv(
        self, other: Incomplete, prover: Incomplete | None = None
    ) -> Incomplete: ...
    @property
    def type(self) -> None: ...
    def typecheck(self, signature: Incomplete | None = None) -> None: ...
    def __add__(self, other: Incomplete) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> None: ...
    def is_pronoun_function(self) -> Incomplete: ...
    def make_EqualityExpression(
        self, first: Incomplete, second: Incomplete
    ) -> Incomplete: ...
    def make_VariableExpression(self, variable: Incomplete) -> Incomplete: ...
    def resolve_anaphora(self) -> Incomplete: ...
    def eliminate_equality(self) -> Incomplete: ...
    def pretty_format(self) -> Incomplete: ...
    def pretty_print(self) -> None: ...
    def draw(self) -> None: ...

class DRS(DrtExpression, Expression):
    refs: Incomplete
    conds: Incomplete
    consequent: Incomplete
    def __init__(
        self,
        refs: Incomplete,
        conds: Incomplete,
        consequent: Incomplete | None = None,
    ) -> None: ...
    def replace(
        self,
        variable: Incomplete,
        expression: Incomplete,
        replace_bound: bool = False,
        alpha_convert: bool = True,
    ) -> Incomplete: ...
    def free(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...
    def visit(
        self, function: Incomplete, combinator: Incomplete
    ) -> Incomplete: ...
    def visit_structured(
        self, function: Incomplete, combinator: Incomplete
    ) -> Incomplete: ...
    def eliminate_equality(self) -> Incomplete: ...
    def fol(self) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    __hash__: Incomplete

def DrtVariableExpression(variable: Incomplete) -> Incomplete: ...

class DrtAbstractVariableExpression(DrtExpression, AbstractVariableExpression):
    def fol(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...
    def eliminate_equality(self) -> Incomplete: ...

class DrtIndividualVariableExpression(
    DrtAbstractVariableExpression, IndividualVariableExpression
): ...
class DrtFunctionVariableExpression(
    DrtAbstractVariableExpression, FunctionVariableExpression
): ...
class DrtEventVariableExpression(
    DrtIndividualVariableExpression, EventVariableExpression
): ...
class DrtConstantExpression(
    DrtAbstractVariableExpression, ConstantExpression
): ...

class DrtProposition(DrtExpression, Expression):
    variable: Incomplete
    drs: Incomplete
    def __init__(self, variable: Incomplete, drs: Incomplete) -> None: ...
    def replace(
        self,
        variable: Incomplete,
        expression: Incomplete,
        replace_bound: bool = False,
        alpha_convert: bool = True,
    ) -> Incomplete: ...
    def eliminate_equality(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    __hash__: Incomplete
    def fol(self) -> Incomplete: ...
    def visit(
        self, function: Incomplete, combinator: Incomplete
    ) -> Incomplete: ...
    def visit_structured(
        self, function: Incomplete, combinator: Incomplete
    ) -> Incomplete: ...

class DrtNegatedExpression(DrtExpression, NegatedExpression):
    def fol(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...

class DrtLambdaExpression(DrtExpression, LambdaExpression):
    def alpha_convert(self, newvar: Incomplete) -> Incomplete: ...
    def fol(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...

class DrtBinaryExpression(DrtExpression, BinaryExpression):
    def get_refs(self, recursive: bool = False) -> Incomplete: ...

class DrtBooleanExpression(DrtBinaryExpression, BooleanExpression): ...

class DrtOrExpression(DrtBooleanExpression, OrExpression):
    def fol(self) -> Incomplete: ...

class DrtEqualityExpression(DrtBinaryExpression, EqualityExpression):
    def fol(self) -> Incomplete: ...

class DrtConcatenation(DrtBooleanExpression):
    consequent: Incomplete
    def __init__(
        self,
        first: Incomplete,
        second: Incomplete,
        consequent: Incomplete | None = None,
    ) -> None: ...
    def replace(
        self,
        variable: Incomplete,
        expression: Incomplete,
        replace_bound: bool = False,
        alpha_convert: bool = True,
    ) -> Incomplete: ...
    def eliminate_equality(self) -> Incomplete: ...
    def simplify(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...
    def getOp(self) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    __hash__: Incomplete
    def fol(self) -> Incomplete: ...
    def visit(
        self, function: Incomplete, combinator: Incomplete
    ) -> Incomplete: ...

class DrtApplicationExpression(DrtExpression, ApplicationExpression):
    def fol(self) -> Incomplete: ...
    def get_refs(self, recursive: bool = False) -> Incomplete: ...

class PossibleAntecedents(list, DrtExpression, Expression):
    def free(self) -> Incomplete: ...
    def replace(
        self,
        variable: Incomplete,
        expression: Incomplete,
        replace_bound: bool = False,
        alpha_convert: bool = True,
    ) -> Incomplete: ...

class AnaphoraResolutionException(Exception): ...

def resolve_anaphora(
    expression: Incomplete, trail: Incomplete = []
) -> Incomplete: ...

class DrsDrawer:
    BUFFER: int
    TOPSPACE: int
    OUTERSPACE: int
    canvas: Incomplete
    drs: Incomplete
    master: Incomplete
    def __init__(
        self,
        dr: Incomplete,
        size_canvas: bool = True,
        canvas: Incomplete | None = None,
    ) -> None: ...
    def draw(self, x: Incomplete = ..., y: Incomplete = ...) -> Incomplete: ...

def demo() -> None: ...
def test_draw() -> None: ...
