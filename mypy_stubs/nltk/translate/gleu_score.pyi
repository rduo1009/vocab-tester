from _typeshed import Incomplete

from nltk.util import everygrams as everygrams
from nltk.util import ngrams as ngrams

def sentence_gleu(
    references: Incomplete,
    hypothesis: Incomplete,
    min_len: int = 1,
    max_len: int = 4,
) -> Incomplete: ...
def corpus_gleu(
    list_of_references: Incomplete,
    hypotheses: Incomplete,
    min_len: int = 1,
    max_len: int = 4,
) -> Incomplete: ...
