import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import re
from pathlib import Path

import pytest
from python_src import lego
from python_src.lego.exceptions import MisleadingFilenameWarning


def test_saver():
    x = lego.reader.read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    lego.saver.save_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.testdump"), x)
    y = lego.reader.read_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.testdump"))
    assert x == y


def test_saver_wronglz4extension():
    x = lego.reader.read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    with pytest.warns(MisleadingFilenameWarning, match=re.escape("The file 'tests/python_src_lego/test_vocab_files/testdump/regular_list.testdump.wrong.lz4' is not being compressed, but the file extension ('.lz4') suggests it is.")):
        lego.saver.save_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.testdump.wrong.lz4"), x, compress=False)


def test_saver_compress():
    x = lego.reader.read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    lego.saver.save_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.testdump.lz4"), x, compress=True)
    y = lego.reader.read_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.testdump.lz4"))
    assert x == y


def test_saver_compress_nolz4extension():
    x = lego.reader.read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    with pytest.warns(MisleadingFilenameWarning, match=re.escape("The file 'tests/python_src_lego/test_vocab_files/testdump/regular_list.compressedtestdump' is being compressed, but the '.lz4' extension is not present and is being added.")):
        lego.saver.save_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.compressedtestdump"), x, compress=True)
    y = lego.reader.read_vocab_dump(Path("tests/python_src_lego/test_vocab_files/testdump/regular_list.compressedtestdump.lz4"))
    assert x == y


def test_nodirectory():
    x = lego.reader.read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    with pytest.raises(FileNotFoundError) as error:
        lego.saver.save_vocab_dump(Path("tests/python_src_lego/test_vocab_filesajofsdifhbd/testdump/regular_list.testdump"), x)
    assert "The directory 'tests/python_src_lego/test_vocab_filesajofsdifhbd/testdump' does not exist" == str(error.value)
