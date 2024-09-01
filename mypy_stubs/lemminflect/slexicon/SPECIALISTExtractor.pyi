from typing import Any

from .SPECIALISTEntry import AuxModVariant as AuxModVariant
from .SPECIALISTEntry import SPECIALISTEntry as SPECIALISTEntry
from .SPECIALISTEntry import StandardVariant as StandardVariant

class SPECIALISTExtractor:
    word_set: set[str]
    lexicon: list[Any]
    def __init__(self, word_set_fn: str | None = None) -> None: ...
    def extract(self, lexicon_fn: str) -> None: ...
