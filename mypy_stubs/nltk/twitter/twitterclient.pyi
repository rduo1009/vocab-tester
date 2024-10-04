from collections.abc import Generator

from _typeshed import Incomplete
from twython import Twython, TwythonStreamer  # type: ignore[import-not-found]

from nltk.twitter.api import (
    BasicTweetHandler as BasicTweetHandler,
)
from nltk.twitter.api import (
    TweetHandlerI as TweetHandlerI,
)
from nltk.twitter.util import (
    credsfromfile as credsfromfile,
)
from nltk.twitter.util import (
    guess_path as guess_path,
)

class Streamer(TwythonStreamer):  # type: ignore[misc]
    handler: Incomplete
    do_continue: bool
    def __init__(
        self,
        app_key: Incomplete,
        app_secret: Incomplete,
        oauth_token: Incomplete,
        oauth_token_secret: Incomplete,
    ) -> None: ...
    def register(self, handler: Incomplete) -> None: ...
    def on_success(self, data: Incomplete) -> None: ...
    def on_error(self, status_code: Incomplete, data: Incomplete) -> None: ...
    def sample(self) -> None: ...
    def filter(
        self, track: str = "", follow: str = "", lang: str = "en"
    ) -> None: ...

class Query(Twython):  # type: ignore[misc]
    handler: Incomplete
    do_continue: bool
    def __init__(
        self,
        app_key: Incomplete,
        app_secret: Incomplete,
        oauth_token: Incomplete,
        oauth_token_secret: Incomplete,
    ) -> None: ...
    def register(self, handler: Incomplete) -> None: ...
    def expand_tweetids(
        self, ids_f: Incomplete, verbose: bool = True
    ) -> Incomplete: ...
    def search_tweets(
        self,
        keywords: Incomplete,
        limit: int = 100,
        lang: str = "en",
        max_id: Incomplete | None = None,
        retries_after_twython_exception: int = 0,
    ) -> Generator[Incomplete, None, None]: ...
    def user_info_from_id(self, userids: Incomplete) -> Incomplete: ...
    def user_tweets(
        self,
        screen_name: Incomplete,
        limit: Incomplete,
        include_rts: str = "false",
    ) -> None: ...

class Twitter:
    streamer: Incomplete
    query: Incomplete
    def __init__(self) -> None: ...
    def tweets(
        self,
        keywords: str = "",
        follow: str = "",
        to_screen: bool = True,
        stream: bool = True,
        limit: int = 100,
        date_limit: Incomplete | None = None,
        lang: str = "en",
        repeat: bool = False,
        gzip_compress: bool = False,
    ) -> None: ...

class TweetViewer(TweetHandlerI):
    def handle(self, data: Incomplete) -> None: ...
    def on_finish(self) -> None: ...

class TweetWriter(TweetHandlerI):
    fprefix: Incomplete
    subdir: Incomplete
    gzip_compress: Incomplete
    fname: Incomplete
    repeat: Incomplete
    output: Incomplete
    def __init__(
        self,
        limit: int = 2000,
        upper_date_limit: Incomplete | None = None,
        lower_date_limit: Incomplete | None = None,
        fprefix: str = "tweets",
        subdir: str = "twitter-files",
        repeat: bool = False,
        gzip_compress: bool = False,
    ) -> None: ...
    def timestamped_file(self) -> Incomplete: ...
    startingup: bool
    def handle(self, data: Incomplete) -> None: ...
    def on_finish(self) -> None: ...
    def do_continue(self) -> Incomplete: ...
