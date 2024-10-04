from _typeshed import Incomplete

from nltk.classify.util import apply_features as apply_features
from nltk.collocations import (
    BigramCollocationFinder as BigramCollocationFinder,
)
from nltk.metrics import BigramAssocMeasures as BigramAssocMeasures
from nltk.probability import FreqDist as FreqDist

class SentimentAnalyzer:
    feat_extractors: Incomplete
    classifier: Incomplete
    def __init__(self, classifier: Incomplete | None = None) -> None: ...
    def all_words(
        self, documents: Incomplete, labeled: Incomplete | None = None
    ) -> Incomplete: ...
    def apply_features(
        self, documents: Incomplete, labeled: Incomplete | None = None
    ) -> Incomplete: ...
    def unigram_word_feats(
        self,
        words: Incomplete,
        top_n: Incomplete | None = None,
        min_freq: int = 0,
    ) -> Incomplete: ...
    def bigram_collocation_feats(
        self,
        documents: Incomplete,
        top_n: Incomplete | None = None,
        min_freq: int = 3,
        assoc_measure: Incomplete = ...,
    ) -> Incomplete: ...
    def classify(self, instance: Incomplete) -> Incomplete: ...
    def add_feat_extractor(
        self, function: Incomplete, **kwargs: Incomplete
    ) -> None: ...
    def extract_features(self, document: Incomplete) -> Incomplete: ...
    def train(
        self,
        trainer: Incomplete,
        training_set: Incomplete,
        save_classifier: Incomplete | None = None,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def save_file(self, content: Incomplete, filename: Incomplete) -> None: ...
    def evaluate(
        self,
        test_set: Incomplete,
        classifier: Incomplete | None = None,
        accuracy: bool = True,
        f_measure: bool = True,
        precision: bool = True,
        recall: bool = True,
        verbose: bool = False,
    ) -> Incomplete: ...
