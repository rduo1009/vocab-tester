import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from src.core.accido.misc import Case, Degree, EndingComponents, Gender, Number
from src.core.transfero.adjective_inflection import find_adjective_inflections, find_main_adjective_inflection
from src.core.transfero.exceptions import InvalidComponentsError


def test_invalid_type():
    with pytest.raises(InvalidComponentsError) as error:
        find_adjective_inflections("happy", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER))
    assert "Invalid type: 'pronoun'" == str(error.value)

    with pytest.raises(InvalidComponentsError) as error:
        find_main_adjective_inflection("happy", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER))
    assert "Invalid type: 'pronoun'" == str(error.value)


def test_invalid_subtype():
    with pytest.raises(InvalidComponentsError) as error:
        find_adjective_inflections("happy", EndingComponents(degree=Degree.POSITIVE))
    assert "Invalid subtype: 'adverb'" == str(error.value)

    with pytest.raises(InvalidComponentsError) as error:
        find_main_adjective_inflection("happy", EndingComponents(degree=Degree.POSITIVE))
    assert "Invalid subtype: 'adverb'" == str(error.value)


def test_adjective_inflection():
    word = "happy"

    assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.POSITIVE)) == {"happy"}
    assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.COMPARATIVE)) == {"happier", "more happy"}
    assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.SUPERLATIVE)) == {"happiest", "most happy", "very happy", "extremely happy", "rather happy", "too happy", "quite happy"}


def test_adjective_inflection_multiple_superlatives():
    word = "far"

    assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.POSITIVE)) == {"far"}
    assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.COMPARATIVE)) == {"farther", "further", "more far"}
    assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.SUPERLATIVE)) == {"farthest", "furthest", "most far", "very far", "extremely far", "rather far", "too far", "quite far"}


def test_adjective_main_inflection():
    word = "happy"

    assert find_main_adjective_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.POSITIVE)) == "happy"
    assert find_main_adjective_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.COMPARATIVE)) == "happier"
    assert find_main_adjective_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.SUPERLATIVE)) == "happiest"


def test_adjective_main_inflection_irregular():
    word = "interesting"

    assert find_main_adjective_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.POSITIVE)) == "interesting"
    assert find_main_adjective_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.COMPARATIVE)) == "more interesting"
    assert find_main_adjective_inflection(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.SUPERLATIVE)) == "most interesting"
