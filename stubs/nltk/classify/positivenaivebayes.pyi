from _typeshed import Incomplete

from nltk.classify.naivebayes import (
    NaiveBayesClassifier as NaiveBayesClassifier,
)
from nltk.probability import (
    DictionaryProbDist as DictionaryProbDist,
)
from nltk.probability import (
    ELEProbDist as ELEProbDist,
)
from nltk.probability import (
    FreqDist as FreqDist,
)

class PositiveNaiveBayesClassifier(NaiveBayesClassifier):
    @staticmethod
    def train(
        positive_featuresets: Incomplete,
        unlabeled_featuresets: Incomplete,
        positive_prob_prior: float = 0.5,
        estimator: Incomplete = ...,
    ) -> Incomplete: ...

def demo() -> None: ...
