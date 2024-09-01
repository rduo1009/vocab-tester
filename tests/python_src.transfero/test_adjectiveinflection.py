import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import EndingComponents
from python_src.transfero.words import find_adjective_inflections


class TestAdjectiveInflectErrors:
    def test_adjective_errors_1(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case="nominative", number="singular", degree="positive"))
        assert "Gender must be specified" == str(error.value)

    def test_adjective_errors_2(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(degree="positive", number="singular", gender="masculine"))
        assert "Case must be specified" == str(error.value)

    def test_adjective_errors_3(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(degree="positive", case="nominative", gender="masculine"))
        assert "Number must be specified" == str(error.value)

    def test_adjective_errors_4(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case="nominative", number="singular", gender="masculine"))
        assert "Degree must be specified" == str(error.value)

    def test_adjective_errors_5(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case="nominative", number="singular", gender="error", degree="positive"))
        assert "Invalid gender: 'error'" == str(error.value)

    def test_adjective_errors_6(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case="error", number="singular", gender="masculine", degree="positive"))
        assert "Invalid case: 'error'" == str(error.value)

    def test_adjective_errors_7(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case="nominative", number="error", gender="masculine", degree="positive"))
        assert "Invalid number: 'error'" == str(error.value)

    def test_adjective_errors_8(self):
        with pytest.raises(ValueError) as error:
            find_adjective_inflections("happy", EndingComponents(case="nominative", number="singular", gender="masculine", degree="error"))
        assert "Invalid degree: 'error'" == str(error.value)


class TestAdjectiveInflection:
    def test_adjective_inflection(self):
        word = "happy"

        assert find_adjective_inflections(word, EndingComponents(case="nominative", number="singular", gender="masculine", degree="positive")) == {"happy"}
        assert find_adjective_inflections(word, EndingComponents(case="nominative", number="singular", gender="masculine", degree="comparative")) == {"happier", "more happy"}
        assert find_adjective_inflections(word, EndingComponents(case="nominative", number="singular", gender="masculine", degree="superlative")) == {"happiest", "most happy", "very happy", "extremely happy", "rather happy", "too happy", "quite happy"}
