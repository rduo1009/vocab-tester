import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pathlib import Path

import pytest
from src.core.accido.endings import Adjective, Noun, Pronoun, RegularWord, Verb
from src.core.accido.misc import Gender, MultipleMeanings
from src.core.lego.exceptions import InvalidVocabFileFormatError
from src.core.lego.misc import VocabList
from src.core.lego.reader import _regenerate_vocab_list, read_vocab_file


def test_reader():
    l = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    assert l == VocabList([
        Verb("audio", "audire", "audivi", "auditus", meaning="hear"),
        Verb("capio", "capire", "capivi", meaning="take"),
        Noun("puella", "puellae", gender=Gender.FEMININE, meaning="girl"),
        Noun("agricola", "agricolae", gender=Gender.MASCULINE, meaning="farmer"),
        Noun("puer", "pueri", gender=Gender.MASCULINE, meaning="boy"),
        Noun("canis", "canis", gender=Gender.MASCULINE, meaning="dog"),
        Noun("nomen", "nominis", gender=Gender.NEUTER, meaning="name"),
        Adjective("ingens", "ingentis", termination=1, declension="3", meaning="large"),
        Adjective("levis", "leve", termination=2, declension="3", meaning="light"),
        Adjective("acer", "acris", "acre", termination=3, declension="3", meaning="keen"),
        Adjective("bonus", "bona", "bonum", declension="212", meaning="good"),
        Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy"),
        RegularWord("in", meaning="into"),
        RegularWord("e", meaning="from"),
        Pronoun("hic", meaning="this"),
        Pronoun("ille", meaning="that"),
    ])


def test_regenerate():
    l = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_list.txt"))
    assert l == _regenerate_vocab_list(l)


def test_reader_with_s():
    l = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/regular_with_s_list.txt"))
    assert l == VocabList([
        Verb("audio", "audire", "audivi", "auditus", meaning="hear"),
        Verb("capio", "capire", "capivi", meaning="take"),
        Noun("puella", "puellae", gender=Gender.FEMININE, meaning="girl"),
        Noun("agricola", "agricolae", gender=Gender.MASCULINE, meaning="farmer"),
        Noun("puer", "pueri", gender=Gender.MASCULINE, meaning="boy"),
        Noun("canis", "canis", gender=Gender.MASCULINE, meaning="dog"),
        Noun("nomen", "nominis", gender=Gender.NEUTER, meaning="name"),
        Adjective("ingens", "ingentis", termination=1, declension="3", meaning="large"),
        Adjective("levis", "leve", termination=2, declension="3", meaning="light"),
        Adjective("acer", "acris", "acre", termination=3, declension="3", meaning="keen"),
        RegularWord("in", meaning="into"),
        RegularWord("e", meaning="from"),
        Pronoun("hic", meaning="this"),
        Pronoun("ille", meaning="that"),
    ])


def test_multiple_meanings():
    l = read_vocab_file(Path("tests/src_core_lego/test_vocab_files/multiple_meanings_list.txt"))
    assert l == VocabList([
        Verb("peto", "petere", "petivi", "petitus", meaning=MultipleMeanings(("attack", "make for", "seek", "ask"))),
        Noun("ancilla", "ancillae", gender=Gender.FEMININE, meaning=MultipleMeanings(("slave-girl", "maid"))),
    ])


def test_invalidpos():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_pos_list.txt"))
    assert "Invalid part of speech: 'Error'" == str(error.value)


def test_invalidlinefmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_linefmt_list.txt"))
    assert "Invalid line format: 'error: error: error'" == str(error.value)


def test_nopos():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/no_pos_list.txt"))
    assert "Part of speech was not given" == str(error.value)


def test_invalidverbfmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_verbfmt_list.txt"))
    assert "Invalid verb format: 'hear: audio, audire, audivi, auditus, error, error, error'" == str(error.value)


def test_invalidnounfmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_nounfmt_list.txt"))
    assert "Invalid noun format: 'dog: canis, canis, error, error'" == str(error.value)


def test_invalidadjfmt():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_adjfmt_list.txt"))
    assert "Invalid adjective format: 'good: bonus, bona, bonum, error, error'" == str(error.value)


def test_decl1():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_decl1_list.txt"))
    assert "Invalid adjective declension: '3'" == str(error.value)


def test_decl2():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_decl2_list.txt"))
    assert "Invalid adjective declension: '4'" == str(error.value)


def test_invalid_gender():
    with pytest.raises(InvalidVocabFileFormatError) as error:
        read_vocab_file(Path("tests/src_core_lego/test_vocab_files/invalid_gender_list.txt"))
    assert "Invalid gender: 'l'" == str(error.value)
