import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import pytest
from python_src.accido.misc import Case, Degree, EndingComponents, Gender, Number
from python_src.transfero.pronoun_inflection import find_main_pronoun_inflection, find_pronoun_inflections


def test_invalid_type():
    with pytest.raises(ValueError) as error:
        find_pronoun_inflections("house", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER, degree=Degree.POSITIVE))
    assert "Invalid type: '<class 'python_src.accido.class_adjective.Adjective'>'" == str(error.value)


class TestPronounInflection:
    def test_pronoun_inflections_1(self):
        word = "this"

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"this"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"this"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"this"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"by this", "by means of this", "with this", "this"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"of this"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"for this", "to this"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"these"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"these"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"these"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"by these", "by means of these", "with these", "these"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"of these"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"for these", "to these"}

    def test_pronoun_inflections_2(self):
        word = "that"

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"that"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"that"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"that"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"by that", "by means of that", "with that", "that"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"of that"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"for that", "to that"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"those"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"those"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"those"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"by those", "by means of those", "with those", "those"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"of those"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == {"for those", "to those"}

    def test_main_pronoun_inflections_1(self):
        word = "this"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "this"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "this"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "this"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "by this"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "of this"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "for this"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "these"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "these"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "these"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "by these"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "of these"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "for these"

    def test_main_pronoun_inflections_2(self):
        word = "that"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "that"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "that"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "that"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "by that"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "of that"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == "for that"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "those"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "those"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "those"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "by those"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "of those"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL, gender=Gender.MASCULINE)) == "for those"


class TestNounlikePronounInflection:
    def test_pronoun_inflections_1(self):
        word = "I"

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == {"I"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == {"I"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == {"me"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == {"of me", "my"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == {"for me", "to me"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == {"me", "with me", "by me", "by means of me"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == {"we"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == {"we"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == {"us"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == {"of us", "our"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"for us", "to us"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == {"us", "with us", "by us", "by means of us"}

    def test_main_pronoun_inflections_1(self):
        word = "I"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == "I"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == "I"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == "me"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == "of me"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == "for me"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == "by me"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == "we"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == "we"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == "us"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == "of us"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == "for us"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == "by us"

    def test_pronoun_inflections_2(self):
        word = "you"

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == {"you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == {"you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == {"you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == {"of you", "your"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == {"for you", "to you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == {"you", "with you", "by you", "by means of you"}

        assert find_pronoun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == {"you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == {"you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == {"you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == {"of you", "your"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"for you", "to you"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == {"you", "with you", "by you", "by means of you"}

    def test_main_pronoun_inflections_2(self):
        word = "you"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == "you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == "you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == "you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == "of you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == "for you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == "by you"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == "you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == "you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == "you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == "of you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == "for you"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == "by you"

    def test_pronoun_inflections_3(self):
        word = "oneself"

        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == {"oneself", "himself", "herself", "itself", "themself"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == {"of oneself", "one's", "of himself", "his", "of herself", "her", "of itself", "its", "of themself", "their"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == {"for oneself", "for himself", "for herself", "for itself", "for themself", "to oneself", "to himself", "to herself", "to itself", "to themself"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == {
            "oneself", "himself", "herself", "itself", "themself",
            "with oneself", "with himself", "with herself", "with itself", "with themself",
            "by oneself", "by himself", "by herself", "by itself", "by themself",
            "by means of oneself", "by means of himself", "by means of herself", "by means of itself", "by means of themself",
        }  # fmt: skip

        assert find_pronoun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == {"themselves"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == {"of themselves", "their"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"for themselves", "to themselves"}
        assert find_pronoun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == {"themselves", "with themselves", "by themselves", "by means of themselves"}

    def test_main_pronoun_inflections_3(self):
        word = "oneself"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == "oneself"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == "of oneself"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == "for oneself"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == "by oneself"

        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == "themselves"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == "of themselves"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == "for themselves"
        assert find_main_pronoun_inflection(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == "by themselves"
