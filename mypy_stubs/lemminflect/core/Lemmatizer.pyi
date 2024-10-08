# Auto-generated by monkeytype

from typing import (
    Dict,
    Optional,
    Tuple,
)

from lemminflect.core.LemmatizerRules import LemmatizerRules

from ..utils.Singleton import _Singleton

# from spacy.tokens.token import Token

class Lemmatizer(_Singleton):
    DICT_UPOS_TYPES: list[str]
    def __init__(self, lemma_lu_fn: str = ..., overrides_fn: str = ...): ...
    def _getLemmaDict(
        self,
    ) -> Dict[
        str,
        Dict[str, Tuple[str, ...]],
    ]: ...
    def _getOOVLemmatizer(self) -> LemmatizerRules: ...
    def _getOverridesDict(self) -> Dict[str, Dict[str, Tuple[str]]]: ...
    def getAllLemmas(
        self, word: str, upos: Optional[str] = ...
    ) -> Dict[str, Tuple[str, ...]]: ...
    def getAllLemmasOOV(
        self, word: str, upos: str
    ) -> Dict[str, Tuple[str]]: ...
    def getLemma(
        self, word: str, upos: str, lemmatize_oov: bool = ...
    ) -> Tuple[str, ...]: ...
    @staticmethod
    def isTagBaseForm(tag: str) -> bool: ...
    # def spacyGetLemma(
    #    self,
    #    token: Token,
    #    form_num: int = ...,
    #    lemmatize_oov: bool = ...,
    #    on_empty_ret_word: bool = ...,
    # ) -> str: ...
