from collections import defaultdict
from collections.abc import Generator
from itertools import chain
from typing import (
    Any,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

from _typeshed import Incomplete

from nltk.collections import *  # type: ignore[import-untyped]
from nltk.internals import (
    deprecated as deprecated,
)
from nltk.internals import (
    raise_unorderable_types as raise_unorderable_types,
)
from nltk.internals import (
    slice_bounds as slice_bounds,
)

def choose(n: int, k: int) -> int: ...
def everygrams(
    sequence: List[str],
    min_len: int = ...,
    max_len: int = ...,
    pad_left: bool = ...,
    pad_right: bool = ...,
    **kwargs: Incomplete,
) -> Iterator[Union[Tuple[str], Tuple[str, str]]]: ...
def ngrams(
    sequence: List[Union[Tuple[str, int], str]], n: int, **kwargs: Incomplete
) -> Iterator[Any]: ...
def pad_sequence(
    sequence: List[str],
    n: int,
    pad_left: bool = ...,
    pad_right: bool = ...,
    left_pad_symbol: Optional[str] = ...,
    right_pad_symbol: Optional[str] = ...,
) -> chain: ...  # type: ignore[type-arg]
def unique_list(xs: List[str]) -> List[str]: ...
def usage(obj: Incomplete) -> None: ...
def in_idle() -> Incomplete: ...
def pr(
    data: Incomplete, start: int = 0, end: Incomplete | None = None
) -> None: ...
def print_string(s: Incomplete, width: int = 70) -> None: ...
def tokenwrap(
    tokens: Incomplete, separator: str = " ", width: int = 70
) -> Incomplete: ...
def cut_string(s: Incomplete, width: int = 70) -> Incomplete: ...

class Index(defaultdict):  # type: ignore[type-arg]
    def __init__(self, pairs: Incomplete) -> None: ...

def re_show(
    regexp: Incomplete, string: Incomplete, left: str = "{", right: str = "}"
) -> None: ...
def filestring(f: Incomplete) -> Incomplete: ...
def breadth_first(
    tree: Incomplete, children: Incomplete = ..., maxdepth: int = -1
) -> Generator[Incomplete, None, None]: ...
def edge_closure(
    tree: Incomplete,
    children: Incomplete = ...,
    maxdepth: int = -1,
    verbose: bool = False,
) -> Generator[Incomplete, None, None]: ...
def edges2dot(
    edges: Incomplete,
    shapes: Incomplete | None = None,
    attr: Incomplete | None = None,
) -> Incomplete: ...
def unweighted_minimum_spanning_digraph(
    tree: Incomplete,
    children: Incomplete = ...,
    shapes: Incomplete | None = None,
    attr: Incomplete | None = None,
) -> Incomplete: ...
def acyclic_breadth_first(
    tree: Incomplete,
    children: Incomplete = ...,
    maxdepth: int = -1,
    verbose: bool = False,
) -> Generator[Incomplete, None, None]: ...
def acyclic_depth_first(
    tree: Incomplete,
    children: Incomplete = ...,
    depth: int = -1,
    cut_mark: Incomplete | None = None,
    traversed: Incomplete | None = None,
    verbose: bool = False,
) -> Incomplete: ...
def acyclic_branches_depth_first(
    tree: Incomplete,
    children: Incomplete = ...,
    depth: int = -1,
    cut_mark: Incomplete | None = None,
    traversed: Incomplete | None = None,
    verbose: bool = False,
) -> Incomplete: ...
def acyclic_dic2tree(node: Incomplete, dic: Incomplete) -> Incomplete: ...
def unweighted_minimum_spanning_dict(
    tree: Incomplete, children: Incomplete = ...
) -> Incomplete: ...
def unweighted_minimum_spanning_tree(
    tree: Incomplete, children: Incomplete = ...
) -> Incomplete: ...
def guess_encoding(data: Incomplete) -> Incomplete: ...
def invert_dict(d: Incomplete) -> Incomplete: ...
def transitive_closure(
    graph: Incomplete, reflexive: bool = False
) -> Incomplete: ...
def invert_graph(graph: Incomplete) -> Incomplete: ...
def clean_html(html: Incomplete) -> None: ...
def clean_url(url: Incomplete) -> None: ...
def flatten(*args: Incomplete) -> Incomplete: ...
def bigrams(
    sequence: Incomplete, **kwargs: Incomplete
) -> Generator[Incomplete, Incomplete, None]: ...
def trigrams(
    sequence: Incomplete, **kwargs: Incomplete
) -> Generator[Incomplete, Incomplete, None]: ...
def skipgrams(
    sequence: Incomplete, n: Incomplete, k: Incomplete, **kwargs: Incomplete
) -> Generator[Incomplete, None, None]: ...
def binary_search_file(
    file: Incomplete,
    key: Incomplete,
    cache: Incomplete | None = None,
    cacheDepth: int = -1,
) -> Incomplete: ...
def set_proxy(
    proxy: Incomplete, user: Incomplete | None = None, password: str = ""
) -> None: ...
def elementtree_indent(elem: Incomplete, level: int = 0) -> None: ...
def pairwise(iterable: Incomplete) -> Incomplete: ...
def parallelize_preprocess(
    func: Incomplete,
    iterator: Incomplete,
    processes: Incomplete,
    progress_bar: bool = False,
) -> Incomplete: ...
