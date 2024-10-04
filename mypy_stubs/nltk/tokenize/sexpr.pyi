from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI

class SExprTokenizer(TokenizerI):
    def __init__(self, parens: str = "()", strict: bool = True) -> None: ...
    def tokenize(self, text: Incomplete) -> Incomplete: ...

sexpr_tokenize: Incomplete
