# fmt: off
# mypy: ignore-errors

import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from types import SimpleNamespace

import pytest

from src.accido.custom_exceptions import InvalidInputError, NoEndingError
from src.accido.edge_cases import PRONOUNS
from src.accido.endings import Pronoun


def test_errors1():
    with pytest.raises(InvalidInputError) as error:
        Pronoun(pronoun="b", meaning="this").endings
    assert "Pronoun 'b' not recognised" == str(error.value)

def test_errors2():
    with pytest.raises(InvalidInputError) as error:
        word = Pronoun(pronoun="hic", meaning="this")
        word.get(gender="a", case="b", number="c")
    assert "Gender 'a', case 'b' or number 'c' not recognised" == str(error.value)

#def test_errors3():
#    with pytest.raises(NoEndingError) as error:
#        word = Pronoun(pronoun="hic", meaning="this")
#        del word.endings["Pmnomsg"]
#        word.get(gender="masculine", case="nominative", number="singular")
#    assert "No ending found for gender 'masculine', case 'nominative' and number 'singular'" == str(error.value)

def test_pick():
    word = Pronoun(pronoun="ille", meaning="that")
    word.pick()

def test_find():
    word = Pronoun(pronoun="ille", meaning="that")
    assert word.find("ille") == [
        SimpleNamespace(case="nominative", number="singular", gender="masculine", string="nominative singular masculine"),
    ]

def test_pronoun():
    assert Pronoun(pronoun="ille", meaning="that").endings == PRONOUNS["ille"]
