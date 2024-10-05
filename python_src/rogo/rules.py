#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains rules for filtering words and questions."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Final

from .. import accido
from .question_classes import QuestionClasses

if TYPE_CHECKING:
    from ..accido.type_aliases import Ending, Endings
    from ..lego.misc import VocabList
    from .type_aliases import Settings, Vocab

RULE_REGEX: Final[dict[str, str]] = {
    # Verb tense/voice/mood
    "exclude-verb-present-active-indicative": r"^Vpreactind[a-z][a-z]\d$",
    "exclude-verb-imperfect-active-indicative": r"^Vimpactind[a-z][a-z]\d$",
    "exclude-verb-perfect-active-indicative": r"^Vperactind[a-z][a-z]\d$",
    "exclude-verb-pluperfect-active-indicative": r"^Vplpactind[a-z][a-z]\d$",
    "exclude-verb-present-active-infinitive": r"^Vpreactinf   $",
    "exclude-verb-present-active-imperative": r"^Vpreactipe[a-z][a-z]\d$",
    "exclude-verb-imperfect-active-subjunctive": r"^Vimpactsbj[a-z][a-z]\d$",
    "exclude-verb-pluperfect-active-subjunctive": r"^Vplpactsbj[a-z][a-z]\d$",

    # Verb number
    "exclude-verb-singular": r"^V[a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]sg\d$",  # noqa: E501
    "exclude-verb-plural": r"^V[a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]pl\d$",  # noqa: E501

    # Verb person
    "exclude-verb-1st-person": r"^V[a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]1$",  # noqa: E501
    "exclude-verb-2nd-person": r"^V[a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]2$",  # noqa: E501
    "exclude-verb-3rd-person": r"^V[a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z][a-z]3$",  # noqa: E501

    # Participles
    "exclude-participles": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z][a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501

    # Participle tense/voice
    "exclude-participle-present-active": r"^Vpreactptc[a-z][a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501
    "exclude-participle-perfect-passive": r"^Vperpasptc[a-z][a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501

    # Participle gender
    "exclude-participle-masculine": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptcm[a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501
    "exclude-participle-feminine": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptcf[a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501
    "exclude-participle-neuter": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptcn[a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501

    # Participle case
    "exclude-participle-nominative": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z]nom[a-z][a-z]$",  # noqa: E501
    "exclude-participle-vocative": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z]voc[a-z][a-z]$",  # noqa: E501
    "exclude-participle-accusative": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z]acc[a-z][a-z]$",  # noqa: E501
    "exclude-participle-genitive": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z]gen[a-z][a-z]$",  # noqa: E501
    "exclude-participle-dative": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z]dat[a-z][a-z]$",  # noqa: E501
    "exclude-participle-ablative": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z]abl[a-z][a-z]$",  # noqa: E501

    # Participle number
    "exclude-participle-singular": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z][a-z][a-z][a-z]sg$",  # noqa: E501
    "exclude-participle-plural": r"^V[a-z][a-z][a-z][a-z][a-z][a-z]ptc[a-z][a-z][a-z][a-z]pl$",  # noqa: E501

    # Noun case
    "exclude-noun-nominative": r"^Nnom[a-z][a-z]$",
    "exclude-noun-vocative": r"^Nvoc[a-z][a-z]$",
    "exclude-noun-accusative": r"^Nacc[a-z][a-z]$",
    "exclude-noun-genitive": r"^Ngen[a-z][a-z]$",
    "exclude-noun-dative": r"^Ndat[a-z][a-z]$",
    "exclude-noun-ablative": r"^Nabl[a-z][a-z]$",

    # Noun number
    "exclude-noun-singular": r"^N[a-z][a-z][a-z]sg$",
    "exclude-noun-plural": r"^N[a-z][a-z][a-z]pl$",

    # Adjective gender
    "exclude-adjective-masculine": r"^A[a-z][a-z][a-z]m[a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501
    "exclude-adjective-feminine": r"^A[a-z][a-z][a-z]f[a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501
    "exclude-adjective-neuter": r"^A[a-z][a-z][a-z]n[a-z][a-z][a-z][a-z][a-z]$",  # noqa: E501

    # Adjective case
    "exclude-adjective-nominative": r"^A[a-z][a-z][a-z][a-z]nom[a-z][a-z]$",
    "exclude-adjective-vocative": r"^A[a-z][a-z][a-z][a-z]voc[a-z][a-z]$",
    "exclude-adjective-accusative": r"^A[a-z][a-z][a-z][a-z]acc[a-z][a-z]$",
    "exclude-adjective-genitive": r"^A[a-z][a-z][a-z][a-z]gen[a-z][a-z]$",
    "exclude-adjective-dative": r"^A[a-z][a-z][a-z][a-z]dat[a-z][a-z]$",
    "exclude-adjective-ablative": r"^A[a-z][a-z][a-z][a-z]abl[a-z][a-z]$",
    
    # Adjective number
    "exclude-adjective-singular": r"^A[a-z][a-z][a-z][a-z][a-z][a-z][a-z]sg$",
    "exclude-adjective-plural": r"^A[a-z][a-z][a-z][a-z][a-z][a-z][a-z]pl$",
    
    # Adjective degree
    "exclude-adjective-positive": r"^Apos[a-z][a-z][a-z][a-z][a-z][a-z]$",
    "exclude-adjective-comparative": r"^Acmp[a-z][a-z][a-z][a-z][a-z][a-z]$",
    "exclude-adjective-superlative": r"^Aspr[a-z][a-z][a-z][a-z][a-z][a-z]$",
    
    # Adverb
    "exclude-adverbs": r"^D[a-z][a-z][a-z]$",
    
    # Adverb degree
    "exclude-adverb-positive": r"^Dpos$",
    "exclude-adverb-comparative": r"^Dcmp$",
    "exclude-adverb-superlative": r"^Dspr$",
    
    # Pronoun gender
    "exclude-pronoun-masculine": r"^Pm[a-z][a-z][a-z][a-z][a-z]$",
    "exclude-pronoun-feminine": r"^Pf[a-z][a-z][a-z][a-z][a-z]$",
    "exclude-pronoun-neuter": r"^Pn[a-z][a-z][a-z][a-z][a-z]$",

    # Pronoun case
    "exclude-pronoun-nominative": r"^P[a-z]nom[a-z][a-z]$",
    "exclude-pronoun-vocative": r"^P[a-z]voc[a-z][a-z]$",
    "exclude-pronoun-accusative": r"^P[a-z]acc[a-z][a-z]$",
    "exclude-pronoun-genitive": r"^P[a-z]gen[a-z][a-z]$",
    "exclude-pronoun-dative": r"^P[a-z]dat[a-z][a-z]$",
    "exclude-pronoun-ablative": r"^P[a-z]abl[a-z][a-z]$",

    # Pronoun number
    "exclude-pronoun-singular": r"^P[a-z][a-z][a-z][a-z]sg$",
    "exclude-pronoun-plural": r"^P[a-z][a-z][a-z][a-z]pl$",
}  # fmt: skip

