#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English nouns."""

from __future__ import annotations

from typing import TYPE_CHECKING

import lemminflect
from inflect import engine

from ..accido.misc import Case, Number
from .exceptions import InvalidWordError

if TYPE_CHECKING:
    from .. import accido

# Distinguish from the lemminflect module
pluralinflect = engine()  # sourcery skip: avoid-global-variables
del engine


def _get_possessive(noun: str) -> str:
    return f"{noun}'" if noun.endswith("s") else f"{noun}'s"


def find_noun_inflections(
    noun: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    """Inflect English nouns using the case and number.

    Parameters
    ----------
    noun : str
        The noun to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the noun.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English noun.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    if not hasattr(components, "case"):
        raise ValueError("Case must be specified")

    if not hasattr(components, "number"):
        raise ValueError("Number must be specified")

    if components.case not in Case:
        raise ValueError(f"Invalid case: '{components.case}'")

    if components.number not in Number:
        raise ValueError(f"Invalid number: '{components.number}'")

    try:
        lemmas: tuple[str, ...] = lemminflect.getLemma(noun, "NOUN")
    except KeyError as e:
        raise InvalidWordError(f"Word {noun} is not a noun") from e

    inflections: set[str] = set()
    for lemma in lemmas:
        inflections |= _inflect_lemma(
            lemma, components.case, components.number
        )

    return inflections


def _inflect_lemma(lemma: str, case: Case, number: Number) -> set[str]:
    base_forms: set[str] = set()

    match number:
        case Number.SINGULAR:
            base_forms = {lemminflect.getInflection(lemma, "NN")[0]}
        case Number.PLURAL:
            base_forms.add(pluralinflect.plural_noun(lemma))
            pluralinflect.classical(all=True)
            base_forms.add(pluralinflect.plural_noun(lemma))
            pluralinflect.classical(all=False)

    match case:
        case Case.NOMINATIVE | Case.VOCATIVE | Case.ACCUSATIVE:
            return base_forms
        case Case.GENITIVE:
            possessive_genitive: set[str] = {
                _get_possessive(base_form) for base_form in base_forms
            }
            if number == Number.SINGULAR:
                return (
                    possessive_genitive
                    | {f"of the {base_form}" for base_form in base_forms}
                    | {
                        pluralinflect.inflect(f"of a('{base_form}')")
                        for base_form in base_forms
                    }
                )
            return possessive_genitive | {
                f"of the {base_form}" for base_form in base_forms
            }
        case Case.DATIVE:
            if number == Number.SINGULAR:
                return (
                    {f"for the {base_form}" for base_form in base_forms}
                    | {
                        pluralinflect.inflect(f"for a('{base_form}')")
                        for base_form in base_forms
                    }
                    | {f"to the {base_form}" for base_form in base_forms}
                    | {
                        pluralinflect.inflect(f"to a('{base_form}')")
                        for base_form in base_forms
                    }
                )
            return (
                {f"for the {base_form}" for base_form in base_forms}
                | {f"for {base_form}" for base_form in base_forms}
                | {f"to the {base_form}" for base_form in base_forms}
                | {f"to {base_form}" for base_form in base_forms}
            )
        case Case.ABLATIVE:
            if number == Number.SINGULAR:
                return (
                    base_forms
                    | {f"with the {base_form}" for base_form in base_forms}
                    | {
                        pluralinflect.inflect(f"with a('{base_form}')")
                        for base_form in base_forms
                    }
                    | {f"by the {base_form}" for base_form in base_forms}
                    | {
                        pluralinflect.inflect(f"by a('{base_form}')")
                        for base_form in base_forms
                    }
                    | {
                        f"by means of the {base_form}"
                        for base_form in base_forms
                    }
                    | {
                        pluralinflect.inflect(f"by means of a('{base_form}')")
                        for base_form in base_forms
                    }
                )
            return (
                base_forms
                | {f"with the {base_form}" for base_form in base_forms}
                | {f"by the {base_form}" for base_form in base_forms}
                | {f"by means of the {base_form}" for base_form in base_forms}
            )
