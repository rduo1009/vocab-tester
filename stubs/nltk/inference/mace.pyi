from _typeshed import Incomplete

from nltk.inference.api import (
    BaseModelBuilderCommand as BaseModelBuilderCommand,
)
from nltk.inference.api import (
    ModelBuilder as ModelBuilder,
)
from nltk.inference.prover9 import (
    Prover9CommandParent as Prover9CommandParent,
)
from nltk.inference.prover9 import (
    Prover9Parent as Prover9Parent,
)
from nltk.sem import Expression as Expression
from nltk.sem import Valuation as Valuation
from nltk.sem.logic import is_indvar as is_indvar

class MaceCommand(Prover9CommandParent, BaseModelBuilderCommand):
    def __init__(
        self,
        goal: Incomplete | None = None,
        assumptions: Incomplete | None = None,
        max_models: int = 500,
        model_builder: Incomplete | None = None,
    ) -> None: ...
    @property
    def valuation(mbc: Incomplete) -> Incomplete: ...

class Mace(Prover9Parent, ModelBuilder):
    def __init__(self, end_size: int = 500) -> None: ...

def spacer(num: int = 30) -> None: ...
def decode_result(found: Incomplete) -> Incomplete: ...
def test_model_found(arguments: Incomplete) -> None: ...
def test_build_model(arguments: Incomplete) -> None: ...
def test_transform_output(argument_pair: Incomplete) -> None: ...
def test_make_relation_set() -> None: ...

arguments: Incomplete

def demo() -> None: ...
