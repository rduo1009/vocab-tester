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
