from abc import abstractmethod

from _typeshed import Incomplete

from nltk import jsontags as jsontags
from nltk.classify import NaiveBayesClassifier as NaiveBayesClassifier
from nltk.probability import ConditionalFreqDist as ConditionalFreqDist
from nltk.tag.api import (
    FeaturesetTaggerI as FeaturesetTaggerI,
)
from nltk.tag.api import (
    TaggerI as TaggerI,
)

class SequentialBackoffTagger(TaggerI):
    def __init__(self, backoff: Incomplete | None = None) -> None: ...
    @property
    def backoff(self) -> Incomplete: ...
    def tag(self, tokens: Incomplete) -> Incomplete: ...
    def tag_one(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...
    @abstractmethod
    def choose_tag(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...

class ContextTagger(SequentialBackoffTagger):
    def __init__(
        self, context_to_tag: Incomplete, backoff: Incomplete | None = None
    ) -> None: ...
    @abstractmethod
    def context(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...
    def choose_tag(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...
    def size(self) -> Incomplete: ...

class DefaultTagger(SequentialBackoffTagger):
    json_tag: str
    def __init__(self, tag: Incomplete) -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
    def choose_tag(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...

class NgramTagger(ContextTagger):
    json_tag: str
    def __init__(
        self,
        n: Incomplete,
        train: Incomplete | None = None,
        model: Incomplete | None = None,
        backoff: Incomplete | None = None,
        cutoff: int = 0,
        verbose: bool = False,
    ) -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
    def context(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...

class UnigramTagger(NgramTagger):
    json_tag: str
    def __init__(
        self,
        train: Incomplete | None = None,
        model: Incomplete | None = None,
        backoff: Incomplete | None = None,
        cutoff: int = 0,
        verbose: bool = False,
    ) -> None: ...
    def context(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...

class BigramTagger(NgramTagger):
    json_tag: str
    def __init__(
        self,
        train: Incomplete | None = None,
        model: Incomplete | None = None,
        backoff: Incomplete | None = None,
        cutoff: int = 0,
        verbose: bool = False,
    ) -> None: ...

class TrigramTagger(NgramTagger):
    json_tag: str
    def __init__(
        self,
        train: Incomplete | None = None,
        model: Incomplete | None = None,
        backoff: Incomplete | None = None,
        cutoff: int = 0,
        verbose: bool = False,
    ) -> None: ...

class AffixTagger(ContextTagger):
    json_tag: str
    def __init__(
        self,
        train: Incomplete | None = None,
        model: Incomplete | None = None,
        affix_length: int = -3,
        min_stem_length: int = 2,
        backoff: Incomplete | None = None,
        cutoff: int = 0,
        verbose: bool = False,
    ) -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
    def context(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...

class RegexpTagger(SequentialBackoffTagger):
    json_tag: str
    def __init__(
        self, regexps: list[tuple[str, str]], backoff: TaggerI | None = None
    ) -> None: ...
    def encode_json_obj(self) -> Incomplete: ...
    @classmethod
    def decode_json_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
    def choose_tag(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...

class ClassifierBasedTagger(SequentialBackoffTagger, FeaturesetTaggerI):
    def __init__(
        self,
        feature_detector: Incomplete | None = None,
        train: Incomplete | None = None,
        classifier_builder: Incomplete = ...,
        classifier: Incomplete | None = None,
        backoff: Incomplete | None = None,
        cutoff_prob: Incomplete | None = None,
        verbose: bool = False,
    ) -> None: ...
    def choose_tag(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...
    def feature_detector(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...
    def classifier(self) -> Incomplete: ...

class ClassifierBasedPOSTagger(ClassifierBasedTagger):
    def feature_detector(
        self, tokens: Incomplete, index: Incomplete, history: Incomplete
    ) -> Incomplete: ...
