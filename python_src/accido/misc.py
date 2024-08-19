#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous functions, classes and constants used by accido."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from types import SimpleNamespace
from typing import Any, Final

"""Mapping of number values to their more concise abbreviated forms."""
NUMBER_SHORTHAND: Final[dict[str, str]] = {
    "singular": "sg",
    "plural": "pl",
}  # fmt: skip

"""Mapping of tense values to their more concise abbreviated forms."""
TENSE_SHORTHAND: Final[dict[str, str]] = {
    "present": "pre",
    "imperfect": "imp",
    "future": "fut",
    "perfect": "per",
    "pluperfect": "plp",
    # "future perfect": "fpr",
}  # fmt: skip

"""Mapping of voice values to their more concise abbreviated forms."""
VOICE_SHORTHAND: Final[dict[str, str]] = {
    "active": "act",
    "passive": "pas",
}  # fmt: skip

"""Mapping of mood values to their more concise abbreviated forms."""
MOOD_SHORTHAND: Final[dict[str, str]] = {
    "indicative": "ind",
    "infinitive": "inf",
    "imperative": "ipe",
    "subjunctive": "sbj",
    "participle": "ptc",
}  # fmt: skip

"""Mapping of case values to their more concise abbreviated forms."""
CASE_SHORTHAND: Final[dict[str, str]] = {
    "nominative": "nom",
    "vocative": "voc",
    "accusative": "acc",
    "genitive": "gen",
    "dative": "dat",
    "ablative": "abl",
}  # fmt: skip

"""Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND: Final[dict[str, str]] = {
    "masculine": "m",
    "feminine": "f",
    "neuter": "n",
}  # fmt: skip

"""Mapping of degree values to their more concise abbreviated forms."""
DEGREE_SHORTHAND: Final[dict[str, str]] = {
    "positive": "pos",
    "comparative": "cmp",
    "superlative": "spr",
}  # fmt: skip

"""Mapping of person values to their more concise abbreviated forms."""
PERSON_SHORTHAND: Final[dict[int, str]] = {
    1: "1st person",
    2: "2nd person",
    3: "3rd person",
}  # fmt: skip


class EndingComponents(SimpleNamespace):
    """A container for the grammatical components of an ending.

    Examples
    --------
    >>> foo = EndingComponents(case="nominative", gender="masculine", \
                               number="singular")
    """

    pass


@dataclass(init=True)
class MultipleMeanings:
    """Represents multiple meanings, with a main meaning and other
    meanings.

    Attributes
    ----------
    raw_meanings : list[str]
    meanings : set[str]
        The meanings.
    main_meaning : str
        The main meaning.

    Notes
    -----
    This class allows for there to be several English definitions of one
    Latin word. This means for translating-to-English questions, synonyms
    can be accepted, but not vice versa.
    """

    raw_meanings: list[str]

    def __str__(self) -> str:
        return self.main_meaning

    def __repr__(self) -> str:
        return f"MultipleMeanings({', '.join(self.raw_meanings)})"

    def __post_init__(self) -> None:
        """If other_meanings is a string, convert it to a list."""
        self.main_meaning: str = self.raw_meanings[0]
        self.meanings: set[str] = set(self.raw_meanings)


class MultipleEndings:
    """Represents multiple endings for a word, where each ending is a
    separate string.
    The fact that the attribute names can be customises means that this
    class can be used for many use cases.
    e.g. MultipleEndings(regular="nostri", partitive="nostrum")
    would allow for nostrum being the partitive genitive, while nostri
    for the rest of the genitive uses.

    Attributes
    ----------
    value : str

    etc.
    """

    def __init__(self, **kwargs: str) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

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
    def __radd__(self, val2: str) -> "MultipleEndings":  # pragma: no cover
        prefixed = {
            key: f"{val2}{value}" for key, value in self.__dict__.items()
        }
        return MultipleEndings(**prefixed)


def key_from_value(dd: dict[Any, Any] | dict[Any, Any], value: Any) -> Any:
    """Returns the value in a dictionary from its key.
    If no key is found with the given value, returns `None`.

    Parameters
    ----------
    dd : dict[Any, Any]
        The dictionary to search.
    value : Any
        The value to search for.

    Returns
    -------
    Any
        The first key whose value matches 'value', or None if not
        found.
    """

    return next((key for key, val in dd.items() if val == value), None)


if sys.version_info >= (3, 12):
    from .type_hints import Ending as Ending
    from .type_hints import Endings as Endings
    from .type_hints import Meaning as Meaning

else:  # pragma: no cover
    # The type statement was added in 3.12, so TypeAlias is used instead
    from typing import TypeAlias

    Ending: TypeAlias = str | MultipleEndings
    Endings: TypeAlias = dict[str, Ending]
    Meaning: TypeAlias = str | MultipleMeanings
