from _typeshed import Incomplete

from nltk.probability import ProbabilisticMixIn
from nltk.tree.parented import MultiParentedTree, ParentedTree
from nltk.tree.tree import Tree

__all__ = [
    "ImmutableProbabilisticTree",
    "ImmutableTree",
    "ImmutableParentedTree",
    "ImmutableMultiParentedTree",
]

class ImmutableTree(Tree):
    def __init__(
        self, node: Incomplete, children: Incomplete | None = None
    ) -> None: ...
    def __setitem__(self, index: Incomplete, value: Incomplete) -> None: ...
    def __setslice__(
        self, i: Incomplete, j: Incomplete, value: Incomplete
    ) -> None: ...
    def __delitem__(self, index: Incomplete) -> None: ...
    def __delslice__(self, i: Incomplete, j: Incomplete) -> None: ...
    def __iadd__(self, other: Incomplete) -> None: ...
    def __imul__(self, other: Incomplete) -> None: ...
    def append(self, v: Incomplete) -> None: ...
    def extend(self, v: Incomplete) -> None: ...
    def pop(self, v: Incomplete | None = None) -> None: ...
    def remove(self, v: Incomplete) -> None: ...
    def reverse(self) -> None: ...
    def sort(self) -> None: ...
    def __hash__(self) -> Incomplete: ...
    def set_label(self, value: Incomplete) -> None: ...

class ImmutableProbabilisticTree(ImmutableTree, ProbabilisticMixIn):
    def __init__(
        self,
        node: Incomplete,
        children: Incomplete | None = None,
        **prob_kwargs: Incomplete,
    ) -> None: ...
    def copy(self, deep: bool = False) -> Incomplete: ...
    @classmethod
    def convert(cls: Incomplete, val: Incomplete) -> Incomplete: ...

class ImmutableParentedTree(ImmutableTree, ParentedTree): ...
class ImmutableMultiParentedTree(ImmutableTree, MultiParentedTree): ...
