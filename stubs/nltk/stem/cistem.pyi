from _typeshed import Incomplete

from nltk.stem.api import StemmerI as StemmerI

class Cistem(StemmerI):
    strip_ge: Incomplete
    repl_xx: Incomplete
    strip_emr: Incomplete
    strip_nd: Incomplete
    strip_t: Incomplete
    strip_esn: Incomplete
    repl_xx_back: Incomplete
    def __init__(self, case_insensitive: bool = False) -> None: ...
    @staticmethod
    def replace_to(word: str) -> str: ...
    @staticmethod
    def replace_back(word: str) -> str: ...
    def stem(self, word: str) -> str: ...
    def segment(self, word: str) -> tuple[str, str]: ...
