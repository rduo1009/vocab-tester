import types

from _typeshed import Incomplete

from nltk.internals import find_binary as find_binary
from nltk.internals import find_file as find_file
from nltk.tag.api import TaggerI as TaggerI

class HunposTagger(TaggerI):
    def __init__(
        self,
        path_to_model: Incomplete,
        path_to_bin: Incomplete | None = None,
        encoding: Incomplete = ...,
        verbose: bool = False,
    ) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Incomplete: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    def tag(self, tokens: Incomplete) -> Incomplete: ...
