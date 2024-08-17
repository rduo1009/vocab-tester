# fmt: off
# mypy: ignore-errors

import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.endings import RegularWord
from python_src.accido.misc import MultipleMeanings


def test_one_meaning():
    word = RegularWord("test1", "test2")
    assert word.meaning.__str__() == "test2"


def test_multiple_meanings():
    word = RegularWord("test1", MultipleMeanings(["test2", "test3", "test4"]))
    assert word.meaning.__str__() == "test2"

#def test_pick():
#    word = RegularWord("test1", "test2")
#    word.pick()
