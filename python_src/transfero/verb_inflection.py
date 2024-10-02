#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English verbs."""

from __future__ import annotations

from typing import TYPE_CHECKING

import lemminflect

from ..accido.misc import Mood, Number, Person, Tense, Voice
from .edge_cases import STATIVE_VERBS
from .exceptions import InvalidWordError

if TYPE_CHECKING:
    from .. import accido


def _verify_verb_inflections(components: accido.misc.EndingComponents) -> None:
    if not hasattr(components, "tense"):
        raise ValueError("Tense must be specified")

    if not hasattr(components, "voice"):
        raise ValueError("Voice must be specified")

    if not hasattr(components, "mood"):
        raise ValueError("Mood must be specified")

    # not an infinitive
    if components.mood != Mood.INFINITIVE:
        if not hasattr(components, "number"):
            raise ValueError("Number must be specified")

        if components.number not in Number:
            raise ValueError(f"Invalid number: '{components.number}'")

        # not a participle or an infinitive
        if components.mood != Mood.PARTICIPLE:
            if not hasattr(components, "person"):
                raise ValueError("Person must be specified")

            if components.person not in {1, 2, 3}:
                raise ValueError(f"Invalid person: '{components.person}'")

        else:
            if not hasattr(components, "case"):
                raise ValueError("Case must be specified")

            if not hasattr(components, "gender"):
                raise ValueError("Gender must be specified")

    if components.voice not in Voice:
        raise ValueError(f"Invalid voice: '{components.voice}'")

    if components.mood not in Mood:
        raise ValueError(f"Invalid mood: '{components.mood}'")

    if components.tense not in Tense:
        raise ValueError(f"Invalid tense: '{components.tense}'")


