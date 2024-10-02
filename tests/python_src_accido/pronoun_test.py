import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from types import SimpleNamespace

from python_src.accido.edge_cases import PRONOUNS
from python_src.accido.endings import Pronoun
from python_src.accido.misc import Case, Gender, Number


class TestPronounDunder:
    def test_find(self):
        word = Pronoun(pronoun="ille", meaning="that")
        assert word.find("ille") == [
            SimpleNamespace(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, string="nominative singular masculine"),
        ]

    def test_repr(self):
        word = Pronoun(pronoun="ille", meaning="that")
        assert repr(word) == "Pronoun(ille, that)"

    def test_str(self):
        word = Pronoun(pronoun="ille", meaning="that")
        assert str(word) == "that: ille, illa, illud"


def test_pronoun():
    assert Pronoun(pronoun="ille", meaning="that").endings == PRONOUNS["ille"]


def test_get():
    word = Pronoun(pronoun="ille", meaning="that")
    assert word.get(gender=Gender.MASCULINE, case=Case.GENITIVE, number=Number.SINGULAR) == "illius"
