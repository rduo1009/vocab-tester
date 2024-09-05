#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""General functions used by vocab-tester and its tests."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


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


def compare(first: Iterable[Any], second: Iterable[Any]) -> bool:
    """Compares two iterables."""
    comparison = list(second)  # make a mutable copy
    try:
        for elem in first:
            comparison.remove(elem)
    except ValueError:  # pragma: no cover
        return False
    return not comparison
