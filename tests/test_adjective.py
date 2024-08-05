# fmt: off
# mypy: ignore-errors

import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from types import SimpleNamespace
from grammatica.endings import Adjective
from grammatica.custom_exceptions import InvalidInputError, NoEndingError



def test_errors1():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy", termination=3)
    assert "2-1-2 adjectives cannot have a termination (termination 3 given)" == str(error.value)

def test_errors2():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", declension="212", meaning="happy")
    assert "2-1-2 adjectives must have 3 principal parts (adjective 'laetus' given)" == str(error.value)

def test_errors3():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", "laetum", declension="3", meaning="happy", termination=1)
    assert "First-termination adjectives must have 2 principal parts (adjective 'laetus')" == str(error.value)

def test_errors4():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", declension="3", meaning="happy", termination=1)
    assert "Genitive 'laeta' not recognised" == str(error.value)

def test_errors5():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", "laetum", declension="3", meaning="happy", termination=2)
    assert "Second-termination adjectives must have 2 principal parts (adjective 'laetus')" == str(error.value)

def test_errors6():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", declension="3", meaning="happy", termination=3)
    assert "Third-termination adjectives must have 3 principal parts (adjective 'laetus')" == str(error.value)

def test_errors7():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", declension="3", meaning="happy", termination=7)
    assert "Termination must be 1, 2 or 3 (given 7)" == str(error.value)

def test_errors8():
    with pytest.raises(InvalidInputError) as error:
        Adjective("laetus", "laeta", "laetum", declension="332801549372", meaning="happy", termination=3)
    assert "Declension 332801549372 not recognised" == str(error.value)

def test_errors9():
    with pytest.raises(InvalidInputError) as error:
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        word.get(case="makinganerror", gender="masculine", number="singular", degree="adgsf", adverb=True)
    assert "Adverbs do not have gender, case or number (given 'masculine', 'makinganerror' and 'singular')" == str(error.value)

def test_errors10():
    with pytest.raises(InvalidInputError) as error:
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        word.get(degree="adgsf", adverb=True)
    assert "Degree 'adgsf' not recognised" == str(error.value)

def test_errors11():
    with pytest.raises(NoEndingError) as error:
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        del word.endings["Dpos"]
        word.get(degree="positive", adverb=True)
    assert "No ending found for degree 'positive'" == str(error.value)

def test_errors12():
    with pytest.raises(InvalidInputError) as error:
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        word.get(case="makinganerror", gender="masculine", number="singular", degree="adgsf")
    assert "Degree 'adgsf', gender 'masculine', case 'makinganerror' or number 'singular' not recognised" == str(error.value)

def test_errors13():
    with pytest.raises(NoEndingError) as error:
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        del word.endings["Aposmnomsg"]
        word.get(case="nominative", gender="masculine", number="singular", degree="positive")
    assert "No ending found for degree 'positive', gender 'masculine', case 'nominative' and number 'singular'" == str(error.value)

def test_repr():
    word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    assert word.__repr__() == "Adjective(laetus, laeta, laetum, None, 212, happy)"


def test_eq():
    word1 = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    word2 = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    assert word1 == word2


def test_lt():
    word1 = Adjective("aalaetus", "laeta", "laetum", declension="212", meaning="happy")
    word2 = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    assert word1 < word2

def compare(s, t):
    t = list(t)   # make a mutable copy
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t

def test_find():
    word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    assert compare(word.find("laeta"), [       
        SimpleNamespace(degree="positive", gender="feminine", case="nominative", number="singular", string="positive nominative singular feminine"),
        SimpleNamespace(degree="positive", gender="feminine", case="vocative", number="singular", string="positive vocative singular feminine"),
        SimpleNamespace(degree="positive", gender="feminine", case="ablative", number="singular", string="positive ablative singular feminine"),
        SimpleNamespace(degree="positive", gender="neuter", case="nominative", number="plural", string="positive nominative plural neuter"),
        SimpleNamespace(degree="positive", gender="neuter", case="vocative", number="plural", string="positive vocative plural neuter"),
        SimpleNamespace(degree="positive", gender="neuter", case="accusative", number="plural", string="positive accusative plural neuter"),
    ])

