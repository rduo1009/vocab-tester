from _typeshed import Incomplete

from nltk.stem.api import StemmerI as StemmerI

__docformat__: str

class PorterStemmer(StemmerI):
    NLTK_EXTENSIONS: str
    MARTIN_EXTENSIONS: str
    ORIGINAL_ALGORITHM: str
    mode: Incomplete
    pool: Incomplete
    vowels: Incomplete
    def __init__(self, mode: Incomplete = ...) -> None: ...
    def stem(
        self, word: Incomplete, to_lowercase: bool = True
    ) -> Incomplete: ...

def demo() -> None: ...
