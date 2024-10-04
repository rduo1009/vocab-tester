from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete

from nltk.internals import deprecated as deprecated
from nltk.internals import overridden as overridden
from nltk.metrics import (
    ConfusionMatrix as ConfusionMatrix,
)
from nltk.metrics import (
    accuracy as accuracy,
)
from nltk.tag.util import untag as untag

class TaggerI(metaclass=ABCMeta):
    @abstractmethod
    def tag(self, tokens: Incomplete) -> Incomplete: ...
    def tag_sents(self, sentences: Incomplete) -> Incomplete: ...
    def evaluate(self, gold: Incomplete) -> Incomplete: ...
    def accuracy(self, gold: Incomplete) -> Incomplete: ...
    def confusion(self, gold: Incomplete) -> Incomplete: ...
    def recall(self, gold: Incomplete) -> dict[str, float]: ...
    def precision(self, gold: Incomplete) -> Incomplete: ...
    def f_measure(
        self, gold: Incomplete, alpha: float = 0.5
    ) -> Incomplete: ...
    def evaluate_per_tag(
        self,
        gold: Incomplete,
        alpha: float = 0.5,
        truncate: Incomplete | None = None,
        sort_by_count: bool = False,
    ) -> Incomplete: ...

class FeaturesetTaggerI(TaggerI): ...
