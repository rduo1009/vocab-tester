from _typeshed import Incomplete

from nltk.classify.api import ClassifierI as ClassifierI
from nltk.probability import (
    DictionaryProbDist as DictionaryProbDist,
)
from nltk.probability import (
    ELEProbDist as ELEProbDist,
)
from nltk.probability import (
    FreqDist as FreqDist,
)
from nltk.probability import (
    sum_logs as sum_logs,
)

class NaiveBayesClassifier(ClassifierI):
    def __init__(
        self, label_probdist: Incomplete, feature_probdist: Incomplete
    ) -> None: ...
    def labels(self) -> Incomplete: ...
    def classify(self, featureset: Incomplete) -> Incomplete: ...
    def prob_classify(self, featureset: Incomplete) -> Incomplete: ...
    def show_most_informative_features(self, n: int = 10) -> Incomplete: ...
    def most_informative_features(self, n: int = 100) -> Incomplete: ...
    @classmethod
    def train(
        cls: Incomplete,
        labeled_featuresets: Incomplete,
        estimator: Incomplete = ...,
    ) -> Incomplete: ...

def demo() -> None: ...
