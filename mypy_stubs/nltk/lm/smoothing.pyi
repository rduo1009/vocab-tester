from _typeshed import Incomplete

from nltk.lm.api import Smoothing as Smoothing
from nltk.probability import ConditionalFreqDist as ConditionalFreqDist

class WittenBell(Smoothing):
    def __init__(
        self, vocabulary: Incomplete, counter: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def alpha_gamma(
        self, word: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def unigram_score(self, word: Incomplete) -> Incomplete: ...

class AbsoluteDiscounting(Smoothing):
    discount: Incomplete
    def __init__(
        self,
        vocabulary: Incomplete,
        counter: Incomplete,
        discount: float = 0.75,
        **kwargs: Incomplete,
    ) -> None: ...
    def alpha_gamma(
        self, word: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def unigram_score(self, word: Incomplete) -> Incomplete: ...

class KneserNey(Smoothing):
    discount: Incomplete
    def __init__(
        self,
        vocabulary: Incomplete,
        counter: Incomplete,
        order: Incomplete,
        discount: float = 0.1,
        **kwargs: Incomplete,
    ) -> None: ...
    def unigram_score(self, word: Incomplete) -> Incomplete: ...
    def alpha_gamma(
        self, word: Incomplete, context: Incomplete
    ) -> Incomplete: ...
