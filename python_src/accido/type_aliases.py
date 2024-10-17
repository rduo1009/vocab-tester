#!/usr/bin/env python3

"""Contains type aliases used by accido."""

from __future__ import annotations

from typing import Literal, TypeIs

from ..accido.misc import MultipleEndings, MultipleMeanings

type Ending = str | MultipleEndings
type Endings = dict[str, Ending]
type Meaning = str | MultipleMeanings

type NounDeclension = Literal[0, 1, 2, 3, 4, 5]
type AdjectiveDeclension = Literal["212", "3"]
type Conjugation = Literal[0, 1, 2, 3, 4, 5]
type Termination = Literal[1, 2, 3]
type Person = Literal[1, 2, 3]


def is_person(x: int) -> TypeIs[Person]:
    """Check if the given value is a valid person (1, 2, or 3).

    Parameters
    ----------
    x : int
        The value to check.

    Returns
    -------
    bool
        True if the value is a valid person, False otherwise.
    """
    return x in {1, 2, 3}


def is_termination(x: int) -> TypeIs[Termination]:
    """Check if the given value is a valid termination (1, 2, or 3).

    Parameters
    ----------
    x : int
        The value to check.

    Returns
    -------
    bool
        True if the value is a valid termination, False otherwise.
    """
    return x in {1, 2, 3}
