from _typeshed import Incomplete

from nltk.corpus import perluniprops as perluniprops
from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.tokenize.util import xml_unescape as xml_unescape

class NISTTokenizer(TokenizerI):
    STRIP_SKIP: Incomplete
    STRIP_EOL_HYPHEN: Incomplete
    PUNCT: Incomplete
    PERIOD_COMMA_PRECEED: Incomplete
    PERIOD_COMMA_FOLLOW: Incomplete
    DASH_PRECEED_DIGIT: Incomplete
    LANG_DEPENDENT_REGEXES: Incomplete
    pup_number: Incomplete
    pup_punct: Incomplete
    pup_symbol: Incomplete
    number_regex: Incomplete
    punct_regex: Incomplete
    symbol_regex: Incomplete
    NONASCII: Incomplete
    PUNCT_1: Incomplete
    PUNCT_2: Incomplete
    SYMBOLS: Incomplete
    INTERNATIONAL_REGEXES: Incomplete
    def lang_independent_sub(self, text: Incomplete) -> Incomplete: ...
    def tokenize(
        self,
        text: Incomplete,
        lowercase: bool = False,
        western_lang: bool = True,
        return_str: bool = False,
    ) -> Incomplete: ...
    def international_tokenize(
        self,
        text: Incomplete,
        lowercase: bool = False,
        split_non_ascii: bool = True,
        return_str: bool = False,
    ) -> Incomplete: ...
