import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pathlib import Path

import pytest
from python_src.accido.endings import Adjective, Noun, Pronoun, RegularWord, Verb
from python_src.accido.misc import Gender
from python_src.lego.misc import VocabList
from python_src.lego.reader import read_vocab_file
from python_src.rogo.asker import ask_question_without_sr
from python_src.rogo.question_classes import ParseWordCompToLatQuestion
from python_src.rogo.type_aliases import Settings

settings: Settings = {
    "exclude-verb-present-active-indicative": False,
    "exclude-verb-imperfect-active-indicative": False,
    "exclude-verb-perfect-active-indicative": False,
    "exclude-verb-pluperfect-active-indicative": False,
    "exclude-verb-present-active-infinitive": False,
    "exclude-verb-present-active-imperative": False,
    "exclude-verb-imperfect-active-subjunctive": False,
    "exclude-verb-pluperfect-active-subjunctive": False,
    "exclude-verb-singular": False,
    "exclude-verb-plural": False,
    "exclude-verb-1st-person": False,
    "exclude-verb-2nd-person": False,
    "exclude-verb-3rd-person": False,
    "exclude-participles": False,
    "exclude-participle-present-active": False,
    "exclude-participle-perfect-passive": False,
    "exclude-participle-masculine": False,
    "exclude-participle-feminine": False,
    "exclude-participle-neuter": False,
    "exclude-participle-nominative": False,
    "exclude-participle-vocative": False,
    "exclude-participle-accusative": False,
    "exclude-participle-genitive": False,
    "exclude-participle-dative": False,
    "exclude-participle-ablative": False,
    "exclude-participle-singular": False,
    "exclude-participle-plural": False,
    "exclude-noun-nominative": False,
    "exclude-noun-vocative": False,
    "exclude-noun-accusative": False,
    "exclude-noun-genitive": False,
    "exclude-noun-dative": False,
    "exclude-noun-ablative": False,
    "exclude-noun-singular": False,
    "exclude-noun-plural": False,
    "exclude-adjective-masculine": False,
    "exclude-adjective-feminine": False,
    "exclude-adjective-neuter": False,
    "exclude-adjective-nominative": False,
    "exclude-adjective-vocative": False,
    "exclude-adjective-accusative": False,
    "exclude-adjective-genitive": False,
    "exclude-adjective-dative": False,
    "exclude-adjective-ablative": False,
    "exclude-adjective-singular": False,
    "exclude-adjective-plural": False,
    "exclude-adjective-positive": False,
    "exclude-adjective-comparative": False,
    "exclude-adjective-superlative": False,
    "exclude-adverbs": False,
    "exclude-adverb-positive": False,
    "exclude-adverb-comparative": False,
    "exclude-adverb-superlative": False,
    "exclude-pronoun-masculine": False,
    "exclude-pronoun-feminine": False,
    "exclude-pronoun-neuter": False,
    "exclude-pronoun-nominative": False,
    "exclude-pronoun-vocative": False,
    "exclude-pronoun-accusative": False,
    "exclude-pronoun-genitive": False,
    "exclude-pronoun-dative": False,
    "exclude-pronoun-ablative": False,
    "exclude-pronoun-singular": False,
    "exclude-pronoun-plural": False,
    "exclude-nouns": False,
    "exclude-verbs": False,
    "exclude-adjectives": False,
    "exclude-pronouns": False,
    "exclude-regulars": False,
    "exclude-verb-first-conjugation": False,
    "exclude-verb-second-conjugation": False,
    "exclude-verb-third-conjugation": False,
    "exclude-verb-fourth-conjugation": False,
    "exclude-verb-thirdio-conjugation": False,
    "exclude-verb-irregular-conjugation": False,
    "exclude-noun-first-declension": False,
    "exclude-noun-second-declension": False,
    "exclude-noun-third-declension": False,
    "exclude-noun-fourth-declension": False,
    "exclude-noun-fifth-declension": False,
    "exclude-noun-irregular-declension": False,
    "exclude-adjective-212-declension": False,
    "exclude-adjective-third-declension": False,
    "include-typein-engtolat": False,
    "include-typein-lattoeng": False,
    "include-parse": False,
    "include-inflect": True,
    "include-principal-parts": False,
    "include-multiplechoice-engtolat": False,
    "include-multiplechoice-lattoeng": False,
    "number-multiplechoice-options": 3,
}


@pytest.mark.manual
def test_inflect_question():
    vocab_list = read_vocab_file(Path("tests/python_src_lego/test_vocab_files/regular_list.txt"))
    amount = 50
    for output in ask_question_without_sr(vocab_list, amount, settings):
        assert type(output) is ParseWordCompToLatQuestion

        assert output.check(output.main_answer)
        ic(output)  # type: ignore[name-defined] # noqa: F821


def test_inflect_question_adjective():
    word = Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")
    vocab_list = VocabList([word])
    amount = 500

    for output in ask_question_without_sr(vocab_list, amount, settings):
        assert type(output) is ParseWordCompToLatQuestion
        assert output.check(output.main_answer)

        assert output.main_answer in word.endings.values()
        assert output.main_answer in output.answers

        for answer in output.answers:
            assert answer in word.endings.values()
            assert output.components in word.find(answer)

        assert output.prompt == str(word)


def test_inflect_question_noun():
    word = Noun("puella", "puellae", gender=Gender.FEMININE, meaning="girl")
    vocab_list = VocabList([word])
    amount = 500

    for output in ask_question_without_sr(vocab_list, amount, settings):
        assert type(output) is ParseWordCompToLatQuestion
        assert output.check(output.main_answer)

        assert output.main_answer in word.endings.values()
        assert output.main_answer in output.answers

        for answer in output.answers:
            assert answer in word.endings.values()
            assert output.components in word.find(answer)

        assert output.prompt == str(word)


def test_inflect_question_pronoun():
    word = Pronoun("hic", meaning="this")
    vocab_list = VocabList([word])
    amount = 500

    for output in ask_question_without_sr(vocab_list, amount, settings):
        assert type(output) is ParseWordCompToLatQuestion
        assert output.check(output.main_answer)

        assert output.main_answer in word.endings.values()
        assert output.main_answer in output.answers

        for answer in output.answers:
            assert answer in word.endings.values()
            assert output.components in word.find(answer)

        assert output.prompt == str(word)


def test_inflect_question_verb():
    word = Verb("doceo", "docere", "docui", "doctus", meaning="teach")
    vocab_list = VocabList([word])
    amount = 500

    for output in ask_question_without_sr(vocab_list, amount, settings):
        assert type(output) is ParseWordCompToLatQuestion
        assert output.check(output.main_answer)

        assert output.main_answer in word.endings.values()
        assert output.main_answer in output.answers

        for answer in output.answers:
            assert answer in word.endings.values()
            assert output.components in word.find(answer)

        assert output.prompt == str(word)


def test_inflect_question_regularword():
    word = RegularWord("in", meaning="in")
    vocab_list = VocabList([word])
    amount = 500

    for output in ask_question_without_sr(vocab_list, amount, settings):
        assert type(output) is ParseWordCompToLatQuestion
        assert output.check(output.main_answer)

        assert output.main_answer in word.endings.values()
        assert output.main_answer in output.answers

        for answer in output.answers:
            assert answer in word.endings.values()
            assert output.components in word.find(answer)

        assert output.prompt == str(word)
