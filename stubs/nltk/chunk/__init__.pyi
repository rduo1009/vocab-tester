from _typeshed import Incomplete

from nltk.chunk.api import ChunkParserI as ChunkParserI
from nltk.chunk.named_entity import Maxent_NE_Chunker as Maxent_NE_Chunker
from nltk.chunk.regexp import RegexpChunkParser as RegexpChunkParser
from nltk.chunk.regexp import RegexpParser as RegexpParser
from nltk.chunk.util import ChunkScore as ChunkScore
from nltk.chunk.util import accuracy as accuracy
from nltk.chunk.util import conllstr2tree as conllstr2tree
from nltk.chunk.util import conlltags2tree as conlltags2tree
from nltk.chunk.util import ieerstr2tree as ieerstr2tree
from nltk.chunk.util import tagstr2tree as tagstr2tree
from nltk.chunk.util import tree2conllstr as tree2conllstr
from nltk.chunk.util import tree2conlltags as tree2conlltags

def ne_chunker(fmt: str = "multiclass") -> Incomplete: ...
def ne_chunk(
    tagged_tokens: Incomplete, binary: bool = False
) -> Incomplete: ...
def ne_chunk_sents(
    tagged_sentences: Incomplete, binary: bool = False
) -> Incomplete: ...
