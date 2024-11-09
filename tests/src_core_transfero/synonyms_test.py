import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.core.transfero.synonyms import find_synonyms


def test_synonyms():
    words = ["house", "car", "happy", "sad", "disgust", "fortune"]
    for word in words:
        synonyms = find_synonyms(word)
        ic(synonyms)  # type: ignore[name-defined] # noqa: F821
