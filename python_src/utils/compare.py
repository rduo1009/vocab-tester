#!/usr/bin/env python3

"""Contains a function that compares iterables.

Notes
-----
Code taken from https://stackoverflow.com/a/7829388
"""

from typing import Iterable


def compare[T](first: Iterable[T], second: Iterable[T]) -> bool:
    """Compares two iterables.

    Parameters
    ----------
    first : Iterable[T]
        The first iterable to compare.
    second : Iterable[T]
        The second iterable to compare.

    Returns
    -------
    bool
        True if the iterables are equal, False otherwise.s

    """
    comparison: list[T] = list(second)  # make a mutable copy
    try:
        for elem in first:
            comparison.remove(elem)
    except ValueError:  # pragma: no cover
        return False
    return not comparison
