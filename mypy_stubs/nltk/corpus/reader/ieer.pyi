from _typeshed import Incomplete

from nltk.corpus.reader.api import *

titles: Incomplete
documents: Incomplete

class IEERDocument:
    text: Incomplete
    docno: Incomplete
    doctype: Incomplete
    date_time: Incomplete
    headline: Incomplete
    def __init__(
        self,
        text: Incomplete,
        docno: Incomplete | None = None,
        doctype: Incomplete | None = None,
        date_time: Incomplete | None = None,
        headline: str = "",
    ) -> None: ...

class IEERCorpusReader(CorpusReader):
    def docs(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def parsed_docs(self, fileids: Incomplete | None = None) -> Incomplete: ...
