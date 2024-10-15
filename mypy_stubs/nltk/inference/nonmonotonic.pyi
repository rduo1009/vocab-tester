from _typeshed import Incomplete

from nltk.inference.api import (
    Prover as Prover,
)
from nltk.inference.api import (
    ProverCommandDecorator as ProverCommandDecorator,
)
from nltk.inference.prover9 import (
    Prover9 as Prover9,
)
from nltk.inference.prover9 import (
    Prover9Command as Prover9Command,
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
    BooleanExpression as BooleanExpression,
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
    ImpExpression as ImpExpression,
)
from nltk.sem.logic import (
    NegatedExpression as NegatedExpression,
)
from nltk.sem.logic import (
    Variable as Variable,
)
from nltk.sem.logic import (
    VariableExpression as VariableExpression,
)
from nltk.sem.logic import (
    operator as operator,
)
from nltk.sem.logic import (
    unique_variable as unique_variable,
)

class ProverParseError(Exception): ...

def get_domain(goal: Incomplete, assumptions: Incomplete) -> Incomplete: ...

class ClosedDomainProver(ProverCommandDecorator):
    def assumptions(self) -> Incomplete: ...
    def goal(self) -> Incomplete: ...
    def replace_quants(
        self, ex: Incomplete, domain: Incomplete
    ) -> Incomplete: ...

class UniqueNamesProver(ProverCommandDecorator):
    def assumptions(self) -> Incomplete: ...

class SetHolder(list):
    def __getitem__(self, item: Incomplete) -> Incomplete: ...

class ClosedWorldProver(ProverCommandDecorator):
    def assumptions(self) -> Incomplete: ...

class PredHolder:
    signatures: Incomplete
    properties: Incomplete
    signature_len: Incomplete
    def __init__(self) -> None: ...
    def append_sig(self, new_sig: Incomplete) -> None: ...
    def append_prop(self, new_prop: Incomplete) -> None: ...
    def validate_sig_len(self, new_sig: Incomplete) -> None: ...

def closed_domain_demo() -> None: ...
def unique_names_demo() -> None: ...
def closed_world_demo() -> None: ...
def combination_prover_demo() -> None: ...
def default_reasoning_demo() -> None: ...
def print_proof(goal: Incomplete, premises: Incomplete) -> None: ...
def demo() -> None: ...
