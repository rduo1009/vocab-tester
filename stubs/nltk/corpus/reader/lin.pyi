from _typeshed import Incomplete

from nltk.corpus.reader import CorpusReader as CorpusReader

class LinThesaurusCorpusReader(CorpusReader):
    def __init__(self, root: Incomplete, badscore: float = 0.0) -> None: ...
    def similarity(
        self,
        ngram1: Incomplete,
        ngram2: Incomplete,
        fileid: Incomplete | None = None,
    ) -> Incomplete: ...
    def scored_synonyms(
        self, ngram: Incomplete, fileid: Incomplete | None = None
    ) -> Incomplete: ...
    def synonyms(
        self, ngram: Incomplete, fileid: Incomplete | None = None
    ) -> Incomplete: ...
    def __contains__(self, ngram: Incomplete) -> bool: ...

def demo() -> None: ...
