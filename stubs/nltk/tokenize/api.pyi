from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import Iterator

from _typeshed import Incomplete

from nltk.internals import overridden as overridden
from nltk.tokenize.util import string_span_tokenize as string_span_tokenize

class TokenizerI(ABC):
    @abstractmethod
    def tokenize(self, s: str) -> list[str]: ...
    def span_tokenize(self, s: str) -> Iterator[tuple[int, int]]: ...
    def tokenize_sents(self, strings: list[str]) -> list[list[str]]: ...
    def span_tokenize_sents(
        self, strings: list[str]
    ) -> Iterator[list[tuple[int, int]]]: ...

class StringTokenizer(TokenizerI):
    def tokenize(self, s: Incomplete) -> Incomplete: ...
    def span_tokenize(
        self, s: Incomplete
    ) -> Generator[Incomplete, Incomplete, None]: ...
