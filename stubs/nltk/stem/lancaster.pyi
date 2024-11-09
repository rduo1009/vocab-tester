from _typeshed import Incomplete

from nltk.stem.api import StemmerI as StemmerI

class LancasterStemmer(StemmerI):
    default_rule_tuple: Incomplete
    rule_dictionary: Incomplete
    def __init__(
        self,
        rule_tuple: Incomplete | None = None,
        strip_prefix_flag: bool = False,
    ) -> None: ...
    def parseRules(self, rule_tuple: Incomplete | None = None) -> None: ...
    def stem(self, word: Incomplete) -> Incomplete: ...
