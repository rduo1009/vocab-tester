from nltk.corpus.reader.aligned import *
from nltk.corpus.reader.api import *
from nltk.corpus.reader.bcp47 import *
from nltk.corpus.reader.bnc import *
from nltk.corpus.reader.bracket_parse import *
from nltk.corpus.reader.categorized_sents import *
from nltk.corpus.reader.chasen import *
from nltk.corpus.reader.childes import *
from nltk.corpus.reader.chunked import *
from nltk.corpus.reader.cmudict import *
from nltk.corpus.reader.comparative_sents import *
from nltk.corpus.reader.conll import *
from nltk.corpus.reader.crubadan import *
from nltk.corpus.reader.dependency import *
from nltk.corpus.reader.framenet import *
from nltk.corpus.reader.ieer import *
from nltk.corpus.reader.indian import *
from nltk.corpus.reader.ipipan import *
from nltk.corpus.reader.knbc import *
from nltk.corpus.reader.lin import *
from nltk.corpus.reader.mte import *
from nltk.corpus.reader.nkjp import *
from nltk.corpus.reader.nombank import *
from nltk.corpus.reader.nps_chat import *
from nltk.corpus.reader.opinion_lexicon import *
from nltk.corpus.reader.panlex_lite import *
from nltk.corpus.reader.panlex_swadesh import *
from nltk.corpus.reader.pl196x import *
from nltk.corpus.reader.plaintext import *
from nltk.corpus.reader.ppattach import *
from nltk.corpus.reader.propbank import *
from nltk.corpus.reader.pros_cons import *
from nltk.corpus.reader.reviews import *
from nltk.corpus.reader.rte import *
from nltk.corpus.reader.semcor import *
from nltk.corpus.reader.senseval import *
from nltk.corpus.reader.sentiwordnet import *
from nltk.corpus.reader.sinica_treebank import *
from nltk.corpus.reader.string_category import *
from nltk.corpus.reader.switchboard import *
from nltk.corpus.reader.tagged import *
from nltk.corpus.reader.timit import *
from nltk.corpus.reader.toolbox import *
from nltk.corpus.reader.twitter import *
from nltk.corpus.reader.udhr import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.verbnet import *
from nltk.corpus.reader.wordlist import *
from nltk.corpus.reader.wordnet import *
from nltk.corpus.reader.xmldocs import *
from nltk.corpus.reader.ycoe import *

__all__ = [
    "CorpusReader",
    "CategorizedCorpusReader",
    "PlaintextCorpusReader",
    "find_corpus_fileids",
    "TaggedCorpusReader",
    "CMUDictCorpusReader",
    "ConllChunkCorpusReader",
    "WordListCorpusReader",
    "PPAttachmentCorpusReader",
    "SensevalCorpusReader",
    "IEERCorpusReader",
    "ChunkedCorpusReader",
    "SinicaTreebankCorpusReader",
    "BracketParseCorpusReader",
    "IndianCorpusReader",
    "ToolboxCorpusReader",
    "TimitCorpusReader",
    "YCOECorpusReader",
    "MacMorphoCorpusReader",
    "SyntaxCorpusReader",
    "AlpinoCorpusReader",
    "RTECorpusReader",
    "StringCategoryCorpusReader",
    "EuroparlCorpusReader",
    "CategorizedBracketParseCorpusReader",
    "CategorizedTaggedCorpusReader",
    "CategorizedPlaintextCorpusReader",
    "PortugueseCategorizedPlaintextCorpusReader",
    "tagged_treebank_para_block_reader",
    "PropbankCorpusReader",
    "VerbnetCorpusReader",
    "BNCCorpusReader",
    "ConllCorpusReader",
    "XMLCorpusReader",
    "NPSChatCorpusReader",
    "SwadeshCorpusReader",
    "WordNetCorpusReader",
    "WordNetICCorpusReader",
    "SwitchboardCorpusReader",
    "DependencyCorpusReader",
    "NombankCorpusReader",
    "IPIPANCorpusReader",
    "Pl196xCorpusReader",
    "TEICorpusView",
    "KNBCorpusReader",
    "ChasenCorpusReader",
    "CHILDESCorpusReader",
    "AlignedCorpusReader",
    "TimitTaggedCorpusReader",
    "LinThesaurusCorpusReader",
    "SemcorCorpusReader",
    "FramenetCorpusReader",
    "UdhrCorpusReader",
    "BNCCorpusReader",
    "SentiWordNetCorpusReader",
    "SentiSynset",
    "TwitterCorpusReader",
    "NKJPCorpusReader",
    "CrubadanCorpusReader",
    "MTECorpusReader",
    "ReviewsCorpusReader",
    "OpinionLexiconCorpusReader",
    "ProsConsCorpusReader",
    "CategorizedSentencesCorpusReader",
    "ComparativeSentencesCorpusReader",
    "PanLexLiteCorpusReader",
    "NonbreakingPrefixesCorpusReader",
    "UnicharsCorpusReader",
    "MWAPPDBCorpusReader",
    "PanlexSwadeshCorpusReader",
    "BCP47CorpusReader",
]

# Names in __all__ with no definition:
#   AlignedCorpusReader
#   AlpinoCorpusReader
#   BCP47CorpusReader
#   BNCCorpusReader
#   BNCCorpusReader
#   BracketParseCorpusReader
#   CHILDESCorpusReader
#   CMUDictCorpusReader
#   CategorizedBracketParseCorpusReader
#   CategorizedCorpusReader
#   CategorizedPlaintextCorpusReader
#   CategorizedSentencesCorpusReader
#   CategorizedTaggedCorpusReader
#   ChasenCorpusReader
#   ChunkedCorpusReader
#   ComparativeSentencesCorpusReader
#   ConllChunkCorpusReader
#   ConllCorpusReader
#   CorpusReader
#   CrubadanCorpusReader
#   DependencyCorpusReader
#   EuroparlCorpusReader
#   FramenetCorpusReader
#   IEERCorpusReader
#   IPIPANCorpusReader
#   IndianCorpusReader
#   KNBCorpusReader
#   LinThesaurusCorpusReader
#   MTECorpusReader
#   MWAPPDBCorpusReader
#   MacMorphoCorpusReader
#   NKJPCorpusReader
#   NPSChatCorpusReader
#   NombankCorpusReader
#   NonbreakingPrefixesCorpusReader
#   OpinionLexiconCorpusReader
#   PPAttachmentCorpusReader
#   PanLexLiteCorpusReader
#   PanlexSwadeshCorpusReader
#   Pl196xCorpusReader
#   PlaintextCorpusReader
#   PortugueseCategorizedPlaintextCorpusReader
#   PropbankCorpusReader
#   ProsConsCorpusReader
#   RTECorpusReader
#   ReviewsCorpusReader
#   SemcorCorpusReader
#   SensevalCorpusReader
#   SentiSynset
#   SentiWordNetCorpusReader
#   SinicaTreebankCorpusReader
#   StringCategoryCorpusReader
#   SwadeshCorpusReader
#   SwitchboardCorpusReader
#   SyntaxCorpusReader
#   TEICorpusView
#   TaggedCorpusReader
#   TimitCorpusReader
#   TimitTaggedCorpusReader
#   ToolboxCorpusReader
#   TwitterCorpusReader
#   UdhrCorpusReader
#   UnicharsCorpusReader
#   VerbnetCorpusReader
#   WordListCorpusReader
#   WordNetCorpusReader
#   WordNetICCorpusReader
#   XMLCorpusReader
#   YCOECorpusReader
#   find_corpus_fileids
#   tagged_treebank_para_block_reader
