# ruff: noqa
# mypy: ignore-errors

import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grammatica.misc import MultipleEndings


def test_multiple_endings():
    multiple_endings = MultipleEndings(baz="a", foo="b", bar="c")
    assert multiple_endings.baz == "a"
    assert multiple_endings.foo == "b"
    assert multiple_endings.bar == "c"
    assert multiple_endings.get_all() == ["a", "b", "c"]
    assert multiple_endings + "\n" == "a/b/c\n"
