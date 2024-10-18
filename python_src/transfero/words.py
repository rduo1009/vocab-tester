#!/usr/bin/env python3

"""Contains functions that inflect English words."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..accido.misc import ComponentsSubtype, ComponentsType
from .adj_to_adv import adj_to_adv
from .adjective_inflection import (
    find_adjective_inflections,
    find_main_adjective_inflection,
)
from .adverb_inflection import (
    find_adverb_inflections,
    find_main_adverb_inflection,
)
from .noun_inflection import find_main_noun_inflection, find_noun_inflections
from .pronoun_inflection import (
    find_main_pronoun_inflection,
    find_pronoun_inflections,
)
from .verb_inflection import find_main_verb_inflection, find_verb_inflections

if TYPE_CHECKING:
    from .. import accido


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
        case ComponentsType.ADJECTIVE:
            if components.subtype == ComponentsSubtype.ADVERB:
                return (
                    find_main_adverb_inflection(word, components)
                    if main
                    else find_adverb_inflections(adj_to_adv(word), components)
                )
            return (
                find_main_adjective_inflection(word, components)
                if main
                else find_adjective_inflections(word, components)
            )

        case ComponentsType.NOUN:
            if components.subtype == ComponentsSubtype.PRONOUN:
                return (
                    find_main_pronoun_inflection(word, components)
                    if main
                    else find_pronoun_inflections(word, components)
                )
            return (
                find_main_noun_inflection(word, components)
                if main
                else find_noun_inflections(word, components)
            )

        case ComponentsType.VERB:
            return (
                find_main_verb_inflection(word, components)
                if main
                else find_verb_inflections(word, components)
            )

        case ComponentsType.PRONOUN:
            return (
                find_main_pronoun_inflection(word, components)
                if main
                else find_pronoun_inflections(word, components)
            )

        case ComponentsType.REGULARWORD:
            return word if main else {word}
