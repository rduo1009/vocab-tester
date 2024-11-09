from _typeshed import Incomplete

from nltk.classify.api import ClassifierI as ClassifierI
from nltk.probability import (
    FreqDist as FreqDist,
)
from nltk.probability import (
    MLEProbDist as MLEProbDist,
)
from nltk.probability import (
    entropy as entropy,
)

class DecisionTreeClassifier(ClassifierI):
    def __init__(
        self,
        label: Incomplete,
        feature_name: Incomplete | None = None,
        decisions: Incomplete | None = None,
        default: Incomplete | None = None,
    ) -> None: ...
    def labels(self) -> Incomplete: ...
    def classify(self, featureset: Incomplete) -> Incomplete: ...
    def error(self, labeled_featuresets: Incomplete) -> Incomplete: ...
    def pretty_format(
        self, width: int = 70, prefix: str = "", depth: int = 4
    ) -> Incomplete: ...
    def pseudocode(self, prefix: str = "", depth: int = 4) -> Incomplete: ...
    @staticmethod
    def train(
        labeled_featuresets: Incomplete,
        entropy_cutoff: float = 0.05,
        depth_cutoff: int = 100,
        support_cutoff: int = 10,
        binary: bool = False,
        feature_values: Incomplete | None = None,
        verbose: bool = False,
    ) -> Incomplete: ...
    @staticmethod
    def leaf(labeled_featuresets: Incomplete) -> Incomplete: ...
    @staticmethod
    def stump(
        feature_name: Incomplete, labeled_featuresets: Incomplete
    ) -> Incomplete: ...
    def refine(
        self,
        labeled_featuresets: Incomplete,
        entropy_cutoff: Incomplete,
        depth_cutoff: Incomplete,
        support_cutoff: Incomplete,
        binary: bool = False,
        feature_values: Incomplete | None = None,
        verbose: bool = False,
    ) -> None: ...
    @staticmethod
    def best_stump(
        feature_names: Incomplete,
        labeled_featuresets: Incomplete,
        verbose: bool = False,
    ) -> Incomplete: ...
    @staticmethod
    def binary_stump(
        feature_name: Incomplete,
        feature_value: Incomplete,
        labeled_featuresets: Incomplete,
    ) -> Incomplete: ...
    @staticmethod
    def best_binary_stump(
        feature_names: Incomplete,
        labeled_featuresets: Incomplete,
        feature_values: Incomplete,
        verbose: bool = False,
    ) -> Incomplete: ...

def f(x: Incomplete) -> Incomplete: ...
def demo() -> None: ...
