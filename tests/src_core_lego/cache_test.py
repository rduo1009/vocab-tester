import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pathlib import Path

from src.core.lego.cache import cache_vocab_file
from src.core.lego.reader import read_vocab_dump


def test_cache():
    hash_string = "66c21bdeb3dcfc4673e51ad4a2513e75ed1cea2e18047847e0f1a1f6f71070d7"
    x, _ = cache_vocab_file(Path("tests/src_core_lego/test_vocab_files/testdump/cache"), Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    y = read_vocab_dump(Path(f"tests/src_core_lego/test_vocab_files/testdump/cache/{hash_string}"))
    assert x == y


def test_regenerate_cache():
    _, _ = cache_vocab_file(Path("tests/src_core_lego/test_vocab_files/testdump/cache"), Path("tests/src_core_lego/test_vocab_files/regular_with_s_list.txt"))
    _, y = cache_vocab_file(Path("tests/src_core_lego/test_vocab_files/testdump/cache"), Path("tests/src_core_lego/test_vocab_files/regular_with_s_list.txt"))
    assert y
