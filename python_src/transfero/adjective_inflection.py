#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adjectives."""

from __future__ import annotations

from typing import TYPE_CHECKING

import lemminflect

from ..accido.misc import Case, Degree, Gender, Number
from .exceptions import InvalidWordError

if TYPE_CHECKING:
    from .. import accido


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
    # Most of these are not necessary, but it helps to catch errors earlier
    if not hasattr(components, "gender"):
        raise ValueError("Gender must be specified")

    if not hasattr(components, "case"):
        raise ValueError("Case must be specified")

    if not hasattr(components, "number"):
        raise ValueError("Number must be specified")

    if not hasattr(components, "degree"):
        raise ValueError("Degree must be specified")

    if components.gender not in Gender:
        raise ValueError(f"Invalid gender: '{components.gender}'")

    if components.case not in Case:
        raise ValueError(f"Invalid case: '{components.case}'")

    if components.number not in Number:
        raise ValueError(f"Invalid number: '{components.number}'")

    try:
        lemmas: tuple[str, ...] = lemminflect.getLemma(adjective, "ADJ")
    except KeyError as e:
        raise InvalidWordError(
            f"Word '{adjective}' is not an adjective"
        ) from e

    inflections: set[str] = set()
    for lemma in lemmas:
        inflections |= _inflect_lemma(lemma, components.degree)

    return inflections


def _inflect_lemma(lemma: str, degree: Degree) -> set[str]:
    match degree:
        case Degree.POSITIVE:
            return {lemma}
        case Degree.COMPARATIVE:
            comparatives: tuple[str, ...] = lemminflect.getInflection(
                lemma, "RBR"
            )
            return {*comparatives, f"more {lemma}"}
        case Degree.SUPERLATIVE:
            superlatives: tuple[str, ...] = lemminflect.getInflection(
                lemma, "RBS"
            )
            return {
                *superlatives,
                f"most {lemma}",
                f"very {lemma}",
                f"extremely {lemma}",
                f"rather {lemma}",
                f"too {lemma}",
                f"quite {lemma}",
            }


# def find_main_adjective_inflection(
#     adjective: str, components: accido.misc.EndingComponents
# ) -> str:
#     """Find the main inflection of an English adjective.
#
#     Parameters
#     ----------
#     adjective : str
#         The adjective to inflect.
#
#     components : EndingComponents
#         The components of the ending.
#
#     Returns
#     -------
#     str
#     The main inflection of the adjective
#     """
#     pass
