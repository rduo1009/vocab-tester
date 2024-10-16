#!/usr/bin/env python3
# -*- coding: future_typing -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

import sys
from typing import Literal

if sys.version_info < (3, 10):  # use backport if python3.9
    from typing_extensions import TypeAlias, TypeGuard
else:
    from typing import TypeAlias, TypeGuard

from ....accido.misc import MultipleEndings, MultipleMeanings

Ending: TypeAlias = str | MultipleEndings
Endings: TypeAlias = dict[str, Ending]
Meaning: TypeAlias = str | MultipleMeanings

NounDeclension: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
AdjectiveDeclension: TypeAlias = Literal["212", "3"]
Conjugation: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
Termination: TypeAlias = Literal[1, 2, 3]
Person: TypeAlias = Literal[1, 2, 3]


def is_person(x: int) -> TypeGuard[Person]:
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


def is_termination(x: int) -> TypeGuard[Termination]:
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
