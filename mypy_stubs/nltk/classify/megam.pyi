from io import TextIOWrapper
from typing import (
    Dict,
    List,
    Tuple,
)

from _typeshed import Incomplete

from nltk.classify.maxent import BinaryMaxentFeatureEncoding

def _write_megam_features(
    vector: List[Tuple[int, int]], stream: TextIOWrapper, bernoulli: bool
) -> Incomplete: ...
def call_megam(args: List[str]) -> Incomplete: ...
def config_megam(bin: None = ...) -> Incomplete: ...
def write_megam_file(
    train_toks: List[Tuple[Dict[str, int], str]],
    encoding: BinaryMaxentFeatureEncoding,
    stream: TextIOWrapper,
    bernoulli: bool = ...,
    explicit: bool = ...,
) -> Incomplete: ...
