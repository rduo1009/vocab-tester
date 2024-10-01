import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest

from python_src.accido.exceptions import InvalidInputError  # isort: skip
from python_src.accido.endings import Verb
from python_src.accido.misc import EndingComponents
from python_src.utils import compare


class TestVerbErrors:
    def test_errors_invalid_infinitive(self):
        with pytest.raises(InvalidInputError) as error:
            Verb(present="celo", infinitive="error", perfect="celavi", ppp="celatus", meaning="hide")
        assert "Invalid infinitive form: 'error'" == str(error.value)

    def test_errors_invalid_present(self):
        with pytest.raises(InvalidInputError) as error:
            Verb(present="error", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert "Invalid present form: 'error' (must end in '-o')" == str(error.value)

    def test_errors_invalid_perfect(self):
        with pytest.raises(InvalidInputError) as error:
            Verb(present="celo", infinitive="celare", perfect="error", ppp="celatus", meaning="hide")
        assert "Invalid perfect form: 'error' (must end in '-i')" == str(error.value)

    def test_errors_invalid_number(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(person=1, number="error", tense="perfect", voice="active", mood="indicative")
        assert "Invalid number: 'error'" == str(error.value)

    def test_errors_invalid_tense(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(person=1, number="singular", tense="error", voice="active", mood="indicative")
        assert "Invalid tense: 'error'" == str(error.value)

    def test_errors_invalid_voice(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(person=1, number="singular", tense="present", voice="error", mood="indicative")
        assert "Invalid voice: 'error'" == str(error.value)

    def test_errors_invalid_mood(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(person=1, number="singular", tense="present", voice="active", mood="error")
        assert "Invalid mood: 'error'" == str(error.value)

    def test_errors_invalid_number_participle(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="error", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="nominative")
        assert "Invalid number: 'error'" == str(error.value)

    def test_errors_invalid_tense_participle(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="error", voice="passive", mood="participle", participle_gender="masculine", participle_case="nominative")
        assert "Invalid tense: 'error'" == str(error.value)

    def test_errors_invalid_voice_participle(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="perfect", voice="error", mood="participle", participle_gender="masculine", participle_case="nominative")
        assert "Invalid voice: 'error'" == str(error.value)

    def test_errors_invalid_gender_participle(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="error", participle_case="nominative")
        assert "Invalid gender: 'error'" == str(error.value)

    def test_errors_invalid_case_participle(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="error")
        assert "Invalid case: 'error'" == str(error.value)

    def test_errors_person_with_participle(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="nominative", person=1)
        assert "Participle cannot have a person (person '1')" == str(error.value)

    def test_errors_participle_gender_not_given(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="present", voice="active", mood="participle", participle_case="nominative")
        assert "Gender not given" == str(error.value)

    def test_errors_participle_case_not_given(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine")
        assert "Case not given" == str(error.value)

    def test_errors_number_not_given(self):
        with pytest.raises(InvalidInputError) as error:
            word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
            word.get(tense="present", voice="active", mood="participle", participle_case="nominative", participle_gender="masculine")
        assert "Number not given" == str(error.value)


class TestVerbDunder:
    def test_getnone(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert not word.get(tense="perfect", voice="passive", mood="indicative", person=2, number="plural")

    def test_repr(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert word.__repr__() == "Verb(celo, celare, celavi, celatus, hide)"

    def test_verb_str(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert str(word) == "hide: celo, celare, celavi, celatus"

    def test_verb_strnoppp(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", meaning="hide")
        assert str(word) == "hide: celo, celare, celavi"

    def test_eq(self):
        word1 = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        word2 = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert word1 == word2

    def test_lt(self):
        word1 = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        word2 = Verb(present="amo", infinitive="amare", perfect="amavi", ppp="amatus", meaning="love")
        # word2 must be smaller than word1 as word1.first = "test1" and word2.first = "aaatest1"
        assert word1 > word2

    def test_find(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert compare(word.find("celabam"), [EndingComponents(person="1st person", number="singular", tense="imperfect", voice="active", mood="indicative", string="imperfect active indicative singular 1st person")])

    def test_find_participle(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")
        assert compare(word.find("celatus"), [EndingComponents(number="singular", case="nominative", gender="masculine", tense="perfect", voice="passive", mood="participle", string="perfect passive participle masculine nominative singular")])


class TestVerbConjugation:
    def test_firstconjugation(self):
        word = Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide")

        assert word.get(person=1, number="singular", tense="present", voice="active", mood="indicative") == "celo"
        assert word.get(person=2, number="singular", tense="present", voice="active", mood="indicative") == "celas"
        assert word.get(person=3, number="singular", tense="present", voice="active", mood="indicative") == "celat"
        assert word.get(person=1, number="plural", tense="present", voice="active", mood="indicative") == "celamus"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="indicative") == "celatis"
        assert word.get(person=3, number="plural", tense="present", voice="active", mood="indicative") == "celant"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="indicative") == "celabam"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="indicative") == "celabas"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="indicative") == "celabat"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="indicative") == "celabamus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="indicative") == "celabatis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="indicative") == "celabant"

        assert word.get(person=1, number="singular", tense="perfect", voice="active", mood="indicative") == "celavi"
        assert word.get(person=2, number="singular", tense="perfect", voice="active", mood="indicative") == "celavisti"
        assert word.get(person=3, number="singular", tense="perfect", voice="active", mood="indicative") == "celavit"
        assert word.get(person=1, number="plural", tense="perfect", voice="active", mood="indicative") == "celavimus"
        assert word.get(person=2, number="plural", tense="perfect", voice="active", mood="indicative") == "celavistis"
        assert word.get(person=3, number="plural", tense="perfect", voice="active", mood="indicative") == "celaverunt"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="indicative") == "celaveram"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="indicative") == "celaveras"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="indicative") == "celaverat"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="indicative") == "celaveramus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="indicative") == "celaveratis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="indicative") == "celaverant"

        assert word.get(tense="present", voice="active", mood="infinitive") == "celare"

        assert word.get(person=2, number="singular", tense="present", voice="active", mood="imperative") == "cela"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="imperative") == "celate"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "celarem"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "celares"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "celaret"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "celaremus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "celaretis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "celarent"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "celavissem"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "celavisses"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "celavisset"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "celavissemus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "celavissetis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "celavissent"

    def test_secondconjugation(self):
        word = Verb(present="pareo", infinitive="parere", perfect="parui", meaning="hide")

        assert word.get(person=1, number="singular", tense="present", voice="active", mood="indicative") == "pareo"
        assert word.get(person=2, number="singular", tense="present", voice="active", mood="indicative") == "pares"
        assert word.get(person=3, number="singular", tense="present", voice="active", mood="indicative") == "paret"
        assert word.get(person=1, number="plural", tense="present", voice="active", mood="indicative") == "paremus"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="indicative") == "paretis"
        assert word.get(person=3, number="plural", tense="present", voice="active", mood="indicative") == "parent"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="indicative") == "parebam"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="indicative") == "parebas"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="indicative") == "parebat"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="indicative") == "parebamus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="indicative") == "parebatis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="indicative") == "parebant"

        assert word.get(person=1, number="singular", tense="perfect", voice="active", mood="indicative") == "parui"
        assert word.get(person=2, number="singular", tense="perfect", voice="active", mood="indicative") == "paruisti"
        assert word.get(person=3, number="singular", tense="perfect", voice="active", mood="indicative") == "paruit"
        assert word.get(person=1, number="plural", tense="perfect", voice="active", mood="indicative") == "paruimus"
        assert word.get(person=2, number="plural", tense="perfect", voice="active", mood="indicative") == "paruistis"
        assert word.get(person=3, number="plural", tense="perfect", voice="active", mood="indicative") == "paruerunt"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="indicative") == "parueram"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="indicative") == "parueras"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="indicative") == "paruerat"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="indicative") == "parueramus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="indicative") == "parueratis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="indicative") == "paruerant"

        assert word.get(tense="present", voice="active", mood="infinitive") == "parere"

        assert word.get(person=2, number="singular", tense="present", voice="active", mood="imperative") == "pare"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="imperative") == "parete"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "parerem"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "pareres"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "pareret"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "pareremus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "pareretis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "parerent"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "paruissem"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "paruisses"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "paruisset"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "paruissemus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "paruissetis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "paruissent"

    def test_thirdconjugation(self):
        word = Verb(present="desero", infinitive="deserere", perfect="deserui", ppp="desertus", meaning="desert")

        assert word.get(person=1, number="singular", tense="present", voice="active", mood="indicative") == "desero"
        assert word.get(person=2, number="singular", tense="present", voice="active", mood="indicative") == "deseris"
        assert word.get(person=3, number="singular", tense="present", voice="active", mood="indicative") == "deserit"
        assert word.get(person=1, number="plural", tense="present", voice="active", mood="indicative") == "deserimus"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="indicative") == "deseritis"
        assert word.get(person=3, number="plural", tense="present", voice="active", mood="indicative") == "deserunt"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="indicative") == "deserebam"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="indicative") == "deserebas"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="indicative") == "deserebat"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="indicative") == "deserebamus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="indicative") == "deserebatis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="indicative") == "deserebant"

        assert word.get(person=1, number="singular", tense="perfect", voice="active", mood="indicative") == "deserui"
        assert word.get(person=2, number="singular", tense="perfect", voice="active", mood="indicative") == "deseruisti"
        assert word.get(person=3, number="singular", tense="perfect", voice="active", mood="indicative") == "deseruit"
        assert word.get(person=1, number="plural", tense="perfect", voice="active", mood="indicative") == "deseruimus"
        assert word.get(person=2, number="plural", tense="perfect", voice="active", mood="indicative") == "deseruistis"
        assert word.get(person=3, number="plural", tense="perfect", voice="active", mood="indicative") == "deseruerunt"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="indicative") == "deserueram"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="indicative") == "deserueras"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="indicative") == "deseruerat"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="indicative") == "deserueramus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="indicative") == "deserueratis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="indicative") == "deseruerant"

        assert word.get(tense="present", voice="active", mood="infinitive") == "deserere"

        assert word.get(person=2, number="singular", tense="present", voice="active", mood="imperative") == "desere"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="imperative") == "deserite"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "desererem"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "desereres"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "desereret"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "desereremus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "desereretis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "desererent"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "deseruissem"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "deseruisses"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "deseruisset"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "deseruissemus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "deseruissetis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "deseruissent"

    def test_thirdioconjugation(self):
        word = Verb(present="patefacio", infinitive="patefacere", perfect="patefeci", ppp="patefactus", meaning="reveal")

        assert word.get(person=1, number="singular", tense="present", voice="active", mood="indicative") == "patefacio"
        assert word.get(person=2, number="singular", tense="present", voice="active", mood="indicative") == "patefacis"
        assert word.get(person=3, number="singular", tense="present", voice="active", mood="indicative") == "patefacit"
        assert word.get(person=1, number="plural", tense="present", voice="active", mood="indicative") == "patefacimus"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="indicative") == "patefacitis"
        assert word.get(person=3, number="plural", tense="present", voice="active", mood="indicative") == "patefaciunt"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="indicative") == "patefaciebam"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="indicative") == "patefaciebas"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="indicative") == "patefaciebat"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="indicative") == "patefaciebamus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="indicative") == "patefaciebatis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="indicative") == "patefaciebant"

        assert word.get(person=1, number="singular", tense="perfect", voice="active", mood="indicative") == "patefeci"
        assert word.get(person=2, number="singular", tense="perfect", voice="active", mood="indicative") == "patefecisti"
        assert word.get(person=3, number="singular", tense="perfect", voice="active", mood="indicative") == "patefecit"
        assert word.get(person=1, number="plural", tense="perfect", voice="active", mood="indicative") == "patefecimus"
        assert word.get(person=2, number="plural", tense="perfect", voice="active", mood="indicative") == "patefecistis"
        assert word.get(person=3, number="plural", tense="perfect", voice="active", mood="indicative") == "patefecerunt"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="indicative") == "patefeceram"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="indicative") == "patefeceras"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="indicative") == "patefecerat"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="indicative") == "patefeceramus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="indicative") == "patefeceratis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="indicative") == "patefecerant"

        assert word.get(tense="present", voice="active", mood="infinitive") == "patefacere"

        assert word.get(person=2, number="singular", tense="present", voice="active", mood="imperative") == "pateface"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="imperative") == "patefacite"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "patefacerem"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "patefaceres"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "patefaceret"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "patefaceremus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "patefaceretis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "patefacerent"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "patefecissem"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "patefecisses"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "patefecisset"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "patefecissemus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "patefecissetis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "patefecissent"

    def test_fourthconjugation(self):
        word = Verb(present="aperio", infinitive="aperire", perfect="aperui", ppp="apertus", meaning="open")

        assert word.get(person=1, number="singular", tense="present", voice="active", mood="indicative") == "aperio"
        assert word.get(person=2, number="singular", tense="present", voice="active", mood="indicative") == "aperis"
        assert word.get(person=3, number="singular", tense="present", voice="active", mood="indicative") == "aperit"
        assert word.get(person=1, number="plural", tense="present", voice="active", mood="indicative") == "aperimus"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="indicative") == "aperitis"
        assert word.get(person=3, number="plural", tense="present", voice="active", mood="indicative") == "aperiunt"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="indicative") == "aperiebam"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="indicative") == "aperiebas"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="indicative") == "aperiebat"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="indicative") == "aperiebamus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="indicative") == "aperiebatis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="indicative") == "aperiebant"

        assert word.get(person=1, number="singular", tense="perfect", voice="active", mood="indicative") == "aperui"
        assert word.get(person=2, number="singular", tense="perfect", voice="active", mood="indicative") == "aperuisti"
        assert word.get(person=3, number="singular", tense="perfect", voice="active", mood="indicative") == "aperuit"
        assert word.get(person=1, number="plural", tense="perfect", voice="active", mood="indicative") == "aperuimus"
        assert word.get(person=2, number="plural", tense="perfect", voice="active", mood="indicative") == "aperuistis"
        assert word.get(person=3, number="plural", tense="perfect", voice="active", mood="indicative") == "aperuerunt"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="indicative") == "aperueram"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="indicative") == "aperueras"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="indicative") == "aperuerat"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="indicative") == "aperueramus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="indicative") == "aperueratis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="indicative") == "aperuerant"

        assert word.get(tense="present", voice="active", mood="infinitive") == "aperire"

        assert word.get(person=2, number="singular", tense="present", voice="active", mood="imperative") == "aperi"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="imperative") == "aperite"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "aperirem"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "aperires"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "aperiret"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "aperiremus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "aperiretis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "aperirent"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "aperuissem"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "aperuisses"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "aperuisset"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "aperuissemus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "aperuissetis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "aperuissent"

    def test_irregularverb_eo(self):
        word = Verb(present="abeo", infinitive="abire", perfect="abii", ppp="abitum", meaning="depart")

        assert word.get(person=1, number="singular", tense="present", voice="active", mood="indicative") == "abeo"
        assert word.get(person=2, number="singular", tense="present", voice="active", mood="indicative") == "abis"
        assert word.get(person=3, number="singular", tense="present", voice="active", mood="indicative") == "abit"
        assert word.get(person=1, number="plural", tense="present", voice="active", mood="indicative") == "abimus"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="indicative") == "abitis"
        assert word.get(person=3, number="plural", tense="present", voice="active", mood="indicative") == "abeunt"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="indicative") == "abibam"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="indicative") == "abibas"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="indicative") == "abibat"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="indicative") == "abibamus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="indicative") == "abibatis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="indicative") == "abibant"

        assert word.get(person=1, number="singular", tense="perfect", voice="active", mood="indicative") == "abii"
        assert word.get(person=2, number="singular", tense="perfect", voice="active", mood="indicative") == "abisti"
        assert word.get(person=3, number="singular", tense="perfect", voice="active", mood="indicative") == "abiit"
        assert word.get(person=1, number="plural", tense="perfect", voice="active", mood="indicative") == "abiimus"
        assert word.get(person=2, number="plural", tense="perfect", voice="active", mood="indicative") == "abistis"
        assert word.get(person=3, number="plural", tense="perfect", voice="active", mood="indicative") == "abierunt"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="indicative") == "abieram"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="indicative") == "abieras"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="indicative") == "abierat"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="indicative") == "abieramus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="indicative") == "abieratis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="indicative") == "abierant"

        assert word.get(tense="present", voice="active", mood="infinitive") == "abire"

        assert word.get(person=2, number="singular", tense="present", voice="active", mood="imperative") == "abi"
        assert word.get(person=2, number="plural", tense="present", voice="active", mood="imperative") == "abite"

        assert word.get(person=1, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "abirem"
        assert word.get(person=2, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "abires"
        assert word.get(person=3, number="singular", tense="imperfect", voice="active", mood="subjunctive") == "abiret"
        assert word.get(person=1, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "abiremus"
        assert word.get(person=2, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "abiretis"
        assert word.get(person=3, number="plural", tense="imperfect", voice="active", mood="subjunctive") == "abirent"

        assert word.get(person=1, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "abissem"
        assert word.get(person=2, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "abisses"
        assert word.get(person=3, number="singular", tense="pluperfect", voice="active", mood="subjunctive") == "abisset"
        assert word.get(person=1, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "abissemus"
        assert word.get(person=2, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "abissetis"
        assert word.get(person=3, number="plural", tense="pluperfect", voice="active", mood="subjunctive") == "abissent"


class TestParticipleConjugation:
    def test_present_participle(self):
        word = Verb(present="porto", infinitive="portare", perfect="portavi", ppp="portatus", meaning="carry")

        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="nominative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="vocative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="accusative") == "portantem"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="genitive") == "portantis"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="dative") == "portanti"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="ablative") == "portante"

        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="nominative") == "portantes"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="vocative") == "portantes"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="accusative") == "portantes"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="genitive") == "portantium"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="dative") == "portantibus"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="masculine", participle_case="ablative") == "portantibus"

        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="nominative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="vocative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="accusative") == "portantem"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="genitive") == "portantis"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="dative") == "portanti"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="ablative") == "portante"

        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="nominative") == "portantes"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="vocative") == "portantes"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="accusative") == "portantes"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="genitive") == "portantium"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="dative") == "portantibus"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="feminine", participle_case="ablative") == "portantibus"

        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="nominative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="vocative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="accusative") == "portans"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="genitive") == "portantis"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="dative") == "portanti"
        assert word.get(number="singular", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="ablative") == "portante"

        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="nominative") == "portantia"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="vocative") == "portantia"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="accusative") == "portantia"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="genitive") == "portantium"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="dative") == "portantibus"
        assert word.get(number="plural", tense="present", voice="active", mood="participle", participle_gender="neuter", participle_case="ablative") == "portantibus"

    def test_ppp(self):
        word = Verb(present="porto", infinitive="portare", perfect="portavi", ppp="portatus", meaning="carry")

        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="nominative") == "portatus"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="vocative") == "portate"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="accusative") == "portatum"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="genitive") == "portati"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="dative") == "portato"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="ablative") == "portato"

        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="nominative") == "portati"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="vocative") == "portati"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="accusative") == "portatos"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="genitive") == "portatorum"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="dative") == "portatis"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="masculine", participle_case="ablative") == "portatis"

        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="nominative") == "portata"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="vocative") == "portata"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="accusative") == "portatam"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="genitive") == "portatae"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="dative") == "portatae"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="ablative") == "portata"

        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="nominative") == "portatae"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="vocative") == "portatae"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="accusative") == "portatas"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="genitive") == "portatarum"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="dative") == "portatis"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="feminine", participle_case="ablative") == "portatis"

        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="nominative") == "portatum"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="vocative") == "portatum"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="accusative") == "portatum"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="genitive") == "portati"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="dative") == "portato"
        assert word.get(number="singular", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="ablative") == "portato"

        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="nominative") == "portata"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="vocative") == "portata"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="accusative") == "portata"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="genitive") == "portatorum"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="dative") == "portatis"
        assert word.get(number="plural", tense="perfect", voice="passive", mood="participle", participle_gender="neuter", participle_case="ablative") == "portatis"
