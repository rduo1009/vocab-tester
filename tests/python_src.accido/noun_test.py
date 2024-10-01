import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from types import SimpleNamespace

import pytest

from python_src.accido.exceptions import InvalidInputError  # isort: skip
from python_src.accido.endings import Noun
from python_src.utils import compare


class TestNounErrors:
    def test_errors_invalid_gender(self):
        with pytest.raises(InvalidInputError) as error:
            Noun(nominative="puer", genitive="pueri", gender="error", meaning="boy")
        assert "Invalid gender: 'error'" == str(error.value)

    def test_errors_invalid_genitive(self):
        with pytest.raises(InvalidInputError) as error:
            Noun(nominative="puer", genitive="error", gender="masculine", meaning="boy")
        assert "Invalid genitive form: 'error'" == str(error.value)

    def test_errors_fifth_declension_neuter(self):
        with pytest.raises(InvalidInputError) as error:
            Noun(nominative="puer", genitive="puerei", gender="neuter", meaning="boy")
        assert "Fifth declension nouns cannot be neuter (noun 'puer' given)" == str(error.value)

    def test_errors_invalid_case(self):
        with pytest.raises(InvalidInputError) as error:
            word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
            word.get(case="error", number="singular")
        assert "Invalid case: 'error'" == str(error.value)

    def test_errors_invalid_number(self):
        with pytest.raises(InvalidInputError) as error:
            word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
            word.get(case="nominative", number="error")
        assert "Invalid number: 'error'" == str(error.value)


class TestNounDunder:
    def test_repr(self):
        word = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
        assert word.__repr__() == "Noun(puer, pueri, masculine, boy)"

    def test_eq(self):
        word1 = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
        word2 = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
        assert word1 == word2

    def test_lt(self):
        word1 = Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy")
        word2 = Noun(nominative="apuer", genitive="pueri", gender="masculine", meaning="boy")
        # word2 must be smaller than word1 as word1.first = "puer" and word2.first = "apuer"
        assert word1 > word2

    def test_find(self):
        word = Noun(nominative="ancilla", genitive="ancillae", gender="feminine", meaning="slavegirl")
        assert compare(word.find("ancilla"),
            [SimpleNamespace(case="nominative", number="singular", string="nominative singular"),
                SimpleNamespace(case="vocative", number="singular", string="vocative singular"),
                    SimpleNamespace(case="ablative", number="singular", string="ablative singular")])  # fmt: skip

    def test_str_masculine(self):
        word = Noun(nominative="servus", genitive="servi", gender="masculine", meaning="slave")
        assert word.__str__() == "slave: servus, servi, (m)"

    def test_str_feminine(self):
        word = Noun(nominative="ancilla", genitive="ancillae", gender="feminine", meaning="slavegirl")
        assert word.__str__() == "slavegirl: ancilla, ancillae, (f)"

    def test_str_neuter(self):
        word = Noun(nominative="templum", genitive="templi", gender="neuter", meaning="temple")
        assert word.__str__() == "temple: templum, templi, (n)"


class TestNounDeclension:
    def test_firstdeclension(self):
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

    def test_seconddeclension_regular(self):
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

    def test_seconddeclension_endinginr(self):
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

    def test_thirddeclension(self):
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

    def test_fourthdeclension(self):
        word = Noun(nominative="manus", genitive="manus", gender="feminine", meaning="hand")
        assert word.get(case="nominative", number="singular") == "manus"
        assert word.get(case="vocative", number="singular") == "manus"
        assert word.get(case="accusative", number="singular") == "manum"
        assert word.get(case="genitive", number="singular") == "manus"
        assert word.get(case="dative", number="singular") == "manui"
        assert word.get(case="ablative", number="singular") == "manu"
        assert word.get(case="nominative", number="plural") == "manus"
        assert word.get(case="vocative", number="plural") == "manus"
        assert word.get(case="accusative", number="plural") == "manus"
        assert word.get(case="genitive", number="plural") == "manuum"
        assert word.get(case="dative", number="plural") == "manibus"
        assert word.get(case="ablative", number="plural") == "manibus"

    def test_fifthdeclension(self):
        word = Noun(nominative="res", genitive="rei", gender="feminine", meaning="thing")
        assert word.get(case="nominative", number="singular") == "res"
        assert word.get(case="vocative", number="singular") == "res"
        assert word.get(case="accusative", number="singular") == "rem"
        assert word.get(case="genitive", number="singular") == "rei"
        assert word.get(case="dative", number="singular") == "rei"
        assert word.get(case="ablative", number="singular") == "re"
        assert word.get(case="nominative", number="plural") == "res"
        assert word.get(case="vocative", number="plural") == "res"
        assert word.get(case="accusative", number="plural") == "res"
        assert word.get(case="genitive", number="plural") == "rerum"
        assert word.get(case="dative", number="plural") == "rebus"
        assert word.get(case="ablative", number="plural") == "rebus"


