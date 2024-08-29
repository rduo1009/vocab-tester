#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English nouns."""

from __future__ import annotations

import lemminflect
from inflect import engine

from .. import accido

pluralinflect = engine()  # To distinguish from the lemminflect module
del engine


def _get_possessive(noun: str) -> str:
    """Return the possessive form of a given noun."""
    if noun.endswith("s"):
        return noun + "'"
    else:
        return noun + "'s"


def find_noun_inflections(
    noun: str, components: accido.misc.EndingComponents
) -> set[str]:
    """Inflect English nouns using the case and number."""

    if hasattr(components, "case"):
        raise ValueError("Case must be specified")

    if hasattr(components, "number"):
        raise ValueError("Number must be specified")

    lemma: str = lemminflect.getLemma(noun, "NOUN")[0]
    base_forms: set[str] = set()

    match components.number:
        case "singular":
            base_forms = {lemminflect.getInflection(lemma, "NN")[0]}

        case "plural":
            base_forms.add(pluralinflect.plural_noun(lemma))
            pluralinflect.classical(all=True)
            base_forms.add(pluralinflect.plural_noun(lemma))
            pluralinflect.classical(all=False)

        case _:
            raise ValueError(f"Invalid number: '{components.number}'")

    match components.case:
        case "nominative" | "vocative" | "accusative":
            return base_forms

        case "genitive":
            possessive_genitive: set[str] = {
                _get_possessive(base_form) for base_form in base_forms
            }

            if components.number == "singular":
                return possessive_genitive | {
                    f"of the {base_form}" for base_form in base_forms
                } | {
                    pluralinflect.inflect(f"of a('{base_form}')") for base_form in base_forms
                }  # fmt: skip

            return possessive_genitive | {
                f"of the {base_form}" for base_form in base_forms
            }

        case "dative":
            if components.number == "singular":
                return {
                    f"for the {base_form}" for base_form in base_forms
                } | {
                    pluralinflect.inflect(f"for a('{base_form}')") 
                    for base_form in base_forms
                } | {
                    f"to the {base_form}" for base_form in base_forms
                } | {
                    pluralinflect.inflect(f"to a('{base_form}')") 
                    for base_form in base_forms
                }  # fmt: skip

            return {
                f"for the {base_form}" for base_form in base_forms
            } | {
                f"for {base_form}" for base_form in base_forms
            } | {
                f"to the {base_form}" for base_form in base_forms
            } | {
                f"to {base_form}" for base_form in base_forms
            }  # fmt: skip

        case "ablative":
            if components.number == "singular":
                return base_forms | {
                    f"with the {base_form}" for base_form in base_forms
                } | {
                    pluralinflect.inflect(f"with a('{base_form}')") 
                    for base_form in base_forms
                } | {
                    f"by the {base_form}" for base_form in base_forms
                } | {
                    pluralinflect.inflect(f"by a('{base_form}')") 
                    for base_form in base_forms
                } | {
                    f"by means of the {base_form}" for base_form in base_forms
                } | {
                    pluralinflect.inflect(f"by means of a('{base_form}')") 
                    for base_form in base_forms
                }  # fmt: skip

            return base_forms | {
                f"with the {base_form}" for base_form in base_forms
            } | {
                f"by the {base_form}" for base_form in base_forms
            } | {
                f"by means of the {base_form}" for base_form in base_forms
            }  # fmt: skip

        case _:
            raise ValueError(f"Invalid case: '{components.case}'")
