#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous functions and classes used by accido."""

from dataclasses import dataclass
from typing import Any

from frozendict import frozendict


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
        return f"MultipleMeanings({",".join(self.meanings)})"

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
    def __radd__(self, val2: str) -> "MultipleEndings":
        prefixed = {
            key: f"{val2}{value}" for key, value in self.__dict__.items()
        }
        return MultipleEndings(**prefixed)


def key_from_value(
    dd: frozendict[Any, Any] | dict[Any, Any], value: Any
) -> Any:
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


# Type annotation support
type Ending = str | MultipleEndings
type Endings = frozendict[str, Ending]
type Meaning = str | MultipleMeanings
