# fmt: off
# mypy: ignore-errors

import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from accido.endings import BasicWord
from accido.misc import MultipleMeanings


def test_one_meaning():
    word = BasicWord("test1", "test2")
    assert word.meaning.__str__() == "test2"


def test_multiple_meanings():
    word = BasicWord("test1", MultipleMeanings(["test2", "test3", "test4"]))
    assert word.meaning.__str__() == "test2"

def test_pick():
    word = BasicWord("test1", "test2")
    word.pick()
