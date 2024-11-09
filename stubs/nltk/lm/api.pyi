from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete

from nltk.lm.counter import NgramCounter as NgramCounter
from nltk.lm.util import log_base2 as log_base2
from nltk.lm.vocabulary import Vocabulary as Vocabulary

class Smoothing(metaclass=ABCMeta):
    vocab: Incomplete
    counts: Incomplete
    def __init__(
        self, vocabulary: Incomplete, counter: Incomplete
    ) -> None: ...
    @abstractmethod
    def unigram_score(self, word: Incomplete) -> Incomplete: ...
    @abstractmethod
    def alpha_gamma(
        self, word: Incomplete, context: Incomplete
    ) -> Incomplete: ...

class LanguageModel(metaclass=ABCMeta):
    order: Incomplete
    vocab: Incomplete
    counts: Incomplete
    def __init__(
        self,
        order: Incomplete,
        vocabulary: Incomplete | None = None,
        counter: Incomplete | None = None,
    ) -> None: ...
    def fit(
        self, text: Incomplete, vocabulary_text: Incomplete | None = None
    ) -> None: ...
    def score(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...
    @abstractmethod
    def unmasked_score(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...
    def logscore(
        self, word: Incomplete, context: Incomplete | None = None
    ) -> Incomplete: ...
    def context_counts(self, context: Incomplete) -> Incomplete: ...
    def entropy(self, text_ngrams: Incomplete) -> Incomplete: ...
    def perplexity(self, text_ngrams: Incomplete) -> Incomplete: ...
    def generate(
        self,
        num_words: int = 1,
        text_seed: Incomplete | None = None,
        random_seed: Incomplete | None = None,
    ) -> Incomplete: ...
