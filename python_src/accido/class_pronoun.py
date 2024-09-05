#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin pronoun with endings."""

from __future__ import annotations

from functools import total_ordering

from ..utils import key_from_value
from .class_word import _Word
from .edge_cases import PRONOUNS
from .exceptions import InvalidInputError
from .misc import (
    CASE_SHORTHAND,
    GENDER_SHORTHAND,
    NUMBER_SHORTHAND,
    Ending,
    EndingComponents,
    Meaning,
)


@total_ordering
class Pronoun(_Word):
    """Representation of a Latin pronoun with endings.

    Attributes
    ----------
    pronoun : str
    meaning : Meaning
    endings : Endings

    Examples
    --------
    >>> foo = Pronoun(pronoun="hic", meaning="this")
    >>> foo["Pmnomsg"]
    'hic'

    Note that the arguments of Pronoun are keyword-only.
    """

    def __init__(self, *, pronoun: str, meaning: Meaning) -> None:
        """Intialises Pronoun and determines the endings.

        Parameters
        ----------
        pronoun : str
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the pronoun entered is not in the pronoun table.

        Notes
        -----
        As pronouns in Latin have irregular endings with little pattern,
        the pronoun endings are manually written out in the edge_cases
        module.
        """

        super().__init__()
        try:
            self.endings = PRONOUNS[pronoun]
        except KeyError as e:
            raise InvalidInputError(
                f"Pronoun '{pronoun}' not recognised"
            ) from e

        self.pronoun: str = pronoun
        self._first = self.pronoun
        self.meaning: Meaning = meaning

        self._mascnom: Ending = self.endings["Pmnomsg"]
        self._femnom: Ending = self.endings["Pfnomsg"]
        self._neutnom: Ending = self.endings["Pnnomsg"]

    def get(self, *, gender: str, case: str, number: str) -> Ending | None:
        """Returns the ending of the pronoun.
        The function returns None if no ending is found.

        Parameters
        ----------
        gender, case, number : str

        Returns
        -------
        Ending
            The ending found.
        None
            If no ending is found

        Raises
        ------
        InvalidInputError
            If the input is invalid.

            If an ending cannot be found.

        Examples
        --------
        >>> foo = Pronoun(pronoun="hic", meaning="this")
        >>> foo.get(gender="masculine", case="nominative", number="singular")
        'hic'

        Note that the arguments of get are keyword-only.
        """

        if gender not in GENDER_SHORTHAND:
            raise InvalidInputError(f"Invalid gender: '{gender}'")

        if case not in CASE_SHORTHAND:
            raise InvalidInputError(f"Invalid case: '{case}'")

        if number not in NUMBER_SHORTHAND:
            raise InvalidInputError(f"Invalid number: '{number}'")

        short_gender: str = GENDER_SHORTHAND[gender]
        short_case: str = CASE_SHORTHAND[case]
        short_number: str = NUMBER_SHORTHAND[number]

        return self.endings.get(f"P{short_gender}{short_case}{short_number}")

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents = EndingComponents(
            gender=key_from_value(GENDER_SHORTHAND, key[1]),
            case=key_from_value(CASE_SHORTHAND, key[2:5]),
            number=key_from_value(NUMBER_SHORTHAND, key[5:7]),
        )
        output.string = f"{output.case} {output.number} {output.gender}"
        return output

    def __repr__(self) -> str:
        return f"Pronoun({self.pronoun}, {self.meaning})"

    def __str__(self) -> str:
        return (
            f"{self.meaning}: {self._mascnom}, {self._femnom}, {self._neutnom}"
        )
