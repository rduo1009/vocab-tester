import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pathlib import Path

from python_src import lego


def test_cache():
    hash_string = "219fc649c2e04aba7788c48c363bca798b278c9e509b7a14622f0da3ff8f22a7"
    x, _ = lego.cache.cache_vocab_file(Path("tests/python_src.lego/test_vocab_files/testdump/cache"), Path("tests/python_src.lego/test_vocab_files/regular_list.txt"))
    y = lego.reader.read_vocab_dump(Path(f"tests/python_src.lego/test_vocab_files/testdump/cache/{hash_string}"))
    assert x == y


def test_regenerate_cache():
    _, _ = lego.cache.cache_vocab_file(Path("tests/python_src.lego/test_vocab_files/testdump/cache"), Path("tests/python_src.lego/test_vocab_files/regular_with_s_list.txt"))
    _, y = lego.cache.cache_vocab_file(Path("tests/python_src.lego/test_vocab_files/testdump/cache"), Path("tests/python_src.lego/test_vocab_files/regular_with_s_list.txt"))
    assert y
