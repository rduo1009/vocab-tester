import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


import pytest

from python_src.accido.exceptions import InvalidInputError  # isort: skip
from python_src.accido.endings import Noun
from python_src.accido.misc import Case, EndingComponents, Gender, Number
from python_src.utils import compare


class TestNounErrors:
    def test_errors_invalid_genitive(self):
        with pytest.raises(InvalidInputError) as error:
            Noun(nominative="puer", genitive="error", gender=Gender.MASCULINE, meaning="boy")
        assert "Invalid genitive form: 'error'" == str(error.value)

    def test_errors_fifth_declension_neuter(self):
        with pytest.raises(InvalidInputError) as error:
            Noun(nominative="puer", genitive="puerei", gender=Gender.NEUTER, meaning="boy")
        assert "Fifth declension nouns cannot be neuter (noun 'puer' given)" == str(error.value)


class TestNounDunder:
    def test_repr(self):
        word = Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy")
        assert word.__repr__() == "Noun(puer, pueri, masculine, boy)"

    def test_eq(self):
        word1 = Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy")
        word2 = Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy")
        assert word1 == word2

    def test_lt(self):
        word1 = Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy")
        word2 = Noun(nominative="apuer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy")
        # word2 must be smaller than word1 as word1.first = "puer" and word2.first = "apuer"
        assert word1 > word2

    def test_find(self):
        word = Noun(nominative="ancilla", genitive="ancillae", gender=Gender.FEMININE, meaning="slavegirl")
        assert compare(word.find("ancilla"),
            [EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, string="nominative singular"),
                EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR, string="vocative singular"),
                    EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR, string="ablative singular")])  # fmt: skip

    def test_str_masculine(self):
        word = Noun(nominative="servus", genitive="servi", gender=Gender.MASCULINE, meaning="slave")
        assert word.__str__() == "slave: servus, servi, (m)"

    def test_str_feminine(self):
        word = Noun(nominative="ancilla", genitive="ancillae", gender=Gender.FEMININE, meaning="slavegirl")
        assert word.__str__() == "slavegirl: ancilla, ancillae, (f)"

    def test_str_neuter(self):
        word = Noun(nominative="templum", genitive="templi", gender=Gender.NEUTER, meaning="temple")
        assert word.__str__() == "temple: templum, templi, (n)"


class TestNounDeclension:
    def test_firstdeclension(self):
        word = Noun(nominative="ancilla", genitive="ancillae", gender=Gender.FEMININE, meaning="slavegirl")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "ancilla"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "ancilla"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "ancillam"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "ancillae"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "ancillae"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "ancilla"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "ancillae"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "ancillae"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "ancillas"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "ancillarum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "ancillis"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "ancillis"

    def test_seconddeclension_regular(self):
        word = Noun(nominative="servus", genitive="servi", gender=Gender.MASCULINE, meaning="slave")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "servus"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "serve"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "servum"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "servi"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "servo"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "servo"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "servi"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "servi"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "servos"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "servorum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "servis"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "servis"

    def test_seconddeclension_endinginr(self):
        word = Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "puer"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "puer"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "puerum"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "pueri"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "puero"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "puero"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "pueri"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "pueri"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "pueros"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "puerorum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "pueris"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "pueris"

    def test_thirddeclension(self):
        word = Noun(nominative="carcer", genitive="carceris", gender=Gender.MASCULINE, meaning="prison")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "carcer"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "carcer"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "carcerem"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "carceris"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "carceri"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "carcere"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "carceres"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "carceres"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "carceres"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "carcerum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "carceribus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "carceribus"

    def test_fourthdeclension(self):
        word = Noun(nominative="manus", genitive="manus", gender=Gender.FEMININE, meaning="hand")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "manus"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "manus"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "manum"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "manus"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "manui"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "manu"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "manus"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "manus"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "manus"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "manuum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "manibus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "manibus"

    def test_fifthdeclension(self):
        word = Noun(nominative="res", genitive="rei", gender=Gender.FEMININE, meaning="thing")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "res"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "res"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "rem"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "rei"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "rei"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "re"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "res"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "res"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "res"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "rerum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "rebus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "rebus"


class TestNounNeuter:
    def test_seconddeclension(self):
        word = Noun(nominative="templum", genitive="templi", gender=Gender.NEUTER, meaning="temple")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "templum"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "templum"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "templum"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "templi"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "templo"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "templo"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "templa"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "templa"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "templa"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "templorum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "templis"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "templis"

    def test_thirddeclension(self):
        word = Noun(nominative="litus", genitive="litoris", gender=Gender.NEUTER, meaning="beach")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "litus"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "litus"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "litus"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "litoris"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "litori"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "litore"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "litora"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "litora"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "litora"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "litorum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "litoribus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "litoribus"

    def test_fourthdeclension(self):
        word = Noun(nominative="cornu", genitive="cornus", gender=Gender.NEUTER, meaning="horn")
        assert word.get(case=Case.NOMINATIVE, number=Number.SINGULAR) == "cornu"
        assert word.get(case=Case.VOCATIVE, number=Number.SINGULAR) == "cornu"
        assert word.get(case=Case.ACCUSATIVE, number=Number.SINGULAR) == "cornu"
        assert word.get(case=Case.GENITIVE, number=Number.SINGULAR) == "cornus"
        assert word.get(case=Case.DATIVE, number=Number.SINGULAR) == "cornu"
        assert word.get(case=Case.ABLATIVE, number=Number.SINGULAR) == "cornu"
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "cornua"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "cornua"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "cornua"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "cornuum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "cornibus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "cornibus"


class TestNounPluraleTantum:
    def test_firstdeclension(self):
        word = Noun(nominative="ancillae", genitive="ancillarum", gender=Gender.FEMININE, meaning="slavegirls")
        assert word.declension == 1
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "ancillae"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "ancillae"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "ancillas"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "ancillarum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "ancillis"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "ancillis"

    def test_seconddeclension(self):
        word = Noun(nominative="servi", genitive="servorum", gender=Gender.MASCULINE, meaning="slaves")
        assert word.declension == 2
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "servi"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "servi"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "servos"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "servorum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "servis"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "servis"

    def test_thirddeclension(self):
        word = Noun(nominative="carceres", genitive="carcerum", gender=Gender.MASCULINE, meaning="prisons")
        assert word.declension == 3
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "carceres"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "carceres"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "carceres"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "carcerum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "carceribus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "carceribus"

    def test_fourthdeclension(self):
        word = Noun(nominative="manus", genitive="manuum", gender=Gender.FEMININE, meaning="hands")
        assert word.declension == 4
        assert word.get(case=Case.NOMINATIVE, number=Number.PLURAL) == "manus"
        assert word.get(case=Case.VOCATIVE, number=Number.PLURAL) == "manus"
        assert word.get(case=Case.ACCUSATIVE, number=Number.PLURAL) == "manus"
        assert word.get(case=Case.GENITIVE, number=Number.PLURAL) == "manuum"
        assert word.get(case=Case.DATIVE, number=Number.PLURAL) == "manibus"
        assert word.get(case=Case.ABLATIVE, number=Number.PLURAL) == "manibus"
