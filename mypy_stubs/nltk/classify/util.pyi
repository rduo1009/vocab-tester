from _typeshed import Incomplete

from nltk.util import LazyMap as LazyMap

def apply_features(
    feature_func: Incomplete,
    toks: Incomplete,
    labeled: Incomplete | None = None,
) -> Incomplete: ...
def attested_labels(tokens: Incomplete) -> Incomplete: ...
def log_likelihood(classifier: Incomplete, gold: Incomplete) -> Incomplete: ...
def accuracy(classifier: Incomplete, gold: Incomplete) -> Incomplete: ...

class CutoffChecker:
    cutoffs: Incomplete
    ll: Incomplete
    acc: Incomplete
    iter: int
    def __init__(self, cutoffs: Incomplete) -> None: ...
    def check(
        self, classifier: Incomplete, train_toks: Incomplete
    ) -> Incomplete: ...

def names_demo_features(name: Incomplete) -> Incomplete: ...
def binary_names_demo_features(name: Incomplete) -> Incomplete: ...
def names_demo(
    trainer: Incomplete, features: Incomplete = ...
) -> Incomplete: ...
def partial_names_demo(
    trainer: Incomplete, features: Incomplete = ...
) -> Incomplete: ...
def wsd_demo(
    trainer: Incomplete, word: Incomplete, features: Incomplete, n: int = 1000
) -> Incomplete: ...
def check_megam_config() -> None: ...
