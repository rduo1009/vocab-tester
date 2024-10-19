#!/usr/bin/env python3

"""Contains functions that pick items from sets."""

from __future__ import annotations

import random


def set_choice[T](s: set[T]) -> T:
    """Chooses a random element from a set.

    Parameters
    ----------
    s : set[T]
    The set to choose from.

    Returns
    -------
    T
        A random element from the set.
    """
    return random.choice(tuple(s))


def set_choice_pop[T](s: set[T]) -> T:
    """Chooses a random element from a set and removes it from the set.

    Parameters
    ----------
    x : set[T]
        The set to choose from.

    Returns
    -------
    T
        A random element from the set.
    """
    value = random.choice(tuple(s))
    s.remove(value)
    return value
