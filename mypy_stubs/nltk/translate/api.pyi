from typing import (
    Any,
    List,
    NamedTuple,
    Tuple,
    Type,
    Union,
)

from _typeshed import Incomplete

PhraseTableEntry: NamedTuple

def _check_alignment(
    num_words: int, num_mots: int, alignment: Alignment
) -> Incomplete: ...

class AlignedSent:
    def __init__(
        self,
        words: List[Union[str, Any]],
        mots: List[Union[str, Any]],
        alignment: None = ...,
    ) -> None: ...
    def _set_alignment(self, alignment: Alignment) -> Incomplete: ...
    @property
    def mots(self) -> List[Union[str, Any]]: ...
    @property
    def words(self) -> List[Union[str, Any]]: ...

class Alignment:
    @staticmethod
    def __new__(
        cls: Type[Alignment], pairs: List[Union[Tuple[int, int], Any]]
    ) -> Alignment: ...

class PhraseTable:
    def __contains__(self, src_phrase: Tuple[str, Ellipsis]) -> bool: ...  # type: ignore[valid-type]
    def __init__(self) -> None: ...
    def add(
        self,
        src_phrase: Union[Tuple[str, ...]],
        trg_phrase: Union[Tuple[str, ...]],
        log_prob: float,
    ) -> Incomplete: ...
    def translations_for(
        self,
        src_phrase: Union[Tuple[str, ...]],
    ) -> List[PhraseTableEntry]: ...  # type: ignore[valid-type]
