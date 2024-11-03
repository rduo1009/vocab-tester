#!/usr/bin/env python3

"""Contains functions that inflect English verbs."""

from __future__ import annotations

from typing import TYPE_CHECKING

import lemminflect

from ..accido.misc import ComponentsType, Mood, Number, Tense, Voice
from .edge_cases import STATIVE_VERBS
from .exceptions import InvalidWordError

if TYPE_CHECKING:
    from .. import accido
    from ..accido.type_aliases import Person


def _verify_verb_inflections(components: accido.misc.EndingComponents) -> None:
    if components.type is not ComponentsType.VERB:
        raise ValueError(f"Invalid type: '{components.type}'")

    if (
        components.mood == Mood.PARTICIPLE
        and components.subtype != "participle"
    ):
        raise ValueError(f"Invalid subtype: '{components.subtype}'")

    if (
        components.mood == Mood.INFINITIVE
        and components.subtype != "infinitive"
    ):
        raise ValueError(f"Invalid subtype: '{components.subtype}'")


def find_verb_inflections(
    verb: str,
    components: accido.misc.EndingComponents,
) -> set[str]:
    """Inflect English verbs using the ending components.

    If a participle is queried, find_participle_inflections is ran
    instead.

    Note that subjunctives are not supported as they do not have an exact
    translation in English.

    Parameters
    ----------
    verb : str
        The verb to inflect.
    components : accido.misc.EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the verb.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English verb.
    """
    _verify_verb_inflections(components)

    if components.mood == Mood.PARTICIPLE:
        return _find_participle_inflections(verb, components)[1]

    try:
        lemmas: tuple[str, ...] = lemminflect.getLemma(verb, "VERB")
    except KeyError as e:  # pragma: no cover
        raise InvalidWordError(f"Word {verb} is not a verb") from e

    inflections: set[str] = set()
    if hasattr(components, "number") and hasattr(components, "person"):
        for lemma in lemmas:
            inflections |= _find_lemma(
                lemma,
                components.tense,
                components.voice,
                components.mood,
                components.number,
                components.person,
            )[1]
    else:
        for lemma in lemmas:
            inflections |= _find_lemma(
                lemma,
                components.tense,
                components.voice,
                components.mood,
            )[1]

    return inflections


def find_main_verb_inflection(
    verb: str, components: accido.misc.EndingComponents
) -> str:
    """Find the main inflection of an English verb.

    Parameters
    ----------
    verb : str
        The verb to inflect.
    components : accido.misc.EndingComponents
        The components of the ending.

    Returns
    -------
    str
        The main inflection of the verb.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English verb.
    ValueError
        If the input (other than the word itself) is invalid.
    """
    _verify_verb_inflections(components)

    if components.mood == Mood.PARTICIPLE:
        return _find_participle_inflections(verb, components)[0]

    try:
        lemma: str = lemminflect.getLemma(verb, "VERB")[0]
    except KeyError as e:  # pragma: no cover
        raise InvalidWordError(f"Word {verb} is not a verb") from e

    if hasattr(components, "number") and hasattr(components, "person"):
        return _find_lemma(
            lemma,
            components.tense,
            components.voice,
            components.mood,
            components.number,
            components.person,
        )[0]

    return _find_lemma(
        lemma,
        components.tense,
        components.voice,
        components.mood,
    )[0]

    # HACK: workaround for pydoclint
    raise ValueError  # pragma: no cover


def _find_lemma(  # noqa: PLR0917
    lemma: str,
    tense: Tense,
    voice: Voice,
    mood: Mood,
    number: Number | None = None,
    person: Person | None = None,
) -> tuple[str, set[str]]:
    match (tense, voice, mood):
        case (Tense.PRESENT, Voice.ACTIVE, Mood.INDICATIVE):
            assert number is not None
            assert person is not None

            return _find_preactind_inflections(
                lemma,
                number,
                person,
            )

        case (Tense.IMPERFECT, Voice.ACTIVE, Mood.INDICATIVE):
            assert number is not None
            assert person is not None

            return _find_impactind_inflections(
                lemma,
                number,
                person,
            )

        case (Tense.PERFECT, Voice.ACTIVE, Mood.INDICATIVE):
            assert number is not None
            assert person is not None

            return _find_peractind_inflections(
                lemma,
                number,
                person,
            )

        case (Tense.PLUPERFECT, Voice.ACTIVE, Mood.INDICATIVE):
            assert number is not None
            assert person is not None

            return _find_plpactind_inflections(
                lemma,
                number,
                person,
            )

        case (Tense.PRESENT, Voice.ACTIVE, Mood.INFINITIVE):
            return _find_preactinf_inflections(lemma)

        case (Tense.PRESENT, Voice.ACTIVE, Mood.IMPERATIVE):
            return _find_preipe_inflections(lemma)

        case _:
            raise NotImplementedError(
                f"The {tense.regular} {voice.regular} "
                f"{mood.regular} has not been implemented",
            )


def _find_preactind_inflections(  # type: ignore[return] # mypy cannot manage tuple match
    lemma: str,
    number: Number,
    person: Person,
) -> tuple[str, set[str]]:
    present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    match (number, person):
        case (Number.SINGULAR, 1):
            return (
                f"I {present_nonthird}",
                {
                    f"I {present_nonthird}",
                    f"I am {present_participle}",
                },
            )

        case (Number.PLURAL, 1):
            return (
                f"we {present_nonthird}",
                {
                    f"we {present_nonthird}",
                    f"we are {present_participle}",
                },
            )

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return (
                f"you {present_nonthird}",
                {
                    f"you {present_nonthird}",
                    f"you are {present_participle}",
                },
            )

        case (Number.SINGULAR, 3):
            return (
                f"he {present_third}",
                {
                    f"he {present_third}",
                    f"he is {present_participle}",
                    f"she {present_third}",
                    f"she is {present_participle}",
                    f"it {present_third}",
                    f"it is {present_participle}",
                },
            )

        case (Number.PLURAL, 3):  # pragma: no branch
            return (
                f"they {present_nonthird}",
                {
                    f"they {present_nonthird}",
                    f"they are {present_participle}",
                },
            )


