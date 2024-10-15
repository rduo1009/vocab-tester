from typing import (
    DefaultDict,
    Dict,
    List,
    Optional,
    Set,
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
    IBMModel4 as IBMModel4,
)
from nltk.translate.ibm_model import AlignmentInfo
from nltk.translate.ibm_model import (
    Counts as Counts,
)
from nltk.translate.ibm_model import (
    longest_target_sentence_length as longest_target_sentence_length,
)

class IBMModel5:
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
                                DefaultDict[Optional[str], float],
                                DefaultDict[str, float],
                            ],
                        ],
                        DefaultDict[
                            int, DefaultDict[int, DefaultDict[int, float]]
                        ],
                    ]
                ],
            ]
        ] = ...,
    ) -> None: ...
    def prob_t_a_given_s(self, alignment_info: AlignmentInfo) -> float: ...
    def prune(
        self, alignment_infos: List[AlignmentInfo]
    ) -> Set[AlignmentInfo]: ...
    def reset_probabilities(self) -> Incomplete: ...
    def set_uniform_probabilities(
        self, sentence_aligned_corpus: List[AlignedSent]
    ) -> Incomplete: ...

class Slots:
    def __init__(self, target_sentence_length: int) -> None: ...
    def __len__(self) -> int: ...
    def occupy(self, position: int) -> Incomplete: ...
    def vacancies_at(self, position: int) -> int: ...

class Model5Counts(Counts):
    head_vacancy: Incomplete
    head_vacancy_for_any_dv: Incomplete
    non_head_vacancy: Incomplete
    non_head_vacancy_for_any_dv: Incomplete
    def __init__(self) -> None: ...
    def update_vacancy(
        self,
        count: Incomplete,
        alignment_info: Incomplete,
        i: Incomplete,
        trg_classes: Incomplete,
        slots: Incomplete,
    ) -> None: ...
