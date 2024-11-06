import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from python_src import accido
from python_src.accido.misc import Case, ComponentsSubtype, Degree, Gender, Mood, Number, Tense, Voice
from python_src.transfero.words import find_inflection


def test_wordinflection_adjective():
    assert find_inflection("happy", accido.misc.EndingComponents(case=Case.NOMINATIVE, gender=Gender.MASCULINE, number=Number.SINGULAR, degree=Degree.COMPARATIVE)) == {"happier", "more happy"}


def test_wordinflection_adverb():
    assert find_inflection("sad", accido.misc.EndingComponents(degree=Degree.POSITIVE)) == {"sadly"}


def test_wordinflection_noun():
    assert find_inflection("house", accido.misc.EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"to houses", "to the houses", "for houses", "for the houses"}


def test_wordinflection_verb():
    assert find_inflection("teach", accido.misc.EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we were teaching"}


def test_wordinflection_pronoun():
    assert find_inflection("this", accido.misc.EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE)) == {"this"}


def test_wordinflection_regularword():
    assert find_inflection("in", accido.misc.EndingComponents()) == {"in"}


def test_mainwordinflection_adjective():
    assert find_inflection("happy", accido.misc.EndingComponents(case=Case.NOMINATIVE, gender=Gender.MASCULINE, number=Number.SINGULAR, degree=Degree.COMPARATIVE), main=True) == "happier"


def test_mainwordinflection_adverb():
    assert find_inflection("sad", accido.misc.EndingComponents(degree=Degree.POSITIVE), main=True) == "sadly"


def test_mainwordinflection_noun():
    assert find_inflection("house", accido.misc.EndingComponents(case=Case.DATIVE, number=Number.PLURAL), main=True) == "for the houses"


def test_mainwordinflection_verb():
    assert find_inflection("teach", accido.misc.EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1), main=True) == "we were teaching"


def test_mainwordinflection_pronoun():
    assert find_inflection("this", accido.misc.EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR, gender=Gender.MASCULINE), main=True) == "this"


def test_mainwordinflection_regularword():
    assert find_inflection("in", accido.misc.EndingComponents(), main=True) == "in"


def test_mainwordinflection_nounlikepronoun():
    components = accido.misc.EndingComponents(case=Case.GENITIVE, number=Number.SINGULAR)
    components.subtype = ComponentsSubtype.PRONOUN
    assert find_inflection("I", components, main=True) == "of me"
