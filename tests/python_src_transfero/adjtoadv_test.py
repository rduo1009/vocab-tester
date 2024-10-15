import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.transfero.exceptions import InvalidWordError
from python_src.transfero.words import adj_to_adv


def test_adjtoadv():
    assert adj_to_adv("happy") == "happily"
    assert adj_to_adv("great") == "greatly"
    assert adj_to_adv("monotonous") == "monotonously"


def test_adjtoadv_error():
    with pytest.raises(InvalidWordError) as error:
        adj_to_adv("house")
    assert "Word 'house' is not an adjective" == str(error.value)
