from _typeshed import Incomplete

borders: Incomplete
contains: Incomplete
city: Incomplete
country: Incomplete
circle_of_lat: Incomplete
circle_of_long: Incomplete
continent: Incomplete
region: Incomplete
ocean: Incomplete
sea: Incomplete
items: Incomplete
item_metadata: Incomplete
rels: Incomplete
not_unary: Incomplete

class Concept:
    prefLabel: Incomplete
    arity: Incomplete
    altLabels: Incomplete
    closures: Incomplete
    extension: Incomplete
    def __init__(
        self,
        prefLabel: Incomplete,
        arity: Incomplete,
        altLabels: Incomplete = [],
        closures: Incomplete = [],
        extension: Incomplete = ...,
    ) -> None: ...
    def augment(self, data: Incomplete) -> Incomplete: ...
    def close(self) -> None: ...

def clause2concepts(
    filename: Incomplete,
    rel_name: Incomplete,
    schema: Incomplete,
    closures: Incomplete = [],
) -> Incomplete: ...
def cities2table(
    filename: Incomplete,
    rel_name: Incomplete,
    dbname: Incomplete,
    verbose: bool = False,
    setup: bool = False,
) -> None: ...
def sql_query(dbname: Incomplete, query: Incomplete) -> Incomplete: ...
def unary_concept(
    label: Incomplete, subj: Incomplete, records: Incomplete
) -> Incomplete: ...
def binary_concept(
    label: Incomplete,
    closures: Incomplete,
    subj: Incomplete,
    obj: Incomplete,
    records: Incomplete,
) -> Incomplete: ...
def process_bundle(rels: Incomplete) -> Incomplete: ...
def make_valuation(
    concepts: Incomplete, read: bool = False, lexicon: bool = False
) -> Incomplete: ...
def val_dump(rels: Incomplete, db: Incomplete) -> None: ...
def val_load(db: Incomplete) -> Incomplete: ...
def label_indivs(
    valuation: Incomplete, lexicon: bool = False
) -> Incomplete: ...
def make_lex(symbols: Incomplete) -> Incomplete: ...
def concepts(items: Incomplete = ...) -> Incomplete: ...
def main() -> None: ...
def sql_demo() -> None: ...
