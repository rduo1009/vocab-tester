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
    IBMModel2 as IBMModel2,
)
from nltk.translate.ibm_model import AlignmentInfo
from nltk.translate.ibm_model import Counts as Counts

class IBMModel3:
    def __init__(
        self,
        sentence_aligned_corpus: List[AlignedSent],
        iterations: int,
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
                            DefaultDict[
                                int, DefaultDict[int, DefaultDict[int, float]]
                            ],
                        ],
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
    def prob_t_a_given_s(self, alignment_info: AlignmentInfo) -> float: ...
    def reset_probabilities(self) -> Incomplete: ...
    def set_uniform_probabilities(
        self, sentence_aligned_corpus: List[AlignedSent]
    ) -> Incomplete: ...

class Model3Counts(Counts):
    distortion: Incomplete
    distortion_for_any_j: Incomplete
    def __init__(self) -> None: ...
    def update_distortion(
        self,
        count: Incomplete,
        alignment_info: Incomplete,
        j: Incomplete,
        l: Incomplete,
        m: Incomplete,
    ) -> None: ...
