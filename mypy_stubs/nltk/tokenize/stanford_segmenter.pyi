from _typeshed import Incomplete

from nltk.internals import (
    config_java as config_java,
)
from nltk.internals import (
    find_dir as find_dir,
)
from nltk.internals import (
    find_file as find_file,
)
from nltk.internals import (
    find_jar as find_jar,
)
from nltk.internals import (
    java as java,
)
from nltk.tokenize.api import TokenizerI as TokenizerI

class StanfordSegmenter:
    java_options: Incomplete
    def __init__(
        self,
        path_to_jar: None = ...,
        path_to_slf4j: None = ...,
        java_class: None = ...,
        path_to_model: None = ...,
        path_to_dict: None = ...,
        path_to_sihan_corpora_dict: None = ...,
        sihan_post_processing: str = ...,
        keep_whitespaces: str = ...,
        encoding: str = ...,
        options: None = ...,
        verbose: bool = ...,
        java_options: str = ...,
    ) -> None: ...
    def default_config(self, lang: Incomplete) -> None: ...
    def tokenize(self, s: Incomplete) -> None: ...
    def segment_file(self, input_file_path: Incomplete) -> Incomplete: ...
    def segment(self, tokens: Incomplete) -> Incomplete: ...
    def segment_sents(self, sentences: Incomplete) -> Incomplete: ...
