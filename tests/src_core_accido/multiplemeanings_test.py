import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.core.accido.misc import MultipleMeanings


def test_repr():
    multiple_endings = MultipleMeanings(("a", "b", "c"))
    assert repr(multiple_endings) == "MultipleMeanings(a, b, c)"


def test_add():
    meanings1 = MultipleMeanings(("a", "b", "c"))
    meanings2 = MultipleMeanings(("d", "e", "f"))
    assert meanings1 + meanings2 == MultipleMeanings(("a", "b", "c", "d", "e", "f"))


def test_add_str():
    meanings = MultipleMeanings(("a", "b", "c"))
    assert meanings + "d" == MultipleMeanings(("a", "b", "c", "d"))
