import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import python_src as src
from python_src.accido.endings import Adjective, Noun, Pronoun, RegularWord, Verb
from python_src.accido.misc import Gender
from python_src.lego.misc import VocabList


def test_vocablist():
    l = VocabList([
        Verb(present="audio", infinitive="audire", perfect="audivi", ppp="auditus", meaning="hear"),
        Noun(nominative="nomen", genitive="nominis", gender=Gender.NEUTER, meaning="name"),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        RegularWord(word="e", meaning="from"),
        Pronoun(pronoun="ille", meaning="that"),
    ])

    assert l.__repr__() == f"VocabList([Verb(audio, audire, audivi, auditus, hear), Noun(nomen, nominis, neuter, name), Adjective(bonus, bona, bonum, None, 212, good), RegularWord(e, from), Pronoun(ille, that)], version={src.__version__})"
