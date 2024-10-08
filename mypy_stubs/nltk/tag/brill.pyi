from _typeshed import Incomplete

from nltk import jsontags as jsontags
from nltk.tag import TaggerI as TaggerI
from nltk.tbl import Feature as Feature
from nltk.tbl import Template as Template

class Word(Feature):
    json_tag: str
    @staticmethod
    def extract_property(
        tokens: Incomplete, index: Incomplete
    ) -> Incomplete: ...

class Pos(Feature):
    json_tag: str
    @staticmethod
    def extract_property(
        tokens: Incomplete, index: Incomplete
    ) -> Incomplete: ...

def nltkdemo18() -> Incomplete: ...
def nltkdemo18plus() -> Incomplete: ...
def fntbl37() -> Incomplete: ...
def brill24() -> Incomplete: ...
def describe_template_sets() -> None: ...

class BrillTagger(TaggerI):
    json_tag: str
    def __init__(
        self,
        initial_tagger: Incomplete,
        rules: Incomplete,
        training_stats: Incomplete | None = None,
    ) -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
    def rules(self) -> Incomplete: ...
    def train_stats(
        self, statistic: Incomplete | None = None
    ) -> Incomplete: ...
    def tag(self, tokens: Incomplete) -> Incomplete: ...
    def print_template_statistics(
        self, test_stats: Incomplete | None = None, printunused: bool = True
    ) -> Incomplete: ...
    def batch_tag_incremental(
        self, sequences: Incomplete, gold: Incomplete
    ) -> Incomplete: ...