def test_declension212():
    word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    assert word.get(degree="positive", gender="masculine", case="nominative", number="singular") == "laetus"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="singular") == "laete"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="singular") == "laetum"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="singular") == "laeti"
    assert word.get(degree="positive", gender="masculine", case="dative", number="singular") == "laeto"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="singular") == "laeto"
    assert word.get(degree="positive", gender="masculine", case="nominative", number="plural") == "laeti"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="plural") == "laeti"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="plural") == "laetos"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="plural") == "laetorum"
    assert word.get(degree="positive", gender="masculine", case="dative", number="plural") == "laetis"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="plural") == "laetis"

    assert word.get(degree="positive", gender="feminine", case="nominative", number="singular") == "laeta"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="singular") == "laeta"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="singular") == "laetam"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="singular") == "laetae"
    assert word.get(degree="positive", gender="feminine", case="dative", number="singular") == "laetae"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="singular") == "laeta"
    assert word.get(degree="positive", gender="feminine", case="nominative", number="plural") == "laetae"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="plural") == "laetae"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="plural") == "laetas"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="plural") == "laetarum"
    assert word.get(degree="positive", gender="feminine", case="dative", number="plural") == "laetis"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="plural") == "laetis"

    assert word.get(degree="positive", gender="neuter", case="nominative", number="singular") == "laetum"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="singular") == "laetum"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="singular") == "laetum"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="singular") == "laeti"
    assert word.get(degree="positive", gender="neuter", case="dative", number="singular") == "laeto"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="singular") == "laeto"
    assert word.get(degree="positive", gender="neuter", case="nominative", number="plural") == "laeta"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="plural") == "laeta"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="plural") == "laeta"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="plural") == "laetorum"
    assert word.get(degree="positive", gender="neuter", case="dative", number="plural") == "laetis"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="plural") == "laetis"

    assert word.get(degree="comparative", gender="masculine", case="nominative", number="singular") == "laetior"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="singular") == "laetior"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="singular") == "laetiorem"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="singular") == "laetioris"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="singular") == "laetiori"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="singular") == "laetiore"
    assert word.get(degree="comparative", gender="masculine", case="nominative", number="plural") == "laetiores"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="plural") == "laetiores"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="plural") == "laetiores"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="plural") == "laetiorum"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="plural") == "laetioribus"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="plural") == "laetioribus"

    assert word.get(degree="comparative", gender="feminine", case="nominative", number="singular") == "laetior"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="singular") == "laetior"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="singular") == "laetiorem"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="singular") == "laetioris"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="singular") == "laetiori"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="singular") == "laetiore"
    assert word.get(degree="comparative", gender="feminine", case="nominative", number="plural") == "laetiores"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="plural") == "laetiores"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="plural") == "laetiores"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="plural") == "laetiorum"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="plural") == "laetioribus"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="plural") == "laetioribus"

    assert word.get(degree="comparative", gender="neuter", case="nominative", number="singular") == "laetius"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="singular") == "laetius"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="singular") == "laetius"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="singular") == "laetioris"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="singular") == "laetiori"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="singular") == "laetiore"
    assert word.get(degree="comparative", gender="neuter", case="nominative", number="plural") == "laetiora"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="plural") == "laetiora"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="plural") == "laetiora"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="plural") == "laetiorum"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="plural") == "laetioribus"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="plural") == "laetioribus"

    assert word.get(degree="superlative", gender="masculine", case="nominative", number="singular") == "laetissimus"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="singular") == "laetissime"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="singular") == "laetissimum"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="singular") == "laetissimi"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="singular") == "laetissimo"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="singular") == "laetissimo"
    assert word.get(degree="superlative", gender="masculine", case="nominative", number="plural") == "laetissimi"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="plural") == "laetissimi"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="plural") == "laetissimos"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="plural") == "laetissimorum"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="plural") == "laetissimis"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="plural") == "laetissimis"

    assert word.get(degree="superlative", gender="feminine", case="nominative", number="singular") == "laetissima"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="singular") == "laetissima"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="singular") == "laetissimam"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="singular") == "laetissimae"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="singular") == "laetissimae"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="singular") == "laetissima"
    assert word.get(degree="superlative", gender="feminine", case="nominative", number="plural") == "laetissimae"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="plural") == "laetissimae"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="plural") == "laetissimas"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="plural") == "laetissimarum"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="plural") == "laetissimis"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="plural") == "laetissimis"

    assert word.get(degree="superlative", gender="neuter", case="nominative", number="singular") == "laetissimum"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="singular") == "laetissimum"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="singular") == "laetissimum"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="singular") == "laetissimi"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="singular") == "laetissimo"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="singular") == "laetissimo"
    assert word.get(degree="superlative", gender="neuter", case="nominative", number="plural") == "laetissima"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="plural") == "laetissima"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="plural") == "laetissima"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="plural") == "laetissimorum"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="plural") == "laetissimis"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="plural") == "laetissimis"


