# fmt: off
# mypy: ignore-errors

import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from types import SimpleNamespace

import pytest

from python_src.accido.custom_exceptions import (
    InvalidInputError,
    NoEndingError,
)
from python_src.accido.endings import Noun


def test_errors1():
    with pytest.raises(InvalidInputError) as error:
        Noun(nominative="puer", genitive="pueri", gender="a", meaning="boy")
    assert "Gender 'a' not recognised" == str(error.value)

def test_errors2():
    with pytest.raises(InvalidInputError) as error:
        Noun(nominative="puer", genitive="puerifaksldsnj", gender="masculine", meaning="boy")
    assert "Genitive form 'puerifaksldsnj' is not valid" == str(error.value)

def test_errors3():
    with pytest.raises(InvalidInputError) as error:
        Noun(nominative="puer", genitive="puerei", gender="neuter", meaning="boy")
    assert "Fifth declension nouns cannot be neuter (noun 'puer')" == str(error.value)

def test_errors4():
    with pytest.raises(InvalidInputError) as error:
        word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
        word.get(case="makinganerror", number="makinganerror")
    assert "Case 'makinganerror' or number 'makinganerror' not recognised" == str(error.value)

#def test_errors5():
#    with pytest.raises(NoEndingError) as error:
#        word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
#        del word.endings["Nnomsg"]
#        word.get(case="nominative", number="singular")
#    assert "No ending found for case 'nominative' and number 'singular'" == str(error.value)

def test_repr():
    word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
    assert word.__repr__() == "Noun(puer, pueri, m, boy)"


def test_eq():
    word1 = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
    word2 = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
    assert word1 == word2


def test_lt():
    word1 = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
    word2 = Noun(nominative="apuer", genitive="pueri", gender="masculine", meaning="boy")
    # word2 must be smaller than word1 as word1.first = "puer" and word2.first = "apuer"
    assert word1 > word2


def compare(s, t):
    t = list(t)   # make a mutable copy
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t

def test_find():
    word = Noun(nominative="ancilla", genitive="ancillae", gender="feminine", meaning="slavegirl")
    assert compare(word.find("ancilla"), [
        SimpleNamespace(case="nominative", number="singular", string="nominative singular"),
        SimpleNamespace(case="vocative", number="singular", string="vocative singular"),
        SimpleNamespace(case="ablative", number="singular", string="ablative singular")
    ])

def test_pick():
    word = Noun(nominative="ancilla", genitive="ancillae", gender="feminine", meaning="slavegirl")
    word.pick()

def test_firstdeclension():
    word = Noun(nominative="ancilla", genitive="ancillae", gender="feminine", meaning="slavegirl")
    assert word.get(case="nominative", number="singular") == "ancilla"
    assert word.get(case="vocative", number="singular") == "ancilla"
    assert word.get(case="accusative", number="singular") == "ancillam"
    assert word.get(case="genitive", number="singular") == "ancillae"
    assert word.get(case="dative", number="singular") == "ancillae"
    assert word.get(case="ablative", number="singular") == "ancilla"
    assert word.get(case="nominative", number="plural") == "ancillae"
    assert word.get(case="vocative", number="plural") == "ancillae"
    assert word.get(case="accusative", number="plural") == "ancillas"
    assert word.get(case="genitive", number="plural") == "ancillarum"
    assert word.get(case="dative", number="plural") == "ancillis"
    assert word.get(case="ablative", number="plural") == "ancillis"


def test_seconddeclension1():
    word = Noun(nominative="servus", genitive="servi", gender="masculine", meaning="slave")
    assert word.get(case="nominative", number="singular") == "servus"
    assert word.get(case="vocative", number="singular") == "serve"
    assert word.get(case="accusative", number="singular") == "servum"
    assert word.get(case="genitive", number="singular") == "servi"
    assert word.get(case="dative", number="singular") == "servo"
    assert word.get(case="ablative", number="singular") == "servo"
    assert word.get(case="nominative", number="plural") == "servi"
    assert word.get(case="vocative", number="plural") == "servi"
    assert word.get(case="accusative", number="plural") == "servos"
    assert word.get(case="genitive", number="plural") == "servorum"
    assert word.get(case="dative", number="plural") == "servis"
    assert word.get(case="ablative", number="plural") == "servis"


def test_seconddeclension2():
    word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
    assert word.get(case="nominative", number="singular") == "puer"
    assert word.get(case="vocative", number="singular") == "puer"
    assert word.get(case="accusative", number="singular") == "puerum"
    assert word.get(case="genitive", number="singular") == "pueri"
    assert word.get(case="dative", number="singular") == "puero"
    assert word.get(case="ablative", number="singular") == "puero"
    assert word.get(case="nominative", number="plural") == "pueri"
    assert word.get(case="vocative", number="plural") == "pueri"
    assert word.get(case="accusative", number="plural") == "pueros"
    assert word.get(case="genitive", number="plural") == "puerorum"
    assert word.get(case="dative", number="plural") == "pueris"
    assert word.get(case="ablative", number="plural") == "pueris"


def test_thirddeclension():
    word = Noun(nominative="carcer", genitive="carceris", gender="masculine", meaning="prison")
    assert word.get(case="nominative", number="singular") == "carcer"
    assert word.get(case="vocative", number="singular") == "carcer"
    assert word.get(case="accusative", number="singular") == "carcerem"
    assert word.get(case="genitive", number="singular") == "carceris"
    assert word.get(case="dative", number="singular") == "carceri"
    assert word.get(case="ablative", number="singular") == "carcere"
    assert word.get(case="nominative", number="plural") == "carceres"
    assert word.get(case="vocative", number="plural") == "carceres"
    assert word.get(case="accusative", number="plural") == "carceres"
    assert word.get(case="genitive", number="plural") == "carcerum"
    assert word.get(case="dative", number="plural") == "carceribus"
    assert word.get(case="ablative", number="plural") == "carceribus"


def test_seconddeclension_neuter():
    word = Noun(nominative="templum", genitive="templi", gender="neuter", meaning="temple")
    assert word.get(case="nominative", number="singular") == "templum"
    assert word.get(case="vocative", number="singular") == "templum"
    assert word.get(case="accusative", number="singular") == "templum"
    assert word.get(case="genitive", number="singular") == "templi"
    assert word.get(case="dative", number="singular") == "templo"
    assert word.get(case="ablative", number="singular") == "templo"
    assert word.get(case="nominative", number="plural") == "templa"
    assert word.get(case="vocative", number="plural") == "templa"
    assert word.get(case="accusative", number="plural") == "templa"
    assert word.get(case="genitive", number="plural") == "templorum"
    assert word.get(case="dative", number="plural") == "templis"
    assert word.get(case="ablative", number="plural") == "templis"


def test_thirddeclension_neuter():
    word = Noun(nominative="litus", genitive="litoris", gender="neuter", meaning="beach")
    assert word.get(case="nominative", number="singular") == "litus"
    assert word.get(case="vocative", number="singular") == "litus"
    assert word.get(case="accusative", number="singular") == "litus"
    assert word.get(case="genitive", number="singular") == "litoris"
    assert word.get(case="dative", number="singular") == "litori"
    assert word.get(case="ablative", number="singular") == "litore"
    assert word.get(case="nominative", number="plural") == "litora"
    assert word.get(case="vocative", number="plural") == "litora"
    assert word.get(case="accusative", number="plural") == "litora"
    assert word.get(case="genitive", number="plural") == "litorum"
    assert word.get(case="dative", number="plural") == "litoribus"
    assert word.get(case="ablative", number="plural") == "litoribus"
