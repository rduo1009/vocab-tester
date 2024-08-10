#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous functions and classes used by accido."""

from dataclasses import dataclass
from typing import Any

from frozendict import frozendict


@dataclass(init=True)
class MultipleMeanings:
    """Represents multiple meanings, with a best meaning and other
    meanings.

    Attributes
    ----------
    meanings : list[str]
        The meanings, the input of the class.
    best_meaning : str
        The best meaning.
    other_meanings : list[str], str
        Other meanings.

    Notes
    -----
    This class allows for there to be several English definitions of one
    Latin word. This means for translating-to-English questions, synonyms
    can be accepted, but not vice versa.

    The meanings and other_meanings list is intended to be ordered from
    better to worse meanings.
    e.g. meanings = ["clever", "cunning", "callid"]
    'Callid' is technically correct, but not a very commonly used word, so
    it is put later in thelist.
    """

    meanings: list[str]

    def __str__(self) -> str:
        return self.best_meaning

    def __repr__(self) -> str:
        return f"MultipleMeanings({",".join(self.meanings)})"

    def __post_init__(self) -> None:
        """If other_meanings is a string, convert it to a list."""
        self.best_meaning: str = self.meanings[0]
        self.other_meanings: list[str] = self.meanings[1:]


class MultipleEndings:
    """Represents multiple endings for a word, where each ending is a
    separate string.
    The fact that the attribute names can be customises means that this
    class can be used for many use cases.
    e.g. MultipleEndings(RegularWord="nostri", partitive="nostrum")
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