def test_declension212_irregular():
    word = Adjective("bonus", "bona", "bonum", declension="212", meaning="happy")
    assert word.get(degree="positive", gender="masculine", case="nominative", number="singular") == "bonus"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="singular") == "bone"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="singular") == "bonum"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="singular") == "boni"
    assert word.get(degree="positive", gender="masculine", case="dative", number="singular") == "bono"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="singular") == "bono"
    assert word.get(degree="positive", gender="masculine", case="nominative", number="plural") == "boni"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="plural") == "boni"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="plural") == "bonos"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="plural") == "bonorum"
    assert word.get(degree="positive", gender="masculine", case="dative", number="plural") == "bonis"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="plural") == "bonis"

    assert word.get(degree="positive", gender="feminine", case="nominative", number="singular") == "bona"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="singular") == "bona"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="singular") == "bonam"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="singular") == "bonae"
    assert word.get(degree="positive", gender="feminine", case="dative", number="singular") == "bonae"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="singular") == "bona"
    assert word.get(degree="positive", gender="feminine", case="nominative", number="plural") == "bonae"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="plural") == "bonae"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="plural") == "bonas"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="plural") == "bonarum"
    assert word.get(degree="positive", gender="feminine", case="dative", number="plural") == "bonis"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="plural") == "bonis"

    assert word.get(degree="positive", gender="neuter", case="nominative", number="singular") == "bonum"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="singular") == "bonum"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="singular") == "bonum"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="singular") == "boni"
    assert word.get(degree="positive", gender="neuter", case="dative", number="singular") == "bono"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="singular") == "bono"
    assert word.get(degree="positive", gender="neuter", case="nominative", number="plural") == "bona"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="plural") == "bona"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="plural") == "bona"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="plural") == "bonorum"
    assert word.get(degree="positive", gender="neuter", case="dative", number="plural") == "bonis"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="plural") == "bonis"

    assert word.get(degree="comparative", gender="masculine", case="nominative", number="singular") == "melior"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="singular") == "melior"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="singular") == "meliorem"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="singular") == "melioris"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="singular") == "meliori"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="singular") == "meliore"
    assert word.get(degree="comparative", gender="masculine", case="nominative", number="plural") == "meliores"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="plural") == "meliores"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="plural") == "meliores"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="plural") == "meliorum"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="plural") == "melioribus"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="plural") == "melioribus"

    assert word.get(degree="comparative", gender="feminine", case="nominative", number="singular") == "melior"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="singular") == "melior"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="singular") == "meliorem"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="singular") == "melioris"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="singular") == "meliori"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="singular") == "meliore"
    assert word.get(degree="comparative", gender="feminine", case="nominative", number="plural") == "meliores"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="plural") == "meliores"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="plural") == "meliores"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="plural") == "meliorum"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="plural") == "melioribus"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="plural") == "melioribus"

    assert word.get(degree="comparative", gender="neuter", case="nominative", number="singular") == "melius"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="singular") == "melius"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="singular") == "melius"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="singular") == "melioris"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="singular") == "meliori"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="singular") == "meliore"
    assert word.get(degree="comparative", gender="neuter", case="nominative", number="plural") == "meliora"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="plural") == "meliora"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="plural") == "meliora"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="plural") == "meliorum"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="plural") == "melioribus"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="plural") == "melioribus"

    assert word.get(degree="superlative", gender="masculine", case="nominative", number="singular") == "optimus"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="singular") == "optime"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="singular") == "optimum"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="singular") == "optimi"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="singular") == "optimo"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="singular") == "optimo"
    assert word.get(degree="superlative", gender="masculine", case="nominative", number="plural") == "optimi"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="plural") == "optimi"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="plural") == "optimos"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="plural") == "optimorum"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="plural") == "optimis"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="plural") == "optimis"

    assert word.get(degree="superlative", gender="feminine", case="nominative", number="singular") == "optima"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="singular") == "optima"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="singular") == "optimam"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="singular") == "optimae"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="singular") == "optimae"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="singular") == "optima"
    assert word.get(degree="superlative", gender="feminine", case="nominative", number="plural") == "optimae"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="plural") == "optimae"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="plural") == "optimas"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="plural") == "optimarum"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="plural") == "optimis"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="plural") == "optimis"

    assert word.get(degree="superlative", gender="neuter", case="nominative", number="singular") == "optimum"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="singular") == "optimum"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="singular") == "optimum"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="singular") == "optimi"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="singular") == "optimo"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="singular") == "optimo"
    assert word.get(degree="superlative", gender="neuter", case="nominative", number="plural") == "optima"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="plural") == "optima"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="plural") == "optima"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="plural") == "optimorum"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="plural") == "optimis"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="plural") == "optimis"


