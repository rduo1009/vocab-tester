from abc import ABCMeta, abstractmethod
from collections.abc import Generator

from _typeshed import Incomplete

from nltk.tbl.feature import Feature as Feature
from nltk.tbl.rule import Rule as Rule

class BrillTemplateI(metaclass=ABCMeta):
    @abstractmethod
    def applicable_rules(
        self, tokens: Incomplete, i: Incomplete, correctTag: Incomplete
    ) -> Incomplete: ...
    @abstractmethod
    def get_neighborhood(
        self, token: Incomplete, index: Incomplete
    ) -> Incomplete: ...

class Template(BrillTemplateI):
    ALLTEMPLATES: Incomplete
    id: Incomplete
    def __init__(self, *features: Incomplete) -> None: ...
    def applicable_rules(
        self, tokens: Incomplete, index: Incomplete, correct_tag: Incomplete
    ) -> Incomplete: ...
    def get_neighborhood(
        self, tokens: Incomplete, index: Incomplete
    ) -> Incomplete: ...
    @classmethod
    def expand(
        cls: Incomplete,
        featurelists: Incomplete,
        combinations: Incomplete | None = None,
        skipintersecting: bool = True,
    ) -> Generator[Incomplete, None, Incomplete]: ...
