from _typeshed import Incomplete

from nltk.tag.api import TaggerI as TaggerI

class CRFTagger(TaggerI):
    def __init__(
        self,
        feature_func: Incomplete | None = None,
        verbose: bool = False,
        training_opt: Incomplete = {},
    ) -> None: ...
    def set_model_file(self, model_file: Incomplete) -> None: ...
    def tag_sents(self, sents: Incomplete) -> Incomplete: ...
    def train(
        self, train_data: Incomplete, model_file: Incomplete
    ) -> None: ...
    def tag(self, tokens: Incomplete) -> Incomplete: ...
