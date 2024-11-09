from typing import (
    Iterator,
    List,
    Tuple,
)

from _typeshed import Incomplete

from nltk.tokenize.api import (
    StringTokenizer as StringTokenizer,
)
from nltk.tokenize.api import (
    TokenizerI as TokenizerI,
)
from nltk.tokenize.util import (
    regexp_span_tokenize as regexp_span_tokenize,
)
from nltk.tokenize.util import (
    string_span_tokenize as string_span_tokenize,
)

class CharTokenizer:
    def span_tokenize(self, s: str) -> Iterator[Tuple[int, int]]: ...
    def tokenize(self, s: str) -> List[str]: ...

class LineTokenizer:
    def __init__(self, blanklines: str = ...): ...

class SpaceTokenizer(StringTokenizer): ...
class TabTokenizer(StringTokenizer): ...

def line_tokenize(
    text: Incomplete, blanklines: str = "discard"
) -> Incomplete: ...
