from _typeshed import Incomplete

from nltk.stem.api import StemmerI as StemmerI

class ARLSTem(StemmerI):
    re_hamzated_alif: Incomplete
    re_alifMaqsura: Incomplete
    re_diacritics: Incomplete
    pr2: Incomplete
    pr3: Incomplete
    pr32: Incomplete
    pr4: Incomplete
    su2: Incomplete
    su22: Incomplete
    su3: Incomplete
    su32: Incomplete
    pl_si2: Incomplete
    pl_si3: Incomplete
    verb_su2: Incomplete
    verb_pr2: Incomplete
    verb_pr22: Incomplete
    verb_pr33: Incomplete
    verb_suf3: Incomplete
    verb_suf2: Incomplete
    verb_suf1: Incomplete
    def __init__(self) -> None: ...
    def stem(self, token: Incomplete) -> Incomplete: ...
    def norm(self, token: Incomplete) -> Incomplete: ...
    def pref(self, token: Incomplete) -> Incomplete: ...
    def suff(self, token: Incomplete) -> Incomplete: ...
    def fem2masc(self, token: Incomplete) -> Incomplete: ...
    def plur2sing(self, token: Incomplete) -> Incomplete: ...
    def verb(self, token: Incomplete) -> Incomplete: ...
    def verb_t1(self, token: Incomplete) -> Incomplete: ...
    def verb_t2(self, token: Incomplete) -> Incomplete: ...
    def verb_t3(self, token: Incomplete) -> Incomplete: ...
    def verb_t4(self, token: Incomplete) -> Incomplete: ...
    def verb_t5(self, token: Incomplete) -> Incomplete: ...
    def verb_t6(self, token: Incomplete) -> Incomplete: ...
