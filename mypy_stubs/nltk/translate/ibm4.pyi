from typing import (
    DefaultDict,
    Dict,
    List,
    Optional,
    Union,
)

from _typeshed import Incomplete

from nltk.translate import (
    AlignedSent as AlignedSent,
)
from nltk.translate import (
    Alignment as Alignment,
)
from nltk.translate import (
    IBMModel as IBMModel,
)
from nltk.translate import (
    IBMModel3 as IBMModel3,
)
from nltk.translate.ibm_model import AlignmentInfo
from nltk.translate.ibm_model import (
    Counts as Counts,
)
from nltk.translate.ibm_model import (
    longest_target_sentence_length as longest_target_sentence_length,
)

class IBMModel4:
    def __init__(
        self,
        sentence_aligned_corpus: List[AlignedSent],
        iterations: int,
        source_word_classes: Optional[Dict[str, int]],
        target_word_classes: Optional[Dict[str, int]],
        probability_tables: Optional[
            Dict[
                str,
                Optional[
                    Union[
                        float,
                        DefaultDict[
                            str,
                            Union[
                                DefaultDict[str, float],
                                DefaultDict[None, float],
                            ],
                        ],
                        DefaultDict[
                            int,
                            Union[
                                DefaultDict[None, DefaultDict[int, float]],
                                DefaultDict[int, DefaultDict[int, float]],
                            ],
                        ],
                        DefaultDict[int, DefaultDict[int, float]],
                        DefaultDict[
                            int,
                            Union[
                                DefaultDict[Optional[str], float],
                                DefaultDict[str, float],
                            ],
                        ],
                    ]
                ],
            ]
        ] = ...,
    ) -> None: ...
    @staticmethod
    def model4_prob_t_a_given_s(
        alignment_info: AlignmentInfo, ibm_model: IBMModel4
    ) -> float: ...
    def prob_t_a_given_s(self, alignment_info: AlignmentInfo) -> float: ...
    def reset_probabilities(self) -> Incomplete: ...
    def set_uniform_probabilities(
        self, sentence_aligned_corpus: List[AlignedSent]
    ) -> Incomplete: ...

class Model4Counts(Counts):
    head_distortion: Incomplete
    head_distortion_for_any_dj: Incomplete
    non_head_distortion: Incomplete
    non_head_distortion_for_any_dj: Incomplete
    def __init__(self) -> None: ...
    def update_distortion(
        self,
        count: Incomplete,
        alignment_info: Incomplete,
        j: Incomplete,
        src_classes: Incomplete,
        trg_classes: Incomplete,
    ) -> None: ...
