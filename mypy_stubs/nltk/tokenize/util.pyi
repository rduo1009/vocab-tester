from collections.abc import Generator
from typing import (
    List,
    Tuple,
)

from _typeshed import Incomplete

def align_tokens(
    tokens: List[str], sentence: str
) -> List[Tuple[int, int]]: ...
def string_span_tokenize(
    s: Incomplete, sep: Incomplete
) -> Generator[Incomplete, None, None]: ...
def regexp_span_tokenize(
    s: Incomplete, regexp: Incomplete
) -> Generator[Incomplete, None, None]: ...
def spans_to_relative(
    spans: Incomplete,
) -> Generator[Incomplete, None, None]: ...

class CJKChars:
    Hangul_Jamo: Incomplete
    CJK_Radicals: Incomplete
    Phags_Pa: Incomplete
    Hangul_Syllables: Incomplete
    CJK_Compatibility_Ideographs: Incomplete
    CJK_Compatibility_Forms: Incomplete
    Katakana_Hangul_Halfwidth: Incomplete
    Supplementary_Ideographic_Plane: Incomplete
    ranges: Incomplete

def is_cjk(character: Incomplete) -> Incomplete: ...
def xml_escape(text: Incomplete) -> Incomplete: ...
def xml_unescape(text: Incomplete) -> Incomplete: ...
