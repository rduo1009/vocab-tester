from typing import Tuple

from _typeshed import Incomplete

NGRAM: int
UNIGRAMS: int
TOTAL: int

class BigramAssocMeasures:
    @staticmethod
    def _contingency(
        n_ii: int, n_ix_xi_tuple: Tuple[int, int], n_xx: int
    ) -> Tuple[int, int, int, int]: ...
    @classmethod
    def phi_sq(cls: Incomplete, *marginals: Incomplete) -> Incomplete: ...
    @classmethod
    def chi_sq(
        cls: Incomplete,
        n_ii: Incomplete,
        n_ix_xi_tuple: Incomplete,
        n_xx: Incomplete,
    ) -> Incomplete: ...
    @classmethod
    def fisher(cls: Incomplete, *marginals: Incomplete) -> Incomplete: ...
    @staticmethod
    def dice(
        n_ii: Incomplete, n_ix_xi_tuple: Incomplete, n_xx: Incomplete
    ) -> Incomplete: ...

class NgramAssocMeasures:
    @classmethod
    def likelihood_ratio(cls: Incomplete, *marginals: Incomplete) -> float: ...
    @classmethod
    def pmi(cls: Incomplete, *marginals: Incomplete) -> float: ...
    @staticmethod
    def raw_freq(*marginals: Incomplete) -> Incomplete: ...
    @classmethod
    def student_t(cls: Incomplete, *marginals: Incomplete) -> Incomplete: ...
    @classmethod
    def chi_sq(cls: Incomplete, *marginals: Incomplete) -> Incomplete: ...
    @staticmethod
    def mi_like(
        *marginals: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    @classmethod
    def poisson_stirling(
        cls: Incomplete, *marginals: Incomplete
    ) -> Incomplete: ...
    @classmethod
    def jaccard(cls: Incomplete, *marginals: Incomplete) -> Incomplete: ...

class QuadgramAssocMeasures:
    @staticmethod
    def _contingency(
        n_iiii: int,
        n_iiix_tuple: Tuple[int, int, int, int],
        n_iixx_tuple: Tuple[int, int, int, int, int, int],
        n_ixxx_tuple: Tuple[int, int, int, int],
        n_xxxx: int,
    ) -> Tuple[
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
    ]: ...

class TrigramAssocMeasures:
    @staticmethod
    def _contingency(
        n_iii: int,
        n_iix_tuple: Tuple[int, int, int],
        n_ixx_tuple: Tuple[int, int, int],
        n_xxx: int,
    ) -> Tuple[int, int, int, int, int, int, int, int]: ...

class ContingencyMeasures:
    def __init__(self, measures: Incomplete) -> None: ...
