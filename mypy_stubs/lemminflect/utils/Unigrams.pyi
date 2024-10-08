from collections import Counter

from ..slexicon.SKey import SKey

class Unigrams:
    counter: Counter[tuple[str, str]]
    counter_word: Counter[str]

    def __init__(self, fn: str) -> None: ...
    def getCount(self, word: str, tag: str | None = None) -> int: ...
    def getCountForLemma(self, word: str, category: SKey) -> int: ...
    def getCountForInflections(
        self, word: str, category: SKey, infl_type: str
    ) -> int: ...
    def save(self, fn: str, min_count: int = 1) -> None: ...
    @staticmethod
    def saveCounter(
        fn: str, counter: Counter[tuple[str, str]], min_count: int = 1
    ) -> None: ...
    @staticmethod
    def load(fn: str) -> Counter[tuple[str, str]]: ...
    @staticmethod
    def convertToWordKey(
        counter: Counter[tuple[str, str]],
    ) -> Counter[str]: ...
