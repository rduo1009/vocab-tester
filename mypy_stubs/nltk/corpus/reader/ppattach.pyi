from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.corpus.reader.util import *

class PPAttachment:
    sent: Incomplete
    verb: Incomplete
    noun1: Incomplete
    prep: Incomplete
    noun2: Incomplete
    attachment: Incomplete
    def __init__(
        self,
        sent: Incomplete,
        verb: Incomplete,
        noun1: Incomplete,
        prep: Incomplete,
        noun2: Incomplete,
        attachment: Incomplete,
    ) -> None: ...

class PPAttachmentCorpusReader(CorpusReader):
    def attachments(self, fileids: Incomplete) -> Incomplete: ...
    def tuples(self, fileids: Incomplete) -> Incomplete: ...
