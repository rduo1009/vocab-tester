#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English words."""

from __future__ import annotations

from .. import accido
from .adj_to_adv import adj_to_adv as adj_to_adv
from .adjective_inflection import (
    find_adjective_inflections as find_adjective_inflections,
)
from .adverb_inflection import (
    find_adverb_inflections as find_adverb_inflections,
)
from .noun_inflection import find_noun_inflections as find_noun_inflections
from .verb_inflection import find_verb_inflections as find_verb_inflections


def find_inflection(
    word: str, pos: type, components: accido.misc.EndingComponents
) -> set[str]:
    """Find the inflections of an English word.

    Parameters
    ----------
    word : str
        The word to inflect.
    pos : type
        The part of speech of the word
    components : accido.misc.EndingComponents
        The components of the word.

    Returns
    -------
    set[str]
        The inflections of the word.

    Raises
    ------
    ValueError
        If the part of speech is unknown. This should never happen.
    """
    match pos:
        case accido.endings.Adjective:
            if components.subtype == "adverb":
                return find_adjective_inflections(word, components)
            return find_adverb_inflections(adj_to_adv(word), components)

        case accido.endings.Noun:
            return find_noun_inflections(word, components)

        case accido.endings.Verb:
            return find_verb_inflections(word, components)

        case accido.endings.Pronoun:
            return find_noun_inflections(word, components)

        case accido.endings.RegularWord:
            return {word}

        case _:
            raise ValueError(f"Unknown POS: {pos}")  # should never happen
