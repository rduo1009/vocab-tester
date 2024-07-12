import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grammatica.endings import Noun


def test_repr():
    word = Noun(nom="puer", gen="pueri", gender="m", meaning="boy")
    assert word.__repr__() == "Noun(puer, pueri, m, boy)"


def test_eq():
    word1 = Noun(nom="puer", gen="pueri", gender="m", meaning="boy")
    word2 = Noun(nom="puer", gen="pueri", gender="m", meaning="boy")
    assert word1 == word2


def test_lt():
    word1 = Noun(nom="puer", gen="pueri", gender="m", meaning="boy")
    word2 = Noun(nom="apuer", gen="pueri", gender="m", meaning="boy")
    # word2 must be smaller than word1 as word1.first = "puer" and word2.first = "apuer"
    assert word1 > word2


def test_gender():
    word1 = Noun(nom="puer", gen="pueri", gender="m", meaning="boy")
    word2 = Noun(nom="puer", gen="pueri", gender="masculine", meaning="boy")
    assert word1 == word2


def test_firstdeclension():
    word = Noun(nom="ancilla", gen="ancillae", gender="f", meaning="slavegirl")
    assert word.get("nominative", "singular") == "ancilla"
    assert word.get("vocative", "singular") == "ancilla"
    assert word.get("accusative", "singular") == "ancillam"
    assert word.get("genitive", "singular") == "ancillae"
    assert word.get("dative", "singular") == "ancillae"
    assert word.get("ablative", "singular") == "ancilla"
    assert word.get("nominative", "plural") == "ancillae"
    assert word.get("vocative", "plural") == "ancillae"
    assert word.get("accusative", "plural") == "ancillas"
    assert word.get("genitive", "plural") == "ancillarum"
    assert word.get("dative", "plural") == "ancillis"
    assert word.get("ablative", "plural") == "ancillis"


def test_seconddeclension1():
    word = Noun(nom="servus", gen="servi", gender="m", meaning="slave")
    assert word.get("nominative", "singular") == "servus"
    assert word.get("vocative", "singular") == "serve"
    assert word.get("accusative", "singular") == "servum"
    assert word.get("genitive", "singular") == "servi"
    assert word.get("dative", "singular") == "servo"
    assert word.get("ablative", "singular") == "servo"
    assert word.get("nominative", "plural") == "servi"
    assert word.get("vocative", "plural") == "servi"
    assert word.get("accusative", "plural") == "servos"
    assert word.get("genitive", "plural") == "servorum"
    assert word.get("dative", "plural") == "servis"
    assert word.get("ablative", "plural") == "servis"


def test_seconddeclension2():
    word = Noun(nom="puer", gen="pueri", gender="m", meaning="boy")
    assert word.get("nominative", "singular") == "puer"
    assert word.get("vocative", "singular") == "puer"
    assert word.get("accusative", "singular") == "puerum"
    assert word.get("genitive", "singular") == "pueri"
    assert word.get("dative", "singular") == "puero"
    assert word.get("ablative", "singular") == "puero"
    assert word.get("nominative", "plural") == "pueri"
    assert word.get("vocative", "plural") == "pueri"
    assert word.get("accusative", "plural") == "pueros"
    assert word.get("genitive", "plural") == "puerorum"
    assert word.get("dative", "plural") == "pueris"
    assert word.get("ablative", "plural") == "pueris"


def test_thirddeclension():
    word = Noun(nom="carcer", gen="carceris", gender="m", meaning="prison")
    assert word.get("nominative", "singular") == "carcer"
    assert word.get("vocative", "singular") == "carcer"
    assert word.get("accusative", "singular") == "carcerem"
    assert word.get("genitive", "singular") == "carceris"
    assert word.get("dative", "singular") == "carceri"
    assert word.get("ablative", "singular") == "carcere"
    assert word.get("nominative", "plural") == "carceres"
    assert word.get("vocative", "plural") == "carceres"
    assert word.get("accusative", "plural") == "carceres"
    assert word.get("genitive", "plural") == "carcerum"
    assert word.get("dative", "plural") == "carceribus"
    assert word.get("ablative", "plural") == "carceribus"


def test_seconddeclension_neuter():
    word = Noun(nom="templum", gen="templi", gender="n", meaning="temple")
    assert word.get("nominative", "singular") == "templum"
    assert word.get("vocative", "singular") == "templum"
    assert word.get("accusative", "singular") == "templum"
    assert word.get("genitive", "singular") == "templi"
    assert word.get("dative", "singular") == "templo"
    assert word.get("ablative", "singular") == "templo"
    assert word.get("nominative", "plural") == "templa"
    assert word.get("vocative", "plural") == "templa"
    assert word.get("accusative", "plural") == "templa"
    assert word.get("genitive", "plural") == "templorum"
    assert word.get("dative", "plural") == "templis"
    assert word.get("ablative", "plural") == "templis"


def test_thirddeclension_neuter():
    word = Noun(nom="litus", gen="litoris", gender="n", meaning="beach")
    assert word.get("nominative", "singular") == "litus"
    assert word.get("vocative", "singular") == "litus"
    assert word.get("accusative", "singular") == "litus"
    assert word.get("genitive", "singular") == "litoris"
    assert word.get("dative", "singular") == "litori"
    assert word.get("ablative", "singular") == "litore"
    assert word.get("nominative", "plural") == "litora"
    assert word.get("vocative", "plural") == "litora"
    assert word.get("accusative", "plural") == "litora"
    assert word.get("genitive", "plural") == "litorum"
    assert word.get("dative", "plural") == "litoribus"
    assert word.get("ablative", "plural") == "litoribus"
