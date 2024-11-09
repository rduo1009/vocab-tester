from _typeshed import Incomplete

from nltk.internals import (
    config_java as config_java,
)
from nltk.internals import (
    find_jar_iter as find_jar_iter,
)
from nltk.internals import (
    find_jars_within_path as find_jars_within_path,
)
from nltk.internals import (
    java as java,
)
from nltk.parse.api import ParserI as ParserI
from nltk.parse.dependencygraph import DependencyGraph as DependencyGraph
from nltk.tree import Tree as Tree

class GenericStanfordParser(ParserI):
    model_path: Incomplete
    corenlp_options: Incomplete
    java_options: Incomplete
    def __init__(
        self,
        path_to_jar: Incomplete | None = None,
        path_to_models_jar: Incomplete | None = None,
        model_path: str = "edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
        encoding: str = "utf8",
        verbose: bool = False,
        java_options: str = "-mx4g",
        corenlp_options: str = "",
    ) -> None: ...
    def parse_sents(
        self, sentences: Incomplete, verbose: bool = False
    ) -> Incomplete: ...
    def raw_parse(
        self, sentence: Incomplete, verbose: bool = False
    ) -> Incomplete: ...
    def raw_parse_sents(
        self, sentences: Incomplete, verbose: bool = False
    ) -> Incomplete: ...
    def tagged_parse(
        self, sentence: Incomplete, verbose: bool = False
    ) -> Incomplete: ...
    def tagged_parse_sents(
        self, sentences: Incomplete, verbose: bool = False
    ) -> Incomplete: ...

class StanfordParser(GenericStanfordParser):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class StanfordDependencyParser(GenericStanfordParser):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

class StanfordNeuralDependencyParser(GenericStanfordParser):
    def __init__(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...
    def tagged_parse_sents(
        self, sentences: Incomplete, verbose: bool = False
    ) -> None: ...
