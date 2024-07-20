# fmt: off
# mypy: ignore-errors

import sys, os  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from grammatica.endings import Pronoun
from grammatica.edge_cases import PRONOUNS


def test_pronoun():
    assert Pronoun(pronoun="hic", meaning="this").endings == PRONOUNS["hic"]
