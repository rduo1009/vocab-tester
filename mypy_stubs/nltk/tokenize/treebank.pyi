from typing import (
    Iterator,
    List,
    Tuple,
)

from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.tokenize.destructive import (
    MacIntyreContractions as MacIntyreContractions,
)
from nltk.tokenize.util import align_tokens as align_tokens

class TreebankWordTokenizer:
    def span_tokenize(self, text: str) -> Iterator[Tuple[int, int]]: ...
    def tokenize(
        self,
        text: str,
        convert_parentheses: bool = ...,
        return_str: bool = ...,
    ) -> List[str]: ...

class TreebankWordDetokenizer(TokenizerI):
    CONTRACTIONS2: Incomplete
    CONTRACTIONS3: Incomplete
    ENDING_QUOTES: Incomplete
    DOUBLE_DASHES: Incomplete
    CONVERT_PARENTHESES: Incomplete
    PARENS_BRACKETS: Incomplete
    PUNCTUATION: Incomplete
    STARTING_QUOTES: Incomplete
    def tokenize(
        self, tokens: list[str], convert_parentheses: bool = False
    ) -> str: ...
    def detokenize(
        self, tokens: list[str], convert_parentheses: bool = False
    ) -> str: ...
