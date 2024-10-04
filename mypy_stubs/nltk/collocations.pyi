from collections.abc import Generator

from _typeshed import Incomplete

__all__ = [
    "BigramCollocationFinder",
    "TrigramCollocationFinder",
    "QuadgramCollocationFinder",
]

class AbstractCollocationFinder:
    word_fd: Incomplete
    N: Incomplete
    ngram_fd: Incomplete
    def __init__(self, word_fd: Incomplete, ngram_fd: Incomplete) -> None: ...
    @classmethod
    def from_documents(
        cls: Incomplete, documents: Incomplete
    ) -> Incomplete: ...
    def apply_freq_filter(self, min_freq: Incomplete) -> Incomplete: ...
    def apply_ngram_filter(self, fn: Incomplete) -> Incomplete: ...
    def apply_word_filter(self, fn: Incomplete) -> Incomplete: ...
    def score_ngrams(self, score_fn: Incomplete) -> Incomplete: ...
    def nbest(self, score_fn: Incomplete, n: Incomplete) -> Incomplete: ...
    def above_score(
        self, score_fn: Incomplete, min_score: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class BigramCollocationFinder(AbstractCollocationFinder):
    default_ws: int
    window_size: Incomplete
    def __init__(
        self, word_fd: Incomplete, bigram_fd: Incomplete, window_size: int = 2
    ) -> None: ...
    @classmethod
    def from_words(
        cls: Incomplete, words: Incomplete, window_size: int = 2
    ) -> Incomplete: ...
    def score_ngram(
        self, score_fn: Incomplete, w1: Incomplete, w2: Incomplete
    ) -> Incomplete: ...

class TrigramCollocationFinder(AbstractCollocationFinder):
    default_ws: int
    wildcard_fd: Incomplete
    bigram_fd: Incomplete
    def __init__(
        self,
        word_fd: Incomplete,
        bigram_fd: Incomplete,
        wildcard_fd: Incomplete,
        trigram_fd: Incomplete,
    ) -> None: ...
    @classmethod
    def from_words(
        cls: Incomplete, words: Incomplete, window_size: int = 3
    ) -> Incomplete: ...
    def bigram_finder(self) -> Incomplete: ...
    def score_ngram(
        self,
        score_fn: Incomplete,
        w1: Incomplete,
        w2: Incomplete,
        w3: Incomplete,
    ) -> Incomplete: ...

class QuadgramCollocationFinder(AbstractCollocationFinder):
    default_ws: int
    iii: Incomplete
    ii: Incomplete
    ixi: Incomplete
    ixxi: Incomplete
    iixi: Incomplete
    ixii: Incomplete
    def __init__(
        self,
        word_fd: Incomplete,
        quadgram_fd: Incomplete,
        ii: Incomplete,
        iii: Incomplete,
        ixi: Incomplete,
        ixxi: Incomplete,
        iixi: Incomplete,
        ixii: Incomplete,
    ) -> None: ...
    @classmethod
    def from_words(
        cls: Incomplete, words: Incomplete, window_size: int = 4
    ) -> Incomplete: ...
    def score_ngram(
        self,
        score_fn: Incomplete,
        w1: Incomplete,
        w2: Incomplete,
        w3: Incomplete,
        w4: Incomplete,
    ) -> Incomplete: ...
