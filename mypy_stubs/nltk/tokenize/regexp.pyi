from collections.abc import Generator
from re import RegexFlag

from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.tokenize.util import regexp_span_tokenize as regexp_span_tokenize

class RegexpTokenizer(TokenizerI):
    def __init__(
        self,
        pattern: str,
        gaps: bool = False,
        discard_empty: bool = True,
        flags: RegexFlag = ...,
    ) -> None: ...
    def tokenize(self, text: Incomplete) -> Incomplete: ...
    def span_tokenize(
        self, text: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class WhitespaceTokenizer(RegexpTokenizer):
    def __init__(self) -> None: ...

class BlanklineTokenizer(RegexpTokenizer):
    def __init__(self) -> None: ...

class WordPunctTokenizer(RegexpTokenizer):
    def __init__(self) -> None: ...

def regexp_tokenize(
    text: Incomplete,
    pattern: Incomplete,
    gaps: bool = False,
    discard_empty: bool = True,
    flags: Incomplete = ...,
) -> Incomplete: ...

blankline_tokenize: Incomplete
wordpunct_tokenize: Incomplete
