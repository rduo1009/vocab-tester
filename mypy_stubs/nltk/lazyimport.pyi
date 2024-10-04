from _typeshed import Incomplete

class LazyModule:
    def __init__(
        self,
        name: Incomplete,
        locals: Incomplete,
        globals: Incomplete | None = None,
    ) -> None: ...
    def __getattr__(self, name: Incomplete) -> Incomplete: ...
    def __setattr__(self, name: Incomplete, value: Incomplete) -> None: ...
