import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pathlib import Path

import pytest
from python_src.accido.endings import Adjective, Noun, Pronoun, RegularWord, Verb
from python_src.accido.misc import Gender, MultipleMeanings
from python_src.lego.exceptions import InvalidVocabFileFormatError
from python_src.lego.misc import VocabList
from python_src.lego.reader import _regenerate_vocab_list, read_vocab_file


def test_reader():
    l = read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    assert l == VocabList([
        Verb(present="audio", infinitive="audire", perfect="audivi", ppp="auditus", meaning="hear"),
        Verb(present="capio", infinitive="capire", perfect="capivi", meaning="take"),
        Noun(nominative="puella", genitive="puellae", gender=Gender.FEMININE, meaning="girl"),
        Noun(nominative="agricola", genitive="agricolae", gender=Gender.MASCULINE, meaning="farmer"),
        Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy"),
        Noun(nominative="canis", genitive="canis", gender=Gender.MASCULINE, meaning="dog"),
        Noun(nominative="nomen", genitive="nominis", gender=Gender.NEUTER, meaning="name"),
        Adjective("ingens", "ingentis", termination=1, declension="3", meaning="large"),
        Adjective("levis", "leve", termination=2, declension="3", meaning="light"),
        Adjective("acer", "acris", "acre", termination=3, declension="3", meaning="keen"),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        RegularWord(word="in", meaning="into"),
        RegularWord(word="e", meaning="from"),
        Pronoun(pronoun="hic", meaning="this"),
        Pronoun(pronoun="ille", meaning="that"),
    ])


def test_regenerate():
    l = read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    assert l == _regenerate_vocab_list(l)


def test_reader_with_s():
    l = read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_with_s_list.txt"))
    assert l == VocabList([
        Verb(present="audio", infinitive="audire", perfect="audivi", ppp="auditus", meaning="hear"),
        Verb(present="capio", infinitive="capire", perfect="capivi", meaning="take"),
        Noun(nominative="puella", genitive="puellae", gender=Gender.FEMININE, meaning="girl"),
        Noun(nominative="agricola", genitive="agricolae", gender=Gender.MASCULINE, meaning="farmer"),
        Noun(nominative="puer", genitive="pueri", gender=Gender.MASCULINE, meaning="boy"),
        Noun(nominative="canis", genitive="canis", gender=Gender.MASCULINE, meaning="dog"),
        Noun(nominative="nomen", genitive="nominis", gender=Gender.NEUTER, meaning="name"),
        Adjective("ingens", "ingentis", termination=1, declension="3", meaning="large"),
        Adjective("levis", "leve", termination=2, declension="3", meaning="light"),
        Adjective("acer", "acris", "acre", termination=3, declension="3", meaning="keen"),
        RegularWord(word="in", meaning="into"),
        RegularWord(word="e", meaning="from"),
        Pronoun(pronoun="hic", meaning="this"),
        Pronoun(pronoun="ille", meaning="that"),
    ])


def test_multiple_meanings():
    l = read_vocab_file(Path("tests/python_src_lego/test_vocab_files/multiple_meanings_list.txt"))
    assert l == VocabList([
        Verb(present="peto", infinitive="petere", perfect="petivi", ppp="petitus", meaning=MultipleMeanings(["attack", "make for", "seek", "ask"])),
        Noun(nominative="ancilla", genitive="ancillae", gender=Gender.FEMININE, meaning=MultipleMeanings(["slave-girl", "maid"])),
    ])


def test_invalidpos():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_pos_list.txt"))
    assert "Invalid part of speech: 'Error'" == str(error.value)


def test_invalidlinefmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_linefmt_list.txt"))
    assert "Invalid line format: 'error: error: error'" == str(error.value)


def test_nopos():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/no_pos_list.txt"))
    assert "Part of speech was not given" == str(error.value)


def test_invalidverbfmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_verbfmt_list.txt"))
    assert "Invalid verb format: 'hear: audio, audire, audivi, auditus, error, error, error'" == str(error.value)


def test_invalidnounfmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_nounfmt_list.txt"))
    assert "Invalid noun format: 'dog: canis, canis, error, error'" == str(error.value)


def test_invalidadjfmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_adjfmt_list.txt"))
    assert "Invalid adjective format: 'good: bonus, bona, bonum, error, error'" == str(error.value)


def test_decl1():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_decl1_list.txt"))
    assert "Invalid adjective declension: '3'" == str(error.value)


def test_decl2():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_decl2_list.txt"))
    assert "Invalid adjective declension: '4'" == str(error.value)


def test_invalid_gender():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/python_src_lego/test_vocab_files/invalid_gender_list.txt"))
    assert "Invalid gender: 'l'" == str(error.value)
