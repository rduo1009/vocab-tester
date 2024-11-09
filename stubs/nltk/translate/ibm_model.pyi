from typing import (
    Any,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.translate.api import AlignedSent

def longest_target_sentence_length(
    sentence_aligned_corpus: List[AlignedSent],
) -> int: ...

class AlignmentInfo:
    def __eq__(self, other: AlignmentInfo) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(
        self,
        alignment: Union[
            Tuple[int, int, int],
            Tuple[int, int],
            Tuple[int, int, int, int],
            Tuple[int],
            Tuple[int, int, int, int, int, int, int],
        ],
        src_sentence: Optional[
            Union[
                Tuple[None, str, str, str, str],
                Tuple[None, str, str, str],
                List[Optional[str]],
                Tuple[None],
            ]
        ],
        trg_sentence: Any,
        cepts: Optional[
            Union[
                List[List[Union[int, Any]]], List[List[Any]], List[List[int]]
            ]
        ],
    ) -> None: ...
    def center_of_cept(self, i: Optional[int]) -> int: ...
    def fertility_of_i(self, i: int) -> int: ...
    def is_head_word(self, j: int) -> bool: ...
    def previous_cept(self, j: int) -> Optional[int]: ...
    def previous_in_tablet(self, j: int) -> int: ...

class IBMModel:
    def __init__(
        self, sentence_aligned_corpus: List[Union[AlignedSent, Any]]
    ) -> None: ...
    def best_model2_alignment(
        self,
        sentence_pair: AlignedSent,
        j_pegged: Optional[int] = ...,
        i_pegged: int = ...,
    ) -> AlignmentInfo: ...
    def hillclimb(
        self, alignment_info: AlignmentInfo, j_pegged: Optional[int] = ...
    ) -> AlignmentInfo: ...
    def init_vocab(
        self, sentence_aligned_corpus: List[Union[AlignedSent, Any]]
    ) -> Incomplete: ...
    def neighboring(
        self, alignment_info: AlignmentInfo, j_pegged: Optional[int] = ...
    ) -> Set[AlignmentInfo]: ...
    def reset_probabilities(self) -> Incomplete: ...
    def sample(
        self, sentence_pair: AlignedSent
    ) -> Tuple[Set[AlignmentInfo], AlignmentInfo]: ...

class Counts:
    t_given_s: Incomplete
    any_t_given_s: Incomplete
    p0: float
    p1: float
    fertility: Incomplete
    fertility_for_any_phi: Incomplete
    def __init__(self) -> None: ...
    def update_lexical_translation(
        self, count: Incomplete, alignment_info: Incomplete, j: Incomplete
    ) -> None: ...
    def update_null_generation(
        self, count: Incomplete, alignment_info: Incomplete
    ) -> None: ...
    def update_fertility(
        self, count: Incomplete, alignment_info: Incomplete
    ) -> None: ...
