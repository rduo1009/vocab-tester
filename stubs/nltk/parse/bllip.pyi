from collections.abc import Generator

from _typeshed import Incomplete

from nltk.parse.api import ParserI

__all__ = ["BllipParser"]

class BllipParser(ParserI):
    rrp: Incomplete
    def __init__(
        self,
        parser_model: Incomplete | None = None,
        reranker_features: Incomplete | None = None,
        reranker_weights: Incomplete | None = None,
        parser_options: Incomplete | None = None,
        reranker_options: Incomplete | None = None,
    ) -> None: ...
    def parse(
        self, sentence: Incomplete
    ) -> Generator[Incomplete, None, None]: ...
    def tagged_parse(
        self, word_and_tag_pairs: Incomplete
    ) -> Generator[Incomplete, None, None]: ...
    @classmethod
    def from_unified_model_dir(
        cls: Incomplete,
        model_dir: Incomplete,
        parser_options: Incomplete | None = None,
        reranker_options: Incomplete | None = None,
    ) -> Incomplete: ...
