from collections.abc import Generator

from _typeshed import Incomplete

from nltk.data import ZipFilePathPointer as ZipFilePathPointer
from nltk.internals import (
    find_dir as find_dir,
)
from nltk.internals import (
    find_file as find_file,
)
from nltk.internals import (
    find_jars_within_path as find_jars_within_path,
)
from nltk.parse.api import ParserI as ParserI
from nltk.parse.dependencygraph import DependencyGraph as DependencyGraph
from nltk.parse.util import taggedsents_to_conll as taggedsents_to_conll

def malt_regex_tagger() -> Incomplete: ...
def find_maltparser(parser_dirname: Incomplete) -> Incomplete: ...
def find_malt_model(model_filename: Incomplete) -> Incomplete: ...

class MaltParser(ParserI):
    malt_jars: Incomplete
    additional_java_args: Incomplete
    model: Incomplete
    working_dir: Incomplete
    tagger: Incomplete
    def __init__(
        self,
        parser_dirname: str = "",
        model_filename: Incomplete | None = None,
        tagger: Incomplete | None = None,
        additional_java_args: Incomplete | None = None,
    ) -> None: ...
    def parse_tagged_sents(
        self,
        sentences: Incomplete,
        verbose: bool = False,
        top_relation_label: str = "null",
    ) -> Generator[Incomplete, None, None]: ...
    def parse_sents(
        self,
        sentences: Incomplete,
        verbose: bool = False,
        top_relation_label: str = "null",
    ) -> Incomplete: ...
    def generate_malt_command(
        self,
        inputfilename: Incomplete,
        outputfilename: Incomplete | None = None,
        mode: Incomplete | None = None,
    ) -> Incomplete: ...
    def train(self, depgraphs: Incomplete, verbose: bool = False) -> None: ...
    def train_from_file(
        self, conll_file: Incomplete, verbose: bool = False
    ) -> Incomplete: ...
