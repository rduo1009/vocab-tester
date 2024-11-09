from collections.abc import Generator
from typing import NamedTuple

from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.wordlist import (
    WordListCorpusReader as WordListCorpusReader,
)
from nltk.tokenize import line_tokenize as line_tokenize

class PanlexLanguage(NamedTuple):
    panlex_uid: Incomplete
    iso639: Incomplete
    iso639_type: Incomplete
    script: Incomplete
    name: Incomplete
    langvar_uid: Incomplete

class PanlexSwadeshCorpusReader(WordListCorpusReader):
    swadesh_size: Incomplete
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def license(self) -> Incomplete: ...
    def language_codes(self) -> Incomplete: ...
    def get_languages(self) -> Generator[Incomplete, None, None]: ...
    def get_macrolanguages(self) -> Incomplete: ...
    def words_by_lang(self, lang_code: Incomplete) -> Incomplete: ...
    def words_by_iso639(self, iso63_code: Incomplete) -> Incomplete: ...
    def entries(self, fileids: Incomplete | None = None) -> Incomplete: ...
