from typing import List

from _typeshed import Incomplete

from nltk.util import ngrams as ngrams

def corpus_nist(
    list_of_references: List[List[List[str]]],
    hypotheses: List[List[str]],
    n: int = ...,
) -> float: ...
def nist_length_penalty(ref_len: int, hyp_len: int) -> float: ...
def sentence_nist(
    references: Incomplete, hypothesis: Incomplete, n: int = 5
) -> Incomplete: ...
