import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from types import SimpleNamespace

import pytest  # type: ignore[import-not-found]
from python_src.accido.custom_exceptions import InvalidInputError
from python_src.accido.edge_cases import PRONOUNS
from python_src.accido.endings import Pronoun


class TestPronounErrors:
    def test_errors1(self):
        with pytest.raises(InvalidInputError) as error:
            Pronoun(pronoun="b", meaning="this").endings
        assert "Pronoun 'b' not recognised" == str(error.value)

    def test_errors2(self):
        with pytest.raises(InvalidInputError) as error:
            word = Pronoun(pronoun="hic", meaning="this")
            word.get(gender="a", case="b", number="c")
        assert "Gender 'a', case 'b' or number 'c' not recognised" == str(error.value)

    # def test_errors3(self):
    #     with pytest.raises() as error:
    #         word = Pronoun(pronoun="hic", meaning="this")
    #         del word.endings["Pmnomsg"]
    #         word.get(gender="masculine", case="nominative", number="singular")
    #     assert "No ending found for gender 'masculine', case 'nominative' and number 'singular'" == str(error.value)


class TestPronounDunder:
    # def test_pick(self):
    #     word = Pronoun(pronoun="ille", meaning="that")
    #     word.pick()

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
