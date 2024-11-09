from itertools import product as product
from typing import (
    Callable,
    Iterable,
    List,
    Tuple,
)

from nltk.corpus import (
    WordNetCorpusReader as WordNetCorpusReader,
)
from nltk.corpus import (
    wordnet as wordnet,
)
from nltk.stem.api import StemmerI
from nltk.stem.porter import PorterStemmer as PorterStemmer

def _count_chunks(matches: List[Tuple[int, int]]) -> int: ...
def _enum_align_words(
    enum_hypothesis_list: List[Tuple[int, str]],
    enum_reference_list: List[Tuple[int, str]],
    stemmer: StemmerI = ...,
    wordnet: WordNetCorpusReader = ...,
) -> Tuple[
    List[Tuple[int, int]], List[Tuple[int, str]], List[Tuple[int, str]]
]: ...
def _enum_stem_match(
    enum_hypothesis_list: List[Tuple[int, str]],
    enum_reference_list: List[Tuple[int, str]],
    stemmer: StemmerI = ...,
) -> Tuple[
    List[Tuple[int, int]], List[Tuple[int, str]], List[Tuple[int, str]]
]: ...
def _enum_wordnetsyn_match(
    enum_hypothesis_list: List[Tuple[int, str]],
    enum_reference_list: List[Tuple[int, str]],
    wordnet: WordNetCorpusReader = ...,
) -> Tuple[
    List[Tuple[int, int]], List[Tuple[int, str]], List[Tuple[int, str]]
]: ...
def _match_enums(
    enum_hypothesis_list: List[Tuple[int, str]],
    enum_reference_list: List[Tuple[int, str]],
) -> Tuple[
    List[Tuple[int, int]], List[Tuple[int, str]], List[Tuple[int, str]]
]: ...
def exact_match(
    hypothesis: Iterable[str], reference: Iterable[str]
) -> tuple[
    list[tuple[int, int]], list[tuple[int, str]], list[tuple[int, str]]
]: ...
def stem_match(
    hypothesis: Iterable[str],
    reference: Iterable[str],
    stemmer: StemmerI = ...,
) -> tuple[
    list[tuple[int, int]], list[tuple[int, str]], list[tuple[int, str]]
]: ...
def wordnetsyn_match(
    hypothesis: Iterable[str],
    reference: Iterable[str],
    wordnet: WordNetCorpusReader = ...,
) -> tuple[
    list[tuple[int, int]], list[tuple[int, str]], list[tuple[int, str]]
]: ...
def align_words(
    hypothesis: Iterable[str],
    reference: Iterable[str],
    stemmer: StemmerI = ...,
    wordnet: WordNetCorpusReader = ...,
) -> tuple[
    list[tuple[int, int]], list[tuple[int, str]], list[tuple[int, str]]
]: ...
def single_meteor_score(
    reference: Iterable[str],
    hypothesis: Iterable[str],
    preprocess: Callable[[str], str] = ...,
    stemmer: StemmerI = ...,
    wordnet: WordNetCorpusReader = ...,
    alpha: float = 0.9,
    beta: float = 3.0,
    gamma: float = 0.5,
) -> float: ...
def meteor_score(
    references: Iterable[Iterable[str]],
    hypothesis: Iterable[str],
    preprocess: Callable[[str], str] = ...,
    stemmer: StemmerI = ...,
    wordnet: WordNetCorpusReader = ...,
    alpha: float = 0.9,
    beta: float = 3.0,
    gamma: float = 0.5,
) -> float: ...
