from _typeshed import Incomplete

from nltk.stem.api import StemmerI as StemmerI

class RegexpStemmer(StemmerI):
    def __init__(self, regexp: Incomplete, min: int = 0) -> None: ...
    def stem(self, word: Incomplete) -> Incomplete: ...
