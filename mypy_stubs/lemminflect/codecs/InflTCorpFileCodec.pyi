# Auto-generated by stubgen

from _typeshed import Incomplete

class Entry:
    lemma: Incomplete
    category: Incomplete
    source: Incomplete
    def __init__(
        self, lemma: Incomplete, category: Incomplete, source: Incomplete
    ) -> None: ...

class InflTCorpFileCodec:
    @staticmethod
    def fromString(line: Incomplete) -> Incomplete: ...
    @staticmethod
    def toString(
        lemma: Incomplete, category: Incomplete, source: Incomplete
    ) -> Incomplete: ...
    @classmethod
    def load(cls: Incomplete, fn: Incomplete) -> Incomplete: ...