def test_declension3_1():
    word = Adjective("egens", "egentis", termination=1, declension="3", meaning="poor")
    assert word.get(degree="positive", gender="masculine", case="nominative", number="singular") == "egens"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="singular") == "egens"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="singular") == "egentem"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="singular") == "egentis"
    assert word.get(degree="positive", gender="masculine", case="dative", number="singular") == "egenti"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="singular") == "egenti"
    assert word.get(degree="positive", gender="masculine", case="nominative", number="plural") == "egentes"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="plural") == "egentes"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="plural") == "egentes"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="plural") == "egentium"
    assert word.get(degree="positive", gender="masculine", case="dative", number="plural") == "egentibus"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="plural") == "egentibus"

    assert word.get(degree="positive", gender="feminine", case="nominative", number="singular") == "egens"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="singular") == "egens"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="singular") == "egentem"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="singular") == "egentis"
    assert word.get(degree="positive", gender="feminine", case="dative", number="singular") == "egenti"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="singular") == "egenti"
    assert word.get(degree="positive", gender="feminine", case="nominative", number="plural") == "egentes"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="plural") == "egentes"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="plural") == "egentes"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="plural") == "egentium"
    assert word.get(degree="positive", gender="feminine", case="dative", number="plural") == "egentibus"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="plural") == "egentibus"

    assert word.get(degree="positive", gender="neuter", case="nominative", number="singular") == "egens"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="singular") == "egens"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="singular") == "egens"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="singular") == "egentis"
    assert word.get(degree="positive", gender="neuter", case="dative", number="singular") == "egenti"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="singular") == "egenti"
    assert word.get(degree="positive", gender="neuter", case="nominative", number="plural") == "egentia"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="plural") == "egentia"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="plural") == "egentia"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="plural") == "egentium"
    assert word.get(degree="positive", gender="neuter", case="dative", number="plural") == "egentibus"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="plural") == "egentibus"

    assert word.get(degree="comparative", gender="masculine", case="nominative", number="singular") == "egentior"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="singular") == "egentior"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="singular") == "egentiorem"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="singular") == "egentioris"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="singular") == "egentiori"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="singular") == "egentiore"
    assert word.get(degree="comparative", gender="masculine", case="nominative", number="plural") == "egentiores"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="plural") == "egentiores"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="plural") == "egentiores"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="plural") == "egentiorum"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="plural") == "egentioribus"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="plural") == "egentioribus"

    assert word.get(degree="comparative", gender="feminine", case="nominative", number="singular") == "egentior"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="singular") == "egentior"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="singular") == "egentiorem"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="singular") == "egentioris"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="singular") == "egentiori"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="singular") == "egentiore"
    assert word.get(degree="comparative", gender="feminine", case="nominative", number="plural") == "egentiores"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="plural") == "egentiores"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="plural") == "egentiores"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="plural") == "egentiorum"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="plural") == "egentioribus"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="plural") == "egentioribus"

    assert word.get(degree="comparative", gender="neuter", case="nominative", number="singular") == "egentius"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="singular") == "egentius"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="singular") == "egentius"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="singular") == "egentioris"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="singular") == "egentiori"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="singular") == "egentiore"
    assert word.get(degree="comparative", gender="neuter", case="nominative", number="plural") == "egentiora"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="plural") == "egentiora"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="plural") == "egentiora"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="plural") == "egentiorum"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="plural") == "egentioribus"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="plural") == "egentioribus"

    assert word.get(degree="superlative", gender="masculine", case="nominative", number="singular") == "egentissimus"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="singular") == "egentissime"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="singular") == "egentissimum"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="singular") == "egentissimi"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="singular") == "egentissimo"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="singular") == "egentissimo"
    assert word.get(degree="superlative", gender="masculine", case="nominative", number="plural") == "egentissimi"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="plural") == "egentissimi"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="plural") == "egentissimos"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="plural") == "egentissimorum"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="plural") == "egentissimis"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="plural") == "egentissimis"

    assert word.get(degree="superlative", gender="feminine", case="nominative", number="singular") == "egentissima"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="singular") == "egentissima"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="singular") == "egentissimam"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="singular") == "egentissimae"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="singular") == "egentissimae"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="singular") == "egentissima"
    assert word.get(degree="superlative", gender="feminine", case="nominative", number="plural") == "egentissimae"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="plural") == "egentissimae"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="plural") == "egentissimas"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="plural") == "egentissimarum"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="plural") == "egentissimis"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="plural") == "egentissimis"

    assert word.get(degree="superlative", gender="neuter", case="nominative", number="singular") == "egentissimum"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="singular") == "egentissimum"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="singular") == "egentissimum"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="singular") == "egentissimi"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="singular") == "egentissimo"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="singular") == "egentissimo"
    assert word.get(degree="superlative", gender="neuter", case="nominative", number="plural") == "egentissima"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="plural") == "egentissima"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="plural") == "egentissima"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="plural") == "egentissimorum"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="plural") == "egentissimis"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="plural") == "egentissimis"


