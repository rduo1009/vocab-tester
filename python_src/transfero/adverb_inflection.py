#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adverbs."""

from __future__ import annotations

import lemminflect

from .. import accido
from .exceptions import InvalidWordError


def find_adverb_inflections(
    adverb: str, components: accido.misc.EndingComponents
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

    if not hasattr(components, "degree"):
        raise ValueError("Degree must be specified")

    try:
        lemma: str = lemminflect.getLemma(adverb, "ADV")[0]
    except KeyError as e:
        raise InvalidWordError(f"Word {adverb} is not an adverb") from e

    match components.degree:
        case "positive":
            return {lemma}

        case "comparative":
            return {f"more {lemma}"}

        case "superlative":
            return {
                f"most {lemma}",
                f"very {lemma}",
                f"extremely {lemma}",
                f"rather {lemma}",
                f"too {lemma}",
                f"quite {lemma}",
            }

        case _:
            raise ValueError(f"Invalid degree: '{components.degree}'")
