from _typeshed import Incomplete

from nltk.tokenize.api import TokenizerI as TokenizerI

class LegalitySyllableTokenizer(TokenizerI):
    legal_frequency_threshold: Incomplete
    vowels: Incomplete
    legal_onsets: Incomplete
    def __init__(
        self,
        tokenized_source_text: Incomplete,
        vowels: str = "aeiouy",
        legal_frequency_threshold: float = 0.001,
    ) -> None: ...
    def find_legal_onsets(self, words: Incomplete) -> Incomplete: ...
    def onset(self, word: Incomplete) -> Incomplete: ...
    def tokenize(self, token: Incomplete) -> Incomplete: ...
