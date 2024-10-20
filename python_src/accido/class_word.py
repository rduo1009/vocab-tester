#!/usr/bin/env python3

"""Representation of a Latin word."""

from __future__ import annotations

from abc import ABC, abstractmethod
from functools import total_ordering
from typing import TYPE_CHECKING, Any

from .misc import EndingComponents, MultipleEndings

if TYPE_CHECKING:
    from .type_aliases import Ending, Endings, Meaning


@total_ordering
class _Word(ABC):  # noqa: PLW1641
    """Representation of an word.

    This class is not intended to be used by the user. Rather, all of the
    other classes inherit from this class.

    Attributes
    ----------
    endings : Ending
    _first : str
        The first principal part. Used so that the word classes can be
        alphabetically sorted.
    meaning : Meaning
        The meaning of the word.
    """

    def __init__(self) -> None:
        """Initialises _Word (and all classes that inherit from it)."""
        self.endings: Endings
        self._first: str
        self.meaning: Meaning

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _Word):
            return NotImplemented
        return self.endings == other.endings

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, _Word):
            return NotImplemented
        return self._first < other._first

    def __getitem__(self, key: str) -> Ending:
        return self.endings[key]

    def find(self, form: str) -> list[EndingComponents]:
        """Finds the accido properties that match the given form.

        Attributes
        ----------
        form : str
            The form to search for.

        Returns
        -------
        list[EndingComponents]
            The list of EndingComponents objects that represent the endings
            that match the given form.
        """
        return [
            self._create_namespace(key)
            for key, value in self.endings.items()
            if (isinstance(value, MultipleEndings) and form in value.get_all())
            or (not isinstance(value, MultipleEndings) and value == form)
        ]

    # Force implementation of these methods
    # docstr-coverage:excused `abstract method`
    @abstractmethod
    def get(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> (
        Ending | None
    ):  # pragma: no cover # sourcery skip: docstrings-for-functions
        ...

    @staticmethod
    @abstractmethod
    def _create_namespace(key: str) -> EndingComponents:  # pragma: no cover
        ...
