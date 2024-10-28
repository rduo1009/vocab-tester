"""Contains functions that deal with duplicates in tuples and lists."""

from collections.abc import Hashable, Sequence
from itertools import groupby


def _is_hashable[T](sequence: Sequence[T]) -> bool:
    return all(isinstance(item, Hashable) for item in sequence)


def contains_duplicates[T](sequence: Sequence[T]) -> bool:
    """Determine if a list or tuple contains duplicate items.

    Parameters
    ----------
    sequence : Sequence[T]
        The list or tuple.

    Returns
    -------
    bool
        True if there are duplicate items, False otherwise.

    Notes
    -----
    Code taken from https://stackoverflow.com/a/1541827
    """
    if _is_hashable(sequence):
        return len(sequence) != len(set(sequence))

    seen: list[T] = []
    for item in sequence:
        if item in seen:
            return True
        seen.append(item)
    return False


def remove_duplicates[C](sequence: Sequence[C]) -> Sequence[C]:
    """Remove duplicates from a list or tuple.

    Note that this does not keep order.

    Parameters
    ----------
    sequence : Sequence[C]
        The list or tuple.

    Returns
    -------
    Sequence[C]
        The list or tuple without duplicates.

    Notes
    -----
    Code taken from https://stackoverflow.com/a/10784473
    """
    if _is_hashable(sequence):
        return type(sequence)(set(sequence))  # type: ignore[call-arg]

    return type(sequence)(k for k, v in groupby(sorted(sequence)))  # type: ignore[call-arg, type-var]
