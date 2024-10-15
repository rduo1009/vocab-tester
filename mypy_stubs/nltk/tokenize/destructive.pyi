from typing import Iterator

from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.tokenize.util import align_tokens as align_tokens

class MacIntyreContractions:
    CONTRACTIONS2: Incomplete
    CONTRACTIONS3: Incomplete
    CONTRACTIONS4: Incomplete

class NLTKWordTokenizer(TokenizerI):
    STARTING_QUOTES: Incomplete
    ENDING_QUOTES: Incomplete
    PUNCTUATION: Incomplete
    PARENS_BRACKETS: Incomplete
    CONVERT_PARENTHESES: Incomplete
    DOUBLE_DASHES: Incomplete
    CONTRACTIONS2: Incomplete
    CONTRACTIONS3: Incomplete
    def tokenize(
        self,
        text: str,
        convert_parentheses: bool = False,
        return_str: bool = False,
    ) -> list[str]: ...
    def span_tokenize(self, text: str) -> Iterator[tuple[int, int]]: ...
