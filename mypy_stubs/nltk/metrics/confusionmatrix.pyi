from _typeshed import Incomplete

from nltk.probability import FreqDist as FreqDist

class ConfusionMatrix:
    def __init__(
        self,
        reference: Incomplete,
        test: Incomplete,
        sort_by_count: bool = False,
    ) -> None: ...
    def __getitem__(self, li_lj_tuple: Incomplete) -> Incomplete: ...
    def pretty_format(
        self,
        show_percents: bool = False,
        values_in_chart: bool = True,
        truncate: Incomplete | None = None,
        sort_by_count: bool = False,
    ) -> Incomplete: ...
    def key(self) -> Incomplete: ...
    def recall(self, value: Incomplete) -> Incomplete: ...
    def precision(self, value: Incomplete) -> Incomplete: ...
    def f_measure(
        self, value: Incomplete, alpha: float = 0.5
    ) -> Incomplete: ...
    def evaluate(
        self,
        alpha: float = 0.5,
        truncate: Incomplete | None = None,
        sort_by_count: bool = False,
    ) -> Incomplete: ...

def demo() -> None: ...
