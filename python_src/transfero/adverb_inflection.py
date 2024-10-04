#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adverbs."""

from __future__ import annotations

import lemminflect

from .. import accido
from ..accido.misc import Degree
from .exceptions import InvalidWordError


def find_adverb_inflections(
    adverb: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    """Inflect English adverbs using the degree.

    Parameters
    ----------
    adverb : str
        The adverb to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the adverb.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English adverb.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    if components.type != accido.endings.Adjective:
        raise ValueError(f"Invalid type: '{components.type}'")
    if components.subtype != "adverb":  # pragma: no cover
        raise ValueError(f"Invalid subtype: '{components.subtype}'")

    try:
        lemmas: tuple[str, ...] = lemminflect.getLemma(adverb, "ADV")
    except KeyError as e:  # pragma: no cover
        raise InvalidWordError(f"Word '{adverb}' is not an adverb") from e

    inflections: set[str] = set()
    for lemma in lemmas:
        inflections |= _inflect_lemma(lemma, components.degree)

    return inflections


def _inflect_lemma(lemma: str, degree: Degree) -> set[str]:
    match degree:
        case Degree.POSITIVE:
            return {lemma}
        case Degree.COMPARATIVE:
            return {f"more {lemma}"}
        case Degree.SUPERLATIVE:
            return {
                f"most {lemma}",
                f"very {lemma}",
                f"extremely {lemma}",
                f"rather {lemma}",
                f"too {lemma}",
                f"quite {lemma}",
            }
