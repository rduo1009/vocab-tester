from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete

from nltk.internals import raise_unorderable_types as raise_unorderable_types

class AbstractCCGCategory(metaclass=ABCMeta):
    @abstractmethod
    def is_primitive(self) -> Incomplete: ...
    @abstractmethod
    def is_function(self) -> Incomplete: ...
    @abstractmethod
    def is_var(self) -> Incomplete: ...
    @abstractmethod
    def substitute(self, substitutions: Incomplete) -> Incomplete: ...
    @abstractmethod
    def can_unify(self, other: Incomplete) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...

class CCGVar(AbstractCCGCategory):
    def __init__(self, prim_only: bool = False) -> None: ...
    @classmethod
    def new_id(cls: Incomplete) -> Incomplete: ...
    @classmethod
    def reset_id(cls: Incomplete) -> None: ...
    def is_primitive(self) -> Incomplete: ...
    def is_function(self) -> Incomplete: ...
    def is_var(self) -> Incomplete: ...
    def substitute(self, substitutions: Incomplete) -> Incomplete: ...
    def can_unify(self, other: Incomplete) -> Incomplete: ...
    def id(self) -> Incomplete: ...

class Direction:
    def __init__(self, dir: Incomplete, restrictions: Incomplete) -> None: ...
    def is_forward(self) -> Incomplete: ...
    def is_backward(self) -> Incomplete: ...
    def dir(self) -> Incomplete: ...
    def restrs(self) -> Incomplete: ...
    def is_variable(self) -> Incomplete: ...
    def can_unify(self, other: Incomplete) -> Incomplete: ...
    def substitute(self, subs: Incomplete) -> Incomplete: ...
    def can_compose(self) -> Incomplete: ...
    def can_cross(self) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...
    def __neg__(self) -> Incomplete: ...

class PrimitiveCategory(AbstractCCGCategory):
    def __init__(
        self, categ: Incomplete, restrictions: Incomplete = []
    ) -> None: ...
    def is_primitive(self) -> Incomplete: ...
    def is_function(self) -> Incomplete: ...
    def is_var(self) -> Incomplete: ...
    def restrs(self) -> Incomplete: ...
    def categ(self) -> Incomplete: ...
    def substitute(self, subs: Incomplete) -> Incomplete: ...
    def can_unify(self, other: Incomplete) -> Incomplete: ...

class FunctionalCategory(AbstractCCGCategory):
    def __init__(
        self, res: Incomplete, arg: Incomplete, dir: Incomplete
    ) -> None: ...
    def is_primitive(self) -> Incomplete: ...
    def is_function(self) -> Incomplete: ...
    def is_var(self) -> Incomplete: ...
    def substitute(self, subs: Incomplete) -> Incomplete: ...
    def can_unify(self, other: Incomplete) -> Incomplete: ...
    def arg(self) -> Incomplete: ...
    def res(self) -> Incomplete: ...
    def dir(self) -> Incomplete: ...