class TestNounNeuter:
    def test_seconddeclension(self):
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

    def test_thirddeclension(self):
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

    def test_fourthdeclension(self):
        word = Noun(nominative="cornu", genitive="cornus", gender="neuter", meaning="horn")
        assert word.get(case="nominative", number="singular") == "cornu"
        assert word.get(case="vocative", number="singular") == "cornu"
        assert word.get(case="accusative", number="singular") == "cornu"
        assert word.get(case="genitive", number="singular") == "cornus"
        assert word.get(case="dative", number="singular") == "cornu"
        assert word.get(case="ablative", number="singular") == "cornu"
        assert word.get(case="nominative", number="plural") == "cornua"
        assert word.get(case="vocative", number="plural") == "cornua"
        assert word.get(case="accusative", number="plural") == "cornua"
        assert word.get(case="genitive", number="plural") == "cornuum"
        assert word.get(case="dative", number="plural") == "cornibus"
        assert word.get(case="ablative", number="plural") == "cornibus"


class TestNounPluraleTantum:
    def test_firstdeclension(self):
        word = Noun(nominative="ancillae", genitive="ancillarum", gender="feminine", meaning="slavegirls")
        assert word.declension == 1
        assert word.get(case="nominative", number="plural") == "ancillae"
        assert word.get(case="vocative", number="plural") == "ancillae"
        assert word.get(case="accusative", number="plural") == "ancillas"
        assert word.get(case="genitive", number="plural") == "ancillarum"
        assert word.get(case="dative", number="plural") == "ancillis"
        assert word.get(case="ablative", number="plural") == "ancillis"

    def test_seconddeclension(self):
        word = Noun(nominative="servi", genitive="servorum", gender="masculine", meaning="slaves")
        assert word.declension == 2
        assert word.get(case="nominative", number="plural") == "servi"
        assert word.get(case="vocative", number="plural") == "servi"
        assert word.get(case="accusative", number="plural") == "servos"
        assert word.get(case="genitive", number="plural") == "servorum"
        assert word.get(case="dative", number="plural") == "servis"
        assert word.get(case="ablative", number="plural") == "servis"

    def test_thirddeclension(self):
        word = Noun(nominative="carceres", genitive="carcerum", gender="masculine", meaning="prisons")
        assert word.declension == 3
        assert word.get(case="nominative", number="plural") == "carceres"
        assert word.get(case="vocative", number="plural") == "carceres"
        assert word.get(case="accusative", number="plural") == "carceres"
        assert word.get(case="genitive", number="plural") == "carcerum"
        assert word.get(case="dative", number="plural") == "carceribus"
        assert word.get(case="ablative", number="plural") == "carceribus"

    def test_fourthdeclension(self):
        word = Noun(nominative="manus", genitive="manuum", gender="feminine", meaning="hands")
        assert word.declension == 4
        assert word.get(case="nominative", number="plural") == "manus"
        assert word.get(case="vocative", number="plural") == "manus"
        assert word.get(case="accusative", number="plural") == "manus"
        assert word.get(case="genitive", number="plural") == "manuum"
        assert word.get(case="dative", number="plural") == "manibus"
        assert word.get(case="ablative", number="plural") == "manibus"
