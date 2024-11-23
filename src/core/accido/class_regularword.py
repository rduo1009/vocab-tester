"""Representation of a Latin word that is undeclinable."""

from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING

from .class_word import _Word
from .misc import EndingComponents, MultipleMeanings

if TYPE_CHECKING:
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
    >>> foo = RegularWord("sed", meaning="but")
    >>> foo.endings
    {'': 'sed'}

    Note that the arguments of RegularWord are keyword-only.
    """

    __slots__ = ("word",)

    def __init__(self, word: str, *, meaning: Meaning) -> None:
        """Initialise RegularWord.

        Parameters
        ----------
        word : str
        meaning : Meaning
        """
        self.word: str = word
        self._first: str = self.word
        self.meaning: Meaning = meaning
        self.endings = {"": self.word}

    def get(self) -> str:
        """Return the word.

        Returns
        -------
        str
            The word.

        Examples
        --------
        >>> foo = RegularWord("sed", meaning="but")
        >>> foo.get()
        'sed'
        """
        return self.word

    @staticmethod
    def _create_components(
        key: str,  # noqa: ARG004
    ) -> EndingComponents:
        return EndingComponents(string="")

    def __repr__(self) -> str:
        return f"RegularWord({self.word}, {self.meaning})"

    def __str__(self) -> str:
        return f"{self.meaning}: {self.word}"

    def __add__(self, other: object) -> RegularWord:
        if not isinstance(other, RegularWord) or self.word != other.word:
            return NotImplemented

        if self.meaning == other.meaning:
            return RegularWord(self.word, meaning=self.meaning)

        new_meaning: Meaning
        if isinstance(self.meaning, MultipleMeanings) or isinstance(
            other.meaning, MultipleMeanings
        ):
            new_meaning = self.meaning + other.meaning
        else:
            new_meaning = MultipleMeanings((self.meaning, other.meaning))

        return RegularWord(self.word, meaning=new_meaning)