def test_declension3_2():
    word = Adjective("facilis", "facile", termination=2, declension="3", meaning="easy")
    assert word.get(degree="positive", gender="masculine", case="nominative", number="singular") == "facilis"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="singular") == "facilis"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="singular") == "facilem"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="singular") == "facilis"
    assert word.get(degree="positive", gender="masculine", case="dative", number="singular") == "facili"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="singular") == "facili"
    assert word.get(degree="positive", gender="masculine", case="nominative", number="plural") == "faciles"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="plural") == "faciles"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="plural") == "faciles"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="plural") == "facilium"
    assert word.get(degree="positive", gender="masculine", case="dative", number="plural") == "facilibus"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="plural") == "facilibus"

    assert word.get(degree="positive", gender="feminine", case="nominative", number="singular") == "facilis"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="singular") == "facilis"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="singular") == "facilem"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="singular") == "facilis"
    assert word.get(degree="positive", gender="feminine", case="dative", number="singular") == "facili"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="singular") == "facili"
    assert word.get(degree="positive", gender="feminine", case="nominative", number="plural") == "faciles"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="plural") == "faciles"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="plural") == "faciles"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="plural") == "facilium"
    assert word.get(degree="positive", gender="feminine", case="dative", number="plural") == "facilibus"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="plural") == "facilibus"

    assert word.get(degree="positive", gender="neuter", case="nominative", number="singular") == "facile"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="singular") == "facile"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="singular") == "facile"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="singular") == "facilis"
    assert word.get(degree="positive", gender="neuter", case="dative", number="singular") == "facili"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="singular") == "facili"
    assert word.get(degree="positive", gender="neuter", case="nominative", number="plural") == "facilia"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="plural") == "facilia"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="plural") == "facilia"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="plural") == "facilium"
    assert word.get(degree="positive", gender="neuter", case="dative", number="plural") == "facilibus"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="plural") == "facilibus"

    assert word.get(degree="comparative", gender="masculine", case="nominative", number="singular") == "facilior"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="singular") == "facilior"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="singular") == "faciliorem"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="singular") == "facilioris"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="singular") == "faciliori"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="singular") == "faciliore"
    assert word.get(degree="comparative", gender="masculine", case="nominative", number="plural") == "faciliores"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="plural") == "faciliores"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="plural") == "faciliores"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="plural") == "faciliorum"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="plural") == "facilioribus"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="plural") == "facilioribus"

    assert word.get(degree="comparative", gender="feminine", case="nominative", number="singular") == "facilior"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="singular") == "facilior"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="singular") == "faciliorem"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="singular") == "facilioris"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="singular") == "faciliori"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="singular") == "faciliore"
    assert word.get(degree="comparative", gender="feminine", case="nominative", number="plural") == "faciliores"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="plural") == "faciliores"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="plural") == "faciliores"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="plural") == "faciliorum"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="plural") == "facilioribus"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="plural") == "facilioribus"

    assert word.get(degree="comparative", gender="neuter", case="nominative", number="singular") == "facilius"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="singular") == "facilius"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="singular") == "facilius"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="singular") == "facilioris"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="singular") == "faciliori"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="singular") == "faciliore"
    assert word.get(degree="comparative", gender="neuter", case="nominative", number="plural") == "faciliora"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="plural") == "faciliora"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="plural") == "faciliora"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="plural") == "faciliorum"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="plural") == "facilioribus"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="plural") == "facilioribus"

    assert word.get(degree="superlative", gender="masculine", case="nominative", number="singular") == "facillimus"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="singular") == "facillime"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="singular") == "facillimum"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="singular") == "facillimi"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="singular") == "facillimo"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="singular") == "facillimo"
    assert word.get(degree="superlative", gender="masculine", case="nominative", number="plural") == "facillimi"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="plural") == "facillimi"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="plural") == "facillimos"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="plural") == "facillimorum"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="plural") == "facillimis"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="plural") == "facillimis"

    assert word.get(degree="superlative", gender="feminine", case="nominative", number="singular") == "facillima"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="singular") == "facillima"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="singular") == "facillimam"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="singular") == "facillimae"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="singular") == "facillimae"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="singular") == "facillima"
    assert word.get(degree="superlative", gender="feminine", case="nominative", number="plural") == "facillimae"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="plural") == "facillimae"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="plural") == "facillimas"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="plural") == "facillimarum"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="plural") == "facillimis"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="plural") == "facillimis"

    assert word.get(degree="superlative", gender="neuter", case="nominative", number="singular") == "facillimum"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="singular") == "facillimum"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="singular") == "facillimum"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="singular") == "facillimi"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="singular") == "facillimo"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="singular") == "facillimo"
    assert word.get(degree="superlative", gender="neuter", case="nominative", number="plural") == "facillima"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="plural") == "facillima"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="plural") == "facillima"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="plural") == "facillimorum"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="plural") == "facillimis"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="plural") == "facillimis"


