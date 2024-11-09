from _typeshed import Incomplete

from nltk.corpus import treebank as treebank
from nltk.tag import (
    BrillTaggerTrainer as BrillTaggerTrainer,
)
from nltk.tag import (
    RegexpTagger as RegexpTagger,
)
from nltk.tag import (
    UnigramTagger as UnigramTagger,
)
from nltk.tag.brill import Pos as Pos
from nltk.tag.brill import Word as Word
from nltk.tbl import Template as Template
from nltk.tbl import error_list as error_list

def demo() -> None: ...
def demo_repr_rule_format() -> None: ...
def demo_str_rule_format() -> None: ...
def demo_verbose_rule_format() -> None: ...
def demo_multiposition_feature() -> None: ...
def demo_multifeature_template() -> None: ...
def demo_template_statistics() -> None: ...
def demo_generated_templates() -> None: ...
def demo_learning_curve() -> None: ...
def demo_error_analysis() -> None: ...
def demo_serialize_tagger() -> None: ...
def demo_high_accuracy_rules() -> None: ...
def postag(
    templates: Incomplete | None = None,
    tagged_data: Incomplete | None = None,
    num_sents: int = 1000,
    max_rules: int = 300,
    min_score: int = 3,
    min_acc: Incomplete | None = None,
    train: float = 0.8,
    trace: int = 3,
    randomize: bool = False,
    ruleformat: str = "str",
    incremental_stats: bool = False,
    template_stats: bool = False,
    error_output: Incomplete | None = None,
    serialize_output: Incomplete | None = None,
    learning_curve_output: Incomplete | None = None,
    learning_curve_take: int = 300,
    baseline_backoff_tagger: Incomplete | None = None,
    separate_baseline_data: bool = False,
    cache_baseline_tagger: Incomplete | None = None,
) -> None: ...

NN_CD_TAGGER: Incomplete
REGEXP_TAGGER: Incomplete

def corpus_size(seqs: Incomplete) -> Incomplete: ...
