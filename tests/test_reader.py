# fmt: off
# mypy: ignore-errors
# ruff: noqa

import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from python_src.accido.endings import LearningVerb, Adjective, RegularWord, Noun, Pronoun
from python_src.lego.reader import read_vocab_file
from python_src.lego.custom_exceptions import InvalidVocabFileFormat
from io import StringIO

def test_reader():
    with open("tests/test_vocab_files/regular_list.txt") as file:
        data = file.read()
    stream = StringIO(data)
    l = read_vocab_file(stream)
    assert l == [
        LearningVerb(present="audio", infinitive="audire", perfect="audivi", ppp="auditus", meaning="hear"),
        LearningVerb(present="capio", infinitive="capire", perfect="capivi", meaning="take"),
        Noun(nominative="puella", genitive="puellae", gender="feminine", meaning="girl"),
        Noun(nominative="agricola", genitive="agricolae", gender="masculine", meaning="farmer"),
        Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy"),
        Noun(nominative="canis", genitive="canis", gender="masculine", meaning="dog"),
        Noun(nominative="nomen", genitive="nominis", gender="neuter", meaning="name"),
        Adjective("ingens", "ingentis", termination=1, declension="3", meaning="large"),
        Adjective("levis", "leve", termination=2, declension="3", meaning="light"),
        Adjective("acer", "acris", "acre", termination=3, declension="3", meaning="keen"),
        Adjective("celer", "celeris", "celere", termination=3, declension="3", meaning="quick"),
        RegularWord(word="in", meaning="into"),
        RegularWord(word="e", meaning="from"),
        Pronoun(pronoun="hic", meaning="this"),
        Pronoun(pronoun="ille", meaning="that")
    ]

def test_reader_with_s():
    with open("tests/test_vocab_files/regular_with_s_list.txt") as file:
        data = file.read()
    stream = StringIO(data)
    l = read_vocab_file(stream)
    assert l == [
        LearningVerb(present="audio", infinitive="audire", perfect="audivi", ppp="auditus", meaning="hear"),
        LearningVerb(present="capio", infinitive="capire", perfect="capivi", meaning="take"),
        Noun(nominative="puella", genitive="puellae", gender="feminine", meaning="girl"),
        Noun(nominative="agricola", genitive="agricolae", gender="masculine", meaning="farmer"),
        Noun(nominative="puer", genitive="pueri", gender="masculine", meaning="boy"),
        Noun(nominative="canis", genitive="canis", gender="masculine", meaning="dog"),
        Noun(nominative="nomen", genitive="nominis", gender="neuter", meaning="name"),
        Adjective("ingens", "ingentis", termination=1, declension="3", meaning="large"),
        Adjective("levis", "leve", termination=2, declension="3", meaning="light"),
        Adjective("acer", "acris", "acre", termination=3, declension="3", meaning="keen"),
        Adjective("celer", "celeris", "celere", termination=3, declension="3", meaning="quick"),
        RegularWord(word="in", meaning="into"),
        RegularWord(word="e", meaning="from"),
        Pronoun(pronoun="hic", meaning="this"),
        Pronoun(pronoun="ille", meaning="that")
    ]

def test_invalidpos():
    with open("tests/test_vocab_files/invalid_pos_list.txt") as file:
        data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid part of speech: Error"==str(error.value)

def test_invalidlinefmt():
    with open("tests/test_vocab_files/invalid_linefmt_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid line format: error: error: error"==str(error.value)

def test_nopos():
    with open("tests/test_vocab_files/no_pos_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Part of speech was not given"==str(error.value)

def test_invalidverbfmt():
    with open("tests/test_vocab_files/invalid_verbfmt_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid verb format: hear: audio, audire, audivi, auditus, error, error, error"==str(error.value)

def test_invalidnounfmt():
    with open("tests/test_vocab_files/invalid_nounfmt_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid noun format: dog: canis, canis, error, error"==str(error.value)

def test_invalidgender():
    with open("tests/test_vocab_files/invalid_gender_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid gender: l"==str(error.value)

def test_invalidadjfmt():
    with open("tests/test_vocab_files/invalid_adjfmt_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid adjective format: good: bonus, bona, bonum, error, error"==str(error.value)

def test_decl1():
    with open("tests/test_vocab_files/invalid_decl1_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid adjective declension: 3"==str(error.value)

def test_decl2():
    with open("tests/test_vocab_files/invalid_decl2_list.txt") as file:
         data = file.read()
    stream = StringIO(data)
    with pytest.raises(InvalidVocabFileFormat) as error:
        l = read_vocab_file(stream)
    assert "Invalid adjective declension: 4"==str(error.value)
