import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import Case, Degree, EndingComponents, Gender, Number
from python_src.transfero.words import find_adjective_inflections


class TestAdjectiveInflectErrors:
    def test_adjective_errors_1(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, degree=Degree.POSITIVE))
        assert "Gender must be specified" == str(error.value)

    def test_adjective_errors_2(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(degree=Degree.POSITIVE, number=Number.SINGULAR, gender=Gender.MASCULINE))
        assert "Case must be specified" == str(error.value)

    def test_adjective_errors_3(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(degree=Degree.POSITIVE, case=Case.NOMINATIVE, gender=Gender.MASCULINE))
        assert "Number must be specified" == str(error.value)

    def test_adjective_errors_4(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE))
        assert "Degree must be specified" == str(error.value)


class TestAdjectiveInflection:
    def test_adjective_inflection(self):
        word = "happy"

        assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.POSITIVE)) == {"happy"}
        assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.COMPARATIVE)) == {"happier", "more happy"}
        assert find_adjective_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE, degree=Degree.SUPERLATIVE)) == {"happiest", "most happy", "very happy", "extremely happy", "rather happy", "too happy", "quite happy"}
