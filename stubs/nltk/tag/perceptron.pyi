from _typeshed import Incomplete

from nltk import jsontags as jsontags
from nltk.data import find as find
from nltk.data import load as load
from nltk.tag.api import TaggerI as TaggerI

TRAINED_TAGGER_PATH: str
TAGGER_JSONS: Incomplete

class AveragedPerceptron:
    json_tag: str
    weights: Incomplete
    classes: Incomplete
    i: int
    def __init__(self, weights: Incomplete | None = None) -> None: ...
    def predict(
        self, features: Incomplete, return_conf: bool = False
    ) -> Incomplete: ...
    def update(
        self, truth: Incomplete, guess: Incomplete, features: Incomplete
    ) -> None: ...
    def average_weights(self) -> None: ...
    def save(self, path: Incomplete) -> Incomplete: ...
    def load(self, path: Incomplete) -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...

class PerceptronTagger(TaggerI):
    json_tag: str
    START: Incomplete
    END: Incomplete
    model: Incomplete
    tagdict: Incomplete
    classes: Incomplete
    def __init__(self, load: bool = True, lang: str = "eng") -> None: ...
    def tag(
        self,
        tokens: Incomplete,
        return_conf: bool = False,
        use_tagdict: bool = True,
    ) -> Incomplete: ...
    def train(
        self,
        sentences: Incomplete,
        save_loc: Incomplete | None = None,
        nr_iter: int = 5,
    ) -> None: ...
    def save_to_json(self, loc: Incomplete, lang: str = "xxx") -> None: ...
    def load_from_json(self, lang: str = "eng") -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
    def normalize(self, word: Incomplete) -> Incomplete: ...
