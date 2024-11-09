from typing import (
    Any,
    DefaultDict,
    List,
    Optional,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.translate.api import PhraseTable

class StackDecoder:
    def __init__(
        self, phrase_table: Optional[PhraseTable], language_model: None
    ) -> None: ...
    def compute_future_scores(
        self, src_sentence: Tuple[str, str, str, str, str, str]
    ) -> DefaultDict[int, DefaultDict[int, float]]: ...
    def distortion_score(
        self, hypothesis: _Hypothesis, next_src_phrase_span: Tuple[int, int]
    ) -> float: ...
    def find_all_src_phrases(
        self, src_sentence: Tuple[str, str, str, str, str, str]
    ) -> List[List[Union[int, Any]]]: ...
    def future_score(
        self,
        hypothesis: _Hypothesis,
        future_score_table: DefaultDict[int, DefaultDict[int, float]],
        sentence_length: int,
    ) -> float: ...
    @staticmethod
    def valid_phrases(
        all_phrases_from: List[List[Union[int, Any]]], hypothesis: _Hypothesis
    ) -> List[Tuple[int, int]]: ...

class _Hypothesis:
    def __init__(
        self,
        raw_score: float = ...,
        src_phrase_span: Tuple[()] = ...,
        trg_phrase: Tuple[()] = ...,
        previous: None = ...,
        future_score: float = ...,
    ) -> None: ...
    def score(self) -> float: ...
    def translated_positions(self) -> List[Any]: ...
    def translation_so_far(self) -> List[Any]: ...
    def untranslated_spans(
        self, sentence_length: int
    ) -> List[Tuple[int, int]]: ...

class _Stack:
    def __contains__(self, hypothesis: _Hypothesis) -> bool: ...
    def __init__(
        self, max_size: int = ..., beam_threshold: float = ...
    ) -> None: ...
    def best(self) -> _Hypothesis: ...
    def push(self, hypothesis: _Hypothesis) -> Incomplete: ...
    def threshold_prune(self) -> Incomplete: ...
