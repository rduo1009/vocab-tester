from abc import ABCMeta, abstractmethod
from datetime import tzinfo

from _typeshed import Incomplete

class LocalTimezoneOffsetWithUTC(tzinfo):  # type: ignore[misc]
    STDOFFSET: Incomplete
    DSTOFFSET: Incomplete
    DSTOFFSET = STDOFFSET
    def utcoffset(self, dt: Incomplete) -> Incomplete: ...

LOCAL: Incomplete

class BasicTweetHandler(metaclass=ABCMeta):
    limit: Incomplete
    counter: int
    do_stop: bool
    max_id: Incomplete
    def __init__(self, limit: int = 20) -> None: ...
    def do_continue(self) -> Incomplete: ...

class TweetHandlerI(BasicTweetHandler):
    upper_date_limit: Incomplete
    lower_date_limit: Incomplete
    startingup: bool
    def __init__(
        self,
        limit: int = 20,
        upper_date_limit: Incomplete | None = None,
        lower_date_limit: Incomplete | None = None,
    ) -> None: ...
    @abstractmethod
    def handle(self, data: Incomplete) -> Incomplete: ...
    @abstractmethod
    def on_finish(self) -> Incomplete: ...
    do_stop: bool
    def check_date_limit(
        self, data: Incomplete, verbose: bool = False
    ) -> None: ...
