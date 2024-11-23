import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


import src
from src.core.accido.endings import Adjective, Noun, Pronoun, RegularWord, Verb
from src.core.accido.misc import Gender, MultipleMeanings
from src.core.lego.misc import VocabList


def test_vocablist():
    l = VocabList([
        Verb("audio", "audire", "audivi", "auditus", meaning="hear"),
        Noun("nomen", "nominis", gender=Gender.NEUTER, meaning="name"),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        RegularWord("e", meaning="from"),
        Pronoun("ille", meaning="that"),
    ])

    assert l.__repr__() == f"VocabList([Verb(audio, audire, audivi, auditus, hear), Noun(nomen, nominis, neuter, name), Adjective(bonus, bona, bonum, None, 212, good), RegularWord(e, from), Pronoun(ille, that)], version={src.__version__})"


def test_vocablist_add():
    list_1 = VocabList([
        Verb("audio", "audire", "audivi", "auditus", meaning="hear"),
        Noun("templum", "templi", gender=Gender.NEUTER, meaning="temple"),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy"),
        RegularWord("e", meaning="from"),
        Pronoun("ille", meaning="that"),
    ])

    list_2 = VocabList([
        Verb("audio", "audire", "audivi", "auditus", meaning="listen"),
        Noun("templum", "templi", gender=Gender.NEUTER, meaning="shrine"),
        Adjective("laetus", "laeta", "laetum", declension="212", meaning="joyful"),
        RegularWord("e", meaning="out"),
        Pronoun("ille", meaning="that"),
    ])

    assert list_1 + list_2 == VocabList([
        Verb("audio", "audire", "audivi", "auditus", meaning=MultipleMeanings(("hear", "listen"))),
        Noun("templum", "templi", gender=Gender.NEUTER, meaning=MultipleMeanings(("temple", "shrine"))),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        Adjective("laetus", "laeta", "laetum", declension="212", meaning=MultipleMeanings(("happy", "joyful"))),
        RegularWord("e", meaning=MultipleMeanings(("from", "out"))),
        Pronoun("ille", meaning="that"),
    ])