def test_declension3_3():
    word = Adjective("celer", "celeris", "celere", termination=3, declension="3", meaning="quick")
    assert word.get(degree="positive", gender="masculine", case="nominative", number="singular") == "celer"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="singular") == "celer"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="singular") == "celerem"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="singular") == "celeris"
    assert word.get(degree="positive", gender="masculine", case="dative", number="singular") == "celeri"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="singular") == "celeri"
    assert word.get(degree="positive", gender="masculine", case="nominative", number="plural") == "celeres"
    assert word.get(degree="positive", gender="masculine", case="vocative", number="plural") == "celeres"
    assert word.get(degree="positive", gender="masculine", case="accusative", number="plural") == "celeres"
    assert word.get(degree="positive", gender="masculine", case="genitive", number="plural") == "celerium"
    assert word.get(degree="positive", gender="masculine", case="dative", number="plural") == "celeribus"
    assert word.get(degree="positive", gender="masculine", case="ablative", number="plural") == "celeribus"

    assert word.get(degree="positive", gender="feminine", case="nominative", number="singular") == "celeris"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="singular") == "celeris"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="singular") == "celerem"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="singular") == "celeris"
    assert word.get(degree="positive", gender="feminine", case="dative", number="singular") == "celeri"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="singular") == "celeri"
    assert word.get(degree="positive", gender="feminine", case="nominative", number="plural") == "celeres"
    assert word.get(degree="positive", gender="feminine", case="vocative", number="plural") == "celeres"
    assert word.get(degree="positive", gender="feminine", case="accusative", number="plural") == "celeres"
    assert word.get(degree="positive", gender="feminine", case="genitive", number="plural") == "celerium"
    assert word.get(degree="positive", gender="feminine", case="dative", number="plural") == "celeribus"
    assert word.get(degree="positive", gender="feminine", case="ablative", number="plural") == "celeribus"

    assert word.get(degree="positive", gender="neuter", case="nominative", number="singular") == "celere"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="singular") == "celere"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="singular") == "celere"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="singular") == "celeris"
    assert word.get(degree="positive", gender="neuter", case="dative", number="singular") == "celeri"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="singular") == "celeri"
    assert word.get(degree="positive", gender="neuter", case="nominative", number="plural") == "celeria"
    assert word.get(degree="positive", gender="neuter", case="vocative", number="plural") == "celeria"
    assert word.get(degree="positive", gender="neuter", case="accusative", number="plural") == "celeria"
    assert word.get(degree="positive", gender="neuter", case="genitive", number="plural") == "celerium"
    assert word.get(degree="positive", gender="neuter", case="dative", number="plural") == "celeribus"
    assert word.get(degree="positive", gender="neuter", case="ablative", number="plural") == "celeribus"

    assert word.get(degree="comparative", gender="masculine", case="nominative", number="singular") == "celerior"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="singular") == "celerior"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="singular") == "celeriorem"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="singular") == "celerioris"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="singular") == "celeriori"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="singular") == "celeriore"
    assert word.get(degree="comparative", gender="masculine", case="nominative", number="plural") == "celeriores"
    assert word.get(degree="comparative", gender="masculine", case="vocative", number="plural") == "celeriores"
    assert word.get(degree="comparative", gender="masculine", case="accusative", number="plural") == "celeriores"
    assert word.get(degree="comparative", gender="masculine", case="genitive", number="plural") == "celeriorum"
    assert word.get(degree="comparative", gender="masculine", case="dative", number="plural") == "celerioribus"
    assert word.get(degree="comparative", gender="masculine", case="ablative", number="plural") == "celerioribus"

    assert word.get(degree="comparative", gender="feminine", case="nominative", number="singular") == "celerior"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="singular") == "celerior"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="singular") == "celeriorem"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="singular") == "celerioris"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="singular") == "celeriori"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="singular") == "celeriore"
    assert word.get(degree="comparative", gender="feminine", case="nominative", number="plural") == "celeriores"
    assert word.get(degree="comparative", gender="feminine", case="vocative", number="plural") == "celeriores"
    assert word.get(degree="comparative", gender="feminine", case="accusative", number="plural") == "celeriores"
    assert word.get(degree="comparative", gender="feminine", case="genitive", number="plural") == "celeriorum"
    assert word.get(degree="comparative", gender="feminine", case="dative", number="plural") == "celerioribus"
    assert word.get(degree="comparative", gender="feminine", case="ablative", number="plural") == "celerioribus"

    assert word.get(degree="comparative", gender="neuter", case="nominative", number="singular") == "celerius"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="singular") == "celerius"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="singular") == "celerius"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="singular") == "celerioris"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="singular") == "celeriori"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="singular") == "celeriore"
    assert word.get(degree="comparative", gender="neuter", case="nominative", number="plural") == "celeriora"
    assert word.get(degree="comparative", gender="neuter", case="vocative", number="plural") == "celeriora"
    assert word.get(degree="comparative", gender="neuter", case="accusative", number="plural") == "celeriora"
    assert word.get(degree="comparative", gender="neuter", case="genitive", number="plural") == "celeriorum"
    assert word.get(degree="comparative", gender="neuter", case="dative", number="plural") == "celerioribus"
    assert word.get(degree="comparative", gender="neuter", case="ablative", number="plural") == "celerioribus"

    assert word.get(degree="superlative", gender="masculine", case="nominative", number="singular") == "celerrimus"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="singular") == "celerrime"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="singular") == "celerrimum"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="singular") == "celerrimi"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="singular") == "celerrimo"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="singular") == "celerrimo"
    assert word.get(degree="superlative", gender="masculine", case="nominative", number="plural") == "celerrimi"
    assert word.get(degree="superlative", gender="masculine", case="vocative", number="plural") == "celerrimi"
    assert word.get(degree="superlative", gender="masculine", case="accusative", number="plural") == "celerrimos"
    assert word.get(degree="superlative", gender="masculine", case="genitive", number="plural") == "celerrimorum"
    assert word.get(degree="superlative", gender="masculine", case="dative", number="plural") == "celerrimis"
    assert word.get(degree="superlative", gender="masculine", case="ablative", number="plural") == "celerrimis"

    assert word.get(degree="superlative", gender="feminine", case="nominative", number="singular") == "celerrima"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="singular") == "celerrima"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="singular") == "celerrimam"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="singular") == "celerrimae"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="singular") == "celerrimae"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="singular") == "celerrima"
    assert word.get(degree="superlative", gender="feminine", case="nominative", number="plural") == "celerrimae"
    assert word.get(degree="superlative", gender="feminine", case="vocative", number="plural") == "celerrimae"
    assert word.get(degree="superlative", gender="feminine", case="accusative", number="plural") == "celerrimas"
    assert word.get(degree="superlative", gender="feminine", case="genitive", number="plural") == "celerrimarum"
    assert word.get(degree="superlative", gender="feminine", case="dative", number="plural") == "celerrimis"
    assert word.get(degree="superlative", gender="feminine", case="ablative", number="plural") == "celerrimis"

    assert word.get(degree="superlative", gender="neuter", case="nominative", number="singular") == "celerrimum"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="singular") == "celerrimum"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="singular") == "celerrimum"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="singular") == "celerrimi"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="singular") == "celerrimo"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="singular") == "celerrimo"
    assert word.get(degree="superlative", gender="neuter", case="nominative", number="plural") == "celerrima"
    assert word.get(degree="superlative", gender="neuter", case="vocative", number="plural") == "celerrima"
    assert word.get(degree="superlative", gender="neuter", case="accusative", number="plural") == "celerrima"
    assert word.get(degree="superlative", gender="neuter", case="genitive", number="plural") == "celerrimorum"
    assert word.get(degree="superlative", gender="neuter", case="dative", number="plural") == "celerrimis"
    assert word.get(degree="superlative", gender="neuter", case="ablative", number="plural") == "celerrimis"

