from collections.abc import Generator

from _typeshed import Incomplete

from nltk.data import ZipFilePathPointer as ZipFilePathPointer
from nltk.internals import find_dir as find_dir
from nltk.tokenize.api import TokenizerI as TokenizerI

class ReppTokenizer(TokenizerI):
    repp_dir: Incomplete
    working_dir: Incomplete
    encoding: Incomplete
    def __init__(
        self, repp_dir: Incomplete, encoding: str = "utf8"
    ) -> None: ...
    def tokenize(self, sentence: Incomplete) -> Incomplete: ...
    def tokenize_sents(
        self, sentences: Incomplete, keep_token_positions: bool = False
    ) -> Generator[Incomplete, None, None]: ...
    def generate_repp_command(
        self, inputfilename: Incomplete
    ) -> Incomplete: ...
    @staticmethod
    def parse_repp_outputs(
        repp_output: Incomplete,
    ) -> Generator[Incomplete, None, None]: ...
    def find_repptokenizer(self, repp_dirname: Incomplete) -> Incomplete: ...
