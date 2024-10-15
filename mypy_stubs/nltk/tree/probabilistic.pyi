from _typeshed import Incomplete

from nltk.probability import ProbabilisticMixIn
from nltk.tree.tree import Tree

__all__ = ["ProbabilisticTree"]

class ProbabilisticTree(Tree, ProbabilisticMixIn):
    def __init__(
        self,
        node: Incomplete,
        children: Incomplete | None = None,
        **prob_kwargs: Incomplete,
    ) -> None: ...
    def copy(self, deep: bool = False) -> Incomplete: ...
    @classmethod
    def convert(cls: Incomplete, val: Incomplete) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
