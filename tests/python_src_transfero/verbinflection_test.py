import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import Case, EndingComponents, Gender, Mood, Number, Tense, Voice
from python_src.transfero.words import find_verb_inflections


class TestVerbInflectionErrors:
    def test_verb_invalidtense(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="error", voice=Voice.PASSIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1))
        assert str(error.value) == "Invalid tense: 'error'"

    def test_verb_error_1a(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE))
        assert str(error.value) == "Mood must be specified"

    def test_verb_error_1b(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(voice=Voice.ACTIVE, mood=Mood.SUBJUNCTIVE))
        assert str(error.value) == "Tense must be specified"

    def test_verb_error_1c(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, mood=Mood.IMPERATIVE))
        assert str(error.value) == "Voice must be specified"

    def test_verb_error_2a(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, person=3))
        assert str(error.value) == "Number must be specified"

    def test_verb_error_2b(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR))
        assert str(error.value) == "Person must be specified"

    def test_verb_invalid_1(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense="error", voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1))
        assert str(error.value) == "Invalid tense: 'error'"

    def test_verb_invalid_2(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=4))
        assert str(error.value) == "Invalid person: '4'"

    def test_verb_invalid_3(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice="error", mood=Mood.INDICATIVE, number=Number.SINGULAR, person=3))
        assert str(error.value) == "Invalid voice: 'error'"

    def test_verb_invalid_4(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number="error", person=1))
        assert str(error.value) == "Invalid number: 'error'"

    def test_verb_invalid_5(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood="error", number=Number.PLURAL, person=1))
        assert str(error.value) == "Invalid mood: 'error'"

    def test_verb_error_3(self):
        with pytest.raises(NotImplementedError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.PASSIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1))
        assert str(error.value) == "The present passive indicative has not been implemented"

    #
    # def test_verb_error_4(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_5(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_6(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("have", EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_7(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"
    #
    # def test_verb_error_8(self):
    #     with pytest.raises(ValueError) as error:
    #         find_verb_inflections("attack", EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=4))
    #     assert str(error.value) == "Invalid number and person: singular 4"


class TestParticipleInflectionErrors:
    def test_participle_error_1a(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.PARTICIPLE, gender=Gender.MASCULINE, number=Number.SINGULAR))
        assert str(error.value) == "Case must be specified"

    def test_participle_error_1b(self):
        with pytest.raises(ValueError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.PARTICIPLE, case=Case.NOMINATIVE, number=Number.SINGULAR))
        assert str(error.value) == "Gender must be specified"

    def test_participle_error_2(self):
        with pytest.raises(NotImplementedError) as error:
            find_verb_inflections("attack", EndingComponents(tense=Tense.PRESENT, voice=Voice.PASSIVE, mood=Mood.PARTICIPLE, case=Case.NOMINATIVE, gender=Gender.MASCULINE, number=Number.SINGULAR))
        assert str(error.value) == "The present passive participle has not been implemented"


class TestVerbInflection:
    def test_verb_present(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1)) == {"I attack", "I am attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=2)) == {"you attack", "you are attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=3)) == {"he attacks", "he is attacking", "she attacks", "she is attacking", "it attacks", "it is attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we attack", "we are attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=2)) == {"you attack", "you are attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=3)) == {"they attack", "they are attacking"}

    def test_verb_imperfect(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1)) == {"I was attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=2)) == {"you were attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=3)) == {"he was attacking", "she was attacking", "it was attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we were attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=2)) == {"you were attacking"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=3)) == {"they were attacking"}

    def test_verb_perfect(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1)) == {"I attacked", "I have attacked", "I did attack"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=2)) == {"you attacked", "you have attacked", "you did attack"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=3)) == {"he attacked", "he has attacked", "he did attack", "she has attacked", "she attacked", "she did attack", "it attacked", "it has attacked", "it did attack"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we attacked", "we have attacked", "we did attack"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=2)) == {"you attacked", "you have attacked", "you did attack"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=3)) == {"they attacked", "they have attacked", "they did attack"}

    def test_verb_pluperfect(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1)) == {"I had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=2)) == {"you had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=3)) == {"he had attacked", "she had attacked", "it had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=2)) == {"you had attacked"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PLUPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=3)) == {"they had attacked"}

    def test_verb_infinitive(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INFINITIVE, number=Number.SINGULAR, person=3)) == {"to attack"}

    def test_verb_present_imperative(self):
        word = "attack"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.IMPERATIVE, number=Number.SINGULAR, person=2)) == {"attack"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.IMPERATIVE, number=Number.PLURAL, person=2)) == {"attack"}

    def test_verb_imperfect_stative(self):
        word = "have"

        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=1)) == {"I had", "I was having"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=2)) == {"you had", "you were having"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.SINGULAR, person=3)) == {"he was having", "he had", "she was having", "she had", "it was having", "it had"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we were having", "we had"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=2)) == {"you were having", "you had"}
        assert find_verb_inflections(word, EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=3)) == {"they were having", "they had"}


def test_participle_inflections():
    word = "attack"

    assert find_verb_inflections(word, EndingComponents(tense=Tense.PERFECT, voice=Voice.PASSIVE, mood=Mood.PARTICIPLE, number=Number.SINGULAR, case=Case.NOMINATIVE, gender=Gender.MASCULINE)) == {"having been attacked"}
    assert find_verb_inflections(word, EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.PARTICIPLE, number=Number.SINGULAR, case=Case.NOMINATIVE, gender=Gender.MASCULINE)) == {"attacking"}
