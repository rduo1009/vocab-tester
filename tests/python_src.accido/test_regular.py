import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest  # type: ignore[import-not-found]
from python_src.accido.endings import RegularWord
from python_src.accido.misc import MultipleMeanings


class TestRegular:
    def test_one_meaning(self):
        word = RegularWord("test1", "test2")
        assert word.meaning.__str__() == "test2"

    def test_multiple_meanings(self):
        word = RegularWord("test1", MultipleMeanings(["test2", "test3", "test4"]))
        assert word.meaning.__str__() == "test2"


class TestRegularDunder:
    # def test_pick(self):
    #     word = RegularWord("test1", "test2")
    #     word.pick()

    def test_get(self):
        word = RegularWord("test1", "test2")
        assert word.get() == "test1"

    def test_repr(self):
        word = RegularWord("test1", "test2")
        assert word.__repr__() == "RegularWord(test1, test2)"
