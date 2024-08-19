#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin word that is undeclinable."""

from __future__ import annotations

from functools import total_ordering

from .class_word import _Word
from .misc import EndingComponents, Meaning


@total_ordering
class RegularWord(_Word):
    """Representation of a Latin word that is undeclinable.

    Attributes
    ----------
    word : str
    meaning : Meaning

    Examples
    --------
    >>> foo = RegularWord(word="sed", meaning="but")
    >>> foo.endings
    {"": "sed"}
    """  # fmt: skip

    def __init__(self, word: str, meaning: Meaning):
        self.word: str = word
        self.meaning: Meaning = meaning
        self.endings = {"": self.word}

    def get(self) -> str:
        """Returns the word.

        Returns
        -------
        str
            The word.
        
        Examples
        --------
        >>> foo = RegularWord(word="sed", meaning="but")
        >>> foo.get()
        "sed"
        """  # fmt: skip
        return self.word

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:  # pragma: no cover
        return NotImplemented

    def __repr__(self) -> str:
        return f"RegularWord({self.word}, {self.meaning})"
