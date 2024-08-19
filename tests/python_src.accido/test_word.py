import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest  # type: ignore[import-not-found]
from python_src.accido.endings import Noun, Pronoun, Verb
from python_src.accido.misc import EndingComponents


def test_eq():
    word1 = Verb(present="test1o", infinitive="testare", perfect="test3i", ppp="test4", meaning="test5")
    assert not word1 == "error"


def test_lt():
    word1 = Verb(present="test1o", infinitive="testare", perfect="test3i", ppp="test4", meaning="test5")
    with pytest.raises(TypeError) as error:
        a = word1 < "error"
    assert error


def test_getitem():
    word1 = Verb(present="test1o", infinitive="testare", perfect="test3i", ppp="test4", meaning="test5")
    assert word1["Vpreactindsg1"] == "test1o"


def test_find_same():
    word = Pronoun(pronoun="ille", meaning="that")
    assert word.find("illa") == [
        EndingComponents(case="nominative", number="singular", gender="feminine", string="nominative singular feminine"),
        EndingComponents(case="ablative", number="singular", gender="feminine", string="ablative singular feminine"),
        EndingComponents(case="nominative", number="plural", gender="neuter", string="nominative plural neuter"),
        EndingComponents(case="accusative", number="plural", gender="neuter", string="accusative plural neuter"),
    ]


def test_find_multipleendings():
    word = Noun(nominative="ego", genitive=None, gender=None, meaning="I")
    assert word.find("nostrum") == [
        EndingComponents(case="genitive", number="plural", string="genitive plural"),
    ]
