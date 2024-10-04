import types
from collections.abc import Generator

from _typeshed import Incomplete

from nltk.internals import config_java as config_java
from nltk.internals import find_jar_iter as find_jar_iter
from nltk.internals import java as java
from nltk.parse.api import ParserI as ParserI
from nltk.parse.dependencygraph import DependencyGraph as DependencyGraph
from nltk.tag.api import TaggerI as TaggerI
from nltk.tokenize.api import TokenizerI as TokenizerI
from nltk.tree import Tree as Tree

class CoreNLPServerError(EnvironmentError): ...

def try_port(port: int = 0) -> Incomplete: ...

class CoreNLPServer:
    url: Incomplete
    verbose: Incomplete
    corenlp_options: Incomplete
    java_options: Incomplete
    def __init__(
        self,
        path_to_jar: Incomplete | None = None,
        path_to_models_jar: Incomplete | None = None,
        verbose: bool = False,
        java_options: Incomplete | None = None,
        corenlp_options: Incomplete | None = None,
        port: Incomplete | None = None,
    ) -> None: ...
    popen: Incomplete
    def start(
        self, stdout: str = "devnull", stderr: str = "devnull"
    ) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self) -> Incomplete: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> Incomplete: ...

class GenericCoreNLPParser(ParserI, TokenizerI, TaggerI):
    url: Incomplete
    encoding: Incomplete
    tagtype: Incomplete
    strict_json: Incomplete
    session: Incomplete
    def __init__(
        self,
        url: str = "http://localhost:9000",
        encoding: str = "utf8",
        tagtype: Incomplete | None = None,
        strict_json: bool = True,
    ) -> None: ...
    def parse_sents(
        self, sentences: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def raw_parse(
        self,
        sentence: Incomplete,
        properties: Incomplete | None = None,
        *args: Incomplete,
        **kwargs: Incomplete,
    ) -> Incomplete: ...
    def api_call(
        self,
        data: Incomplete,
        properties: Incomplete | None = None,
        timeout: int = 60,
    ) -> Incomplete: ...
    def raw_parse_sents(
        self,
        sentences: Incomplete,
        verbose: bool = False,
        properties: Incomplete | None = None,
        *args: Incomplete,
        **kwargs: Incomplete,
    ) -> Generator[Incomplete, None, None]: ...
    def parse_text(
        self, text: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Generator[Incomplete, None, None]: ...
    def tokenize(
        self, text: Incomplete, properties: Incomplete | None = None
    ) -> Generator[Incomplete, None, None]: ...
    def tag_sents(self, sentences: Incomplete) -> Incomplete: ...
    def tag(self, sentence: str) -> list[tuple[str, str]]: ...
    def raw_tag_sents(
        self, sentences: Incomplete
    ) -> Generator[Incomplete, None, None]: ...

class CoreNLPParser(GenericCoreNLPParser):
    parser_annotator: str
    def make_tree(self, result: Incomplete) -> Incomplete: ...

class CoreNLPDependencyParser(GenericCoreNLPParser):
    parser_annotator: str
    def make_tree(self, result: Incomplete) -> Incomplete: ...

def transform(sentence: Incomplete) -> Generator[Incomplete, None, None]: ...
