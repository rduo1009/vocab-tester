from _typeshed import Incomplete

from nltk.util import ngrams as ngrams

def sentence_chrf(
    reference: Incomplete,
    hypothesis: Incomplete,
    min_len: int = 1,
    max_len: int = 6,
    beta: float = 3.0,
    ignore_whitespace: bool = True,
) -> Incomplete: ...
def chrf_precision_recall_fscore_support(
    reference: Incomplete,
    hypothesis: Incomplete,
    n: Incomplete,
    beta: float = 3.0,
    epsilon: float = 1e-16,
) -> Incomplete: ...
def corpus_chrf(
    references: Incomplete,
    hypotheses: Incomplete,
    min_len: int = 1,
    max_len: int = 6,
    beta: float = 3.0,
    ignore_whitespace: bool = True,
) -> Incomplete: ...
