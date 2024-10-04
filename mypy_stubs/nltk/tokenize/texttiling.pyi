from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI

BLOCK_COMPARISON: Incomplete
VOCABULARY_INTRODUCTION: Incomplete
LC: Incomplete
HC: Incomplete
DEFAULT_SMOOTHING: Incomplete

class TextTilingTokenizer(TokenizerI):
    def __init__(
        self,
        w: int = 20,
        k: int = 10,
        similarity_method: Incomplete = ...,
        stopwords: Incomplete | None = None,
        smoothing_method: Incomplete = ...,
        smoothing_width: int = 2,
        smoothing_rounds: int = 1,
        cutoff_policy: Incomplete = ...,
        demo_mode: bool = False,
    ) -> None: ...
    def tokenize(self, text: Incomplete) -> Incomplete: ...

class TokenTableField:
    def __init__(
        self,
        first_pos: Incomplete,
        ts_occurences: Incomplete,
        total_count: int = 1,
        par_count: int = 1,
        last_par: int = 0,
        last_tok_seq: Incomplete | None = None,
    ) -> None: ...

class TokenSequence:
    def __init__(
        self,
        index: Incomplete,
        wrdindex_list: Incomplete,
        original_length: Incomplete | None = None,
    ) -> None: ...

def smooth(
    x: Incomplete, window_len: int = 11, window: str = "flat"
) -> Incomplete: ...
def demo(text: Incomplete | None = None) -> None: ...
