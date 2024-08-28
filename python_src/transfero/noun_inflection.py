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
    # Something has gone very wrong here if this happens, but just to be safe
    if not (hasattr(components, "case") and hasattr(components, "number")):
        raise ValueError("Case and number must be specified")

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
            raise ValueError(f"Number '{components.number}' not recognised")

    match components.case:
        case "nominative" | "vocative" | "accusative" | "ablative":
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

        case _:
            raise ValueError(f"Case '{components.case}' not recognised")
