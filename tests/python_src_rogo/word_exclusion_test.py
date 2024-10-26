import os
import sys  # noqa: E401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from typing import Sequence

from python_src.accido.endings import Adjective, Noun, Verb
from python_src.accido.misc import Gender
from python_src.lego.misc import VocabList
from python_src.rogo.rules import filter_words
from python_src.rogo.type_aliases import Settings

default_settings: Settings = {
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
    "include-inflect": False,
    "include-principal-parts": False,
    "include-multiplechoice-engtolat": False,
    "include-multiplechoice-lattoeng": False,
    "number-multiplechoice-options": 3,
}


def test_word_exclusion_adjective():
    words: list[Adjective] = [Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy"), Adjective("ingens", "ingentis", declension="3", termination=1, meaning="large")]
    vocab_list = VocabList(words)  # type: ignore[arg-type]

    settings = default_settings.copy()

    settings["exclude-adjective-212-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert filter_words(vocab_list, settings) == [Adjective("ingens", "ingentis", declension="3", termination=1, meaning="large")]
    settings["exclude-adjective-212-declension"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-adjective-third-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert filter_words(vocab_list, settings) == [Adjective("laetus", "laeta", "laetum", declension="212", meaning="happy")]
    settings["exclude-adjective-third-declension"] = False  # type: ignore[typeddict-readonly-mutated]


def test_word_exclusion_noun():
    words: Sequence[Noun] = [
        Noun(nominative="ancilla", genitive="ancillae", gender=Gender.FEMININE, meaning="slavegirl"),
        Noun(nominative="servus", genitive="servi", gender=Gender.MASCULINE, meaning="slave"),
        Noun(nominative="carcer", genitive="carceris", gender=Gender.MASCULINE, meaning="prison"),
        Noun(nominative="manus", genitive="manus", gender=Gender.FEMININE, meaning="hand"),
        Noun(nominative="res", genitive="rei", gender=Gender.FEMININE, meaning="thing"),
        Noun(nominative="ego", meaning="I"),
    ]
    vocab_list = VocabList(words)  # type: ignore[arg-type]

    settings = default_settings.copy()

    settings["exclude-noun-first-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.declension != 1 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-noun-first-declension"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-noun-second-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.declension != 2 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-noun-second-declension"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-noun-third-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.declension != 3 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-noun-third-declension"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-noun-fourth-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.declension != 4 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-noun-fourth-declension"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-noun-fifth-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.declension != 5 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-noun-fifth-declension"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-noun-irregular-declension"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.declension != 0 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-noun-irregular-declension"] = False  # type: ignore[typeddict-readonly-mutated]


def test_word_exclusion_verb():
    words: Sequence[Verb] = [
        Verb(present="celo", infinitive="celare", perfect="celavi", ppp="celatus", meaning="hide"),
        Verb(present="pareo", infinitive="parere", perfect="parui", meaning="hide"),
        Verb(present="desero", infinitive="deserere", perfect="deserui", ppp="desertus", meaning="desert"),
        Verb(present="patefacio", infinitive="patefacere", perfect="patefeci", ppp="patefactus", meaning="reveal"),
        Verb(present="aperio", infinitive="aperire", perfect="aperui", ppp="apertus", meaning="open"),
        Verb(present="abeo", infinitive="abire", perfect="abii", ppp="abitum", meaning="depart"),
    ]
    vocab_list = VocabList(words)  # type: ignore[arg-type]

    settings = default_settings.copy()

    settings["exclude-verb-first-conjugation"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.conjugation != 1 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-verb-first-conjugation"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-verb-second-conjugation"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.conjugation != 2 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-verb-second-conjugation"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-verb-third-conjugation"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.conjugation != 3 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-verb-third-conjugation"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-verb-fourth-conjugation"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.conjugation != 4 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-verb-fourth-conjugation"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-verb-thirdio-conjugation"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.conjugation != 5 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-verb-thirdio-conjugation"] = False  # type: ignore[typeddict-readonly-mutated]

    settings["exclude-verb-irregular-conjugation"] = True  # type: ignore[typeddict-readonly-mutated]
    assert any(word.conjugation != 0 for word in filter_words(vocab_list, settings))  # type: ignore[attr-defined]
    settings["exclude-verb-irregular-conjugation"] = False  # type: ignore[typeddict-readonly-mutated]
