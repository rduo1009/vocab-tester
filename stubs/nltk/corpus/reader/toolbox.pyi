from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *
from nltk.toolbox import ToolboxData as ToolboxData

class ToolboxCorpusReader(CorpusReader):
    def xml(
        self, fileids: Incomplete, key: Incomplete | None = None
    ) -> Incomplete: ...
    def fields(
        self,
        fileids: Incomplete,
        strip: bool = True,
        unwrap: bool = True,
        encoding: str = "utf8",
        errors: str = "strict",
        unicode_fields: Incomplete | None = None,
    ) -> Incomplete: ...
    def entries(
        self, fileids: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def words(self, fileids: Incomplete, key: str = "lx") -> Incomplete: ...

def demo() -> None: ...
