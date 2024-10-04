from typing import (
    List,
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
    IBMModel1 as IBMModel1,
)
from nltk.translate.ibm_model import AlignmentInfo
from nltk.translate.ibm_model import Counts as Counts

class IBMModel2:
    def __init__(
        self,
        sentence_aligned_corpus: List[AlignedSent],
        iterations: int,
        probability_tables: None = ...,
    ) -> None: ...
    def align(self, sentence_pair: AlignedSent) -> Incomplete: ...
    def align_all(self, parallel_corpus: List[AlignedSent]) -> Incomplete: ...
    def prob_t_a_given_s(self, alignment_info: AlignmentInfo) -> float: ...
    def set_uniform_probabilities(
        self, sentence_aligned_corpus: List[AlignedSent]
    ) -> Incomplete: ...

class Model2Counts(Counts):
    alignment: Incomplete
    alignment_for_any_i: Incomplete
    def __init__(self) -> None: ...
    def update_lexical_translation(
        self, count: Incomplete, s: Incomplete, t: Incomplete
    ) -> None: ...
    def update_alignment(
        self,
        count: Incomplete,
        i: Incomplete,
        j: Incomplete,
        l: Incomplete,
        m: Incomplete,
    ) -> None: ...
