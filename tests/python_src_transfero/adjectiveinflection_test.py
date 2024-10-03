import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from python_src.accido.misc import Case, Degree, EndingComponents, Gender, Number
from python_src.transfero.words import find_adjective_inflections


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
