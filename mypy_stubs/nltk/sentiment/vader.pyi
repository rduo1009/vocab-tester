from _typeshed import Incomplete

from nltk.util import pairwise as pairwise

class VaderConstants:
    B_INCR: float
    B_DECR: float
    C_INCR: float
    N_SCALAR: float
    NEGATE: Incomplete
    BOOSTER_DICT: Incomplete
    SPECIAL_CASE_IDIOMS: Incomplete
    REGEX_REMOVE_PUNCTUATION: Incomplete
    PUNC_LIST: Incomplete
    def __init__(self) -> None: ...
    def negated(
        self, input_words: Incomplete, include_nt: bool = True
    ) -> Incomplete: ...
    def normalize(self, score: Incomplete, alpha: int = 15) -> Incomplete: ...
    def scalar_inc_dec(
        self, word: Incomplete, valence: Incomplete, is_cap_diff: Incomplete
    ) -> Incomplete: ...

class SentiText:
    text: Incomplete
    PUNC_LIST: Incomplete
    REGEX_REMOVE_PUNCTUATION: Incomplete
    words_and_emoticons: Incomplete
    is_cap_diff: Incomplete
    def __init__(
        self,
        text: Incomplete,
        punc_list: Incomplete,
        regex_remove_punctuation: Incomplete,
    ) -> None: ...
    def allcap_differential(self, words: Incomplete) -> Incomplete: ...

class SentimentIntensityAnalyzer:
    lexicon_file: Incomplete
    lexicon: Incomplete
    constants: Incomplete
    def __init__(
        self,
        lexicon_file: str = "sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt",
    ) -> None: ...
    def make_lex_dict(self) -> Incomplete: ...
    def polarity_scores(self, text: Incomplete) -> Incomplete: ...
    def sentiment_valence(
        self,
        valence: Incomplete,
        sentitext: Incomplete,
        item: Incomplete,
        i: Incomplete,
        sentiments: Incomplete,
    ) -> Incomplete: ...
    def score_valence(
        self, sentiments: Incomplete, text: Incomplete
    ) -> Incomplete: ...
