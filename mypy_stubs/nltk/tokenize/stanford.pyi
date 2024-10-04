from _typeshed import Incomplete

from nltk.internals import (
    config_java as config_java,
)
from nltk.internals import (
    find_jar as find_jar,
)
from nltk.internals import (
    java as java,
)
from nltk.parse.corenlp import CoreNLPParser as CoreNLPParser
from nltk.tokenize.api import TokenizerI as TokenizerI

class StanfordTokenizer(TokenizerI):
    java_options: Incomplete
    def __init__(
        self,
        path_to_jar: Incomplete | None = None,
        encoding: str = "utf8",
        options: Incomplete | None = None,
        verbose: bool = False,
        java_options: str = "-mx1000m",
    ) -> None: ...
    def tokenize(self, s: Incomplete) -> Incomplete: ...
