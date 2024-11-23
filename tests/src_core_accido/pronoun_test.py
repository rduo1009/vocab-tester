import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


import pytest
from src.core.accido.edge_cases import PRONOUNS
from src.core.accido.endings import Noun, Pronoun
from src.core.accido.exceptions import InvalidInputError
from src.core.accido.misc import Case, EndingComponents, Gender, MultipleMeanings, Number


class TestPronounDunder:
    def test_find(self):
        word = Pronoun("ille", meaning="that")
        assert word.find("ille") == [
            EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, string="nominative singular masculine"),
        ]

    def test_repr(self):
        word = Pronoun("ille", meaning="that")
        assert repr(word) == "Pronoun(ille, that)"

    def test_str(self):
        word = Pronoun("ille", meaning="that")
        assert str(word) == "that: ille, illa, illud"

    def test_add_different_word(self):
        word1 = Pronoun("ille", meaning="that")
        word2 = Pronoun("hic", meaning="this")
        with pytest.raises(TypeError):
            word1 + word2

    def test_add_different_pos(self):
        word1 = Pronoun("ille", meaning="that")
        word2 = Noun("puella", "puellae", gender=Gender.FEMININE, meaning="girl")
        with pytest.raises(TypeError):
            word1 + word2

    def test_add(self):
        word1 = Pronoun("ille", meaning="that")
        word2 = Pronoun("ille", meaning="he")
        assert word1 + word2 == Pronoun("ille", meaning=MultipleMeanings(("that", "he")))


def test_pronoun():
    assert Pronoun("ille", meaning="that").endings == PRONOUNS["ille"]


def test_get():
    word = Pronoun("ille", meaning="that")
    assert word.get(gender=Gender.MASCULINE, case=Case.GENITIVE, number=Number.SINGULAR) == "illius"


def test_errors_cannot_recognise():
    with pytest.raises(InvalidInputError) as error:
        Pronoun("error", meaning="this").endings
    assert "Pronoun 'error' not recognised" == str(error.value)
