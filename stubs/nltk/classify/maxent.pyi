from typing import (
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.collections import OrderedDict  # type: ignore[import-untyped]

def train_maxent_classifier_with_megam(
    train_toks: List[Tuple[Dict[str, int], str]],
    trace: int = ...,
    encoding: None = ...,
    labels: None = ...,
    gaussian_prior_sigma: int = ...,
    **kwargs: Incomplete,
) -> Incomplete: ...

class BinaryMaxentFeatureEncoding:
    def __init__(
        self,
        labels: Union[List[str], Set[str]],
        mapping: Union[Dict[Tuple[str, int, str], int], OrderedDict],
        unseen_features: bool = ...,
        alwayson_features: bool = ...,
    ) -> None: ...
    def encode(
        self, featureset: Dict[str, int], label: str
    ) -> List[Tuple[int, int]]: ...
    def labels(self) -> List[str]: ...
    @classmethod
    def train(
        cls: Incomplete,
        train_toks: List[Tuple[Dict[str, int], str]],
        count_cutoff: int = ...,
        labels: None = ...,
        **options: Incomplete,
    ) -> BinaryMaxentFeatureEncoding: ...

class MaxentClassifier:
    @classmethod
    def train(
        cls: Incomplete,
        train_toks: List[Tuple[Dict[str, int], str]],
        algorithm: Optional[str] = ...,
        trace: int = ...,
        encoding: None = ...,
        labels: None = ...,
        gaussian_prior_sigma: int = ...,
        **cutoffs: Incomplete,
    ) -> Incomplete: ...

class TadmEventMaxentFeatureEncoding:
    def __init__(
        self,
        labels: List[str],
        mapping: OrderedDict,
        unseen_features: bool = ...,
        alwayson_features: bool = ...,
    ) -> None: ...
    def encode(
        self, featureset: Dict[str, int], label: str
    ) -> List[Tuple[int, int]]: ...
    def labels(self) -> List[str]: ...
    @classmethod
    def train(
        cls: Incomplete,
        train_toks: List[Tuple[Dict[str, int], str]],
        count_cutoff: int = ...,
        labels: None = ...,
        **options: Incomplete,
    ) -> TadmEventMaxentFeatureEncoding: ...

class TadmMaxentClassifier:
    @classmethod
    def train(
        cls: Incomplete,
        train_toks: List[Tuple[Dict[str, int], str]],
        **kwargs: Incomplete,
    ) -> Incomplete: ...
