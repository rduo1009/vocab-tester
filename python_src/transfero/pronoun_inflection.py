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
    if components.type is not accido.endings.Pronoun:
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
    if components.type is not accido.endings.Pronoun:
        raise ValueError(f"Invalid type: '{components.type}'")

    return _inflect_lemma(pronoun, components.case, components.number)[0]


def _inflect_lemma(lemma: str, case: Case, number: Number) -> tuple[str, ...]:
    try:
        return PRONOUNS[lemma][case, number]
    except KeyError as e:  # pragma: no cover
        raise NotImplementedError(
            f"Word {lemma} has not been implemented as a pronoun"
        ) from e


type Inflections = dict[tuple[Case, Number], tuple[str, ...]]
PRONOUNS: Final[dict[str, Inflections]] = {
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
}
