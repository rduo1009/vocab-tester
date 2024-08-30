#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English adjectives."""

from __future__ import annotations

import lemminflect

from .. import accido


def find_adjective_inflections(
    adjective: str, components: accido.misc.EndingComponents
) -> set[str]:
    """Inflect English adjectives using the degree."""

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

    lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]

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
