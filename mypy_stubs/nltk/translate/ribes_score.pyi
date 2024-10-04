from typing import (
    Any,
    Iterator,
    List,
    Tuple,
    Union,
)

from nltk.util import choose as choose
from nltk.util import ngrams as ngrams

def corpus_ribes(
    list_of_references: List[List[List[str]]],
    hypotheses: List[List[str]],
    alpha: float = ...,
    beta: float = ...,
) -> float: ...
def find_increasing_sequences(
    worder: List[int],
) -> Iterator[
    Union[
        Tuple[int, int],
        Tuple[int, int, int],
        Tuple[int, int, int, int, int, int],
        Tuple[int, int, int, int],
    ]
]: ...
def kendall_tau(
    worder: List[Union[int, Any]], normalize: bool = ...
) -> float: ...
def position_of_ngram(ngram: Tuple[str, str], sentence: List[str]) -> int: ...
def sentence_ribes(
    references: List[List[str]],
    hypothesis: List[str],
    alpha: float = ...,
    beta: float = ...,
) -> float: ...
def word_rank_alignment(
    reference: List[str], hypothesis: List[str], character_based: bool = ...
) -> List[Union[int, Any]]: ...
