#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin pronoun with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING

from .class_word import _Word
from .edge_cases import PRONOUNS
from .exceptions import InvalidInputError
from .misc import (
    Case,
    EndingComponents,
    Gender,
    Number,
)

if TYPE_CHECKING:
    from .type_aliases import Ending, Meaning


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
                f"Pronoun '{pronoun}' not recognised",
            ) from e

        self.pronoun: str = pronoun
        self._first = self.pronoun
        self.meaning: Meaning = meaning

        self._mascnom: Ending = self.endings["Pmnomsg"]
        self._femnom: Ending = self.endings["Pfnomsg"]
        self._neutnom: Ending = self.endings["Pnnomsg"]

    def get(
        self, *, gender: Gender | str, case: Case | str, number: Number | str
    ) -> Ending | None:
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
        >>> foo.get(
        ...     gender=Gender.MASCULINE,
        ...     case=Case.NOMINATIVE,
        ...     number=Number.SINGULAR,
        ... )
        'hic'

        Note that the arguments of get are keyword-only.
        """
        if isinstance(gender, str):
            try:
                gender = Gender(gender.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid gender: '{gender}'") from e

        if isinstance(case, str):
            try:
                case = Case(case.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid case: '{case}'") from e

        if isinstance(number, str):
            try:
                number = Number(number.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid number: '{number}'") from e

        short_gender: str = gender.shorthand
        short_case: str = case.shorthand
        short_number: str = number.shorthand

        return self.endings.get(f"P{short_gender}{short_case}{short_number}")

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents = EndingComponents(
            gender=Gender(key[1]).regular,
            case=Case(key[2:5]).regular,
            number=Number(key[5:7]).regular,
        )
        output.string = f"{output.case} {output.number} {output.gender}"
        return output

    def __repr__(self) -> str:
        return f"Pronoun({self.pronoun}, {self.meaning})"

    def __str__(self) -> str:
        return (
            f"{self.meaning}: {self._mascnom}, {self._femnom}, {self._neutnom}"
        )
