#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin pronoun with endings."""

from __future__ import annotations

from functools import total_ordering

from .class_word import _Word
from .custom_exceptions import InvalidInputError
from .edge_cases import PRONOUNS
from .misc import (
    CASE_SHORTHAND,
    GENDER_SHORTHAND,
    NUMBER_SHORTHAND,
    Ending,
    EndingComponents,
    Meaning,
    key_from_value,
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
    >>> foo.endings
    {"Pmnomsg": "hic", "Pmaccsg": "hunc", "Pmgensg": "huius", ...}

    Note that the arguments of Pronoun are keyword-only.
    """  # fmt: skip

    def __init__(self, *, pronoun: str, meaning: Meaning):
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
        except KeyError:
            raise InvalidInputError(f"Pronoun '{pronoun}' not recognised")

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
        >>> foo.get(gender="masculine", case="nominative", \
        ...         number="singular")
        "hic"

        Note that the arguments of get are keyword-only.
        """  # fmt: skip
        try:
            short_gender: str = GENDER_SHORTHAND[gender]
            short_case: str = CASE_SHORTHAND[case]
            short_number: str = NUMBER_SHORTHAND[number]
        except KeyError:
            raise InvalidInputError(
                f"Gender '{gender}', case '{case}' or number '{number}' not recognised"
            )

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
