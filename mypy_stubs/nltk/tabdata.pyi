from _typeshed import Incomplete

def rm_nl(s: Incomplete) -> Incomplete: ...

class TabEncoder:
    def list2txt(self, s: Incomplete) -> Incomplete: ...
    def set2txt(self, s: Incomplete) -> Incomplete: ...
    def tup2tab(self, tup: Incomplete) -> Incomplete: ...
    def tups2tab(self, x: Incomplete) -> Incomplete: ...
    def dict2tab(self, d: Incomplete) -> Incomplete: ...
    def ivdict2tab(self, d: Incomplete) -> Incomplete: ...

class TabDecoder:
    def txt2list(self, f: Incomplete) -> Incomplete: ...
    def txt2set(self, f: Incomplete) -> Incomplete: ...
    def tab2tup(self, s: Incomplete) -> Incomplete: ...
    def tab2tups(self, f: Incomplete) -> Incomplete: ...
    def tab2dict(self, f: Incomplete) -> Incomplete: ...
    def tab2ivdict(self, f: Incomplete) -> Incomplete: ...

class MaxentEncoder(TabEncoder):
    def tupdict2tab(self, d: Incomplete) -> Incomplete: ...

class MaxentDecoder(TabDecoder):
    def tupkey2dict(self, f: Incomplete) -> Incomplete: ...

class PunktDecoder(TabDecoder):
    def tab2intdict(self, f: Incomplete) -> Incomplete: ...
