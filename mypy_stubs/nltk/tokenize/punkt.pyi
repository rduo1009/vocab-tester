from re import Pattern
from typing import (
    Any,
    Iterator,
    List,
    Set,
    Tuple,
    Type,
    Union,
)

from _typeshed import Incomplete

from nltk.probability import FreqDist as FreqDist
from nltk.tokenize.api import TokenizerI as TokenizerI

REASON_DEFAULT_DECISION: str
REASON_KNOWN_COLLOCATION: str
REASON_ABBR_WITH_ORTHOGRAPHIC_HEURISTIC: str
REASON_ABBR_WITH_SENTENCE_STARTER: str
REASON_INITIAL_WITH_ORTHOGRAPHIC_HEURISTIC: str
REASON_NUMBER_WITH_ORTHOGRAPHIC_HEURISTIC: str
REASON_INITIAL_WITH_SPECIAL_ORTHOGRAPHIC_HEURISTIC: str

def _pair_iter(iterator: Union[str, List[PunktToken]]) -> Iterator[Any]: ...

class PunktBaseClass:
    def __init__(
        self,
        lang_vars: None = ...,
        token_cls: Type[PunktToken] = ...,
        params: None = ...,
    ) -> None: ...
    def _annotate_first_pass(
        self, tokens: Iterator[PunktToken]
    ) -> Iterator[PunktToken]: ...
    def _first_pass_annotation(self, aug_tok: PunktToken) -> None: ...
    def _tokenize_words(self, plaintext: str) -> Iterator[PunktToken]: ...

class PunktLanguageVars:
    @property
    def _re_non_word_chars(self) -> str: ...
    @property
    def _re_sent_end_chars(self) -> str: ...
    def _word_tokenizer_re(self) -> Pattern: ...
    def period_context_re(self) -> Pattern: ...
    def word_tokenize(self, s: str) -> List[str]: ...

class PunktParameters:
    def __init__(self) -> None: ...
    def _debug_ortho_context(self, typ: str) -> Incomplete: ...
    def add_ortho_context(self, typ: str, flag: int) -> Incomplete: ...
    def clear_collocations(self) -> Incomplete: ...
    def clear_sent_starters(self) -> Incomplete: ...

class PunktToken:
    def __init__(self, tok: str, **params: Incomplete) -> None: ...
    def _get_type(self, tok: str) -> str: ...
    @property
    def first_case(self) -> Incomplete: ...
    @property
    def first_lower(self) -> bool: ...
    @property
    def first_upper(self) -> bool: ...
    @property
    def is_ellipsis(self) -> None: ...
    @property
    def is_initial(self) -> None: ...
    @property
    def is_number(self) -> bool: ...
    @property
    def type_no_period(self) -> str: ...
    @property
    def type_no_sentperiod(self) -> str: ...

class PunktTrainer:
    def __init__(
        self,
        train_text: Incomplete | None = None,
        verbose: bool = False,
        lang_vars: Incomplete | None = None,
        token_cls: Type[PunktToken] = ...,
    ) -> None: ...
    @staticmethod
    def _dunning_log_likelihood(
        count_a: int, count_b: int, count_ab: int, N: int
    ) -> float: ...
    def _find_collocations(self) -> Incomplete: ...
    def _find_sent_starters(self) -> Incomplete: ...
    def _get_orthography_data(
        self, tokens: List[PunktToken]
    ) -> Incomplete: ...
    def _get_sentbreak_count(self, tokens: List[PunktToken]) -> int: ...
    def _reclassify_abbrev_types(
        self, types: Set[str]
    ) -> Iterator[Tuple[str, float, bool]]: ...
    def _train_tokens(
        self, tokens: Iterator[Any], verbose: bool
    ) -> Incomplete: ...
    def _unique_types(self, tokens: List[PunktToken]) -> Set[str]: ...
    def get_params(self) -> Incomplete: ...
    ABBREV: float
    IGNORE_ABBREV_PENALTY: bool
    ABBREV_BACKOFF: int
    COLLOCATION: float
    SENT_STARTER: int
    INCLUDE_ALL_COLLOCS: bool
    INCLUDE_ABBREV_COLLOCS: bool
    MIN_COLLOC_FREQ: int
    def train(
        self, text: Incomplete, verbose: bool = False, finalize: bool = True
    ) -> None: ...
    def train_tokens(
        self, tokens: Incomplete, verbose: bool = False, finalize: bool = True
    ) -> None: ...
    def finalize_training(self, verbose: bool = False) -> None: ...
    def freq_threshold(
        self,
        ortho_thresh: int = 2,
        type_thresh: int = 2,
        colloc_thres: int = 2,
        sentstart_thresh: int = 2,
    ) -> None: ...
    def find_abbrev_types(self) -> None: ...

class PunktSentenceTokenizer(PunktBaseClass, TokenizerI):
    def __init__(
        self,
        train_text: Incomplete | None = None,
        verbose: bool = False,
        lang_vars: Incomplete | None = None,
        token_cls: Incomplete = ...,
    ) -> None: ...
    def train(
        self, train_text: Incomplete, verbose: bool = False
    ) -> Incomplete: ...
    def tokenize(
        self, text: str, realign_boundaries: bool = True
    ) -> list[str]: ...
    def debug_decisions(self, text: str) -> Iterator[dict[str, Any]]: ...
    def span_tokenize(
        self, text: str, realign_boundaries: bool = True
    ) -> Iterator[tuple[int, int]]: ...
    def sentences_from_text(
        self, text: str, realign_boundaries: bool = True
    ) -> list[str]: ...
    def text_contains_sentbreak(self, text: str) -> bool: ...
    def sentences_from_text_legacy(self, text: str) -> Iterator[str]: ...
    def sentences_from_tokens(
        self, tokens: Iterator[PunktToken]
    ) -> Iterator[PunktToken]: ...
    def dump(self, tokens: Iterator[PunktToken]) -> None: ...
    PUNCTUATION: Incomplete

class PunktTokenizer(PunktSentenceTokenizer):
    def __init__(self, lang: str = "english") -> None: ...
    def load_lang(self, lang: str = "english") -> None: ...
    def save_params(self) -> None: ...

def load_punkt_params(lang_dir: Incomplete) -> Incomplete: ...
def save_punkt_params(
    params: Incomplete, dir: str = "/tmp/punkt_tab"
) -> None: ...

DEBUG_DECISION_FMT: str

def format_debug_decision(d: Incomplete) -> Incomplete: ...
def demo(
    text: Incomplete, tok_cls: Incomplete = ..., train_cls: Incomplete = ...
) -> Incomplete: ...
