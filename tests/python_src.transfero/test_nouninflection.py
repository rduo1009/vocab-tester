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

    def test_noun_error_3(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(case="nominative"))
        assert str(error.value) == "Number must be specified"

    def test_noun_error_4(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(number="singular"))
        assert str(error.value) == "Case must be specified"


class TestNounInflection:
    def test_noun_inflections_1(self):
        word = "house"
        assert find_noun_inflections(word, EndingComponents(case="nominative", number="singular")) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="singular")) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="singular")) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="singular")) == {"house", "with the house", "with a house", "by the house", "by a house", "by means of the house", "by means of a house"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="singular")) == {"of the house", "house's", "of a house"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="singular")) == {"for the house", "to the house", "for a house", "to a house"}

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="plural")) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="plural")) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="plural")) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="plural")) == {"houses", "with the houses", "by the houses", "by means of the houses"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="plural")) == {"of the houses", "houses'"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="plural")) == {"for the houses", "for houses", "to the houses", "to houses"}

    def test_noun_inflections_2(self):
        word = "cactus"

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="singular")) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="singular")) == {"cactus", "with the cactus", "with a cactus", "by the cactus", "by a cactus", "by means of the cactus", "by means of a cactus"}
        assert find_noun_inflections(word, EndingComponents(case="genitive", number="singular")) == {"of the cactus", "cactus'", "of a cactus"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="singular")) == {"for the cactus", "to the cactus", "for a cactus", "to a cactus"}

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="plural")) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="plural")) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="plural")) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="plural")) == {"cacti", "with the cacti", "by the cacti", "by means of the cacti", "cactuses", "with the cactuses", "by the cactuses", "by means of the cactuses"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="plural")) == {"of the cacti", "cacti's", "of the cactuses", "cactuses'"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="plural")) == {"for the cacti", "for cacti", "to the cacti", "to cacti", "for the cactuses", "for cactuses", "to the cactuses", "to cactuses"}

    def test_noun_inflections_3(self):
        word = "apple"

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="singular")) == {"apple"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="singular")) == {"apple"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="singular")) == {"apple"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="singular")) == {"apple", "with the apple", "with an apple", "by the apple", "by an apple", "by means of the apple", "by means of an apple"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="singular")) == {"of the apple", "apple's", "of an apple"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="singular")) == {"for the apple", "to the apple", "for an apple", "to an apple"}

        assert find_noun_inflections(word, EndingComponents(case="nominative", number="plural")) == {"apples"}
        assert find_noun_inflections(word, EndingComponents(case="vocative", number="plural")) == {"apples"}
        assert find_noun_inflections(word, EndingComponents(case="accusative", number="plural")) == {"apples"}
        assert find_noun_inflections(word, EndingComponents(case="ablative", number="plural")) == {"apples", "with the apples", "by the apples", "by means of the apples"}

        assert find_noun_inflections(word, EndingComponents(case="genitive", number="plural")) == {"of the apples", "apples'"}
        assert find_noun_inflections(word, EndingComponents(case="dative", number="plural")) == {"for the apples", "for apples", "to the apples", "to apples"}
