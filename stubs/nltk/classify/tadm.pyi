from io import TextIOWrapper
from typing import (
    Dict,
    List,
    Tuple,
)

from _typeshed import Incomplete

from nltk.classify.maxent import TadmEventMaxentFeatureEncoding

def call_tadm(args: List[str]) -> Incomplete: ...
def config_tadm(bin: None = ...) -> Incomplete: ...
def write_tadm_file(
    train_toks: List[Tuple[Dict[str, int], str]],
    encoding: TadmEventMaxentFeatureEncoding,
    stream: TextIOWrapper,
) -> Incomplete: ...
