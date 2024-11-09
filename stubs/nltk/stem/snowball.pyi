from _typeshed import Incomplete

from nltk.corpus import stopwords as stopwords
from nltk.stem import porter as porter
from nltk.stem.api import StemmerI as StemmerI
from nltk.stem.util import (
    prefix_replace as prefix_replace,
)
from nltk.stem.util import (
    suffix_replace as suffix_replace,
)

class SnowballStemmer(StemmerI):
    languages: Incomplete
    stemmer: Incomplete
    stopwords: Incomplete
    def __init__(
        self, language: Incomplete, ignore_stopwords: bool = False
    ) -> None: ...
    def stem(self, token: Incomplete) -> Incomplete: ...

class _LanguageSpecificStemmer(StemmerI):  # type: ignore[misc]
    stopwords: Incomplete
    def __init__(self, ignore_stopwords: bool = False) -> None: ...

class PorterStemmer(_LanguageSpecificStemmer, porter.PorterStemmer):
    def __init__(self, ignore_stopwords: bool = False) -> None: ...

class _ScandinavianStemmer(_LanguageSpecificStemmer): ...  # type: ignore[misc]
class _StandardStemmer(_LanguageSpecificStemmer): ...

class ArabicStemmer(_StandardStemmer):
    is_verb: bool
    is_noun: bool
    is_defined: bool
    suffixes_verb_step1_success: bool
    suffix_verb_step2a_success: bool
    suffix_verb_step2b_success: bool
    suffix_noun_step2c2_success: bool
    suffix_noun_step1a_success: bool
    suffix_noun_step2a_success: bool
    suffix_noun_step2b_success: bool
    suffixe_noun_step1b_success: bool
    prefix_step2a_success: bool
    prefix_step3a_noun_success: bool
    prefix_step3b_noun_success: bool
    def stem(self, word: Incomplete) -> Incomplete: ...

class DanishStemmer(_ScandinavianStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class DutchStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class EnglishStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class FinnishStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class FrenchStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class GermanStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class HungarianStemmer(_LanguageSpecificStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class ItalianStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class NorwegianStemmer(_ScandinavianStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class PortugueseStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class RomanianStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class RussianStemmer(_LanguageSpecificStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class SpanishStemmer(_StandardStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

class SwedishStemmer(_ScandinavianStemmer):
    def stem(self, word: Incomplete) -> Incomplete: ...

def demo() -> None: ...
