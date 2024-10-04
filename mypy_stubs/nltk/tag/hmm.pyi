from typing import (
    Callable,
    List,
    Tuple,
    Union,
)

from _typeshed import Incomplete
from numpy import (
    float64,
    ndarray,
)

from nltk.metrics import accuracy as accuracy
from nltk.probability import (
    ConditionalFreqDist as ConditionalFreqDist,
)
from nltk.probability import (
    ConditionalProbDist as ConditionalProbDist,
)
from nltk.probability import (
    DictionaryConditionalProbDist,
    DictionaryProbDist,
)
from nltk.probability import (
    FreqDist as FreqDist,
)
from nltk.probability import (
    LidstoneProbDist as LidstoneProbDist,
)
from nltk.probability import (
    MLEProbDist as MLEProbDist,
)
from nltk.probability import (
    MutableProbDist as MutableProbDist,
)
from nltk.probability import (
    RandomProbDist as RandomProbDist,
)
from nltk.tag.api import TaggerI as TaggerI
from nltk.util import LazyMap as LazyMap
from nltk.util import unique_list as unique_list

def _create_hmm_tagger(
    states: List[str],
    symbols: List[str],
    A: Union[List[List[float]], ndarray],  # type: ignore[type-arg]
    B: Union[List[List[float]], ndarray],  # type: ignore[type-arg]
    pi: Union[List[float], ndarray],  # type: ignore[type-arg]
) -> HiddenMarkovModelTagger: ...
def _market_hmm_example() -> (
    Tuple[HiddenMarkovModelTagger, List[str], List[str]]
): ...
def _ninf_array(shape: Tuple[int, int]) -> ndarray: ...  # type: ignore[type-arg]
def logsumexp2(arr: ndarray) -> float64: ...  # type: ignore[type-arg]

class HiddenMarkovModelTagger(TaggerI):
    def __init__(
        self,
        symbols: List[str],
        states: List[str],
        transitions: DictionaryConditionalProbDist,
        outputs: DictionaryConditionalProbDist,
        priors: DictionaryProbDist,
        transform: Callable = ...,  # type: ignore[type-arg]
    ) -> None: ...
    def _backward_probability(
        self, unlabeled_sequence: List[Tuple[str, None]]
    ) -> ndarray: ...
    def _forward_probability(
        self, unlabeled_sequence: List[Tuple[str, None]]
    ) -> ndarray: ...
    def _output_logprob(self, state: str, symbol: str) -> float: ...
    def _outputs_vector(self, symbol: str) -> ndarray: ...  # type: ignore[type-arg]
    def _transitions_matrix(self) -> ndarray: ...  # type: ignore[type-arg]
    @classmethod
    def train(
        cls: Incomplete,
        labeled_sequence: Incomplete,
        test_sequence: Incomplete | None = None,
        unlabeled_sequence: Incomplete | None = None,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def probability(self, sequence: Incomplete) -> Incomplete: ...
    def log_probability(self, sequence: Incomplete) -> Incomplete: ...
    def tag(self, unlabeled_sequence: Incomplete) -> Incomplete: ...
    def reset_cache(self) -> None: ...
    def best_path(self, unlabeled_sequence: Incomplete) -> Incomplete: ...
    def best_path_simple(
        self, unlabeled_sequence: Incomplete
    ) -> Incomplete: ...
    def random_sample(
        self, rng: Incomplete, length: Incomplete
    ) -> Incomplete: ...
    def entropy(self, unlabeled_sequence: Incomplete) -> Incomplete: ...
    def point_entropy(self, unlabeled_sequence: Incomplete) -> Incomplete: ...
    def test(
        self,
        test_sequence: Incomplete,
        verbose: bool = False,
        **kwargs: Incomplete,
    ) -> Incomplete: ...

class HiddenMarkovModelTrainer:
    def __init__(
        self,
        states: Incomplete | None = None,
        symbols: Incomplete | None = None,
    ) -> None: ...
    def train(
        self,
        labeled_sequences: Incomplete | None = None,
        unlabeled_sequences: Incomplete | None = None,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def train_unsupervised(
        self,
        unlabeled_sequences: Incomplete,
        update_outputs: bool = True,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def train_supervised(
        self,
        labelled_sequences: Incomplete,
        estimator: Incomplete | None = None,
    ) -> Incomplete: ...

def demo() -> None: ...
def load_pos(num_sents: Incomplete) -> Incomplete: ...
def demo_pos() -> Incomplete: ...
def demo_pos_bw(
    test: int = 10,
    supervised: int = 20,
    unsupervised: int = 10,
    verbose: bool = True,
    max_iterations: int = 5,
) -> Incomplete: ...
def demo_bw() -> None: ...
