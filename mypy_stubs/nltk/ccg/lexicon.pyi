from _typeshed import Incomplete

from nltk.ccg.api import CCGVar as CCGVar
from nltk.ccg.api import Direction as Direction
from nltk.ccg.api import FunctionalCategory as FunctionalCategory
from nltk.ccg.api import PrimitiveCategory as PrimitiveCategory
from nltk.internals import deprecated as deprecated
from nltk.sem.logic import Expression as Expression

PRIM_RE: Incomplete
NEXTPRIM_RE: Incomplete
APP_RE: Incomplete
LEX_RE: Incomplete
RHS_RE: Incomplete
SEMANTICS_RE: Incomplete
COMMENTS_RE: Incomplete

class Token:
    def __init__(
        self,
        token: Incomplete,
        categ: Incomplete,
        semantics: Incomplete | None = None,
    ) -> None: ...
    def categ(self) -> Incomplete: ...
    def semantics(self) -> Incomplete: ...
    def __cmp__(self, other: Incomplete) -> Incomplete: ...

class CCGLexicon:
    def __init__(
        self,
        start: Incomplete,
        primitives: Incomplete,
        families: Incomplete,
        entries: Incomplete,
    ) -> None: ...
    def categories(self, word: Incomplete) -> Incomplete: ...
    def start(self) -> Incomplete: ...

def matchBrackets(string: Incomplete) -> Incomplete: ...
def nextCategory(string: Incomplete) -> Incomplete: ...
def parseApplication(ap: Incomplete) -> Incomplete: ...
def parseSubscripts(subscr: Incomplete) -> Incomplete: ...
def parsePrimitiveCategory(
    chunks: Incomplete,
    primitives: Incomplete,
    families: Incomplete,
    var: Incomplete,
) -> Incomplete: ...
def augParseCategory(
    line: Incomplete,
    primitives: Incomplete,
    families: Incomplete,
    var: Incomplete | None = None,
) -> Incomplete: ...
def fromstring(
    lex_str: Incomplete, include_semantics: bool = False
) -> Incomplete: ...
def parseLexicon(lex_str: Incomplete) -> Incomplete: ...

openccg_tinytiny: Incomplete
