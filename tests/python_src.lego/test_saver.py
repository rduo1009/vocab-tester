import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pathlib import Path

import pytest
from python_src import lego


def test_saver():
    x = lego.reader.read_vocab_file(Path("tests/python_src.lego/test_vocab_files/regular_list.txt"))
    lego.saver.save_vocab_dump(Path("tests/python_src.lego/test_vocab_files/testdump/regular_list.testdump"), x)
    y = lego.reader.read_vocab_dump(Path("tests/python_src.lego/test_vocab_files/testdump/regular_list.testdump"))
    assert x == y


def test_nodirectory():
    x = lego.reader.read_vocab_file(Path("tests/python_src.lego/test_vocab_files/regular_list.txt"))
    with pytest.raises(FileNotFoundError) as error:
        lego.saver.save_vocab_dump(Path("tests/python_src.lego/test_vocab_filesajofsdifhbd/testdump/regular_list.testdump"), x)
    assert "The directory tests/python_src.lego/test_vocab_filesajofsdifhbd/testdump does not exist." == str(error.value)
