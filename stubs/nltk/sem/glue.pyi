from _typeshed import Incomplete

from nltk.internals import Counter as Counter
from nltk.sem import drt as drt
from nltk.sem import linearlogic as linearlogic
from nltk.sem.logic import (
    AbstractVariableExpression as AbstractVariableExpression,
)
from nltk.sem.logic import Expression as Expression
from nltk.sem.logic import LambdaExpression as LambdaExpression
from nltk.sem.logic import Variable as Variable
from nltk.sem.logic import VariableExpression as VariableExpression
from nltk.tag import BigramTagger as BigramTagger
from nltk.tag import RegexpTagger as RegexpTagger
from nltk.tag import TrigramTagger as TrigramTagger
from nltk.tag import UnigramTagger as UnigramTagger

SPEC_SEMTYPES: Incomplete
OPTIONAL_RELATIONSHIPS: Incomplete

class GlueFormula:
    meaning: Incomplete
    glue: Incomplete
    indices: Incomplete
    def __init__(
        self,
        meaning: Incomplete,
        glue: Incomplete,
        indices: Incomplete | None = None,
    ) -> None: ...
    def applyto(self, arg: Incomplete) -> Incomplete: ...
    def make_VariableExpression(self, name: Incomplete) -> Incomplete: ...
    def make_LambdaExpression(
        self: Incomplete, variable: Incomplete, term: Incomplete
    ) -> Incomplete: ...
    def lambda_abstract(self, other: Incomplete) -> Incomplete: ...
    def compile(self, counter: Incomplete | None = None) -> Incomplete: ...
    def simplify(self) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...

class GlueDict(dict):
    filename: Incomplete
    file_encoding: Incomplete
    def __init__(
        self, filename: Incomplete, encoding: Incomplete | None = None
    ) -> None: ...
    def read_file(self, empty_first: bool = True) -> None: ...
    def to_glueformula_list(
        self,
        depgraph: Incomplete,
        node: Incomplete | None = None,
        counter: Incomplete | None = None,
        verbose: bool = False,
    ) -> Incomplete: ...
    def lookup(
        self, node: Incomplete, depgraph: Incomplete, counter: Incomplete
    ) -> Incomplete: ...
    def add_missing_dependencies(
        self, node: Incomplete, depgraph: Incomplete
    ) -> None: ...
    def get_semtypes(self, node: Incomplete) -> Incomplete: ...
    def get_glueformulas_from_semtype_entry(
        self,
        lookup: Incomplete,
        word: Incomplete,
        node: Incomplete,
        depgraph: Incomplete,
        counter: Incomplete,
    ) -> Incomplete: ...
    def get_meaning_formula(
        self, generic: Incomplete, word: Incomplete
    ) -> Incomplete: ...
    def initialize_labels(
        self,
        expr: Incomplete,
        node: Incomplete,
        depgraph: Incomplete,
        unique_index: Incomplete,
    ) -> Incomplete: ...
    def find_label_name(
        self,
        name: Incomplete,
        node: Incomplete,
        depgraph: Incomplete,
        unique_index: Incomplete,
    ) -> Incomplete: ...
    def get_label(self, node: Incomplete) -> Incomplete: ...
    def lookup_unique(
        self, rel: Incomplete, node: Incomplete, depgraph: Incomplete
    ) -> Incomplete: ...
    def get_GlueFormula_factory(self) -> Incomplete: ...

class Glue:
    verbose: Incomplete
    remove_duplicates: Incomplete
    depparser: Incomplete
    prover: Incomplete
    semtype_file: Incomplete
    def __init__(
        self,
        semtype_file: Incomplete | None = None,
        remove_duplicates: bool = False,
        depparser: Incomplete | None = None,
        verbose: bool = False,
    ) -> None: ...
    def train_depparser(self, depgraphs: Incomplete | None = None) -> None: ...
    def parse_to_meaning(self, sentence: Incomplete) -> Incomplete: ...
    def get_readings(self, agenda: Incomplete) -> Incomplete: ...
    def parse_to_compiled(self, sentence: Incomplete) -> Incomplete: ...
    def dep_parse(self, sentence: Incomplete) -> Incomplete: ...
    def depgraph_to_glue(self, depgraph: Incomplete) -> Incomplete: ...
    def get_glue_dict(self) -> Incomplete: ...
    def gfl_to_compiled(self, gfl: Incomplete) -> Incomplete: ...
    def get_pos_tagger(self) -> Incomplete: ...

class DrtGlueFormula(GlueFormula):
    meaning: Incomplete
    glue: Incomplete
    indices: Incomplete
    def __init__(
        self,
        meaning: Incomplete,
        glue: Incomplete,
        indices: Incomplete | None = None,
    ) -> None: ...
    def make_VariableExpression(self, name: Incomplete) -> Incomplete: ...
    def make_LambdaExpression(
        self, variable: Incomplete, term: Incomplete
    ) -> Incomplete: ...

class DrtGlueDict(GlueDict):
    def get_GlueFormula_factory(self) -> Incomplete: ...

class DrtGlue(Glue):
    def __init__(
        self,
        semtype_file: Incomplete | None = None,
        remove_duplicates: bool = False,
        depparser: Incomplete | None = None,
        verbose: bool = False,
    ) -> None: ...
    def get_glue_dict(self) -> Incomplete: ...

def demo(show_example: int = -1) -> None: ...
