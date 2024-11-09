from _typeshed import Incomplete

from nltk.corpus.reader.api import *
from nltk.internals import import_from_stdlib as import_from_stdlib
from nltk.tree import Tree as Tree

class TimitCorpusReader(CorpusReader):
    speakers: Incomplete
    def __init__(self, root: Incomplete, encoding: str = "utf8") -> None: ...
    def fileids(self, filetype: Incomplete | None = None) -> Incomplete: ...
    def utteranceids(
        self,
        dialect: Incomplete | None = None,
        sex: Incomplete | None = None,
        spkrid: Incomplete | None = None,
        sent_type: Incomplete | None = None,
        sentid: Incomplete | None = None,
    ) -> Incomplete: ...
    def transcription_dict(self) -> Incomplete: ...
    def spkrid(self, utterance: Incomplete) -> Incomplete: ...
    def sentid(self, utterance: Incomplete) -> Incomplete: ...
    def utterance(
        self, spkrid: Incomplete, sentid: Incomplete
    ) -> Incomplete: ...
    def spkrutteranceids(self, speaker: Incomplete) -> Incomplete: ...
    def spkrinfo(self, speaker: Incomplete) -> Incomplete: ...
    def phones(self, utterances: Incomplete | None = None) -> Incomplete: ...
    def phone_times(
        self, utterances: Incomplete | None = None
    ) -> Incomplete: ...
    def words(self, utterances: Incomplete | None = None) -> Incomplete: ...
    def word_times(
        self, utterances: Incomplete | None = None
    ) -> Incomplete: ...
    def sents(self, utterances: Incomplete | None = None) -> Incomplete: ...
    def sent_times(
        self, utterances: Incomplete | None = None
    ) -> Incomplete: ...
    def phone_trees(
        self, utterances: Incomplete | None = None
    ) -> Incomplete: ...
    def wav(
        self,
        utterance: Incomplete,
        start: int = 0,
        end: Incomplete | None = None,
    ) -> Incomplete: ...
    def audiodata(
        self,
        utterance: Incomplete,
        start: int = 0,
        end: Incomplete | None = None,
    ) -> Incomplete: ...
    def play(
        self,
        utterance: Incomplete,
        start: int = 0,
        end: Incomplete | None = None,
    ) -> None: ...

class SpeakerInfo:
    id: Incomplete
    sex: Incomplete
    dr: Incomplete
    use: Incomplete
    recdate: Incomplete
    birthdate: Incomplete
    ht: Incomplete
    race: Incomplete
    edu: Incomplete
    comments: Incomplete
    def __init__(
        self,
        id: Incomplete,
        sex: Incomplete,
        dr: Incomplete,
        use: Incomplete,
        recdate: Incomplete,
        birthdate: Incomplete,
        ht: Incomplete,
        race: Incomplete,
        edu: Incomplete,
        comments: Incomplete | None = None,
    ) -> None: ...

def read_timit_block(stream: Incomplete) -> Incomplete: ...
