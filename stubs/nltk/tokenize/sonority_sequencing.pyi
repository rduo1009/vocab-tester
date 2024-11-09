from typing import (
    List,
    Tuple,
)

from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.util import ngrams as ngrams

class SyllableTokenizer:
    vowels: Incomplete
    phoneme_map: Incomplete
    def __init__(
        self, lang: str = "en", sonority_hierarchy: bool = ...
    ) -> None: ...
    def assign_values(self, token: str) -> List[Tuple[str, int]]: ...
    def tokenize(self, token: str) -> List[str]: ...
    def validate_syllables(self, syllable_list: List[str]) -> List[str]: ...
