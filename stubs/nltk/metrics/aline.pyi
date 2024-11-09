from typing import (
    Any,
    List,
    Tuple,
    Union,
)

from _typeshed import Incomplete
from numpy import (
    float64,
    ndarray,
)

inf: Incomplete
C_skip: int
C_sub: int
C_exp: int
C_vwl: int
consonants: Incomplete
R_c: Incomplete
R_v: Incomplete
similarity_matrix: Incomplete
salience: Incomplete
feature_matrix: Incomplete

def R(p: str, q: str) -> List[str]: ...
def V(p: str) -> int: ...
def _retrieve(
    i: int,
    j: int,
    s: Union[int, float64],
    S: ndarray,
    T: float64,
    str1: str,
    str2: str,
    out: List[Union[Any, Tuple[str, str]]],
) -> List[Tuple[str, str]]: ...
def align(
    str1: str, str2: str, epsilon: int = ...
) -> List[List[Tuple[str, str]]]: ...
def delta(p: str, q: str) -> float64: ...
def diff(p: str, q: str, f: str) -> float: ...
def sigma_exp(p: str, q: str) -> float64: ...
def sigma_skip(p: str) -> int: ...
def sigma_sub(p: str, q: str) -> float64: ...

cognate_data: str
