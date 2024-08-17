# fmt: off
# mypy: ignore-errors
# ruff: noqa

import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from pathlib import Path

from python_src import lego

def test_saver():
    x = lego.reader.read_vocab_file(Path("tests/python_src.lego/test_vocab_files/regular_list.txt"))
    lego.saver.save_vocab_dump(Path("tests/python_src.lego/test_vocab_files/testdump/regular_list.testdump"), x)
    y = lego.reader.read_vocab_dump(Path("tests/python_src.lego/test_vocab_files/testdump/regular_list.testdump"))
    assert x == y
