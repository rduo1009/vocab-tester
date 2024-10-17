#!/usr/bin/env python3

"""Contains functions that inflect English adjectives."""

from __future__ import annotations

import lemminflect

from .. import accido
from ..accido.misc import Degree
from .edge_cases import NOT_COMPARABLE_ADJECTIVES
from .exceptions import InvalidWordError


def find_adjective_inflections(
    adjective: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    """Inflect English adjectives using the degree.

    Parameters
    ----------
    adjective : str
        The adjective to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the adjective.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English adjective.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    if components.type is not accido.endings.Adjective:
        raise ValueError(f"Invalid type: '{components.type}'")
    if components.subtype is not None:
        raise ValueError(f"Invalid subtype: '{components.subtype}'")

    try:
        lemmas: tuple[str, ...] = lemminflect.getLemma(adjective, "ADJ")
    except KeyError as e:  # pragma: no cover
        raise InvalidWordError(
            f"Word '{adjective}' is not an adjective"
        ) from e

    inflections: set[str] = set()
    for lemma in lemmas:
        inflections |= _inflect_lemma(lemma, components.degree)[1]

    return inflections


def find_main_adjective_inflection(
    adjective: str, components: accido.misc.EndingComponents
) -> str:
    """Find the main inflection of an English adjective.

    Parameters.
    ----------
    adjective : str
        The adjective to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    str
        The main inflection of the adjective.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English adjective.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    if components.type is not accido.endings.Adjective:
        raise ValueError(f"Invalid type: '{components.type}'")
    if components.subtype is not None:
        raise ValueError(f"Invalid subtype: '{components.subtype}'")

    try:
        lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]
    except KeyError as e:  # pragma: no cover
        raise InvalidWordError(
            f"Word '{adjective}' is not an adjective"
        ) from e

    return _inflect_lemma(lemma, components.degree)[0]


def _inflect_lemma(lemma: str, degree: Degree) -> tuple[str, set[str]]:
    not_comparable: bool = lemma in NOT_COMPARABLE_ADJECTIVES

    match degree:
        case Degree.POSITIVE:
            return (lemma, {lemma})
        case Degree.COMPARATIVE:
            comparatives: tuple[str, ...] = lemminflect.getInflection(
                lemma, "RBR"
            )
            return (
                f"more {lemma}" if not_comparable else comparatives[0],
                {*comparatives, f"more {lemma}"},
            )
        case Degree.SUPERLATIVE:
            superlatives: tuple[str, ...] = lemminflect.getInflection(
                lemma, "RBS"
            )
            return (
                f"most {lemma}" if not_comparable else superlatives[0],
                {
                    *superlatives,
                    f"most {lemma}",
                    f"very {lemma}",
                    f"extremely {lemma}",
                    f"rather {lemma}",
                    f"too {lemma}",
                    f"quite {lemma}",
                },
            )
