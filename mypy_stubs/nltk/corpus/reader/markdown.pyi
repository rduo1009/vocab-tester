from typing import NamedTuple

from _typeshed import Incomplete

from nltk.corpus.reader.api import (
    CategorizedCorpusReader as CategorizedCorpusReader,
)
from nltk.corpus.reader.plaintext import (
    PlaintextCorpusReader as PlaintextCorpusReader,
)
from nltk.corpus.reader.util import (
    concat as concat,
)
from nltk.corpus.reader.util import (
    read_blankline_block as read_blankline_block,
)
from nltk.tokenize import (
    blankline_tokenize as blankline_tokenize,
)
from nltk.tokenize import (
    sent_tokenize as sent_tokenize,
)
from nltk.tokenize import (
    word_tokenize as word_tokenize,
)

def comma_separated_string_args(func: Incomplete) -> Incomplete: ...
def read_parse_blankline_block(
    stream: Incomplete, parser: Incomplete
) -> Incomplete: ...

class MarkdownBlock:
    content: Incomplete
    truncate_at: int
    def __init__(self, content: Incomplete) -> None: ...
    @property
    def raw(self) -> Incomplete: ...
    @property
    def words(self) -> Incomplete: ...
    @property
    def sents(self) -> Incomplete: ...
    @property
    def paras(self) -> Incomplete: ...

class CodeBlock(MarkdownBlock):
    language: Incomplete
    def __init__(self, language: Incomplete, *args: Incomplete) -> None: ...
    @property
    def sents(self) -> Incomplete: ...
    @property
    def lines(self) -> Incomplete: ...
    @property
    def paras(self) -> Incomplete: ...

class MarkdownSection(MarkdownBlock):
    heading: Incomplete
    level: Incomplete
    def __init__(
        self, heading: Incomplete, level: Incomplete, *args: Incomplete
    ) -> None: ...

class Image(NamedTuple):
    label: Incomplete
    src: Incomplete
    title: Incomplete

class Link(NamedTuple):
    label: Incomplete
    href: Incomplete
    title: Incomplete

class List(NamedTuple):
    is_ordered: Incomplete
    items: Incomplete

class MarkdownCorpusReader(PlaintextCorpusReader):
    parser: Incomplete
    def __init__(
        self,
        *args: Incomplete,
        parser: Incomplete | None = None,
        **kwargs: Incomplete,
    ) -> None: ...

class CategorizedMarkdownCorpusReader(
    CategorizedCorpusReader, MarkdownCorpusReader
):
    def __init__(
        self, *args: Incomplete, cat_field: str = "tags", **kwargs: Incomplete
    ) -> None: ...
    def categories(self, fileids: Incomplete | None = None) -> Incomplete: ...
    def fileids(self, categories: Incomplete | None = None) -> Incomplete: ...
    def raw(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def words(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def sents(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def paras(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def concatenated_view(
        self, reader: Incomplete, fileids: Incomplete, categories: Incomplete
    ) -> Incomplete: ...
    def metadata_reader(self, stream: Incomplete) -> Incomplete: ...
    def metadata(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def blockquote_reader(self, stream: Incomplete) -> Incomplete: ...
    def blockquotes(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def code_block_reader(self, stream: Incomplete) -> Incomplete: ...
    def code_blocks(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def image_reader(self, stream: Incomplete) -> Incomplete: ...
    def images(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def link_reader(self, stream: Incomplete) -> Incomplete: ...
    def links(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def list_reader(self, stream: Incomplete) -> Incomplete: ...
    def lists(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
    def section_reader(self, stream: Incomplete) -> Incomplete: ...
    def sections(
        self,
        fileids: Incomplete | None = None,
        categories: Incomplete | None = None,
    ) -> Incomplete: ...
