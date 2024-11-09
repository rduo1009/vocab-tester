from _typeshed import Incomplete

from nltk.sem.logic import SubstituteBindingsI

__all__ = [
    "FeatStruct",
    "FeatDict",
    "FeatList",
    "unify",
    "subsumes",
    "conflicts",
    "Feature",
    "SlashFeature",
    "RangeFeature",
    "SLASH",
    "TYPE",
    "FeatStructReader",
]

class FeatStruct(SubstituteBindingsI):
    def __new__(
        cls: Incomplete,
        features: Incomplete | None = None,
        **morefeatures: Incomplete,
    ) -> Incomplete: ...
    def equal_values(
        self, other: Incomplete, check_reentrance: bool = False
    ) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...
    def freeze(self) -> None: ...
    def frozen(self) -> Incomplete: ...
    def copy(self, deep: bool = True) -> Incomplete: ...
    def __deepcopy__(self, memo: Incomplete) -> None: ...
    def cyclic(self) -> Incomplete: ...
    def walk(self) -> Incomplete: ...
    def substitute_bindings(self, bindings: Incomplete) -> Incomplete: ...
    def retract_bindings(self, bindings: Incomplete) -> Incomplete: ...
    def variables(self) -> Incomplete: ...
    def rename_variables(
        self,
        vars: Incomplete | None = None,
        used_vars: Incomplete = (),
        new_vars: Incomplete | None = None,
    ) -> Incomplete: ...
    def remove_variables(self) -> Incomplete: ...
    def unify(
        self,
        other: Incomplete,
        bindings: Incomplete | None = None,
        trace: bool = False,
        fail: Incomplete | None = None,
        rename_vars: bool = True,
    ) -> Incomplete: ...
    def subsumes(self, other: Incomplete) -> Incomplete: ...

class FeatDict(FeatStruct, dict):  # type: ignore[type-arg]
    def __init__(
        self, features: Incomplete | None = None, **morefeatures: Incomplete
    ) -> None: ...
    def __getitem__(self, name_or_path: Incomplete) -> Incomplete: ...
    def get(
        self, name_or_path: Incomplete, default: Incomplete | None = None
    ) -> Incomplete: ...
    def __contains__(self, name_or_path: Incomplete) -> bool: ...
    def has_key(self, name_or_path: Incomplete) -> Incomplete: ...
    def __delitem__(self, name_or_path: Incomplete) -> None: ...
    def __setitem__(
        self, name_or_path: Incomplete, value: Incomplete
    ) -> None: ...
    clear: Incomplete
    pop: Incomplete
    popitem: Incomplete
    setdefault: Incomplete
    def update(
        self, features: Incomplete | None = None, **morefeatures: Incomplete
    ) -> None: ...
    def __deepcopy__(self, memo: Incomplete) -> Incomplete: ...

class FeatList(FeatStruct, list):  # type: ignore[type-arg]
    def __init__(self, features: Incomplete = ()) -> None: ...
    def __getitem__(self, name_or_path: Incomplete) -> Incomplete: ...
    def __delitem__(self, name_or_path: Incomplete) -> None: ...
    def __setitem__(
        self, name_or_path: Incomplete, value: Incomplete
    ) -> None: ...
    __iadd__: Incomplete
    __imul__: Incomplete
    append: Incomplete
    extend: Incomplete
    insert: Incomplete
    pop: Incomplete
    remove: Incomplete
    reverse: Incomplete
    sort: Incomplete
    def __deepcopy__(self, memo: Incomplete) -> Incomplete: ...

class _UnificationFailure: ...

def unify(
    fstruct1: Incomplete,
    fstruct2: Incomplete,
    bindings: Incomplete | None = None,
    trace: bool = False,
    fail: Incomplete | None = None,
    rename_vars: bool = True,
    fs_class: str = "default",
) -> Incomplete: ...

class _UnificationFailureError(Exception): ...

def subsumes(fstruct1: Incomplete, fstruct2: Incomplete) -> Incomplete: ...
def conflicts(
    fstruct1: Incomplete, fstruct2: Incomplete, trace: int = 0
) -> Incomplete: ...

class SubstituteBindingsSequence(SubstituteBindingsI):
    def variables(self) -> Incomplete: ...
    def substitute_bindings(self, bindings: Incomplete) -> Incomplete: ...
    def subst(self, v: Incomplete, bindings: Incomplete) -> Incomplete: ...

class FeatureValueTuple(SubstituteBindingsSequence, tuple): ...  # type: ignore[type-arg]
class FeatureValueSet(SubstituteBindingsSequence, frozenset): ...  # type: ignore[type-arg]

class FeatureValueUnion(SubstituteBindingsSequence, frozenset):  # type: ignore[type-arg]
    def __new__(cls: Incomplete, values: Incomplete) -> Incomplete: ...

class FeatureValueConcat(SubstituteBindingsSequence, tuple):  # type: ignore[type-arg]
    def __new__(cls: Incomplete, values: Incomplete) -> Incomplete: ...

class Feature:
    def __init__(
        self,
        name: Incomplete,
        default: Incomplete | None = None,
        display: Incomplete | None = None,
    ) -> None: ...
    @property
    def name(self) -> Incomplete: ...
    @property
    def default(self) -> Incomplete: ...
    @property
    def display(self) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...
    def read_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        parser: Incomplete,
    ) -> Incomplete: ...
    def unify_base_values(
        self, fval1: Incomplete, fval2: Incomplete, bindings: Incomplete
    ) -> Incomplete: ...

class SlashFeature(Feature):
    def read_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        parser: Incomplete,
    ) -> Incomplete: ...

class RangeFeature(Feature):
    RANGE_RE: Incomplete
    def read_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        parser: Incomplete,
    ) -> Incomplete: ...
    def unify_base_values(
        self, fval1: Incomplete, fval2: Incomplete, bindings: Incomplete
    ) -> Incomplete: ...

SLASH: Incomplete
TYPE: Incomplete

class CustomFeatureValue:
    def unify(self, other: Incomplete) -> None: ...
    def __eq__(self, other: Incomplete) -> Incomplete: ...
    def __ne__(self, other: Incomplete) -> Incomplete: ...
    def __lt__(self, other: Incomplete) -> Incomplete: ...
    def __hash__(self) -> Incomplete: ...

class FeatStructReader:
    def __init__(
        self,
        features: Incomplete = ...,
        fdict_class: Incomplete = ...,
        flist_class: Incomplete = ...,
        logic_parser: Incomplete | None = None,
    ) -> None: ...
    def fromstring(
        self, s: Incomplete, fstruct: Incomplete | None = None
    ) -> Incomplete: ...
    def read_partial(
        self,
        s: Incomplete,
        position: int = 0,
        reentrances: Incomplete | None = None,
        fstruct: Incomplete | None = None,
    ) -> Incomplete: ...
    def read_value(
        self, s: Incomplete, position: Incomplete, reentrances: Incomplete
    ) -> Incomplete: ...
    VALUE_HANDLERS: Incomplete
    def read_fstruct_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_str_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_int_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_var_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_sym_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_app_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_logic_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_tuple_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
    def read_set_value(
        self,
        s: Incomplete,
        position: Incomplete,
        reentrances: Incomplete,
        match: Incomplete,
    ) -> Incomplete: ...
