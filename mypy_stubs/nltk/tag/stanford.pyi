from _typeshed import Incomplete

from nltk.internals import (
    config_java as config_java,
)
from nltk.internals import (
    find_file as find_file,
)
from nltk.internals import (
    find_jar as find_jar,
)
from nltk.internals import (
    java as java,
)
from nltk.tag.api import TaggerI as TaggerI

class StanfordTagger(TaggerI):
    java_options: Incomplete
    def __init__(
        self,
        model_filename: Incomplete,
        path_to_jar: Incomplete | None = None,
        encoding: str = "utf8",
        verbose: bool = False,
        java_options: str = "-mx1000m",
    ) -> None: ...
    def tag(self, tokens: Incomplete) -> Incomplete: ...
    def tag_sents(self, sentences: Incomplete) -> Incomplete: ...
    def parse_output(
        self, text: Incomplete, sentences: Incomplete | None = None
    ) -> Incomplete: ...

class StanfordPOSTagger(StanfordTagger):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class StanfordNERTagger(StanfordTagger):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def parse_output(
        self, text: Incomplete, sentences: Incomplete
    ) -> Incomplete: ...
