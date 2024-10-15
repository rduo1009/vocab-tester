from _typeshed import Incomplete

from nltk.internals import overridden as overridden

class ClassifierI:
    def labels(self) -> None: ...
    def classify(self, featureset: Incomplete) -> Incomplete: ...
    def prob_classify(self, featureset: Incomplete) -> Incomplete: ...
    def classify_many(self, featuresets: Incomplete) -> Incomplete: ...
    def prob_classify_many(self, featuresets: Incomplete) -> Incomplete: ...

class MultiClassifierI:
    def labels(self) -> None: ...
    def classify(self, featureset: Incomplete) -> Incomplete: ...
    def prob_classify(self, featureset: Incomplete) -> Incomplete: ...
    def classify_many(self, featuresets: Incomplete) -> Incomplete: ...
    def prob_classify_many(self, featuresets: Incomplete) -> Incomplete: ...
