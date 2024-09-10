import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


import pytest  # type: ignore

from python_src.accido.exceptions import InvalidInputError  # isort: skip
from python_src.accido.endings import Adjective
from python_src.accido.misc import EndingComponents
from python_src.utils import compare


class TestAdjectiveErrors:
    def test_errors_termination_with_212(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy", termination=3)
        assert "2-1-2 adjectives cannot have a termination (termination '3' given)" == str(error.value)

    def test_errors_wrong_number_principal_parts_212(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", declension="212", meaning="happy")
        assert "2-1-2 adjectives must have 3 principal parts (adjective 'laetus' given)" == str(error.value)

    def test_errors_wrong_number_principal_parts_31(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", "laetum", declension="3", meaning="happy", termination=1)
        assert "First-termination adjectives must have 2 principal parts (adjective 'laetus' given)" == str(error.value)

    def test_errors_invalid_genitive(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", declension="3", meaning="happy", termination=1)
        assert "Invalid genitive form: 'laeta' (must end in '-is')" == str(error.value)

    def test_errors_wrong_number_principal_parts_32(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", "laetum", declension="3", meaning="happy", termination=2)
        assert "Second-termination adjectives must have 2 principal parts (adjective 'laetus' given)" == str(error.value)

    def test_errors_wrong_number_principal_parts_33(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", declension="3", meaning="happy", termination=3)
        assert "Third-termination adjectives must have 3 principal parts (adjective 'laetus' given)" == str(error.value)

    def test_errors_invalid_termination(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", declension="3", meaning="happy", termination=7)
        assert "Termination must be 1, 2 or 3 (given '7')" == str(error.value)

    def test_errors_invalid_declension(self):
        with pytest.raises(InvalidInputError) as error:
            Adjective("laetus", "laeta", "laetum", declension="4", meaning="happy", termination=3)
        assert "Invalid declension: '4'" == str(error.value)

    def test_errors_adverbs_donothave(self):
        with pytest.raises(InvalidInputError) as error:
            word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
            word.get(case="nominative", gender="masculine", number="singular", degree="adgsf", adverb=True)
        assert "Adverbs do not have gender, case or number (given 'masculine', 'nominative' and 'singular')" == str(error.value)

    def test_errors_invalid_degree_adverb(self):
        with pytest.raises(InvalidInputError) as error:
            word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
            word.get(degree="error", adverb=True)
        assert "Invalid degree: 'error'" == str(error.value)

    def test_errors_invalid_degree_normal(self):
        with pytest.raises(InvalidInputError) as error:
            word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
            word.get(case="nominative", gender="masculine", number="singular", degree="error")
        assert "Invalid degree: 'error'" == str(error.value)

    def test_errors_invalid_case(self):
        with pytest.raises(InvalidInputError) as error:
            word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
            word.get(case="error", gender="masculine", number="singular", degree="positive")
        assert "Invalid case: 'error'" == str(error.value)

    def test_errors_invalid_gender(self):
        with pytest.raises(InvalidInputError) as error:
            word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
            word.get(case="nominative", gender="error", number="singular", degree="positive")
        assert "Invalid gender: 'error'" == str(error.value)

    def test_errors_invalid_number(self):
        with pytest.raises(InvalidInputError) as error:
            word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
            word.get(case="nominative", gender="masculine", number="error", degree="positive")
        assert "Invalid number: 'error'" == str(error.value)


class TestAdjectiveDunder:
    def test_repr(self):
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        assert word.__repr__() == "Adjective(laetus, laeta, laetum, None, 212, happy)"

    def test_eq(self):
        word1 = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        word2 = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        assert word1 == word2

    def test_lt(self):
        word1 = Adjective("aalaetus", "laeta", "laetum", declension="212", meaning="happy")
        word2 = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        assert word1 < word2

    def test_find(self):
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")

        assert compare(
            word.find("laeta"),
            [
                EndingComponents(degree="positive", gender="feminine", case="nominative", number="singular", string="positive nominative singular feminine"),
                EndingComponents(degree="positive", gender="feminine", case="vocative", number="singular", string="positive vocative singular feminine"),
                EndingComponents(degree="positive", gender="feminine", case="ablative", number="singular", string="positive ablative singular feminine"),
                EndingComponents(degree="positive", gender="neuter", case="nominative", number="plural", string="positive nominative plural neuter"),
                EndingComponents(degree="positive", gender="neuter", case="vocative", number="plural", string="positive vocative plural neuter"),
                EndingComponents(degree="positive", gender="neuter", case="accusative", number="plural", string="positive accusative plural neuter"),
            ],
        )

        assert compare(word.find("laete"), [EndingComponents(degree="positive", gender="masculine", case="vocative", number="singular", string="positive vocative singular masculine"), EndingComponents(degree="positive", string="positive")])

    def test_str_212(self):
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        assert word.__str__() == "happy: laetus, laeta, laetum, (2-1-2)"

    def test_str_31(self):
        word = Adjective("egens", "egentis", termination=1, declension="3", meaning="poor")
        assert word.__str__() == "poor: egens, egentis, (3-1)"

    def test_str_32(self):
        word = Adjective("facilis", "facile", termination=2, declension="3", meaning="easy")
        assert word.__str__() == "easy: facilis, facile, (3-2)"

    def test_str_33(self):
        word = Adjective("celer", "celeris", "celere", termination=3, declension="3", meaning="quick")
        assert word.__str__() == "quick: celer, celeris, celere, (3-3)"


class TestAdjectiveDeclension:
    def test_declension212(self):
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

    def test_declension212_irregular(self):
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

    def test_declension3_1_regular(self):
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

    def test_declension3_1_with_rr(self):
        word = Adjective("uber", "uberis", termination=1, declension="3", meaning="fruitful")

        assert word.get(degree="positive", gender="masculine", case="nominative", number="singular") == "uber"
        assert word.get(degree="positive", gender="masculine", case="vocative", number="singular") == "uber"
        assert word.get(degree="positive", gender="masculine", case="accusative", number="singular") == "uberem"
        assert word.get(degree="positive", gender="masculine", case="genitive", number="singular") == "uberis"
        assert word.get(degree="positive", gender="masculine", case="dative", number="singular") == "uberi"
        assert word.get(degree="positive", gender="masculine", case="ablative", number="singular") == "uberi"
        assert word.get(degree="positive", gender="masculine", case="nominative", number="plural") == "uberes"
        assert word.get(degree="positive", gender="masculine", case="vocative", number="plural") == "uberes"
        assert word.get(degree="positive", gender="masculine", case="accusative", number="plural") == "uberes"
        assert word.get(degree="positive", gender="masculine", case="genitive", number="plural") == "uberium"
        assert word.get(degree="positive", gender="masculine", case="dative", number="plural") == "uberibus"
        assert word.get(degree="positive", gender="masculine", case="ablative", number="plural") == "uberibus"

        assert word.get(degree="positive", gender="feminine", case="nominative", number="singular") == "uber"
        assert word.get(degree="positive", gender="feminine", case="vocative", number="singular") == "uber"
        assert word.get(degree="positive", gender="feminine", case="accusative", number="singular") == "uberem"
        assert word.get(degree="positive", gender="feminine", case="genitive", number="singular") == "uberis"
        assert word.get(degree="positive", gender="feminine", case="dative", number="singular") == "uberi"
        assert word.get(degree="positive", gender="feminine", case="ablative", number="singular") == "uberi"
        assert word.get(degree="positive", gender="feminine", case="nominative", number="plural") == "uberes"
        assert word.get(degree="positive", gender="feminine", case="vocative", number="plural") == "uberes"
        assert word.get(degree="positive", gender="feminine", case="accusative", number="plural") == "uberes"
        assert word.get(degree="positive", gender="feminine", case="genitive", number="plural") == "uberium"
        assert word.get(degree="positive", gender="feminine", case="dative", number="plural") == "uberibus"
        assert word.get(degree="positive", gender="feminine", case="ablative", number="plural") == "uberibus"

        assert word.get(degree="positive", gender="neuter", case="nominative", number="singular") == "uber"
        assert word.get(degree="positive", gender="neuter", case="vocative", number="singular") == "uber"
        assert word.get(degree="positive", gender="neuter", case="accusative", number="singular") == "uber"
        assert word.get(degree="positive", gender="neuter", case="genitive", number="singular") == "uberis"
        assert word.get(degree="positive", gender="neuter", case="dative", number="singular") == "uberi"
        assert word.get(degree="positive", gender="neuter", case="ablative", number="singular") == "uberi"
        assert word.get(degree="positive", gender="neuter", case="nominative", number="plural") == "uberia"
        assert word.get(degree="positive", gender="neuter", case="vocative", number="plural") == "uberia"
        assert word.get(degree="positive", gender="neuter", case="accusative", number="plural") == "uberia"
        assert word.get(degree="positive", gender="neuter", case="genitive", number="plural") == "uberium"
        assert word.get(degree="positive", gender="neuter", case="dative", number="plural") == "uberibus"
        assert word.get(degree="positive", gender="neuter", case="ablative", number="plural") == "uberibus"

        assert word.get(degree="comparative", gender="masculine", case="nominative", number="singular") == "uberior"
        assert word.get(degree="comparative", gender="masculine", case="vocative", number="singular") == "uberior"
        assert word.get(degree="comparative", gender="masculine", case="accusative", number="singular") == "uberiorem"
        assert word.get(degree="comparative", gender="masculine", case="genitive", number="singular") == "uberioris"
        assert word.get(degree="comparative", gender="masculine", case="dative", number="singular") == "uberiori"
        assert word.get(degree="comparative", gender="masculine", case="ablative", number="singular") == "uberiore"
        assert word.get(degree="comparative", gender="masculine", case="nominative", number="plural") == "uberiores"
        assert word.get(degree="comparative", gender="masculine", case="vocative", number="plural") == "uberiores"
        assert word.get(degree="comparative", gender="masculine", case="accusative", number="plural") == "uberiores"
        assert word.get(degree="comparative", gender="masculine", case="genitive", number="plural") == "uberiorum"
        assert word.get(degree="comparative", gender="masculine", case="dative", number="plural") == "uberioribus"
        assert word.get(degree="comparative", gender="masculine", case="ablative", number="plural") == "uberioribus"

        assert word.get(degree="comparative", gender="feminine", case="nominative", number="singular") == "uberior"
        assert word.get(degree="comparative", gender="feminine", case="vocative", number="singular") == "uberior"
        assert word.get(degree="comparative", gender="feminine", case="accusative", number="singular") == "uberiorem"
        assert word.get(degree="comparative", gender="feminine", case="genitive", number="singular") == "uberioris"
        assert word.get(degree="comparative", gender="feminine", case="dative", number="singular") == "uberiori"
        assert word.get(degree="comparative", gender="feminine", case="ablative", number="singular") == "uberiore"
        assert word.get(degree="comparative", gender="feminine", case="nominative", number="plural") == "uberiores"
        assert word.get(degree="comparative", gender="feminine", case="vocative", number="plural") == "uberiores"
        assert word.get(degree="comparative", gender="feminine", case="accusative", number="plural") == "uberiores"
        assert word.get(degree="comparative", gender="feminine", case="genitive", number="plural") == "uberiorum"
        assert word.get(degree="comparative", gender="feminine", case="dative", number="plural") == "uberioribus"
        assert word.get(degree="comparative", gender="feminine", case="ablative", number="plural") == "uberioribus"

        assert word.get(degree="comparative", gender="neuter", case="nominative", number="singular") == "uberius"
        assert word.get(degree="comparative", gender="neuter", case="vocative", number="singular") == "uberius"
        assert word.get(degree="comparative", gender="neuter", case="accusative", number="singular") == "uberius"
        assert word.get(degree="comparative", gender="neuter", case="genitive", number="singular") == "uberioris"
        assert word.get(degree="comparative", gender="neuter", case="dative", number="singular") == "uberiori"
        assert word.get(degree="comparative", gender="neuter", case="ablative", number="singular") == "uberiore"
        assert word.get(degree="comparative", gender="neuter", case="nominative", number="plural") == "uberiora"
        assert word.get(degree="comparative", gender="neuter", case="vocative", number="plural") == "uberiora"
        assert word.get(degree="comparative", gender="neuter", case="accusative", number="plural") == "uberiora"
        assert word.get(degree="comparative", gender="neuter", case="genitive", number="plural") == "uberiorum"
        assert word.get(degree="comparative", gender="neuter", case="dative", number="plural") == "uberioribus"
        assert word.get(degree="comparative", gender="neuter", case="ablative", number="plural") == "uberioribus"

        assert word.get(degree="superlative", gender="masculine", case="nominative", number="singular") == "uberrimus"
        assert word.get(degree="superlative", gender="masculine", case="vocative", number="singular") == "uberrime"
        assert word.get(degree="superlative", gender="masculine", case="accusative", number="singular") == "uberrimum"
        assert word.get(degree="superlative", gender="masculine", case="genitive", number="singular") == "uberrimi"
        assert word.get(degree="superlative", gender="masculine", case="dative", number="singular") == "uberrimo"
        assert word.get(degree="superlative", gender="masculine", case="ablative", number="singular") == "uberrimo"
        assert word.get(degree="superlative", gender="masculine", case="nominative", number="plural") == "uberrimi"
        assert word.get(degree="superlative", gender="masculine", case="vocative", number="plural") == "uberrimi"
        assert word.get(degree="superlative", gender="masculine", case="accusative", number="plural") == "uberrimos"
        assert word.get(degree="superlative", gender="masculine", case="genitive", number="plural") == "uberrimorum"
        assert word.get(degree="superlative", gender="masculine", case="dative", number="plural") == "uberrimis"
        assert word.get(degree="superlative", gender="masculine", case="ablative", number="plural") == "uberrimis"

        assert word.get(degree="superlative", gender="feminine", case="nominative", number="singular") == "uberrima"
        assert word.get(degree="superlative", gender="feminine", case="vocative", number="singular") == "uberrima"
        assert word.get(degree="superlative", gender="feminine", case="accusative", number="singular") == "uberrimam"
        assert word.get(degree="superlative", gender="feminine", case="genitive", number="singular") == "uberrimae"
        assert word.get(degree="superlative", gender="feminine", case="dative", number="singular") == "uberrimae"
        assert word.get(degree="superlative", gender="feminine", case="ablative", number="singular") == "uberrima"
        assert word.get(degree="superlative", gender="feminine", case="nominative", number="plural") == "uberrimae"
        assert word.get(degree="superlative", gender="feminine", case="vocative", number="plural") == "uberrimae"
        assert word.get(degree="superlative", gender="feminine", case="accusative", number="plural") == "uberrimas"
        assert word.get(degree="superlative", gender="feminine", case="genitive", number="plural") == "uberrimarum"
        assert word.get(degree="superlative", gender="feminine", case="dative", number="plural") == "uberrimis"
        assert word.get(degree="superlative", gender="feminine", case="ablative", number="plural") == "uberrimis"

        assert word.get(degree="superlative", gender="neuter", case="nominative", number="singular") == "uberrimum"
        assert word.get(degree="superlative", gender="neuter", case="vocative", number="singular") == "uberrimum"
        assert word.get(degree="superlative", gender="neuter", case="accusative", number="singular") == "uberrimum"
        assert word.get(degree="superlative", gender="neuter", case="genitive", number="singular") == "uberrimi"
        assert word.get(degree="superlative", gender="neuter", case="dative", number="singular") == "uberrimo"
        assert word.get(degree="superlative", gender="neuter", case="ablative", number="singular") == "uberrimo"
        assert word.get(degree="superlative", gender="neuter", case="nominative", number="plural") == "uberrima"
        assert word.get(degree="superlative", gender="neuter", case="vocative", number="plural") == "uberrima"
        assert word.get(degree="superlative", gender="neuter", case="accusative", number="plural") == "uberrima"
        assert word.get(degree="superlative", gender="neuter", case="genitive", number="plural") == "uberrimorum"
        assert word.get(degree="superlative", gender="neuter", case="dative", number="plural") == "uberrimis"
        assert word.get(degree="superlative", gender="neuter", case="ablative", number="plural") == "uberrimis"

    def test_declension3_2(self):
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

    def test_declension3_3(self):
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


class TestAdverb:
    def test_adverb_212(self):
        word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
        assert word.get(degree="positive", adverb=True) == "laete"
        assert word.get(degree="comparative", adverb=True) == "laetius"
        assert word.get(degree="superlative", adverb=True) == "laetissime"

    def test_adverb_31(self):
        word = Adjective("prudens", "prudentis", termination=1, declension="3", meaning="wise")
        assert word.get(degree="positive", adverb=True) == "prudenter"
        assert word.get(degree="comparative", adverb=True) == "prudentius"
        assert word.get(degree="superlative", adverb=True) == "prudentissime"

    def test_adverb_32(self):
        word = Adjective("fortis", "forte", termination=2, declension="3", meaning="strong")
        assert word.get(degree="positive", adverb=True) == "fortiter"
        assert word.get(degree="comparative", adverb=True) == "fortius"
        assert word.get(degree="superlative", adverb=True) == "fortissime"

    def test_adverb_33(self):
        word = Adjective("celer", "celeris", "celere", termination=3, declension="3", meaning="quick")
        assert word.get(degree="positive", adverb=True) == "celeriter"
        assert word.get(degree="comparative", adverb=True) == "celerius"
        assert word.get(degree="superlative", adverb=True) == "celerrime"

    def test_irregularadverb1(self):
        word = Adjective("bonus", "bona", "bonum", declension="212", meaning="happy")
        assert word.get(degree="positive", adverb=True) == "bene"
        assert word.get(degree="comparative", adverb=True) == "melius"
        assert word.get(degree="superlative", adverb=True) == "optime"

    def test_irregularadverb2(self):
        word = Adjective("bonus", "bonis", declension="3", termination=1, meaning="happy")
        assert word.get(degree="positive", adverb=True) == "bene"
        assert word.get(degree="comparative", adverb=True) == "melius"
        assert word.get(degree="superlative", adverb=True) == "optime"

    def test_irregularadverb3(self):
        word = Adjective("bonus", "bona", declension="3", termination=2, meaning="happy")
        assert word.get(degree="positive", adverb=True) == "bene"
        assert word.get(degree="comparative", adverb=True) == "melius"
        assert word.get(degree="superlative", adverb=True) == "optime"

    def test_irregularadverb4(self):
        word = Adjective("bonus", "bona", "bonum", declension="3", termination=3, meaning="happy")
        assert word.get(degree="positive", adverb=True) == "bene"
        assert word.get(degree="comparative", adverb=True) == "melius"
        assert word.get(degree="superlative", adverb=True) == "optime"

    def test_irregularadverb_noadverb(self):
        word = Adjective("magnus", "magna", "magnum", declension="212", meaning="big")
        a = word.get(degree="positive", adverb=True)
        assert a is None
