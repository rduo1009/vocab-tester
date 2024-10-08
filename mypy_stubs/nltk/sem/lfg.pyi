from _typeshed import Incomplete

from nltk.internals import Counter as Counter

class FStructure(dict):
    def safeappend(self, key: Incomplete, item: Incomplete) -> None: ...
    def __setitem__(self, key: Incomplete, value: Incomplete) -> None: ...
    def __getitem__(self, key: Incomplete) -> Incomplete: ...
    def __contains__(self, key: Incomplete) -> bool: ...
    def to_glueformula_list(self, glue_dict: Incomplete) -> Incomplete: ...
    def to_depgraph(self, rel: Incomplete | None = None) -> Incomplete: ...
    @staticmethod
    def read_depgraph(depgraph: Incomplete) -> Incomplete: ...
    def pretty_format(self, indent: int = 3) -> Incomplete: ...

def demo_read_depgraph() -> None: ...