CLASS_RULES: Final[dict[str, str]] = {
    "include-typein-engtolat": QuestionClasses.TYPEIN_ENGTOLAT,
    "include-typein-lattoeng": QuestionClasses.TYPEIN_LATTOENG,
    "include-parse": QuestionClasses.PARSEWORD_LATTOCOMP,
    "include-inflect": QuestionClasses.PARSEWORD_COMPTOLAT,
}


def filter_words(vocab_list: VocabList, settings: Settings) -> Vocab:
    """Filter the vocabulary list based on the settings given.

    Parameters
    ----------
    vocab_list : VocabList
        The vocabulary list to filter.
    settings : Settings
        The settings to use for filtering.

    Returns
    -------
    Vocab
        The filtered vocabulary list.
    """

    def _filter_classes(
        vocab_list: Vocab,
        classes: tuple[type, ...],
    ) -> Vocab:
        return [item for item in vocab_list if not isinstance(item, classes)]

    vocab: Vocab = vocab_list.vocab
    to_exclude: list[type] = []

    if settings["exclude-nouns"]:
        to_exclude.append(accido.endings.Noun)
    if settings["exclude-verbs"]:
        to_exclude.append(accido.endings.Verb)
    if settings["exclude-adjectives"]:
        to_exclude.append(accido.endings.Adjective)
    if settings["exclude-pronouns"]:
        to_exclude.append(accido.endings.Pronoun)
    if settings["exclude-regulars"]:
        to_exclude.append(accido.endings.RegularWord)

    if to_exclude:
        vocab = _filter_classes(vocab, tuple(to_exclude))

    item: accido.endings._Word

    # Iterate over copy of list to avoid errors
    for item in vocab[:]:
        if type(item) is accido.endings.Verb:
            assert type(settings["exclude-verb-first-conjugation"]) is bool
            assert type(settings["exclude-verb-second-conjugation"]) is bool
            assert type(settings["exclude-verb-third-conjugation"]) is bool
            assert type(settings["exclude-verb-fourth-conjugation"]) is bool
            assert type(settings["exclude-verb-thirdio-conjugation"]) is bool

            current_conjugation: int = item.conjugation
            conjugation_excluded: bool = (
                (
                    settings["exclude-verb-first-conjugation"]
                    and current_conjugation == 1
                )
                or (
                    settings["exclude-verb-second-conjugation"]
                    and current_conjugation == 2
                )
                or (
                    settings["exclude-verb-third-conjugation"]
                    and current_conjugation == 3
                )
                or (
                    settings["exclude-verb-fourth-conjugation"]
                    and current_conjugation == 4
                )
                or (
                    settings["exclude-verb-thirdio-conjugation"]
                    and current_conjugation == 5
                )
            )
            if conjugation_excluded:
                vocab.remove(item)

        elif type(item) is accido.endings.Noun:
            assert type(settings["exclude-noun-first-declension"]) is bool
            assert type(settings["exclude-noun-second-declension"]) is bool
            assert type(settings["exclude-noun-third-declension"]) is bool
            assert type(settings["exclude-noun-fourth-declension"]) is bool
            assert type(settings["exclude-noun-fifth-declension"]) is bool
            assert type(settings["exclude-noun-irregular-declension"]) is bool

            current_declension: int = item.declension
            declension_excluded: bool = (
                (
                    settings["exclude-noun-first-declension"]
                    and current_declension == 1
                )
                or (
                    settings["exclude-noun-second-declension"]
                    and current_declension == 2
                )
                or (
                    settings["exclude-noun-third-declension"]
                    and current_declension == 3
                )
                or (
                    settings["exclude-noun-fourth-declension"]
                    and current_declension == 4
                )
                or (
                    settings["exclude-noun-fifth-declension"]
                    and current_declension == 5
                )
                or (
                    settings["exclude-noun-irregular-declension"]
                    and current_declension == 0
                )
            )
            if declension_excluded:
                vocab.remove(item)

        elif type(item) is accido.endings.Adjective:
            assert type(settings["exclude-adjective-212-declension"]) is bool
            assert type(settings["exclude-adjective-third-declension"]) is bool

            current_adj_declension: str = item.declension
            if (
                settings["exclude-adjective-212-declension"]
                and current_adj_declension == "212"
            ) or (
                settings["exclude-adjective-third-declension"]
                and current_adj_declension == "3"
            ):
                vocab.remove(item)
    return vocab


def filter_endings(endings: Endings, settings: Settings) -> dict[str, Ending]:
    """Filter the endings to exclude any endings specified in the settings.

    Parameters
    ----------
    endings : Endings
        The endings to filter.
    settings : Settings
        The settings to use for filtering.

    Returns
    -------
    dict[str, Ending]
        The filtered endings.
    """
    filtered_endings: dict[str, Ending] = dict(endings)

    for setting, value in settings.items():
        if value and (setting in RULE_REGEX):
            regex_pattern: str = RULE_REGEX[setting]
            filtered_endings = {
                key: ending
                for key, ending in filtered_endings.items()
                if not re.match(regex_pattern, key)
            }

    return filtered_endings


def filter_questions(settings: Settings) -> list[QuestionClasses]:
    """Filter the question types using the settings.

    Parameters
    ----------
    settings : Settings
        The settings to use for filtering.

    Returns
    -------
    list[str]
        The filtered classes.
    """
    classes: list[str] = []
    for key, value in CLASS_RULES.items():
        if settings[key]:
            classes.append(value)
    return classes
