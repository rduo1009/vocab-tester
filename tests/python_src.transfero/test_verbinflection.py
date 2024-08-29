import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import EndingComponents
from python_src.transfero.words import find_verb_inflections


class TestVerbInflectionErrors:
    def test_verb_invalidtense(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="error", voice="passive", mood="indicative", number="singular", person=1))
        assert str(error.value) == "Invalid tense: 'error'"

    def test_verb_error_1a(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active"))
        assert str(error.value) == "Mood must be specified"

    def test_verb_error_1b(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(voice="active", mood="subjunctive"))
        assert str(error.value) == "Tense must be specified"

    def test_verb_error_1c(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", mood="imperative"))
        assert str(error.value) == "Voice must be specified"

    def test_verb_error_2a(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="indicative", person=3))
        assert str(error.value) == "Number must be specified"

    def test_verb_error_2b(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="indicative", number="singular"))
        assert str(error.value) == "Person must be specified"

    def test_verb_invalid_1(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="error", voice="active", mood="indicative", number="singular", person=1))
        assert str(error.value) == "Invalid tense: 'error'"

    def test_verb_invalid_2(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="indicative", number="singular", person=4))
        assert str(error.value) == "Invalid person: '4'"

    def test_verb_invalid_3(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="error", mood="indicative", number="singular", person=3))
        assert str(error.value) == "Invalid voice: 'error'"

    def test_verb_invalid_4(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="indicative", number="error", person=1))
        assert str(error.value) == "Invalid number: 'error'"

    def test_verb_invalid_5(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="error", number="plural", person=1))
        assert str(error.value) == "Invalid mood: 'error'"

    def test_verb_error_3(self):
        with pytest.raises(NotImplementedError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="passive", mood="indicative", number="singular", person=1))
        assert str(error.value) == "The present passive indicative has not been implemented"

    #
    # def test_verb_error_4(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="indicative", number="singular", person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_5(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_6(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("have", EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_7(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense="perfect", voice="active", mood="indicative", number="singular", person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_8(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="singular", person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"


class TestParticipleInflectionErrors:
    def test_participle_error_1a(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="participle", gender="masculine", number="singular"))
        assert str(error.value) == "Case must be specified"

    def test_participle_error_1b(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="active", mood="participle", case="nominative", number="singular"))
        assert str(error.value) == "Gender must be specified"

    def test_participle_error_2(self):
        with pytest.raises(NotImplementedError) as error:
            find_verb_inflections("attack", EndingComponents(tense="present", voice="passive", mood="participle", case="nominative", gender="masculine", number="singular"))
        assert str(error.value) == "The present passive participle has not been implemented"


class TestVerbInflection:
    def test_verb_present(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="indicative", number="singular", person=1)) == {"I attack", "I am attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="indicative", number="singular", person=2)) == {"you attack", "you are attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="indicative", number="singular", person=3)) == {"he attacks", "he is attacking", "she attacks", "she is attacking", "it attacks", "it is attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="indicative", number="plural", person=1)) == {"we attack", "we are attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="indicative", number="plural", person=2)) == {"you attack", "you are attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="indicative", number="plural", person=3)) == {"they attack", "they are attacking"}

    def test_verb_imperfect(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=1)) == {"I was attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=2)) == {"you were attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=3)) == {"he was attacking", "she was attacking", "it was attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="plural", person=1)) == {"we were attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="plural", person=2)) == {"you were attacking"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="plural", person=3)) == {"they were attacking"}

    def test_verb_perfect(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="active", mood="indicative", number="singular", person=1)) == {"I attacked", "I have attacked", "I did attack"}
        assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="active", mood="indicative", number="singular", person=2)) == {"you attacked", "you have attacked", "you did attack"}
        assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="active", mood="indicative", number="singular", person=3)) == {"he attacked", "he has attacked", "he did attack", "she has attacked", "she attacked", "she did attack", "it attacked", "it has attacked", "it did attack"}
        assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="active", mood="indicative", number="plural", person=1)) == {"we attacked", "we have attacked", "we did attack"}
        assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="active", mood="indicative", number="plural", person=2)) == {"you attacked", "you have attacked", "you did attack"}
        assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="active", mood="indicative", number="plural", person=3)) == {"they attacked", "they have attacked", "they did attack"}

    def test_verb_pluperfect(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="singular", person=1)) == {"I had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="singular", person=2)) == {"you had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="singular", person=3)) == {"he had attacked", "she had attacked", "it had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="plural", person=1)) == {"we had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="plural", person=2)) == {"you had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense="pluperfect", voice="active", mood="indicative", number="plural", person=3)) == {"they had attacked"}

    def test_verb_infinitive(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="infinitive", number="singular", person=3)) == {"to attack"}

    def test_verb_present_imperative(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="imperative", number="singular", person=2)) == {"attack"}
        assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="imperative", number="plural", person=2)) == {"attack"}

    def test_verb_imperfect_stative(self):
        word = "have"

        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=1)) == {"I had", "I was having"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=2)) == {"you had", "you were having"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="singular", person=3)) == {"he was having", "he had", "she was having", "she had", "it was having", "it had"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="plural", person=1)) == {"we were having", "we had"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="plural", person=2)) == {"you were having", "you had"}
        assert find_verb_inflections(word, EndingComponents(tense="imperfect", voice="active", mood="indicative", number="plural", person=3)) == {"they were having", "they had"}


def test_participle_inflections():
    word = "attack"

    assert find_verb_inflections(word, EndingComponents(tense="perfect", voice="passive", mood="participle", number="singular", case="nominative", gender="masculine")) == {"having been attacked"}
    assert find_verb_inflections(word, EndingComponents(tense="present", voice="active", mood="participle", number="singular", case="nominative", gender="masculine")) == {"attacking"}
