from _typeshed import Incomplete

from nltk.data import find as find
from nltk.data import load as load
from nltk.tag.api import TaggerI as TaggerI
from nltk.tag.brill import BrillTagger as BrillTagger
from nltk.tag.brill_trainer import BrillTaggerTrainer as BrillTaggerTrainer
from nltk.tag.crf import CRFTagger as CRFTagger
from nltk.tag.hmm import (
    HiddenMarkovModelTagger as HiddenMarkovModelTagger,
)
from nltk.tag.hmm import (
    HiddenMarkovModelTrainer as HiddenMarkovModelTrainer,
)
from nltk.tag.hunpos import HunposTagger as HunposTagger
from nltk.tag.mapping import (
    map_tag as map_tag,
)
from nltk.tag.mapping import (
    tagset_mapping as tagset_mapping,
)
from nltk.tag.perceptron import PerceptronTagger as PerceptronTagger
from nltk.tag.senna import (
    SennaChunkTagger as SennaChunkTagger,
)
from nltk.tag.senna import (
    SennaNERTagger as SennaNERTagger,
)
from nltk.tag.senna import (
    SennaTagger as SennaTagger,
)
from nltk.tag.sequential import (
    AffixTagger as AffixTagger,
)
from nltk.tag.sequential import (
    BigramTagger as BigramTagger,
)
from nltk.tag.sequential import (
    ClassifierBasedPOSTagger as ClassifierBasedPOSTagger,
)
from nltk.tag.sequential import (
    ClassifierBasedTagger as ClassifierBasedTagger,
)
from nltk.tag.sequential import (
    ContextTagger as ContextTagger,
)
from nltk.tag.sequential import (
    DefaultTagger as DefaultTagger,
)
from nltk.tag.sequential import (
    NgramTagger as NgramTagger,
)
from nltk.tag.sequential import (
    RegexpTagger as RegexpTagger,
)
from nltk.tag.sequential import (
    SequentialBackoffTagger as SequentialBackoffTagger,
)
from nltk.tag.sequential import (
    TrigramTagger as TrigramTagger,
)
from nltk.tag.sequential import (
    UnigramTagger as UnigramTagger,
)
from nltk.tag.stanford import (
    StanfordNERTagger as StanfordNERTagger,
)
from nltk.tag.stanford import (
    StanfordPOSTagger as StanfordPOSTagger,
)
from nltk.tag.stanford import (
    StanfordTagger as StanfordTagger,
)
from nltk.tag.tnt import TnT as TnT
from nltk.tag.util import (
    str2tuple as str2tuple,
)
from nltk.tag.util import (
    tuple2str as tuple2str,
)
from nltk.tag.util import (
    untag as untag,
)

PRETRAINED_TAGGERS: Incomplete

def pos_tag(
    tokens: Incomplete, tagset: Incomplete | None = None, lang: str = "eng"
) -> Incomplete: ...
def pos_tag_sents(
    sentences: Incomplete, tagset: Incomplete | None = None, lang: str = "eng"
) -> Incomplete: ...
