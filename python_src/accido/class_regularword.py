#!/usr/bin/env python3

"""Representation of a Latin word that is undeclinable."""

from functools import total_ordering

from .class_word import _Word
from .misc import EndingComponents
from .type_aliases import Meaning


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
    {'': 'sed'}

    Note that the arguments of RegularWord are keyword-only.
    """

    def __init__(self, *, word: str, meaning: Meaning) -> None:
        """Initialises RegularWord.

        Parameters
        ----------
        word : str
        meaning : Meaning
        """
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
        'sed'
        """
        return self.word

    @staticmethod
    def _create_namespace(
        key: str,  # noqa: ARG004
    ) -> EndingComponents:  # pragma: no cover # this should never be ran
        return EndingComponents(string="")

    def __repr__(self) -> str:
        return f"RegularWord({self.word}, {self.meaning})"
