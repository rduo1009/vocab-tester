#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adverbs."""

from __future__ import annotations

from typing import TYPE_CHECKING

import lemminflect

from ...transfero.exceptions import InvalidWordError

if TYPE_CHECKING:
    from ... import accido


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
    if not hasattr(components, "degree"):
        raise ValueError("Degree must be specified")

    try:
        lemma: str = lemminflect.getLemma(adverb, "ADV")[0]
    except KeyError as e:
        raise InvalidWordError(f"Word {adverb} is not an adverb") from e

    if components.degree == "positive":
        return {lemma}

    if components.degree == "comparative":
        return {f"more {lemma}"}

    if components.degree == "superlative":
        return {
            f"most {lemma}",
            f"very {lemma}",
            f"extremely {lemma}",
            f"rather {lemma}",
            f"too {lemma}",
            f"quite {lemma}",
        }

    raise ValueError(f"Invalid degree: '{components.degree}'")
