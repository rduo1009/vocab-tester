#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adverbs."""

from __future__ import annotations

import lemminflect

from .. import accido


def find_adverb_inflections(
    adverb: str, components: accido.misc.EndingComponents
) -> set[str]:
    """Inflect English adverbs using the degree."""

    if not hasattr(components, "degree"):
        raise ValueError("Degree must be specified")

    lemma: str = lemminflect.getLemma(adverb, "ADV")[0]

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
