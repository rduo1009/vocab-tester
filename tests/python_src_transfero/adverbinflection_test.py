import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import pytest
from python_src.accido.misc import Case, Degree, EndingComponents, Gender, Number
from python_src.transfero.words import find_adverb_inflections, find_main_adverb_inflection  # type: ignore[attr-defined]


def test_invalid_type():
    with pytest.raises(ValueError) as error:
        find_adverb_inflections("happily", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER))
    assert "Invalid type:" in str(error.value)

    with pytest.raises(ValueError) as error:
        find_main_adverb_inflection("happily", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER))
    assert "Invalid type:" in str(error.value)


def test_invalid_subtype():
    with pytest.raises(ValueError) as error:
        find_adverb_inflections("happily", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER, degree=Degree.POSITIVE))
    assert "Invalid subtype: 'None'" == str(error.value)

    with pytest.raises(ValueError) as error:
        find_main_adverb_inflection("happily", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.NEUTER, degree=Degree.POSITIVE))
    assert "Invalid subtype: 'None'" == str(error.value)


def test_adverb_inflection():
    word = "happily"
    assert find_adverb_inflections(word, EndingComponents(degree=Degree.POSITIVE)) == {"happily"}
    assert find_adverb_inflections(word, EndingComponents(degree=Degree.COMPARATIVE)) == {"more happily"}
    assert find_adverb_inflections(word, EndingComponents(degree=Degree.SUPERLATIVE)) == {"most happily", "very happily", "extremely happily", "rather happily", "too happily", "quite happily"}


def test_adverb_main_inflection():
    word = "happily"
    assert find_main_adverb_inflection(word, EndingComponents(degree=Degree.POSITIVE)) == "happily"
    assert find_main_adverb_inflection(word, EndingComponents(degree=Degree.COMPARATIVE)) == "more happily"
    assert find_main_adverb_inflection(word, EndingComponents(degree=Degree.SUPERLATIVE)) == "most happily"
