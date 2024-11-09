from re import Pattern
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.chunk.api import ChunkParserI as ChunkParserI
from nltk.tree import Tree as Tree

class StripRule(RegexpChunkRule):
    def __init__(self, tag_pattern: Incomplete, descr: Incomplete) -> None: ...

class UnChunkRule(RegexpChunkRule):
    def __init__(self, tag_pattern: Incomplete, descr: Incomplete) -> None: ...

class MergeRule(RegexpChunkRule):
    def __init__(
        self,
        left_tag_pattern: Incomplete,
        right_tag_pattern: Incomplete,
        descr: Incomplete,
    ) -> None: ...

class SplitRule(RegexpChunkRule):
    def __init__(
        self,
        left_tag_pattern: Incomplete,
        right_tag_pattern: Incomplete,
        descr: Incomplete,
    ) -> None: ...

class ExpandLeftRule(RegexpChunkRule):
    def __init__(
        self,
        left_tag_pattern: Incomplete,
        right_tag_pattern: Incomplete,
        descr: Incomplete,
    ) -> None: ...

class ExpandRightRule(RegexpChunkRule):
    def __init__(
        self,
        left_tag_pattern: Incomplete,
        right_tag_pattern: Incomplete,
        descr: Incomplete,
    ) -> None: ...

class ChunkRuleWithContext(RegexpChunkRule):
    def __init__(
        self,
        left_context_tag_pattern: Incomplete,
        chunk_tag_pattern: Incomplete,
        right_context_tag_pattern: Incomplete,
        descr: Incomplete,
    ) -> None: ...

CHUNK_TAG_PATTERN: Incomplete

def demo_eval(chunkparser: Incomplete, text: Incomplete) -> None: ...
def demo() -> None: ...
def tag_pattern2re_pattern(tag_pattern: str) -> str: ...

class ChunkRule:
    def __init__(self, tag_pattern: str, descr: str) -> None: ...

class ChunkString:
    def __init__(self, chunk_struct: Tree, debug_level: int = ...) -> None: ...
    def _tag(self, tok: Tuple[str, str]) -> str: ...
    def _verify(self, s: str, verify_tags: int) -> Incomplete: ...
    def to_chunkstruct(self, chunk_label: str = ...) -> Tree: ...
    def xform(self, regexp: Pattern, repl: str) -> Incomplete: ...  # type: ignore[type-arg]

class RegexpChunkParser:
    def __init__(
        self,
        rules: List[ChunkRule],
        chunk_label: str = ...,
        root_label: str = ...,
        trace: int = ...,
    ) -> None: ...
    def _notrace_apply(self, chunkstr: ChunkString) -> Incomplete: ...
    def parse(
        self, chunk_struct: List[Tuple[str, str]], trace: Optional[int] = ...
    ) -> Tree: ...

class RegexpChunkRule:
    def __init__(self, regexp: Pattern, repl: str, descr: str) -> None: ...  # type: ignore[type-arg]
    def apply(self, chunkstr: ChunkString) -> Incomplete: ...
    @staticmethod
    def fromstring(s: str) -> ChunkRule: ...

class RegexpParser:
    def __init__(
        self,
        grammar: str,
        root_label: str = ...,
        loop: int = ...,
        trace: int = ...,
    ) -> None: ...
    def _add_stage(
        self,
        rules: List[Union[Any, ChunkRule]],
        lhs: Optional[str],
        root_label: str,
        trace: int,
    ) -> Incomplete: ...
    def _read_grammar(
        self, grammar: str, root_label: str, trace: int
    ) -> Incomplete: ...
    def parse(
        self, chunk_struct: List[Tuple[str, str]], trace: None = ...
    ) -> Tree: ...
