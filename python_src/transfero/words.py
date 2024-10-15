#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English words."""

from __future__ import annotations

import sys

from .. import accido
from .adj_to_adv import adj_to_adv

if sys.version_info >= (3, 10):
    from .adjective_inflection import (
        find_adjective_inflections,
        find_main_adjective_inflection,
    )
    from .adverb_inflection import (
        find_adverb_inflections,
        find_main_adverb_inflection,
    )
    from .noun_inflection import (
        find_main_noun_inflection,
        find_noun_inflections,
    )
    from .pronoun_inflection import (
        find_main_pronoun_inflection,
        find_pronoun_inflections,
    )
    from .verb_inflection import (
        find_main_verb_inflection,
        find_verb_inflections,
    )
else:
    from .._compat.py38.tranfero.adjective_inflection import (
        find_adjective_inflections,
        find_main_adjective_inflection,
    )
    from .._compat.py38.tranfero.adverb_inflection import (
        find_adverb_inflections,
        find_main_adverb_inflection,
    )
    from .._compat.py38.tranfero.noun_inflection import (
        find_main_noun_inflection,
        find_noun_inflections,
    )
    from .._compat.py38.tranfero.pronoun_inflection import (
        find_main_pronoun_inflection,
        find_pronoun_inflections,
    )
    from .._compat.py38.tranfero.verb_inflection import (
        find_main_verb_inflection,
        find_verb_inflections,
    )


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
                    find_main_adverb_inflection(word, components)
                    if main
                    else find_adverb_inflections(adj_to_adv(word), components)
                )
            return (
                find_main_adjective_inflection(word, components)
                if main
                else find_adjective_inflections(word, components)
            )

        case accido.endings.Noun:
            if components.subtype == "pronoun":
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

        case accido.endings.Verb:
            return (
                find_main_verb_inflection(word, components)
                if main
                else find_verb_inflections(word, components)
            )

        case accido.endings.Pronoun:
            return (
                find_main_pronoun_inflection(word, components)
                if main
                else find_pronoun_inflections(word, components)
            )

        case accido.endings.RegularWord:
            return word if main else {word}

        case _:  # pragma: no cover
            raise ValueError(
                f"Unknown part of speech: {components.type}"
            )  # should never happen
