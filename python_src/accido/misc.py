#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous functions, classes and constants used by accido."""

from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace

from aenum import Enum, MultiValue


class Number(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the grammatical number."""

    SINGULAR = "singular", "sg"
    PLURAL = "plural", "pl"


class Tense(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the tense of a verb."""

    PRESENT = "present", "pre"
    IMPERFECT = "imperfect", "imp"
    FUTURE = "future", "fut"
    PERFECT = "perfect", "per"
    PLUPERFECT = "pluperfect", "plp"
    # FUTURE_PERFECT = "future perfect", "fpr"


class Voice(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the voice of a verb."""

    ACTIVE = "active", "act"
    PASSIVE = "passive", "pas"


class Mood(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the mood of a verb."""

    INDICATIVE = "indicative", "ind"
    INFINITIVE = "infinitive", "inf"
    IMPERATIVE = "imperative", "ipe"
    SUBJUNCTIVE = "subjunctive", "sbj"
    PARTICIPLE = "participle", "ptc"


class Case(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the case of a noun."""

    NOMINATIVE = "nominative", "nom"
    VOCATIVE = "vocative", "voc"
    ACCUSATIVE = "accusative", "acc"
    GENITIVE = "genitive", "gen"
    DATIVE = "dative", "dat"
    ABLATIVE = "ablative", "abl"


class Gender(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the gender of a noun or adjective."""

    MASCULINE = "masculine", "m"
    FEMININE = "feminine", "f"
    NEUTER = "neuter", "n"


class Degree(Enum, settings=MultiValue, init="regular shorthand"):
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


class EndingComponents(SimpleNamespace):
    """A container for the grammatical components of an ending.

    Examples
    --------
    >>> foo = EndingComponents(case="nominative", gender="masculine", \
                               number="singular")
    >>> foo.case
    'nominative'
    """


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
