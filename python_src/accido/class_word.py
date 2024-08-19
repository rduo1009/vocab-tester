#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin word."""

from __future__ import annotations

from abc import ABC, abstractmethod
from functools import total_ordering
from typing import Any

from .misc import Ending, EndingComponents, Endings, MultipleEndings


@total_ordering
class _Word(ABC):
    """Representation of an word.
    This class is not intended to be used by the user. Rather, all of the
    other classes inherit from this class.

    Attributes
    ----------
    endings : Ending
    _first : str
        The first principal part. Used so that the word classes can be
        alphabetically sorted.
    """

    def __init__(self) -> None:
        self.endings: Endings
        self._first: str
        self._unique_endings: set[Ending] = set()

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
        """Finds the accidol properties that match the given form.

        Attributes
        ----------
        form : str
            The form to search for.

        Returns
        -------
        list[EndingComponents]
            The list of EndingComponents objects that represent the endings 
            that match the given form.
        """  # fmt: skip

        results = []
        for key, value in self.endings.items():
            if isinstance(value, MultipleEndings):
                if form in value.get_all():
                    results.append(self._create_namespace(key))
            elif value == form:
                results.append(self._create_namespace(key))
        return results

    # Force implementation of these methods
    @abstractmethod
    def get(
        self, *args: Any, **kwargs: Any
    ) -> Ending | None:  # pragma: no cover
        pass

    @staticmethod
    @abstractmethod
    def _create_namespace(key: str) -> EndingComponents:  # pragma: no cover
        pass