def _find_impactind_inflections(  # type: ignore[return] # mypy cannot manage tuple match
    lemma: str,
    number: Number,
    person: Person,
) -> tuple[str, set[str]]:
    present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    if lemma in STATIVE_VERBS:
        past: str = lemminflect.getInflection(lemma, "VBD")[0]

        match (number, person):
            case (Number.SINGULAR, 1):
                return (
                    f"I {past}",
                    {
                        f"I {past}",
                        f"I was {present_participle}",
                    },
                )

            case (Number.PLURAL, 1):
                return (
                    f"we {past}",
                    {f"we {past}", f"we were {present_participle}"},
                )

            case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
                return (
                    f"you {past}",
                    {f"you {past}", f"you were {present_participle}"},
                )

            case (Number.SINGULAR, 3):
                return (
                    f"he {past}",
                    {
                        f"he {past}",
                        f"he was {present_participle}",
                        f"she {past}",
                        f"she was {present_participle}",
                        f"it {past}",
                        f"it was {present_participle}",
                    },
                )

            case (Number.PLURAL, 3):  # pragma: no branch
                return (
                    f"they {past}",
                    {f"they {past}", f"they were {present_participle}"},
                )

    match (number, person):
        case (Number.SINGULAR, 1):
            return (
                f"I was {present_participle}",
                {f"I was {present_participle}"},
            )

        case (Number.PLURAL, 1):
            return (
                f"we were {present_participle}",
                {f"we were {present_participle}"},
            )

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return (
                f"you were {present_participle}",
                {f"you were {present_participle}"},
            )

        case (Number.SINGULAR, 3):
            return (
                f"he was {present_participle}",
                {
                    f"he was {present_participle}",
                    f"she was {present_participle}",
                    f"it was {present_participle}",
                },
            )

        case (Number.PLURAL, 3):  # pragma: no branch
            return (
                f"they were {present_participle}",
                {f"they were {present_participle}"},
            )


def _find_peractind_inflections(  # type: ignore[return] # mypy cannot manage tuple match
    lemma: str,
    number: Number,
    person: Person,
) -> tuple[str, set[str]]:
    past = lemminflect.getInflection(lemma, "VBD")[0]

    match (number, person):
        case (Number.SINGULAR, 1):
            return (
                f"I {past}",
                {
                    f"I {past}",
                    f"I have {past}",
                    f"I did {lemma}",
                },
            )

        case (Number.PLURAL, 1):
            return (
                f"we {past}",
                {
                    f"we {past}",
                    f"we have {past}",
                    f"we did {lemma}",
                },
            )

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return (
                f"you {past}",
                {
                    f"you {past}",
                    f"you have {past}",
                    f"you did {lemma}",
                },
            )

        case (Number.SINGULAR, 3):
            return (
                f"he {past}",
                {
                    f"he {past}",
                    f"he has {past}",
                    f"he did {lemma}",
                    f"she {past}",
                    f"she has {past}",
                    f"she did {lemma}",
                    f"it {past}",
                    f"it has {past}",
                    f"it did {lemma}",
                },
            )

        case (Number.PLURAL, 3):  # pragma: no branch
            return (
                f"they {past}",
                {
                    f"they {past}",
                    f"they have {past}",
                    f"they did {lemma}",
                },
            )


def _find_plpactind_inflections(  # type: ignore[return] # mypy cannot manage tuple match
    lemma: str,
    number: Number,
    person: Person,
) -> tuple[str, set[str]]:
    past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]

    match (number, person):
        case (Number.SINGULAR, 1):
            return (f"I had {past_participle}", {f"I had {past_participle}"})

        case (Number.PLURAL, 1):
            return (f"we had {past_participle}", {f"we had {past_participle}"})

        case (Number.SINGULAR, 2) | (Number.PLURAL, 2):
            return (
                f"you had {past_participle}",
                {f"you had {past_participle}"},
            )

        case (Number.SINGULAR, 3):
            return (
                f"he had {past_participle}",
                {
                    f"he had {past_participle}",
                    f"she had {past_participle}",
                    f"it had {past_participle}",
                },
            )

        case (Number.PLURAL, 3):  # pragma: no branch
            return (
                f"they had {past_participle}",
                {f"they had {past_participle}"},
            )


def _find_participle_inflections(
    verb: str,
    components: accido.misc.EndingComponents,
) -> tuple[str, set[str]]:
    lemma: str = lemminflect.getLemma(verb, "NOUN")[0]

    match (components.tense, components.voice):
        case (Tense.PERFECT, Voice.PASSIVE):
            past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
            return (
                f"having been {past_participle}",
                {f"having been {past_participle}"},
            )

        case (Tense.PRESENT, Voice.ACTIVE):
            present_participle: str = lemminflect.getInflection(lemma, "VBG")[
                0
            ]
            return (present_participle, {present_participle})

        case _:
            raise NotImplementedError(
                f"The {components.tense.regular} {components.voice.regular} "
                "participle has not been implemented",
            )


def _find_preactinf_inflections(lemma: str) -> tuple[str, set[str]]:
    return (f"to {lemma}", {f"to {lemma}"})


def _find_preipe_inflections(lemma: str) -> tuple[str, set[str]]:
    return (lemma, {lemma})
