from _typeshed import Incomplete

from nltk.lm.api import LanguageModel as LanguageModel
from nltk.lm.api import Smoothing as Smoothing
from nltk.lm.smoothing import (
    AbsoluteDiscounting as AbsoluteDiscounting,
)
from nltk.lm.smoothing import (
    KneserNey as KneserNey,
)
from nltk.lm.smoothing import (
    WittenBell as WittenBell,
)

class MLE(LanguageModel):
    def unmasked_score(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...

class Lidstone(LanguageModel):
    gamma: Incomplete
    def __init__(
        self, gamma: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def unmasked_score(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...

class Laplace(Lidstone):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class StupidBackoff(LanguageModel):
    alpha: Incomplete
    def __init__(
        self, alpha: float = 0.4, *args: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def unmasked_score(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...

class InterpolatedLanguageModel(LanguageModel):
    estimator: Incomplete
    def __init__(
        self,
        smoothing_cls: Incomplete,
        order: Incomplete,
        **kwargs: Incomplete,
    ) -> None: ...
    def unmasked_score(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...

class WittenBellInterpolated(InterpolatedLanguageModel):
    def __init__(self, order: Incomplete, **kwargs: Incomplete) -> None: ...

class AbsoluteDiscountingInterpolated(InterpolatedLanguageModel):
    def __init__(
        self, order: Incomplete, discount: float = 0.75, **kwargs: Incomplete
    ) -> None: ...

class KneserNeyInterpolated(InterpolatedLanguageModel):
    def __init__(
        self, order: Incomplete, discount: float = 0.1, **kwargs: Incomplete
    ) -> None: ...
