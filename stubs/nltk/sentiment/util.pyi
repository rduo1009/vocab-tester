from _typeshed import Incomplete

from nltk.corpus import (
    CategorizedPlaintextCorpusReader as CategorizedPlaintextCorpusReader,
)
from nltk.data import load as load
from nltk.tokenize import PunktTokenizer as PunktTokenizer
from nltk.tokenize.casual import EMOTICON_RE as EMOTICON_RE

NEGATION: str
NEGATION_RE: Incomplete
CLAUSE_PUNCT: str
CLAUSE_PUNCT_RE: Incomplete
HAPPY: Incomplete
SAD: Incomplete

def timer(method: Incomplete) -> Incomplete: ...
def extract_unigram_feats(
    document: Incomplete, unigrams: Incomplete, handle_negation: bool = False
) -> Incomplete: ...
def extract_bigram_feats(
    document: Incomplete, bigrams: Incomplete
) -> Incomplete: ...
def mark_negation(
    document: Incomplete, double_neg_flip: bool = False, shallow: bool = False
) -> Incomplete: ...
def output_markdown(filename: Incomplete, **kwargs: Incomplete) -> None: ...
def split_train_test(
    all_instances: Incomplete, n: Incomplete | None = None
) -> Incomplete: ...
def json2csv_preprocess(
    json_file: Incomplete,
    outfile: Incomplete,
    fields: Incomplete,
    encoding: str = "utf8",
    errors: str = "replace",
    gzip_compress: bool = False,
    skip_retweets: bool = True,
    skip_tongue_tweets: bool = True,
    skip_ambiguous_tweets: bool = True,
    strip_off_emoticons: bool = True,
    remove_duplicates: bool = True,
    limit: Incomplete | None = None,
) -> None: ...
def parse_tweets_set(
    filename: Incomplete,
    label: Incomplete,
    word_tokenizer: Incomplete | None = None,
    sent_tokenizer: Incomplete | None = None,
    skip_header: bool = True,
) -> Incomplete: ...
def demo_tweets(
    trainer: Incomplete,
    n_instances: Incomplete | None = None,
    output: Incomplete | None = None,
) -> None: ...
def demo_movie_reviews(
    trainer: Incomplete,
    n_instances: Incomplete | None = None,
    output: Incomplete | None = None,
) -> None: ...
def demo_subjectivity(
    trainer: Incomplete,
    save_analyzer: bool = False,
    n_instances: Incomplete | None = None,
    output: Incomplete | None = None,
) -> Incomplete: ...
def demo_sent_subjectivity(text: Incomplete) -> None: ...
def demo_liu_hu_lexicon(sentence: Incomplete, plot: bool = False) -> None: ...
def demo_vader_instance(text: Incomplete) -> None: ...
def demo_vader_tweets(
    n_instances: Incomplete | None = None, output: Incomplete | None = None
) -> None: ...
