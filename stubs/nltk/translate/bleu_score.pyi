from typing import (
    Any,
    Callable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

from _typeshed import Incomplete
from numpy import ndarray

from nltk.util import ngrams as ngrams

def brevity_penalty(closest_ref_len: int, hyp_len: int) -> float: ...
def closest_ref_length(
    references: List[List[Union[str, Any]]], hyp_len: int
) -> int: ...
def corpus_bleu(
    list_of_references: List[List[List[Union[str, Any]]]],
    hypotheses: List[List[Union[str, Any]]],
    weights: Any = ...,
    smoothing_function: Optional[Callable] = ...,  # type: ignore[type-arg]
    auto_reweigh: bool = ...,
) -> Union[float, List[float], int]: ...
def modified_precision(
    references: List[List[Union[str, Any]]],
    hypothesis: List[Union[str, Any]],
    n: int,
) -> Fraction: ...
def sentence_bleu(
    references: List[List[Union[str, Any]]],
    hypothesis: List[Union[str, Any]],
    weights: Union[
        Tuple[float, float, float, float],
        Tuple[float, float],
        ndarray,
        Tuple[float],
    ] = ...,
    smoothing_function: Optional[Callable] = ...,  # type: ignore[type-arg]
    auto_reweigh: bool = ...,
) -> Union[int, float]: ...

class Fraction:
    @staticmethod
    def __new__(
        cls: Type[Fraction],
        numerator: int = ...,
        denominator: Optional[int] = ...,
        _normalize: bool = ...,
    ) -> Fraction: ...
    @property
    def denominator(self) -> int: ...
    @property
    def numerator(self) -> int: ...

class SmoothingFunction:
    def __init__(
        self, epsilon: float = ..., alpha: int = ..., k: int = ...
    ) -> None: ...
    def method0(
        self, p_n: List[Fraction], *args: Incomplete, **kwargs: Incomplete
    ) -> List[Union[Fraction, float]]: ...
