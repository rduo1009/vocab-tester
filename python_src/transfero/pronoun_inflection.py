#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English pronouns."""

from __future__ import annotations

from typing import Final

from .. import accido
from ..accido.misc import Case, Number


def find_pronoun_inflections(
    pronoun: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    """Inflect English pronouns using the case and number.

    Pronouns in Latin also have a gender, but this is not used in English.

    Parameters
    ----------
    pronoun : str
        The pronoun to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the pronoun.

    Raises
    ------
    NotImplementedError
        If the word is not a valid English pronoun.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    if components.type not in {accido.endings.Noun, accido.endings.Pronoun}:
        raise ValueError(f"Invalid type: '{components.type}'")

    return set(_inflect_lemma(pronoun, components.case, components.number))


def find_main_pronoun_inflection(
    pronoun: str,
    components: accido.misc.EndingComponents,
) -> str:
    """Find the main inflection of an English pronoun.

    Pronouns in Latin also have a gender, but this is not used in English.

    Parameters
    ----------
    pronoun : str
        The pronoun to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    str
        The main inflection of the pronoun.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English pronoun.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    if components.type not in {accido.endings.Noun, accido.endings.Pronoun}:
        raise ValueError(f"Invalid type: '{components.type}'")

    return _inflect_lemma(pronoun, components.case, components.number)[0]


def _inflect_lemma(lemma: str, case: Case, number: Number) -> tuple[str, ...]:
    try:
        return PRONOUNS[lemma][case, number]
    except KeyError as e:  # pragma: no cover
        raise NotImplementedError(
            f"Word {lemma} has not been implemented as a pronoun"
        ) from e


# NOTE: had to avoid the type statement, but its worth keeping things in
# the one file
_Inflections = dict[tuple[Case, Number], tuple[str, ...]]

PRONOUNS: Final[dict[str, _Inflections]] = {
    "this": {
        (Case.NOMINATIVE, Number.SINGULAR): ("this",),
        (Case.NOMINATIVE, Number.PLURAL): ("these",),
        (Case.VOCATIVE, Number.SINGULAR): ("this",),
        (Case.VOCATIVE, Number.PLURAL): ("these",),
        (Case.ACCUSATIVE, Number.SINGULAR): ("this",),
        (Case.ACCUSATIVE, Number.PLURAL): ("these",),
        (Case.GENITIVE, Number.SINGULAR): ("of this",),
        (Case.GENITIVE, Number.PLURAL): ("of these",),
        (Case.DATIVE, Number.SINGULAR): (
            "for this",
            "to this",
        ),
        (Case.DATIVE, Number.PLURAL): (
            "for these",
            "to these",
        ),
        (Case.ABLATIVE, Number.SINGULAR): (
            "by this",
            "by means of this",
            "with this",
            "this",
        ),
        (Case.ABLATIVE, Number.PLURAL): (
            "by these",
            "by means of these",
            "with these",
            "these",
        ),
    },
    "that": {
        (Case.NOMINATIVE, Number.SINGULAR): ("that",),
        (Case.NOMINATIVE, Number.PLURAL): ("those",),
        (Case.VOCATIVE, Number.SINGULAR): ("that",),
        (Case.VOCATIVE, Number.PLURAL): ("those",),
        (Case.ACCUSATIVE, Number.SINGULAR): ("that",),
        (Case.ACCUSATIVE, Number.PLURAL): ("those",),
        (Case.GENITIVE, Number.SINGULAR): ("of that",),
        (Case.GENITIVE, Number.PLURAL): ("of those",),
        (Case.DATIVE, Number.SINGULAR): (
            "for that",
            "to that",
        ),
        (Case.DATIVE, Number.PLURAL): (
            "for those",
            "to those",
        ),
        (Case.ABLATIVE, Number.SINGULAR): (
            "by that",
            "by means of that",
            "with that",
            "that",
        ),
        (Case.ABLATIVE, Number.PLURAL): (
            "by those",
            "by means of those",
            "with those",
            "those",
        ),
    },
    "I": {
        (Case.NOMINATIVE, Number.SINGULAR): ("I",),
        (Case.NOMINATIVE, Number.PLURAL): ("we",),
        (Case.VOCATIVE, Number.SINGULAR): ("I",),
        (Case.VOCATIVE, Number.PLURAL): ("we",),
        (Case.ACCUSATIVE, Number.SINGULAR): ("me",),
        (Case.ACCUSATIVE, Number.PLURAL): ("us",),
        (Case.GENITIVE, Number.SINGULAR): ("of me", "my"),
        (Case.GENITIVE, Number.PLURAL): ("of us", "our"),
        (Case.DATIVE, Number.SINGULAR): (
            "for me",
            "to me",
        ),
        (Case.DATIVE, Number.PLURAL): (
            "for us",
            "to us",
        ),
        (Case.ABLATIVE, Number.SINGULAR): (
            "by me",
            "by means of me",
            "with me",
            "me",
        ),
        (Case.ABLATIVE, Number.PLURAL): (
            "by us",
            "by means of us",
            "with us",
            "us",
        ),
    },
    "you": {
        (Case.NOMINATIVE, Number.SINGULAR): ("you",),
        (Case.NOMINATIVE, Number.PLURAL): ("you",),
        (Case.VOCATIVE, Number.SINGULAR): ("you",),
        (Case.VOCATIVE, Number.PLURAL): ("you",),
        (Case.ACCUSATIVE, Number.SINGULAR): ("you",),
        (Case.ACCUSATIVE, Number.PLURAL): ("you",),
        (Case.GENITIVE, Number.SINGULAR): ("of you", "your"),
        (Case.GENITIVE, Number.PLURAL): ("of you", "your"),
        (Case.DATIVE, Number.SINGULAR): (
            "for you",
            "to you",
        ),
        (Case.DATIVE, Number.PLURAL): (
            "for you",
            "to you",
        ),
        (Case.ABLATIVE, Number.SINGULAR): (
            "by you",
            "by means of you",
            "with you",
            "you",
        ),
        (Case.ABLATIVE, Number.PLURAL): (
            "by you",
            "by means of you",
            "with you",
            "you",
        ),
    },
    "oneself": {
        (Case.ACCUSATIVE, Number.SINGULAR): (
            "oneself",
            "himself",
            "herself",
            "itself",
            "themself",
        ),
        (Case.ACCUSATIVE, Number.PLURAL): ("themselves",),
        (Case.GENITIVE, Number.SINGULAR): (
            "of oneself",
            "one's",
            "of himself",
            "his",
            "of herself",
            "her",
            "of itself",
            "its",
            "of themself",
            "their",
        ),
        (Case.GENITIVE, Number.PLURAL): ("of themselves", "their"),
        (Case.DATIVE, Number.SINGULAR): (
            "for oneself",
            "for himself",
            "for herself",
            "for itself",
            "for themself",
            "to oneself",
            "to himself",
            "to herself",
            "to itself",
            "to themself",
        ),
        (Case.DATIVE, Number.PLURAL): (
            "for themselves",
            "to themselves",
        ),
        (Case.ABLATIVE, Number.SINGULAR): (
            "by oneself",
            "by himself",
            "by herself",
            "by itself",
            "by themself",
            "by means of oneself",
            "by means of himself",
            "by means of herself",
            "by means of itself",
            "by means of themself",
            "with oneself",
            "with himself",
            "with herself",
            "with itself",
            "with themself",
            "oneself",
            "himself",
            "herself",
            "itself",
            "themself",
        ),
        (Case.ABLATIVE, Number.PLURAL): (
            "by themselves",
            "by means of themselves",
            "with themselves",
            "themselves",
        ),
    },
}
