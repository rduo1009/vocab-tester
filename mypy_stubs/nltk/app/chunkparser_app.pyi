from _typeshed import Incomplete

from nltk.chunk import ChunkScore as ChunkScore
from nltk.chunk import RegexpChunkParser as RegexpChunkParser
from nltk.chunk.regexp import RegexpChunkRule as RegexpChunkRule
from nltk.corpus import conll2000 as conll2000
from nltk.corpus import treebank_chunk as treebank_chunk
from nltk.draw.util import ShowText as ShowText
from nltk.tree import Tree as Tree
from nltk.util import in_idle as in_idle

class RegexpChunkApp:
    TAGSET: Incomplete
    HELP: Incomplete
    HELP_AUTOTAG: Incomplete
    def normalize_grammar(self, grammar: Incomplete) -> Incomplete: ...
    tagset: Incomplete
    chunker: Incomplete
    grammar: Incomplete
    normalized_grammar: Incomplete
    grammar_changed: int
    devset: Incomplete
    devset_name: Incomplete
    devset_index: int
    def __init__(
        self,
        devset_name: str = "conll2000",
        devset: Incomplete | None = None,
        grammar: str = "",
        chunk_label: str = "NP",
        tagset: Incomplete | None = None,
    ) -> None: ...
    def toggle_show_trace(self, *e: Incomplete) -> Incomplete: ...
    charnum: Incomplete
    linenum: Incomplete
    def show_trace(self, *e: Incomplete) -> None: ...
    def show_help(self, tab: Incomplete) -> Incomplete: ...
    top: Incomplete
    def destroy(self, *e: Incomplete) -> None: ...
    def show_devset(self, index: Incomplete | None = None) -> None: ...
    def update(self, *event: Incomplete) -> None: ...
    def reset(self) -> None: ...
    SAVE_GRAMMAR_TEMPLATE: str
    def save_grammar(self, filename: Incomplete | None = None) -> None: ...
    def load_grammar(self, filename: Incomplete | None = None) -> None: ...
    def save_history(self, filename: Incomplete | None = None) -> None: ...
    def about(self, *e: Incomplete) -> None: ...
    def set_devset_size(self, size: Incomplete | None = None) -> None: ...
    def resize(self, size: Incomplete | None = None) -> None: ...
    def mainloop(self, *args: Incomplete, **kwargs: Incomplete) -> None: ...

def app() -> None: ...
