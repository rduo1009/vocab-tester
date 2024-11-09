from _typeshed import Incomplete

from nltk.probability import (
    ConditionalFreqDist as ConditionalFreqDist,
)
from nltk.probability import (
    FreqDist as FreqDist,
)
from nltk.tag.api import TaggerI as TaggerI

class TnT(TaggerI):
    unknown: int
    known: int
    def __init__(
        self,
        unk: Incomplete | None = None,
        Trained: bool = False,
        N: int = 1000,
        C: bool = False,
    ) -> None: ...
    def train(self, data: Incomplete) -> None: ...
    def tagdata(self, data: Incomplete) -> Incomplete: ...
    def tag(self, data: Incomplete) -> Incomplete: ...

def basic_sent_chop(data: Incomplete, raw: bool = True) -> Incomplete: ...
def demo() -> None: ...
def demo2() -> None: ...
def demo3() -> None: ...