def find_verb_inflections(
    verb: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    """Inflect English verbs using the tense, voice, mood, number and
    person. If a participle is queried, find_participle_inflections is ran
    instead.

    Note that subjunctives are not supported as they do not have an exact
    translation in English.

    Parameters
    ----------
    verb : str
        The verb to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the verb.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English verb.
    ValueError
        If the input (other than the word itself) is invalid.
    """  # noqa: D205
    _verify_verb_inflections(components)

    if components.mood == Mood.PARTICIPLE:
        return _find_participle_inflections(verb, components)

    try:
        lemma: str = lemminflect.getLemma(verb, "VERB")[0]
    except KeyError as e:
        raise InvalidWordError(f"Word {verb} is not a verb") from e

    match (components.tense, components.voice, components.mood):
        case (Tense.PRESENT, Voice.ACTIVE, Mood.INDICATIVE):
            return _find_preactind_inflections(
                lemma,
                components.number,
                components.person,
            )

        case (Tense.IMPERFECT, Voice.ACTIVE, Mood.INDICATIVE):
            return _find_impactind_inflections(
                lemma,
                components.number,
                components.person,
            )

        case (Tense.PERFECT, Voice.ACTIVE, Mood.INDICATIVE):
            return _find_peractind_inflections(
                lemma,
                components.number,
                components.person,
            )

        case (Tense.PLUPERFECT, Voice.ACTIVE, Mood.INDICATIVE):
            return _find_plpactind_inflections(
                lemma,
                components.number,
                components.person,
            )

        case (Tense.PRESENT, Voice.ACTIVE, Mood.INFINITIVE):
            return _find_preactinf_inflections(lemma)

        case (Tense.PRESENT, Voice.ACTIVE, Mood.IMPERATIVE):
            return _find_preipe_inflections(lemma)

        case _:
            raise NotImplementedError(
                f"The {components.tense.regular} {components.voice.regular} "
                f"{components.mood.regular} has not been implemented",
            )


def _find_preactind_inflections(
    lemma: str,
    number: Number,
    person: Person,
) -> set[str]:
    present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    match (number, person):
        case (Number.SINGULAR, 1):
            return {
                f"I {present_nonthird}",
                f"I am {present_participle}",
            }

        case (Number.PLURAL, 1):
            return {
                f"we {present_nonthird}",
                f"we are {present_participle}",
            }

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return {
                f"you {present_nonthird}",
                f"you are {present_participle}",
            }

        case (Number.SINGULAR, 3):
            return {
                f"he {present_third}",
                f"he is {present_participle}",
                f"she {present_third}",
                f"she is {present_participle}",
                f"it {present_third}",
                f"it is {present_participle}",
            }

        case (Number.PLURAL, 3):
            return {
                f"they {present_nonthird}",
                f"they are {present_participle}",
            }

    raise ValueError(
        f"Invalid number and person: '{number.regular}' '{person}'"
    )


def _find_impactind_inflections(
    lemma: str,
    number: Number,
    person: Person,
) -> set[str]:
    present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    if lemma in STATIVE_VERBS:
        past: str = lemminflect.getInflection(lemma, "VBD")[0]

        match (number, person):
            case (Number.SINGULAR, 1):
                return {f"I {past}", f"I was {present_participle}"}

            case (Number.PLURAL, 1):
                return {f"we {past}", f"we were {present_participle}"}

            case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
                return {f"you {past}", f"you were {present_participle}"}

            case (Number.SINGULAR, 3):
                return {
                    f"he {past}",
                    f"he was {present_participle}",
                    f"she {past}",
                    f"she was {present_participle}",
                    f"it {past}",
                    f"it was {present_participle}",
                }

            case (Number.PLURAL, 3):
                return {f"they {past}", f"they were {present_participle}"}

            # case _:
            #     raise ValueError(
            #         f"Invalid number and person: '{number}' '{person}'"
            #     )

    match (number, person):
        case (Number.SINGULAR, 1):
            return {f"I was {present_participle}"}

        case (Number.PLURAL, 1):
            return {f"we were {present_participle}"}

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return {f"you were {present_participle}"}

        case (Number.SINGULAR, 3):
            return {
                f"he was {present_participle}",
                f"she was {present_participle}",
                f"it was {present_participle}",
            }

        case (Number.PLURAL, 3):
            return {f"they were {present_participle}"}

    raise ValueError(f"Invalid number and person: '{number}' '{person}'")


def _find_peractind_inflections(
    lemma: str,
    number: Number,
    person: Person,
) -> set[str]:
    past = lemminflect.getInflection(lemma, "VBD")[0]

    match (number, person):
        case (Number.SINGULAR, 1):
            return {f"I {past}", f"I have {past}", f"I did {lemma}"}

        case (Number.PLURAL, 1):
            return {f"we {past}", f"we have {past}", f"we did {lemma}"}

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return {f"you {past}", f"you have {past}", f"you did {lemma}"}

        case (Number.SINGULAR, 3):
            return {
                f"he {past}",
                f"he has {past}",
                f"he did {lemma}",
                f"she {past}",
                f"she has {past}",
                f"she did {lemma}",
                f"it {past}",
                f"it has {past}",
                f"it did {lemma}",
            }

        case (Number.PLURAL, 3):
            return {f"they {past}", f"they have {past}", f"they did {lemma}"}

    raise ValueError(f"Invalid number and person: '{number}' '{person}'")


def _find_plpactind_inflections(
    lemma: str,
    number: Number,
    person: Person,
) -> set[str]:
    past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]

    match (number, person):
        case (Number.SINGULAR, 1):
            return {f"I had {past_participle}"}

        case (Number.PLURAL, 1):
            return {f"we had {past_participle}"}

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return {f"you had {past_participle}"}

        case (Number.SINGULAR, 3):
            return {
                f"he had {past_participle}",
                f"she had {past_participle}",
                f"it had {past_participle}",
            }

        case (Number.PLURAL, 3):
            return {f"they had {past_participle}"}

    raise ValueError(f"Invalid number and person: '{number}' '{person}'")


def _find_participle_inflections(
    verb: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    lemma: str = lemminflect.getLemma(verb, "NOUN")[0]

    match (components.tense, components.voice):
        case (Tense.PERFECT, Voice.PASSIVE):
            past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
            return {f"having been {past_participle}"}

        case (Tense.PRESENT, Voice.ACTIVE):
            present_participle: str = lemminflect.getInflection(lemma, "VBG")[
                0
            ]
            return {present_participle}

        case _:
            raise NotImplementedError(
                f"The {components.tense.regular} {components.voice.regular} "
                "participle has not been implemented",
            )


def _find_preactinf_inflections(lemma: str) -> set[str]:
    return {f"to {lemma}"}


def _find_preipe_inflections(lemma: str) -> set[str]:
    return {f"{lemma}"}
