import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.endings import Noun, Pronoun, Verb
from python_src.accido.misc import Case, EndingComponents, Gender, Number


def test_eq():
    word1 = Verb(present="test1o", infinitive="testare", perfect="test3i", ppp="test4", meaning="test5")
    assert not word1 == "error"


def test_lt():
    foo = Verb(present="test1o", infinitive="testare", perfect="test3i", ppp="test4", meaning="test5")
    with pytest.raises(TypeError) as error:
        foo < "2"
    assert error


def test_getitem():
    word1 = Verb(present="test1o", infinitive="testare", perfect="test3i", ppp="test4", meaning="test5")
    assert word1["Vpreactindsg1"] == "test1o"


def test_find_same():
    word = Pronoun(pronoun="ille", meaning="that")
    assert word.find("illa") == [
        EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.FEMININE, string="nominative singular feminine"),
        EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR, gender=Gender.FEMININE, string="ablative singular feminine"),
        EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL, gender=Gender.NEUTER, string="nominative plural neuter"),
        EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.NEUTER, string="accusative plural neuter"),
    ]


def test_find_multipleendings():
    word = Noun(nominative="ego", genitive=None, gender=None, meaning="I")
    a = EndingComponents(case=Case.GENITIVE, number=Number.PLURAL, string="genitive plural")
    a.subtype = "pronoun"
    assert word.find("nostrum") == [a]
