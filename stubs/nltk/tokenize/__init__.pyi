from _typeshed import Incomplete

from nltk.data import load as load
from nltk.tokenize.casual import (
    TweetTokenizer as TweetTokenizer,
)
from nltk.tokenize.casual import (
    casual_tokenize as casual_tokenize,
)
from nltk.tokenize.destructive import NLTKWordTokenizer as NLTKWordTokenizer
from nltk.tokenize.legality_principle import (
    LegalitySyllableTokenizer as LegalitySyllableTokenizer,
)
from nltk.tokenize.mwe import MWETokenizer as MWETokenizer
from nltk.tokenize.punkt import (
    PunktSentenceTokenizer as PunktSentenceTokenizer,
)
from nltk.tokenize.punkt import (
    PunktTokenizer as PunktTokenizer,
)
from nltk.tokenize.regexp import (
    BlanklineTokenizer as BlanklineTokenizer,
)
from nltk.tokenize.regexp import (
    RegexpTokenizer as RegexpTokenizer,
)
from nltk.tokenize.regexp import (
    WhitespaceTokenizer as WhitespaceTokenizer,
)
from nltk.tokenize.regexp import (
    WordPunctTokenizer as WordPunctTokenizer,
)
from nltk.tokenize.regexp import (
    blankline_tokenize as blankline_tokenize,
)
from nltk.tokenize.regexp import (
    regexp_tokenize as regexp_tokenize,
)
from nltk.tokenize.regexp import (
    wordpunct_tokenize as wordpunct_tokenize,
)
from nltk.tokenize.repp import ReppTokenizer as ReppTokenizer
from nltk.tokenize.sexpr import (
    SExprTokenizer as SExprTokenizer,
)
from nltk.tokenize.sexpr import (
    sexpr_tokenize as sexpr_tokenize,
)
from nltk.tokenize.simple import (
    LineTokenizer as LineTokenizer,
)
from nltk.tokenize.simple import (
    SpaceTokenizer as SpaceTokenizer,
)
from nltk.tokenize.simple import (
    TabTokenizer as TabTokenizer,
)
from nltk.tokenize.simple import (
    line_tokenize as line_tokenize,
)
from nltk.tokenize.sonority_sequencing import (
    SyllableTokenizer as SyllableTokenizer,
)
from nltk.tokenize.stanford_segmenter import (
    StanfordSegmenter as StanfordSegmenter,
)
from nltk.tokenize.texttiling import TextTilingTokenizer as TextTilingTokenizer
from nltk.tokenize.toktok import ToktokTokenizer as ToktokTokenizer
from nltk.tokenize.treebank import (
    TreebankWordDetokenizer as TreebankWordDetokenizer,
)
from nltk.tokenize.treebank import (
    TreebankWordTokenizer as TreebankWordTokenizer,
)
from nltk.tokenize.util import (
    regexp_span_tokenize as regexp_span_tokenize,
)
from nltk.tokenize.util import (
    string_span_tokenize as string_span_tokenize,
)

def sent_tokenize(
    text: Incomplete, language: str = "english"
) -> Incomplete: ...
def word_tokenize(
    text: Incomplete, language: str = "english", preserve_line: bool = False
) -> Incomplete: ...
