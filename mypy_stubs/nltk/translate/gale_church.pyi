from collections.abc import Generator

from _typeshed import Incomplete
from scipy.stats import norm as norm  # type: ignore[import-not-found]

def erfcc(x: Incomplete) -> Incomplete: ...
def norm_cdf(x: Incomplete) -> Incomplete: ...

LOG2: Incomplete

class LanguageIndependent:
    PRIORS: Incomplete
    AVERAGE_CHARACTERS: int
    VARIANCE_CHARACTERS: float

def trace(
    backlinks: Incomplete,
    source_sents_lens: Incomplete,
    target_sents_lens: Incomplete,
) -> Incomplete: ...
def align_log_prob(
    i: Incomplete,
    j: Incomplete,
    source_sents: Incomplete,
    target_sents: Incomplete,
    alignment: Incomplete,
    params: Incomplete,
) -> Incomplete: ...
def align_blocks(
    source_sents_lens: Incomplete,
    target_sents_lens: Incomplete,
    params: Incomplete = ...,
) -> Incomplete: ...
def align_texts(
    source_blocks: Incomplete,
    target_blocks: Incomplete,
    params: Incomplete = ...,
) -> Incomplete: ...
def split_at(
    it: Incomplete, split_value: Incomplete
) -> Generator[Incomplete, None, None]: ...
def parse_token_stream(
    stream: Incomplete, soft_delimiter: Incomplete, hard_delimiter: Incomplete
) -> Incomplete: ...
