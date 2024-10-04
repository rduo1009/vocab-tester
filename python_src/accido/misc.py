#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous functions, classes and constants used by accido."""

from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace
from typing import TYPE_CHECKING, Final, Literal

from .. import accido

if TYPE_CHECKING:
    # HACK: To avoid mypy errors.
    from enum import Enum
else:
    from aenum import Enum

from aenum import MultiValue  # type: ignore[import-untyped]


class _EndingComponentEnum(Enum):
    regular: str
    shorthand: str


class Number(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the grammatical number."""

    SINGULAR = "singular", "sg"
    PLURAL = "plural", "pl"


class Tense(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the tense of a verb."""

    PRESENT = "present", "pre"
    IMPERFECT = "imperfect", "imp"
    FUTURE = "future", "fut"
    PERFECT = "perfect", "per"
    PLUPERFECT = "pluperfect", "plp"
    # FUTURE_PERFECT = "future perfect", "fpr"


class Voice(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the voice of a verb."""

    ACTIVE = "active", "act"
    PASSIVE = "passive", "pas"


class Mood(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the mood of a verb."""

    INDICATIVE = "indicative", "ind"
    INFINITIVE = "infinitive", "inf"
    IMPERATIVE = "imperative", "ipe"
    SUBJUNCTIVE = "subjunctive", "sbj"
    PARTICIPLE = "participle", "ptc"


class Case(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the case of a noun."""

    NOMINATIVE = "nominative", "nom"
    VOCATIVE = "vocative", "voc"
    ACCUSATIVE = "accusative", "acc"
    GENITIVE = "genitive", "gen"
    DATIVE = "dative", "dat"
    ABLATIVE = "ablative", "abl"


class Gender(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the gender of a noun or adjective."""

    MASCULINE = "masculine", "m"
    FEMININE = "feminine", "f"
    NEUTER = "neuter", "n"


class Degree(
    _EndingComponentEnum, settings=MultiValue, init="regular shorthand"
):
    """Represents the degree of an adjective."""

    POSITIVE = "positive", "pos"
    COMPARATIVE = "comparative", "cmp"
    SUPERLATIVE = "superlative", "spr"


"""Mapping of person values to their more concise abbreviated forms."""
PERSON_SHORTHAND: Final[dict[int, str]] = {
    1: "1st person",
    2: "2nd person",
    3: "3rd person",
}

type Person = Literal[1, 2, 3]


class EndingComponents:
    """A container for the grammatical components of an ending.

    Examples
    --------
    >>> foo = EndingComponents(
    ...     case=Case.NOMINATIVE,
    ...     number=Number.SINGULAR,
    ...     string="nominative singular",
    ... )
    >>> foo.number.regular
    'singular'

    For nouns.

    >>> foo = EndingComponents(
    ...     case=Case.NOMINATIVE,
    ...     gender=Gender.MASCULINE,
    ...     number=Number.SINGULAR,
    ...     string="nominative singular masculine",
    ... )
    >>> foo.case.regular
    'nominative'

    For pronouns.

    >>> foo = EndingComponents(
    ...     case=Case.NOMINATIVE,
    ...     gender=Gender.MASCULINE,
    ...     number=Number.SINGULAR,
    ...     degree=Degree.SUPERLATIVE,
    ...     string="nominative singular masculine superlative",
    ... )
    >>> foo.case.regular
    'nominative'

    For adjectives.

    >>> foo = EndingComponents(degree=Degree.SUPERLATIVE, string="superlative")
    >>> foo.degree.regular
    'superlative'

    For adverbs.

    >>> foo = EndingComponents(
    ...     tense=Tense.IMPERFECT,
    ...     voice=Voice.ACTIVE,
    ...     mood=Mood.INDICATIVE,
    ...     number=Number.SINGULAR,
    ...     person=1,
    ...     string="imperfect active indicative singular 1st person",
    ... )
    >>> foo.person
    1

    For verbs.

    >>> foo = EndingComponents(
    ...     tense=Tense.PERFECT,
    ...     voice=Voice.PASSIVE,
    ...     mood=Mood.PARTICIPLE,
    ...     gender=Gender.MASCULINE,
    ...     case=Case.NOMINATIVE,
    ...     number=Number.SINGULAR,
    ...     string="perfect passive participle masculine nominative singular",
    ... )
    >>> foo.tense.regular
    'perfect'

    For participles.

    >>> foo = EndingComponents(
    ...     tense=Tense.PERFECT,
    ...     voice=Voice.ACTIVE,
    ...     mood=Mood.INFINITIVE,
    ...     string="perfect active infinitive",
    ... )
    >>> foo.mood.regular
    'infinitive'

    For infinitives.
    """

    def __init__(
        self,
        *,
        case: Case | None = None,
        number: Number | None = None,
        gender: Gender | None = None,
        tense: Tense | None = None,
        voice: Voice | None = None,
        mood: Mood | None = None,
        person: Person | None = None,
        degree: Degree | None = None,
        string: str = "",  # HACK: Should be required.
    ) -> None:
        """Initialises EndingComponents.

        Determines the type and subtype of the ending.

        Parameters
        ----------
        case : Case | None, optional
            The case of the ending.
        number : Number | None, optional
            The number of the ending.
        gender : Gender | None, optional
            The gender of the ending
        tense : Tense | None, optional
            The tense of the ending.
        voice : Voice | None, optional
            The voice of the ending.
        mood : Mood | None, optional
            The mood of the ending.
        person : Person | None, optional
            The person of the ending.
        degree : Degree | None, optional
            The degree of the ending.
        string : str, default=""
            The string representation of the ending. It is actually required,
            but it is not possible to make it required because of the way
            the class is initialised.

        Raises
        ------
        ValueError
            If no string is provided. (should never happen)
        """
        if case:
            self.case: Case = case
        if number:
            self.number: Number = number
        if gender:
            self.gender: Gender = gender
        if tense:
            self.tense: Tense = tense
        if voice:
            self.voice: Voice = voice
        if mood:
            self.mood: Mood = mood
        if degree:
            self.degree: Degree = degree
        if person:
            self.person: Person = person
        if string:
            self.string: str = string
        else:  # pragma: no cover
            raise ValueError("No string provided.")

        self.type: type[accido.endings._Word]
        self.subtype: str | None
        self.type, self.subtype = self._determine_type()

    def _get_non_null_attributes(self) -> list[str]:
        return [
            attr
            for attr, value in vars(self).items()
            if value is not None and attr != "string"
        ]

    def _determine_type(self) -> tuple[type[accido.endings._Word], str | None]:
        attributes = self._get_non_null_attributes()

        if set(attributes) == {"tense", "voice", "mood", "person", "number"}:
            return (accido.endings.Verb, None)
        if set(attributes) == {"tense", "voice", "mood"}:
            return (accido.endings.Verb, "infinitive")
        if set(attributes) == {
            "tense",
            "voice",
            "mood",
            "number",
            "gender",
            "case",
        }:
            return (accido.endings.Verb, "participle")
        if set(attributes) == {"degree"}:
            return (accido.endings.Adjective, "adverb")
        if set(attributes) == {"number", "gender", "case", "degree"}:
            return (accido.endings.Adjective, None)
        if set(attributes) == {"number", "gender", "case"}:
            return (accido.endings.Pronoun, None)
        if set(attributes) == {"number", "case"}:
            return (accido.endings.Noun, None)
        if not set(attributes):
            return (accido.endings.RegularWord, None)
        raise ValueError(
            f"Invalid combination of attributes: {', '.join(attributes)}"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EndingComponents):
            return NotImplemented

        self_attrs = self._get_non_null_attributes()
        other_attrs = other._get_non_null_attributes()

        if self_attrs != other_attrs:
            return False

        return all(
            getattr(self, attr) == getattr(other, attr) for attr in self_attrs
        )

    def __repr__(self) -> str:
        return self.string

    def __hash__(self) -> int:
        return hash(
            tuple(
                getattr(self, attr) for attr in self._get_non_null_attributes()
            )
        )


@dataclass(init=True)
class MultipleMeanings:
    """Represents multiple meanings, with a main meaning and other meanings.

    Attributes
    ----------
    meanings : list[str]
        The meanings.

    Notes
    -----
    This class allows for there to be several English definitions of one
    Latin word. This means for translating-to-English questions, synonyms
    can be accepted, but not vice versa.

    Examples
    --------
    >>> foo = MultipleMeanings(["hide", "conceal"])
    >>> foo.meanings
    ['hide', 'conceal']

    >>> foo.__str__()
    'hide'
    """

    meanings: list[str]

    def __str__(self) -> str:
        return self.meanings[0]

    def __repr__(self) -> str:
        return f"MultipleMeanings({', '.join(self.meanings)})"


class MultipleEndings(SimpleNamespace):
    """Represents multiple endings for a word, where each ending is a
    separate string.

    The fact that the attribute names can be customised means that this
    class can be used for many use cases.
    e.g. MultipleEndings(regular="nostri", partitive="nostrum")
    would allow for nostrum being the partitive genitive, while nostri
    for the rest of the genitive uses.

    Attributes
    ----------
    value : str
    etc.

    Examples
    --------
    >>> foo = MultipleEndings(regular="nostri", partitive="nostrum")
    >>> foo.regular
    'nostri'

    >>> foo.__str__()
    'nostri/nostrum'

    >>> foo.get_all()
    ['nostri', 'nostrum']
    """  # noqa: D205

    def get_all(self) -> list[str]:
        """Returns a list of all the possible endings.

        Returns
        -------
        list[str]
            The endings.
        """
        return list(self.__dict__.values())

    def __str__(self) -> str:
        return "/".join(self.__dict__.values())

    def __add__(self, val2: str) -> str:
        return self.__str__() + val2

    # Allows for a prefix to be added to all of the endings.
    def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
        prefixed = {
            key: f"{val2}{value}" for key, value in self.__dict__.items()
        }
        return MultipleEndings(**prefixed)
