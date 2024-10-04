from _typeshed import Incomplete

from nltk.inference.api import (
    BaseProverCommand as BaseProverCommand,
)
from nltk.inference.api import (
    Prover as Prover,
)
from nltk.sem.logic import (
    AllExpression as AllExpression,
)
from nltk.sem.logic import (
    AndExpression as AndExpression,
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
    NegatedExpression as NegatedExpression,
)
from nltk.sem.logic import (
    OrExpression as OrExpression,
)

p9_return_codes: Incomplete

class Prover9CommandParent:
    def print_assumptions(self, output_format: str = "nltk") -> None: ...

class Prover9Command(Prover9CommandParent, BaseProverCommand):
    def __init__(
        self,
        goal: Incomplete | None = None,
        assumptions: Incomplete | None = None,
        timeout: int = 60,
        prover: Incomplete | None = None,
    ) -> None: ...
    def decorate_proof(
        self, proof_string: Incomplete, simplify: bool = True
    ) -> Incomplete: ...

class Prover9Parent:
    def config_prover9(
        self, binary_location: Incomplete, verbose: bool = False
    ) -> None: ...
    def prover9_input(
        self, goal: Incomplete, assumptions: Incomplete
    ) -> Incomplete: ...
    def binary_locations(self) -> Incomplete: ...

def convert_to_prover9(input: Incomplete) -> Incomplete: ...

class Prover9(Prover9Parent, Prover):
    def __init__(self, timeout: int = 60) -> None: ...
    def prover9_input(
        self, goal: Incomplete, assumptions: Incomplete
    ) -> Incomplete: ...

class Prover9Exception(Exception):
    def __init__(
        self, returncode: Incomplete, message: Incomplete
    ) -> None: ...

class Prover9FatalException(Prover9Exception): ...
class Prover9LimitExceededException(Prover9Exception): ...

def test_config() -> None: ...
def test_convert_to_prover9(expr: Incomplete) -> None: ...
def test_prove(arguments: Incomplete) -> None: ...

arguments: Incomplete
expressions: Incomplete

def spacer(num: int = 45) -> None: ...
def demo() -> None: ...
