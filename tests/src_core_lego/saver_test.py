import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import re
from pathlib import Path

import pytest
from src.core.lego.exceptions import MisleadingFilenameWarning
from src.core.lego.reader import read_vocab_dump, read_vocab_file
from src.core.lego.saver import save_vocab_dump


def test_saver():
    x = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    save_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.testdump"), x)
    y = read_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.testdump"))
    assert x == y


def test_saver_wronglz4extension():
    x = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    with pytest.warns(MisleadingFilenameWarning, match=re.escape("The file 'tests/src_core_lego/test_vocab_files/testdump/regular_list.testdump.wrong.lz4' is not being compressed, but the file extension ('.lz4') suggests it is.")):
        save_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.testdump.wrong.lz4"), x, compress=False)


def test_saver_compress():
    x = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    save_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.testdump.lz4"), x, compress=True)
    y = read_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.testdump.lz4"))
    assert x == y


def test_saver_compress_nolz4extension():
    x = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    with pytest.warns(MisleadingFilenameWarning, match=re.escape("The file 'tests/src_core_lego/test_vocab_files/testdump/regular_list.compressedtestdump' is being compressed, but the '.lz4' extension is not present and is being added.")):
        save_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.compressedtestdump"), x, compress=True)
    y = read_vocab_dump(Path("tests/src_core_lego/test_vocab_files/testdump/regular_list.compressedtestdump.lz4"))
    assert x == y


def test_nodirectory():
    x = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    with pytest.raises(FileNotFoundError) as error:
        save_vocab_dump(Path("tests/src_core_lego/test_vocab_filesajofsdifhbd/testdump/regular_list.testdump"), x)
    assert "The directory 'tests/src_core_lego/test_vocab_filesajofsdifhbd/testdump' does not exist" == str(error.value)
