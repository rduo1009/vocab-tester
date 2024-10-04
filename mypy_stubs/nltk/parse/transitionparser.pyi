from _typeshed import Incomplete

from nltk.parse import (
    DependencyEvaluator as DependencyEvaluator,
)
from nltk.parse import (
    DependencyGraph as DependencyGraph,
)
from nltk.parse import (
    ParserI as ParserI,
)

class Configuration:
    stack: Incomplete
    buffer: Incomplete
    arcs: Incomplete
    def __init__(self, dep_graph: Incomplete) -> None: ...
    def extract_features(self) -> Incomplete: ...

class Transition:
    LEFT_ARC: str
    RIGHT_ARC: str
    SHIFT: str
    REDUCE: str
    def __init__(self, alg_option: Incomplete) -> None: ...
    def left_arc(
        self, conf: Incomplete, relation: Incomplete
    ) -> Incomplete: ...
    def right_arc(
        self, conf: Incomplete, relation: Incomplete
    ) -> Incomplete: ...
    def reduce(self, conf: Incomplete) -> Incomplete: ...
    def shift(self, conf: Incomplete) -> Incomplete: ...

class TransitionParser(ParserI):
    ARC_STANDARD: str
    ARC_EAGER: str
    def __init__(self, algorithm: Incomplete) -> None: ...
    def train(
        self,
        depgraphs: Incomplete,
        modelfile: Incomplete,
        verbose: bool = True,
    ) -> None: ...
    def parse(
        self, depgraphs: Incomplete, modelFile: Incomplete
    ) -> Incomplete: ...

def demo() -> None: ...
