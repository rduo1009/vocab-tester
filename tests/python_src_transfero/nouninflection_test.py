import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src.accido.misc import Case, EndingComponents, Number
from python_src.transfero.words import find_noun_inflections


class TestNounInflectErrors:
    def test_noun_error_1(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(case="error", number=Number.SINGULAR))
        assert str(error.value) == "Invalid case: 'error'"

    def test_noun_error_2(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(case=Case.NOMINATIVE, number="error"))
        assert str(error.value) == "Invalid number: 'error'"

    def test_noun_error_3(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(case=Case.NOMINATIVE))
        assert str(error.value) == "Number must be specified"

    def test_noun_error_4(self):
        with pytest.raises(ValueError) as error:
            find_noun_inflections("house", EndingComponents(number=Number.SINGULAR))
        assert str(error.value) == "Case must be specified"


class TestNounInflection:
    def test_noun_inflections_1(self):
        word = "house"
        assert find_noun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == {"house"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == {"house", "with the house", "with a house", "by the house", "by a house", "by means of the house", "by means of a house"}

        assert find_noun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == {"of the house", "house's", "of a house"}
        assert find_noun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == {"for the house", "to the house", "for a house", "to a house"}

        assert find_noun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == {"houses"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == {"houses", "with the houses", "by the houses", "by means of the houses"}

        assert find_noun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == {"of the houses", "houses'"}
        assert find_noun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"for the houses", "for houses", "to the houses", "to houses"}

    def test_noun_inflections_2(self):
        word = "cactus"

        assert find_noun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == {"cactus"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == {"cactus", "with the cactus", "with a cactus", "by the cactus", "by a cactus", "by means of the cactus", "by means of a cactus"}
        assert find_noun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == {"of the cactus", "cactus'", "of a cactus"}
        assert find_noun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == {"for the cactus", "to the cactus", "for a cactus", "to a cactus"}

        assert find_noun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == {"cacti", "cactuses"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == {"cacti", "with the cacti", "by the cacti", "by means of the cacti", "cactuses", "with the cactuses", "by the cactuses", "by means of the cactuses"}

        assert find_noun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == {"of the cacti", "cacti's", "of the cactuses", "cactuses'"}
        assert find_noun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"for the cacti", "for cacti", "to the cacti", "to cacti", "for the cactuses", "for cactuses", "to the cactuses", "to cactuses"}

    def test_noun_inflections_3(self):
        word = "apple"

        assert find_noun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == {"apple"}
        assert find_noun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.SINGULAR)) == {"apple"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.SINGULAR)) == {"apple"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.SINGULAR)) == {"apple", "with the apple", "with an apple", "by the apple", "by an apple", "by means of the apple", "by means of an apple"}

        assert find_noun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)) == {"of the apple", "apple's", "of an apple"}
        assert find_noun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.SINGULAR)) == {"for the apple", "to the apple", "for an apple", "to an apple"}

        assert find_noun_inflections(word, EndingComponents(case=Case.NOMINATIVE, number=Number.PLURAL)) == {"apples"}
        assert find_noun_inflections(word, EndingComponents(case=Case.VOCATIVE, number=Number.PLURAL)) == {"apples"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ACCUSATIVE, number=Number.PLURAL)) == {"apples"}
        assert find_noun_inflections(word, EndingComponents(case=Case.ABLATIVE, number=Number.PLURAL)) == {"apples", "with the apples", "by the apples", "by means of the apples"}

        assert find_noun_inflections(word, EndingComponents(case=Case.GENITIVE, number=Number.PLURAL)) == {"of the apples", "apples'"}
        assert find_noun_inflections(word, EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"for the apples", "for apples", "to the apples", "to apples"}
