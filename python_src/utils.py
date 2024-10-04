#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""General functions used by vocab-tester and its tests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterable


def compare(first: Iterable[Any], second: Iterable[Any]) -> bool:
    """Compares two iterables.

    Parameters
    ----------
    first : Iterable[Any]
        The first iterable to compare.
    second : Iterable[Any]
        The second iterable to compare.

    Returns
    -------
    bool
        True if the iterables are equal, False otherwise.

    Notes
    -----
    Code taken from https://stackoverflow.com/a/7829388
    """
    comparison = list(second)  # make a mutable copy
    try:
        for elem in first:
            comparison.remove(elem)
    except ValueError:  # pragma: no cover
        return False
    return not comparison
