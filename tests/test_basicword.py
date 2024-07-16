import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from grammatica.endings import BasicWord
from grammatica.misc import MultipleMeanings


def test_one_meaning():
    word = BasicWord("test1", "test2")
    assert word.meaning.__str__() == "test2"


def test_multiple_meanings():
    word = BasicWord("test1", MultipleMeanings("test2", ["test3", "test4"]))
    assert word.meaning.__str__() == "test2"
