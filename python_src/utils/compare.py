#!/usr/bin/env python3

"""Contains a function that compares sequences."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def compare[T](first: Sequence[T], second: Sequence[T]) -> bool:
    """Compare two sequences.

    Parameters
    ----------
    first : Sequence[T]
        The first iterable to compare.
    second : Sequence[T]
        The second iterable to compare.

    Returns
    -------
    bool
        True if the sequences are equal, False otherwise.

    Notes
    -----
    Code taken from https://stackoverflow.com/a/7829388
    """
    comparison: list[T] = list(second)  # make a mutable copy

    try:
        for elem in first:
            comparison.remove(elem)
    except ValueError:  # pragma: no cover
        return False

    return not comparison
