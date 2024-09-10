import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from types import SimpleNamespace

import pytest
from python_src.accido.edge_cases import PRONOUNS
from python_src.accido.endings import Pronoun
from python_src.accido.exceptions import InvalidInputError


class TestPronounErrors:
    def test_errors_cannot_recognise(self):
        with pytest.raises(InvalidInputError) as error:
            Pronoun(pronoun="error", meaning="this").endings
        assert "Pronoun 'error' not recognised" == str(error.value)

    def test_errors_invalid_gender(self):
        with pytest.raises(InvalidInputError) as error:
            word = Pronoun(pronoun="hic", meaning="this")
            word.get(gender="error", case="nominative", number="singular")
        assert "Invalid gender: 'error'" == str(error.value)

    def test_errors_invalid_case(self):
        with pytest.raises(InvalidInputError) as error:
            word = Pronoun(pronoun="hic", meaning="this")
            word.get(gender="masculine", case="error", number="singular")
        assert "Invalid case: 'error'" == str(error.value)

    def test_errors_invalid_number(self):
        with pytest.raises(InvalidInputError) as error:
            word = Pronoun(pronoun="hic", meaning="this")
            word.get(gender="masculine", case="nominative", number="error")
        assert "Invalid number: 'error'" == str(error.value)


class TestPronounDunder:
    def test_find(self):
        word = Pronoun(pronoun="ille", meaning="that")
        assert word.find("ille") == [
            SimpleNamespace(case="nominative", number="singular", gender="masculine", string="nominative singular masculine"),
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
    assert word.get(gender="masculine", case="genitive", number="singular") == "illius"