def test_adverb1():
    word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    assert word.get(degree="positive", adverb=True) == "laete"
    assert word.get(degree="comparative", adverb=True) == "laetius"
    assert word.get(degree="superlative", adverb=True) == "laetissime"

def test_adverb2():
    word = Adjective("prudens", "prudentis", termination=1, declension="3", meaning="wise")
    assert word.get(degree="positive", adverb=True) == "prudenter"
    assert word.get(degree="comparative", adverb=True) == "prudentius"
    assert word.get(degree="superlative", adverb=True) == "prudentissime"

def test_adverb3():
    word = Adjective("fortis", "forte", termination=2, declension="3", meaning="strong")
    assert word.get(degree="positive", adverb=True) == "fortiter"
    assert word.get(degree="comparative", adverb=True) == "fortius"
    assert word.get(degree="superlative", adverb=True) == "fortissime"

def test_adverb4():
    word = Adjective("celer", "celeris", "celere", termination=3, declension="3", meaning="quick")
    assert word.get(degree="positive", adverb=True) == "celeriter"
    assert word.get(degree="comparative", adverb=True) == "celerius"
    assert word.get(degree="superlative", adverb=True) == "celerrime"

def test_irregularadverb1():
    word = Adjective("bonus", "bona", "bonum", declension="212", meaning="happy")
    assert word.get(degree="positive", adverb=True) == "bene"
    assert word.get(degree="comparative", adverb=True) == "melius"
    assert word.get(degree="superlative", adverb=True) == "optime"

def test_irregularadverb2():
    word = Adjective("bonus", "bonis", declension="3", termination=1, meaning="happy")
    assert word.get(degree="positive", adverb=True) == "bene"
    assert word.get(degree="comparative", adverb=True) == "melius"
    assert word.get(degree="superlative", adverb=True) == "optime"

def test_irregularadverb3():
    word = Adjective("bonus", "bona", declension="3", termination=2, meaning="happy")
    assert word.get(degree="positive", adverb=True) == "bene"
    assert word.get(degree="comparative", adverb=True) == "melius"
    assert word.get(degree="superlative", adverb=True) == "optime"

def test_irregularadverb4():
    word = Adjective("bonus", "bona", "bonum", declension="3", termination=3, meaning="happy")
    assert word.get(degree="positive", adverb=True) == "bene"
    assert word.get(degree="comparative", adverb=True) == "melius"
    assert word.get(degree="superlative", adverb=True) == "optime"
