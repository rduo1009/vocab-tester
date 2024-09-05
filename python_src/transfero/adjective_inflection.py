#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adjectives."""

from __future__ import annotations

import lemminflect

from .. import accido
from .exceptions import InvalidWordError


def find_adjective_inflections(
    adjective: str, components: accido.misc.EndingComponents
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

    if components.gender not in {"masculine", "feminine", "neuter"}:
        raise ValueError(f"Invalid gender: '{components.gender}'")

    if components.case not in {
        "nominative",
        "vocative",
        "accusative",
        "genitive",
        "dative",
        "ablative",
    }:
        raise ValueError(f"Invalid case: '{components.case}'")

    if components.number not in {"singular", "plural"}:
        raise ValueError(f"Invalid number: '{components.number}'")

    try:
        lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]
    except KeyError:
        raise InvalidWordError(f"Word '{adjective}' is not an adjective")

    match components.degree:
        case "positive":
            return {lemma}

        case "comparative":
            comparative: str = lemminflect.getInflection(lemma, "RBR")[0]

            return {comparative, f"more {lemma}"}

        case "superlative":
            superlative: str = lemminflect.getInflection(lemma, "RBS")[0]

            return {
                superlative,
                f"most {lemma}",
                f"very {lemma}",
                f"extremely {lemma}",
                f"rather {lemma}",
                f"too {lemma}",
                f"quite {lemma}",
            }

        case _:
            raise ValueError(f"Invalid degree: '{components.degree}'")
