import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import EndingComponents
from python_src.transfero.words import find_noun_inflections


class TestNounInflectErrors:
    def test_noun_error_1(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(case="error", number="singular"))
        assert str(error.value) == "Case 'error' not recognised"

    def test_noun_error_2(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(case="nominative", number="error"))
        assert str(error.value) == "Number 'error' not recognised"


class TestNounInflection:
    def test_noun_inflections_1(self):
        word = "house"
        assert find_noun_inflections(word, EndingComponents(case="nominative", number="singular")) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="singular")) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="singular")) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="singular")) == {"house"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="singular")) == {"of the house", "house's", "of a house"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="singular")) == {"for the house", "to the house", "for a house", "to a house"}

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="plural")) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="plural")) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="plural")) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="plural")) == {"houses"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="plural")) == {"of the houses", "houses'"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="plural")) == {"for the houses", "for houses", "to the houses", "to houses"}

    def test_noun_inflections_2(self):
        word = "cactus"

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="genitive", number="singular")) == {"of the cactus", "cactus'", "of a cactus"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="singular")) == {"for the cactus", "to the cactus", "for a cactus", "to a cactus"}

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="plural")) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="plural")) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="plural")) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="plural")) == {"cacti", "cactuses"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="plural")) == {"of the cacti", "cacti's", "of the cactuses", "cactuses'"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="plural")) == {"for the cacti", "for cacti", "to the cacti", "to cacti", "for the cactuses", "for cactuses", "to the cactuses", "to cactuses"}
