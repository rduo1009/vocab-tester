from _typeshed import Incomplete

from nltk.tag import BrillTagger as BrillTagger
from nltk.tag import untag as untag

class BrillTaggerTrainer:
    def __init__(
        self,
        initial_tagger: Incomplete,
        templates: Incomplete,
        trace: int = 0,
        deterministic: Incomplete | None = None,
        ruleformat: str = "str",
    ) -> None: ...
    def train(
        self,
        train_sents: Incomplete,
        max_rules: int = 200,
        min_score: int = 2,
        min_acc: Incomplete | None = None,
    ) -> Incomplete: ...
