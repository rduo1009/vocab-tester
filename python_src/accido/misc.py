#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous functions, classes and constants used by accido."""

from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace
from typing import Final

"""Mapping of number values to their more concise abbreviated forms."""
NUMBER_SHORTHAND: Final[dict[str, str]] = {
    "singular": "sg",
    "plural": "pl",
}

"""Mapping of tense values to their more concise abbreviated forms."""
TENSE_SHORTHAND: Final[dict[str, str]] = {
    "present": "pre",
    "imperfect": "imp",
    "future": "fut",
    "perfect": "per",
    "pluperfect": "plp",
    # "future perfect": "fpr",
}

"""Mapping of voice values to their more concise abbreviated forms."""
VOICE_SHORTHAND: Final[dict[str, str]] = {
    "active": "act",
    "passive": "pas",
}

"""Mapping of mood values to their more concise abbreviated forms."""
MOOD_SHORTHAND: Final[dict[str, str]] = {
    "indicative": "ind",
    "infinitive": "inf",
    "imperative": "ipe",
    "subjunctive": "sbj",
    "participle": "ptc",
}

"""Mapping of case values to their more concise abbreviated forms."""
CASE_SHORTHAND: Final[dict[str, str]] = {
    "nominative": "nom",
    "vocative": "voc",
    "accusative": "acc",
    "genitive": "gen",
    "dative": "dat",
    "ablative": "abl",
}

"""Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND: Final[dict[str, str]] = {
    "masculine": "m",
    "feminine": "f",
    "neuter": "n",
}

"""Mapping of degree values to their more concise abbreviated forms."""
DEGREE_SHORTHAND: Final[dict[str, str]] = {
    "positive": "pos",
    "comparative": "cmp",
    "superlative": "spr",
}

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
