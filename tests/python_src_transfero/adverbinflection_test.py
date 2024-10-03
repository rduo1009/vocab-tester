import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from python_src.accido.misc import Degree, EndingComponents
from python_src.transfero.words import find_adverb_inflections


def test_adverb_inflection():
    word = "happily"
    assert find_adverb_inflections(word, EndingComponents(degree=Degree.POSITIVE)) == {"happily"}
    assert find_adverb_inflections(word, EndingComponents(degree=Degree.COMPARATIVE)) == {"more happily"}
    assert find_adverb_inflections(word, EndingComponents(degree=Degree.SUPERLATIVE)) == {"most happily", "very happily", "extremely happily", "rather happily", "too happily", "quite happily"}
