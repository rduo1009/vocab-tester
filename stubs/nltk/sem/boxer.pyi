from _typeshed import Incomplete

from nltk.internals import find_binary as find_binary
from nltk.sem.drt import (
    DRS as DRS,
)
from nltk.sem.drt import (
    DrtApplicationExpression as DrtApplicationExpression,
)
from nltk.sem.drt import (
    DrtEqualityExpression as DrtEqualityExpression,
)
from nltk.sem.drt import (
    DrtNegatedExpression as DrtNegatedExpression,
)
from nltk.sem.drt import (
    DrtOrExpression as DrtOrExpression,
)
from nltk.sem.drt import (
    DrtParser as DrtParser,
)
from nltk.sem.drt import (
    DrtProposition as DrtProposition,
)
from nltk.sem.drt import (
    DrtTokens as DrtTokens,
)
from nltk.sem.drt import (
    DrtVariableExpression as DrtVariableExpression,
)
from nltk.sem.logic import (
    ExpectedMoreTokensException as ExpectedMoreTokensException,
)
from nltk.sem.logic import (
    LogicalExpressionException as LogicalExpressionException,
)
from nltk.sem.logic import (
    UnexpectedTokenException as UnexpectedTokenException,
)
from nltk.sem.logic import (
    Variable as Variable,
)

class Boxer:
    def __init__(
        self,
        boxer_drs_interpreter: Incomplete | None = None,
        elimeq: bool = False,
        bin_dir: Incomplete | None = None,
        verbose: bool = False,
        resolve: bool = True,
    ) -> None: ...
    def set_bin_dir(
        self, bin_dir: Incomplete, verbose: bool = False
    ) -> None: ...
    def interpret(
        self,
        input: Incomplete,
        discourse_id: Incomplete | None = None,
        question: bool = False,
        verbose: bool = False,
    ) -> Incomplete: ...
    def interpret_multi(
        self,
        input: Incomplete,
        discourse_id: Incomplete | None = None,
        question: bool = False,
        verbose: bool = False,
    ) -> Incomplete: ...
    def interpret_sents(
        self,
        inputs: Incomplete,
        discourse_ids: Incomplete | None = None,
        question: bool = False,
        verbose: bool = False,
    ) -> Incomplete: ...
    def interpret_multi_sents(
        self,
        inputs: Incomplete,
        discourse_ids: Incomplete | None = None,
        question: bool = False,
        verbose: bool = False,
    ) -> Incomplete: ...

class BoxerOutputDrsParser(DrtParser):
    discourse_id: Incomplete
    sentence_id_offset: Incomplete
    quote_chars: Incomplete
    def __init__(self, discourse_id: Incomplete | None = None) -> None: ...
    def parse(
        self, data: Incomplete, signature: Incomplete | None = None
    ) -> Incomplete: ...
    def get_all_symbols(self) -> Incomplete: ...
    def handle(self, tok: Incomplete, context: Incomplete) -> Incomplete: ...
    def attempt_adjuncts(
        self, expression: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def parse_condition(self, indices: Incomplete) -> Incomplete: ...
    def handle_drs(self, tok: Incomplete) -> Incomplete: ...
    def handle_condition(
        self, tok: Incomplete, indices: Incomplete
    ) -> Incomplete: ...
    def parse_drs(self) -> Incomplete: ...
    def parse_variable(self) -> Incomplete: ...
    def parse_index(self) -> Incomplete: ...

class BoxerDrsParser(DrtParser):
    discourse_id: Incomplete
    def __init__(self, discourse_id: Incomplete | None = None) -> None: ...
    def get_all_symbols(self) -> Incomplete: ...
    def attempt_adjuncts(
        self, expression: Incomplete, context: Incomplete
    ) -> Incomplete: ...
    def handle(self, tok: Incomplete, context: Incomplete) -> Incomplete: ...
    def nullableIntToken(self) -> Incomplete: ...
    def get_next_token_variable(
        self, description: Incomplete
    ) -> Incomplete: ...

class AbstractBoxerDrs:
    def variables(self) -> Incomplete: ...
    def variable_types(self) -> Incomplete: ...
    def atoms(self) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...

class BoxerDrs(AbstractBoxerDrs):
    refs: Incomplete
    conds: Incomplete
    consequent: Incomplete
    def __init__(
        self,
        refs: Incomplete,
        conds: Incomplete,
        consequent: Incomplete | None = None,
    ) -> None: ...
    def atoms(self) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    __hash__: Incomplete

class BoxerNot(AbstractBoxerDrs):
    drs: Incomplete
    def __init__(self, drs: Incomplete) -> None: ...
    def atoms(self) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    __hash__: Incomplete

class BoxerIndexed(AbstractBoxerDrs):
    discourse_id: Incomplete
    sent_index: Incomplete
    word_indices: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
    ) -> None: ...
    def atoms(self) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    __hash__: Incomplete

class BoxerPred(BoxerIndexed):
    var: Incomplete
    name: Incomplete
    pos: Incomplete
    sense: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        var: Incomplete,
        name: Incomplete,
        pos: Incomplete,
        sense: Incomplete,
    ) -> None: ...
    def change_var(self, var: Incomplete) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerNamed(BoxerIndexed):
    var: Incomplete
    name: Incomplete
    type: Incomplete
    sense: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        var: Incomplete,
        name: Incomplete,
        type: Incomplete,
        sense: Incomplete,
    ) -> None: ...
    def change_var(self, var: Incomplete) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerRel(BoxerIndexed):
    var1: Incomplete
    var2: Incomplete
    rel: Incomplete
    sense: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        var1: Incomplete,
        var2: Incomplete,
        rel: Incomplete,
        sense: Incomplete,
    ) -> None: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerProp(BoxerIndexed):
    var: Incomplete
    drs: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        var: Incomplete,
        drs: Incomplete,
    ) -> None: ...
    def referenced_labels(self) -> Incomplete: ...
    def atoms(self) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerEq(BoxerIndexed):
    var1: Incomplete
    var2: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        var1: Incomplete,
        var2: Incomplete,
    ) -> None: ...
    def atoms(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerCard(BoxerIndexed):
    var: Incomplete
    value: Incomplete
    type: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        var: Incomplete,
        value: Incomplete,
        type: Incomplete,
    ) -> None: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerOr(BoxerIndexed):
    drs1: Incomplete
    drs2: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        drs1: Incomplete,
        drs2: Incomplete,
    ) -> None: ...
    def atoms(self) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class BoxerWhq(BoxerIndexed):
    ans_types: Incomplete
    drs1: Incomplete
    variable: Incomplete
    drs2: Incomplete
    def __init__(
        self,
        discourse_id: Incomplete,
        sent_index: Incomplete,
        word_indices: Incomplete,
        ans_types: Incomplete,
        drs1: Incomplete,
        variable: Incomplete,
        drs2: Incomplete,
    ) -> None: ...
    def atoms(self) -> Incomplete: ...
    def clean(self) -> Incomplete: ...
    def renumber_sentences(self, f: Incomplete) -> Incomplete: ...
    def __iter__(self) -> Incomplete: ...

class PassthroughBoxerDrsInterpreter:
    def interpret(self, ex: Incomplete) -> Incomplete: ...

class NltkDrtBoxerDrsInterpreter:
    def __init__(self, occur_index: bool = False) -> None: ...
    def interpret(self, ex: Incomplete) -> Incomplete: ...

class UnparseableInputException(Exception): ...
