from abc import ABCMeta, abstractmethod
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from _typeshed import Incomplete
from matplotlib.axes._axes import Axes  # type: ignore[import-not-found]
from numpy import float64

__all__ = [
    "ConditionalFreqDist",
    "ConditionalProbDist",
    "ConditionalProbDistI",
    "CrossValidationProbDist",
    "DictionaryConditionalProbDist",
    "DictionaryProbDist",
    "ELEProbDist",
    "FreqDist",
    "SimpleGoodTuringProbDist",
    "HeldoutProbDist",
    "ImmutableProbabilisticMixIn",
    "LaplaceProbDist",
    "LidstoneProbDist",
    "MLEProbDist",
    "MutableProbDist",
    "KneserNeyProbDist",
    "ProbDistI",
    "ProbabilisticMixIn",
    "UniformProbDist",
    "WittenBellProbDist",
    "add_logs",
    "log_likelihood",
    "sum_logs",
    "entropy",
]

def _get_kwarg(
    kwargs: Dict[str, str], key: str, default: bool
) -> Union[str, bool]: ...

class ConditionalFreqDist:
    def conditions(self) -> List[Any]: ...
    def plot(
        self,
        *args: Incomplete,
        samples: Incomplete | None = None,
        title: str = "",
        cumulative: bool = False,
        percents: bool = False,
        conditions: Incomplete | None = None,
        show: bool = False,
        **kwargs: Incomplete,
    ) -> Axes: ...
    def __init__(self, cond_samples: Incomplete | None = None) -> None: ...
    def __reduce__(self) -> Incomplete: ...
    def N(self) -> Incomplete: ...
    def tabulate(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def __add__(self, other: Incomplete) -> Incomplete: ...
    def __sub__(self, other: Incomplete) -> Incomplete: ...
    def __or__(self, other: Incomplete) -> Incomplete: ...
    def __and__(self, other: Incomplete) -> Incomplete: ...
    def __le__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def __ge__(self, other: Incomplete) -> Incomplete: ...
    def __gt__(self, other: Incomplete) -> Incomplete: ...
    def deepcopy(self) -> Incomplete: ...
    copy = deepcopy

class DictionaryConditionalProbDist:
    def __init__(
        self, probdist_dict: Dict[str, DictionaryProbDist]
    ) -> None: ...

class DictionaryProbDist:
    def __init__(
        self,
        prob_dict: Optional[Dict[str, Union[float64, float]]] = None,
        log: bool = False,
        normalize: bool = False,
    ) -> None: ...
    def logprob(self, sample: str) -> float: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...

class FreqDist:
    def B(self) -> int: ...
    def N(self) -> int: ...
    def __init__(self, samples: Optional[List[str]] = None) -> None: ...
    def __iter__(self) -> Iterator[Union[str, Tuple[str, str]]]: ...
    def __setitem__(
        self, key: Union[int, str, Tuple[str, str]], val: int
    ) -> None: ...
    def __delitem__(self, key: Incomplete) -> None: ...
    def update(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def setdefault(self, key: Incomplete, val: Incomplete) -> None: ...
    def hapaxes(self) -> Incomplete: ...
    def Nr(
        self, r: Incomplete, bins: Incomplete | None = None
    ) -> Incomplete: ...
    def r_Nr(self, bins: Incomplete | None = None) -> Incomplete: ...
    def freq(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def plot(
        self,
        *args: Incomplete,
        title: str = "",
        cumulative: bool = False,
        percents: bool = False,
        show: bool = False,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def tabulate(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def copy(self) -> Incomplete: ...
    def __add__(self, other: Incomplete) -> Incomplete: ...
    def __sub__(self, other: Incomplete) -> Incomplete: ...
    def __or__(self, other: Incomplete) -> Incomplete: ...
    def __and__(self, other: Incomplete) -> Incomplete: ...
    def __le__(self, other: Incomplete) -> Incomplete: ...
    def __ge__(self, other: Incomplete) -> Incomplete: ...
    __lt__: Incomplete
    __gt__: Incomplete
    def pprint(
        self, maxlen: int = 10, stream: Incomplete | None = None
    ) -> None: ...
    def pformat(self, maxlen: int = 10) -> Incomplete: ...

class ProbDistI(metaclass=ABCMeta):
    SUM_TO_ONE: bool
    @abstractmethod
    def __init__(self) -> Incomplete: ...
    @abstractmethod
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def logprob(self, sample: Incomplete) -> Incomplete: ...
    @abstractmethod
    def max(self) -> Incomplete: ...
    @abstractmethod
    def samples(self) -> Incomplete: ...
    def discount(self) -> Incomplete: ...
    def generate(self) -> Incomplete: ...

class UniformProbDist(ProbDistI):
    def __init__(self, samples: Incomplete) -> None: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...

class RandomProbDist(ProbDistI):
    def __init__(self, samples: Incomplete) -> None: ...
    @classmethod
    def unirand(cls: Incomplete, samples: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def samples(self) -> Incomplete: ...

class MLEProbDist(ProbDistI):
    def __init__(
        self, freqdist: Incomplete, bins: Incomplete | None = None
    ) -> None: ...
    def freqdist(self) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...

class LidstoneProbDist(ProbDistI):
    SUM_TO_ONE: bool
    def __init__(
        self,
        freqdist: Incomplete,
        gamma: Incomplete,
        bins: Incomplete | None = None,
    ) -> None: ...
    def freqdist(self) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...
    def discount(self) -> Incomplete: ...

class LaplaceProbDist(LidstoneProbDist):
    def __init__(
        self, freqdist: Incomplete, bins: Incomplete | None = None
    ) -> None: ...

class ELEProbDist(LidstoneProbDist):
    def __init__(
        self, freqdist: Incomplete, bins: Incomplete | None = None
    ) -> None: ...

class HeldoutProbDist(ProbDistI):
    SUM_TO_ONE: bool
    def __init__(
        self,
        base_fdist: Incomplete,
        heldout_fdist: Incomplete,
        bins: Incomplete | None = None,
    ) -> None: ...
    def base_fdist(self) -> Incomplete: ...
    def heldout_fdist(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def discount(self) -> None: ...

class CrossValidationProbDist(ProbDistI):
    SUM_TO_ONE: bool
    def __init__(self, freqdists: Incomplete, bins: Incomplete) -> None: ...
    def freqdists(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def discount(self) -> None: ...

class WittenBellProbDist(ProbDistI):
    def __init__(
        self, freqdist: Incomplete, bins: Incomplete | None = None
    ) -> None: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...
    def freqdist(self) -> Incomplete: ...
    def discount(self) -> None: ...

class SimpleGoodTuringProbDist(ProbDistI):
    SUM_TO_ONE: bool
    def __init__(
        self, freqdist: Incomplete, bins: Incomplete | None = None
    ) -> None: ...
    def find_best_fit(self, r: Incomplete, nr: Incomplete) -> None: ...
    def smoothedNr(self, r: Incomplete) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def check(self) -> None: ...
    def discount(self) -> Incomplete: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...
    def freqdist(self) -> Incomplete: ...

class MutableProbDist(ProbDistI):
    def __init__(
        self,
        prob_dist: Incomplete,
        samples: Incomplete,
        store_logs: bool = True,
    ) -> None: ...
    def max(self) -> Incomplete: ...
    def samples(self) -> Incomplete: ...
    def prob(self, sample: Incomplete) -> Incomplete: ...
    def logprob(self, sample: Incomplete) -> Incomplete: ...
    def update(
        self, sample: Incomplete, prob: Incomplete, log: bool = True
    ) -> None: ...

class KneserNeyProbDist(ProbDistI):
    def __init__(
        self,
        freqdist: Incomplete,
        bins: Incomplete | None = None,
        discount: float = 0.75,
    ) -> None: ...
    def prob(self, trigram: Incomplete) -> Incomplete: ...
    def discount(self) -> Incomplete: ...
    def set_discount(self, discount: Incomplete) -> None: ...
    def samples(self) -> Incomplete: ...
    def max(self) -> Incomplete: ...

def log_likelihood(
    test_pdist: Incomplete, actual_pdist: Incomplete
) -> Incomplete: ...
def entropy(pdist: Incomplete) -> Incomplete: ...

class ConditionalProbDistI(dict, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> Incomplete: ...
    def conditions(self) -> Incomplete: ...

class ConditionalProbDist(ConditionalProbDistI):
    def __init__(
        self,
        cfdist: Incomplete,
        probdist_factory: Incomplete,
        *factory_args: Incomplete,
        **factory_kw_args: Incomplete,
    ) -> None: ...
    def __missing__(self, key: Incomplete) -> Incomplete: ...

def add_logs(logx: Incomplete, logy: Incomplete) -> Incomplete: ...
def sum_logs(logs: Incomplete) -> Incomplete: ...

class ProbabilisticMixIn:
    def __init__(self, **kwargs: Incomplete) -> None: ...
    def set_prob(self, prob: Incomplete) -> None: ...
    def set_logprob(self, logprob: Incomplete) -> None: ...
    def prob(self) -> Incomplete: ...
    def logprob(self) -> Incomplete: ...

class ImmutableProbabilisticMixIn(ProbabilisticMixIn):
    def set_prob(self, prob: Incomplete) -> None: ...
    def set_logprob(self, prob: Incomplete) -> None: ...