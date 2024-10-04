from _typeshed import Incomplete

from nltk.internals import deprecated as deprecated

HIER_SEPARATOR: str

def extract_fields(tweet: Incomplete, fields: Incomplete) -> Incomplete: ...
def json2csv(
    fp: Incomplete,
    outfile: Incomplete,
    fields: Incomplete,
    encoding: str = "utf8",
    errors: str = "replace",
    gzip_compress: bool = False,
) -> None: ...
def outf_writer_compat(
    outfile: Incomplete,
    encoding: Incomplete,
    errors: Incomplete,
    gzip_compress: bool = False,
) -> Incomplete: ...
def json2csv_entities(
    tweets_file: Incomplete,
    outfile: Incomplete,
    main_fields: Incomplete,
    entity_type: Incomplete,
    entity_fields: Incomplete,
    encoding: str = "utf8",
    errors: str = "replace",
    gzip_compress: bool = False,
) -> None: ...
def get_header_field_list(
    main_fields: Incomplete, entity_type: Incomplete, entity_fields: Incomplete
) -> Incomplete: ...
