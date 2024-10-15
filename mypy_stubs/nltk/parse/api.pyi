from _typeshed import Incomplete

from nltk.internals import overridden as overridden

class ParserI:
    def grammar(self) -> None: ...
    def parse(
        self, sent: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def parse_sents(
        self, sents: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def parse_all(
        self, sent: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
    def parse_one(
        self, sent: Incomplete, *args: Incomplete, **kwargs: Incomplete
    ) -> Incomplete: ...
