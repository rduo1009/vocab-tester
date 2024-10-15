from _typeshed import Incomplete

def _(words: Incomplete, vocab: Incomplete) -> Incomplete: ...

class Vocabulary:
    unk_label: Incomplete
    counts: Incomplete
    def __init__(
        self,
        counts: Incomplete | None = None,
        unk_cutoff: int = 1,
        unk_label: str = "<UNK>",
    ) -> None: ...
    @property
    def cutoff(self) -> Incomplete: ...
    def update(
        self, *counter_args: Incomplete, **counter_kwargs: Incomplete
    ) -> None: ...
    def lookup(self, words: Incomplete) -> Incomplete: ...
    def __getitem__(self, item: Incomplete) -> Incomplete: ...
    def __contains__(self, item: Incomplete) -> bool: ...
    def __iter__(self) -> Incomplete: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
