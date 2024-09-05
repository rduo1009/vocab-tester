import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import EndingComponents
from python_src.transfero.words import find_adverb_inflections
from python_src.utils import compare


class TestAdverbInflectErrors:
    def test_adverb_errors_1(self):
        with pytest.raises(ValueError) as error:
            find_adverb_inflections("happily", EndingComponents())

        assert "Degree must be specified" == str(error.value)

    def test_adverb_errors_2(self):
        with pytest.raises(ValueError) as error:
            find_adverb_inflections("happily", EndingComponents(degree="error"))

        assert "Invalid degree: 'error'" == str(error.value)


class TestAdverbInflection:
    def test_adverb_inflection(self):
        word = "happily"
        assert find_adverb_inflections(word, EndingComponents(degree="positive")) == {"happily"}
        assert find_adverb_inflections(word, EndingComponents(degree="comparative")) == {"more happily"}
        assert find_adverb_inflections(word, EndingComponents(degree="superlative")) == {"most happily", "very happily", "extremely happily", "rather happily", "too happily", "quite happily"}
