from _typeshed import Incomplete

from nltk.classify.api import ClassifierI

__all__ = ["SklearnClassifier"]

class SklearnClassifier(ClassifierI):
    def __init__(
        self,
        estimator: Incomplete,
        dtype: Incomplete = ...,
        sparse: bool = True,
    ) -> None: ...
    def classify_many(self, featuresets: Incomplete) -> Incomplete: ...
    def prob_classify_many(self, featuresets: Incomplete) -> Incomplete: ...
    def labels(self) -> Incomplete: ...
    def train(self, labeled_featuresets: Incomplete) -> Incomplete: ...
