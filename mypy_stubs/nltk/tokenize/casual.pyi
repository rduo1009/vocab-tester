import regex
from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI

EMOTICONS: str
URLS: str
FLAGS: str
PHONE_REGEX: str
REGEXPS: Incomplete
REGEXPS_PHONE: Incomplete
HANG_RE: Incomplete
EMOTICON_RE: Incomplete
ENT_RE: Incomplete
HANDLES_RE: Incomplete

class TweetTokenizer(TokenizerI):
    preserve_case: Incomplete
    reduce_len: Incomplete
    strip_handles: Incomplete
    match_phone_numbers: Incomplete
    def __init__(
        self,
        preserve_case: bool = True,
        reduce_len: bool = False,
        strip_handles: bool = False,
        match_phone_numbers: bool = True,
    ) -> None: ...
    def tokenize(self, text: str) -> list[str]: ...
    @property
    def WORD_RE(self) -> regex.Pattern: ...
    @property
    def PHONE_WORD_RE(self) -> regex.Pattern: ...

def reduce_lengthening(text: Incomplete) -> Incomplete: ...
def remove_handles(text: Incomplete) -> Incomplete: ...
def casual_tokenize(
    text: Incomplete,
    preserve_case: bool = True,
    reduce_len: bool = False,
    strip_handles: bool = False,
    match_phone_numbers: bool = True,
) -> Incomplete: ...
