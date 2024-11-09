from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.util import Trie as Trie

class MWETokenizer(TokenizerI):
    def __init__(
        self, mwes: Incomplete | None = None, separator: str = "_"
    ) -> None: ...
    def add_mwe(self, mwe: Incomplete) -> None: ...
    def tokenize(self, text: Incomplete) -> Incomplete: ...
