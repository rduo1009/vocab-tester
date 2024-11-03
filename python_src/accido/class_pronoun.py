#!/usr/bin/env python3

"""Representation of a Latin pronoun with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING

from .class_word import _Word
from .edge_cases import PRONOUNS
from .exceptions import InvalidInputError
from .misc import Case, EndingComponents, Gender, Number

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
        """Initialise Pronoun and determines the endings.

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

        # HACK: hopefully this is the case!
        assert type(self.endings["Pmnomsg"]) is str
        assert type(self.endings["Pfnomsg"]) is str
        assert type(self.endings["Pnnomsg"]) is str

        self.mascnom: str = self.endings["Pmnomsg"]
        self.femnom: str = self.endings["Pfnomsg"]
        self.neutnom: str = self.endings["Pnnomsg"]

    def get(
        self, *, gender: Gender, case: Case, number: Number
    ) -> Ending | None:
        """Return the ending of the pronoun.

        The function returns None if no ending is found.

        Parameters
        ----------
        gender : Gender
            The gender of the pronoun.
        case : Case
            The case of the pronoun.
        number : Number
            The number of the pronoun.

        Returns
        -------
        Ending | None
            The ending found, or None if no ending is found

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
        short_gender: str = gender.shorthand
        short_case: str = case.shorthand
        short_number: str = number.shorthand

        return self.endings.get(f"P{short_gender}{short_case}{short_number}")

    @staticmethod
    def _create_components(key: str) -> EndingComponents:
        output: EndingComponents = EndingComponents(
            gender=Gender(key[1]),
            case=Case(key[2:5]),
            number=Number(key[5:7]),
        )
        output.string = (
            f"{output.case.regular} {output.number.regular} "
            f"{output.gender.regular}"
        )
        return output

    def __repr__(self) -> str:
        return f"Pronoun({self.pronoun}, {self.meaning})"

    def __str__(self) -> str:
        return f"{self.meaning}: {self.mascnom}, {self.femnom}, {self.neutnom}"
