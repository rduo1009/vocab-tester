from abc import ABCMeta, abstractmethod
from collections.abc import Generator

from _typeshed import Incomplete

from nltk.ccg.api import FunctionalCategory as FunctionalCategory

class UndirectedBinaryCombinator(metaclass=ABCMeta):
    @abstractmethod
    def can_combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Incomplete: ...
    @abstractmethod
    def combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Incomplete: ...

class DirectedBinaryCombinator(metaclass=ABCMeta):
    @abstractmethod
    def can_combine(
        self, left: Incomplete, right: Incomplete
    ) -> Incomplete: ...
    @abstractmethod
    def combine(self, left: Incomplete, right: Incomplete) -> Incomplete: ...

class ForwardCombinator(DirectedBinaryCombinator):
    def __init__(
        self, combinator: Incomplete, predicate: Incomplete, suffix: str = ""
    ) -> None: ...
    def can_combine(
        self, left: Incomplete, right: Incomplete
    ) -> Incomplete: ...
    def combine(
        self, left: Incomplete, right: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class BackwardCombinator(DirectedBinaryCombinator):
    def __init__(
        self, combinator: Incomplete, predicate: Incomplete, suffix: str = ""
    ) -> None: ...
    def can_combine(
        self, left: Incomplete, right: Incomplete
    ) -> Incomplete: ...
    def combine(
        self, left: Incomplete, right: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...

class UndirectedFunctionApplication(UndirectedBinaryCombinator):
    def can_combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Incomplete: ...
    def combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

def forwardOnly(left: Incomplete, right: Incomplete) -> Incomplete: ...
def backwardOnly(left: Incomplete, right: Incomplete) -> Incomplete: ...

ForwardApplication: Incomplete
BackwardApplication: Incomplete

class UndirectedComposition(UndirectedBinaryCombinator):
    def can_combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Incomplete: ...
    def combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

def bothForward(left: Incomplete, right: Incomplete) -> Incomplete: ...
def bothBackward(left: Incomplete, right: Incomplete) -> Incomplete: ...
def crossedDirs(left: Incomplete, right: Incomplete) -> Incomplete: ...
def backwardBxConstraint(
    left: Incomplete, right: Incomplete
) -> Incomplete: ...

ForwardComposition: Incomplete
BackwardComposition: Incomplete
BackwardBx: Incomplete

class UndirectedSubstitution(UndirectedBinaryCombinator):
    def can_combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Incomplete: ...
    def combine(
        self, function: Incomplete, argument: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

def forwardSConstraint(left: Incomplete, right: Incomplete) -> Incomplete: ...
def backwardSxConstraint(
    left: Incomplete, right: Incomplete
) -> Incomplete: ...

ForwardSubstitution: Incomplete
BackwardSx: Incomplete

def innermostFunction(cate: Incomplete) -> Incomplete: ...

class UndirectedTypeRaise(UndirectedBinaryCombinator):
    def can_combine(
        self, function: Incomplete, arg: Incomplete
    ) -> Incomplete: ...
    def combine(
        self, function: Incomplete, arg: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

def forwardTConstraint(left: Incomplete, right: Incomplete) -> Incomplete: ...
def backwardTConstraint(left: Incomplete, right: Incomplete) -> Incomplete: ...

ForwardT: Incomplete
BackwardT: Incomplete
