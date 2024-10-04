import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from python_src import accido
from python_src.accido.misc import Case, Degree, Gender, Mood, Number, Tense, Voice
from python_src.transfero.words import find_inflection


def test_wordinflection_errors():
    with pytest.raises(ValueError) as error:
        find_inflection("test", accido.endings._Word, accido.misc.EndingComponents(tense=Tense.PRESENT, voice=Voice.ACTIVE, mood=Mood.INFINITIVE))  # type: ignore[type-abstract]
    assert str(error.value) == "Unknown part of speech: <class 'python_src.accido.class_word._Word'>"


def test_wordinflection_adjective():
    assert find_inflection("happy", accido.endings.Adjective, accido.misc.EndingComponents(case=Case.NOMINATIVE, gender=Gender.MASCULINE, number=Number.SINGULAR, degree=Degree.COMPARATIVE)) == {"happier", "more happy"}


def test_wordinflection_adverb():
    assert find_inflection("sad", accido.endings.Adjective, accido.misc.EndingComponents(degree=Degree.POSITIVE)) == {"sadly"}


def test_wordinflection_noun():
    assert find_inflection("house", accido.endings.Noun, accido.misc.EndingComponents(case=Case.DATIVE, number=Number.PLURAL)) == {"to houses", "to the houses", "for houses", "for the houses"}


def test_wordinflection_verb():
    assert find_inflection("teach", accido.endings.Verb, accido.misc.EndingComponents(tense=Tense.IMPERFECT, voice=Voice.ACTIVE, mood=Mood.INDICATIVE, number=Number.PLURAL, person=1)) == {"we were teaching"}


def test_wordinflection_pronoun():
    assert find_inflection("I", accido.endings.Pronoun, accido.misc.EndingComponents(case=Case.NOMINATIVE, number=Number.SINGULAR)) == {"I"}


def test_wordinflection_regularword():
    assert find_inflection("in", accido.endings.RegularWord, accido.misc.EndingComponents()) == {"in"}
