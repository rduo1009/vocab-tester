#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English words."""

from __future__ import annotations

from .. import accido
from .adj_to_adv import adj_to_adv as adj_to_adv
from .adjective_inflection import (
    find_adjective_inflections,
    find_main_adjective_inflection,
)
from .adverb_inflection import (
    find_adverb_inflections,
    find_main_adverb_inflection,
)
from .noun_inflection import find_main_noun_inflection, find_noun_inflections
from .verb_inflection import find_main_verb_inflection, find_verb_inflections


def find_inflection(
    word: str,
    components: accido.misc.EndingComponents,
    *,
    main: bool = False,
) -> set[str] | str:
    """Find the inflections of an English word.

    Parameters
    ----------
    word : str
        The word to inflect.
    components : accido.misc.EndingComponents
        The components of the word.
    main : bool, optional = False
        Whether to return the main inflection or all of the inflections.

    Returns
    -------
    str
        The main inflection of the word.
    set[str]
        The inflections of the word.

    Raises
    ------
    ValueError
        If the part of speech is unknown. This should never happen.
    """
    match components.type:
        case accido.endings.Adjective:
            if components.subtype == "adverb":
                return (
                    find_adverb_inflections(adj_to_adv(word), components)
                    if not main
                    else find_main_adverb_inflection(word, components)
                )
            return (
                find_adjective_inflections(word, components)
                if not main
                else find_main_adjective_inflection(word, components)
            )

        case accido.endings.Noun:
            return (
                find_noun_inflections(word, components)
                if not main
                else find_main_noun_inflection(word, components)
            )

        case accido.endings.Verb:
            return (
                find_verb_inflections(word, components)
                if not main
                else find_main_verb_inflection(word, components)
            )

        case accido.endings.Pronoun:
            return (
                find_noun_inflections(word, components)
                if not main
                else find_main_noun_inflection(word, components)
            )

        case accido.endings.RegularWord:
            return {word} if not main else word

        case _:
            raise ValueError(
                f"Unknown part of speech: {components.type}"
            )  # should never happen
