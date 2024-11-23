import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from src.core.accido.endings import Noun, RegularWord
from src.core.accido.misc import Gender, MultipleMeanings


class TestRegular:
    def test_one_meaning(self):
        word = RegularWord("test1", meaning="test2")
        assert word.meaning.__str__() == "test2"

    def test_multiple_meanings(self):
        word = RegularWord("test1", meaning=MultipleMeanings(("test2", "test3", "test4")))
        assert word.meaning.__str__() == "test2"


class TestRegularDunder:
    # def test_pick(self):
    #     word = RegularWord("test1", "test2")
    #     word.pick()

    def test_get(self):
        word = RegularWord("test1", meaning="test2")
        assert word.get() == "test1"

    def test_repr(self):
        word = RegularWord("test1", meaning="test2")
        assert word.__repr__() == "RegularWord(test1, test2)"

    def test_add_different_word(self):
        word1 = RegularWord("test1", meaning="test2")
        word2 = RegularWord("test3", meaning="test4")
        with pytest.raises(TypeError):
            word1 + word2

    def test_add_different_pos(self):
        word1 = RegularWord("test1", meaning="test2")
        word2 = Noun("puella", "puellae", gender=Gender.FEMININE, meaning="girl")
        with pytest.raises(TypeError):
            word1 + word2

    def test_add(self):
        word1 = RegularWord("test1", meaning="test2")
        word2 = RegularWord("test1", meaning="test3")
        assert word1 + word2 == RegularWord("test1", meaning=MultipleMeanings(("test2", "test3")))
