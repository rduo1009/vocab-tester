#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin noun with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import Literal, Optional

from .class_word import _Word
from .custom_exceptions import InvalidInputError
from .edge_cases import IRREGULAR_NOUNS
from .misc import (
    CASE_SHORTHAND,
    GENDER_SHORTHAND,
    NUMBER_SHORTHAND,
    Ending,
    EndingComponents,
    Endings,
    Meaning,
    key_from_value,
)


@total_ordering
class Noun(_Word):
    """Representation of a Latin noun with endings.

    Attributes
    ----------
    nominative, genitive : str
    meaning : Meaning
    declension : {0, 1, 2, 3, 4, 5}
        The declension of the noun. The value 0 represents an irregular
        declension.
    endings : Endings
    plurale_tantum : bool
        If the noun is a plurale tantum or not.
    gender : {"masculine", "feminine", "neuter"}
    
    Examples
    --------
    >>> foo = Noun(nominative="ancilla", genitive="ancillae", \
    ...            gender="feminine", meaning="slavegirl")
    >>> foo.endings
    {"Nnomsg": "ancilla", "Nvocsg": "ancilla", "Naccsg": "ancillam", ...}

    Note that all arguments of Noun are keyword-only.

    Notes
    -----
    Accido relies on the assumption that there are no neuter or plurale
    tantum fifth declension nouns (there doesn't seem to be any).
    """  # fmt: skip

    def __init__(
        self,
        *,
        nominative: str,
        genitive: Optional[str],
        gender: Optional[str],
        meaning: Meaning,
    ) -> None:
        """Initialises Noun and determines the declension and endings.

        Parameters
        ----------
        nominative, genitive : str
        gender : {"masculine", "feminine", "neuter"}
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the input is not valid (invalid gender value or genitive).
        """
        super().__init__()

        if gender:
            if gender not in GENDER_SHORTHAND:
                raise InvalidInputError(f"Gender '{gender}' not recognised")
            self.gender: str = gender

        self.nominative: str = nominative
        if genitive:
            self.genitive: str = genitive
        self.meaning: Meaning = meaning
        self.plurale_tantum: bool = False

        self._first: str = self.nominative
        self.declension: Literal[0, 1, 2, 3, 4, 5]
        self._stem: str

        if self.nominative in IRREGULAR_NOUNS:
            self.endings = IRREGULAR_NOUNS[nominative]
            self.declension = 0
            return

        # The ordering of this is strange because e.g. ending -ei ends in 'i' as well as 'ei'
        # so 5th declension check must come before 2nd declension check, etc.
        if self.genitive[-2:] == "ei":
            self.declension = 5
            self._stem = self.genitive[:-2]  # diei > di-
        elif self.genitive[-2:] == "ae":
            self.declension = 1
            self._stem = self.genitive[:-2]  # puellae -> puell-
        elif self.genitive[-1:] == "i":
            self.declension = 2
            self._stem = self.genitive[:-1]  # servi -> serv-
        elif self.genitive[-2:] == "is":
            self.declension = 3
            self._stem = self.genitive[:-2]  # canis -> can-
        elif self.genitive[-2:] == "us":
            self.declension = 4
            self._stem = self.genitive[:-2]  # manus -> man-

        elif self.genitive[-3:] == "uum":
            self.declension = 4
            self._stem = self.genitive[:-3]  # manuum -> man-
            self.plurale_tantum = True
        elif self.genitive[-4:] == "arum":
            self.declension = 1
            self._stem = self.genitive[:-4]  # puellarum -> puell-
            self.plurale_tantum = True
        elif self.genitive[-4:] == "orum":
            self.declension = 2
            self._stem = self.genitive[:-4]  # servorum -> serv-
            self.plurale_tantum = True
        # elif self.genitive[-4:] == "erum":
        #     self.declension = 5
        #     self._stem = self.genitive[:-4]  # dierum > di-
        #     self.plurale_tantum = True
        elif self.genitive[-2:] == "um":
            self.declension = 3
            self._stem = self.genitive[:-2]  # canum -> can-
            self.plurale_tantum = True

        else:
            raise InvalidInputError(
                f"Genitive form '{self.genitive}' is not valid"
            )

        temp_endings: dict[str, Ending]
        match self.declension:
            case 1:
                temp_endings = {
                    "Nnomsg": self.nominative,  # puella
                    "Nvocsg": self.nominative,  # puella
                    "Naccsg": self._stem + "am",  # puellam
                    "Ngensg": self.genitive,  # puellae
                    "Ndatsg": self._stem + "ae",  # puellae
                    "Nablsg": self._stem + "a",  # puella
                    "Nnompl": self._stem + "ae",  # puellae
                    "Nvocpl": self._stem + "ae",  # puellae
                    "Naccpl": self._stem + "as",  # puellas
                    "Ngenpl": self._stem + "arum",  # puellarum
                    "Ndatpl": self._stem + "is",  # puellis
                    "Nablpl": self._stem + "is",  # puellis
                }

            case 2:
                temp_endings = {
                    "Nnomsg": self.nominative,  # servus
                    "Nvocsg": self.nominative
                    if self.nominative[-2:] == "er"
                    else self._stem + "e",  # serve
                    "Naccsg": self._stem + "um",  # servum
                    "Ngensg": self.genitive,  # servi
                    "Ndatsg": self._stem + "o",  # servo
                    "Nablsg": self._stem + "o",  # servo
                    "Nnompl": self._stem + "i",  # servi
                    "Nvocpl": self._stem + "i",  # servi
                    "Naccpl": self._stem + "os",  # servos
                    "Ngenpl": self._stem + "orum",  # servorum
                    "Ndatpl": self._stem + "is",  # servis
                    "Nablpl": self._stem + "is",  # servis
                }

            case 3:
                temp_endings = {
                    "Nnomsg": self.nominative,  # mercator
                    "Nvocsg": self.nominative,  # mercator
                    "Naccsg": self._stem + "em",  # mercatorem
                    "Ngensg": self.genitive,  # mercatoris
                    "Ndatsg": self._stem + "i",  # mercatori
                    "Nablsg": self._stem + "e",  # mercatore
                    "Nnompl": self._stem + "es",  # mercatores
                    "Nvocpl": self._stem + "es",  # mercatores
                    "Naccpl": self._stem + "es",  # mercatores
                    "Ngenpl": self._stem + "um",  # mercatorum
                    "Ndatpl": self._stem + "ibus",  # mercatoribus
                    "Nablpl": self._stem + "ibus",  # mercatoribus
                }

            case 4:
                temp_endings = {
                    "Nnomsg": self.nominative,  # manus
                    "Nvocsg": self.nominative,  # manus
                    "Naccsg": self._stem + "um",  # manum
                    "Ngensg": self._stem + "us",  # manus
                    "Ndatsg": self._stem + "ui",  # manui
                    "Nablsg": self._stem + "u",  # manu
                    "Nnompl": self._stem + "us",  # manus
                    "Nvocpl": self._stem + "us",  # manus
                    "Naccpl": self._stem + "us",  # manus
                    "Ngenpl": self._stem + "uum",  # manuum
                    "Ndatpl": self._stem + "ibus",  # manibus
                    "Nablpl": self._stem + "ibus",  # manibus
                }

            case 5:
                temp_endings = {
                    "Nnomsg": self.nominative,  # res
                    "Nvocsg": self.nominative,  # res
                    "Naccsg": self._stem + "em",  # rem
                    "Ngensg": self._stem + "ei",  # rei
                    "Ndatsg": self._stem + "ei",  # rei
                    "Nablsg": self._stem + "e",  # re
                    "Nnompl": self._stem + "es",  # res
                    "Nvocpl": self._stem + "es",  # res
                    "Naccpl": self._stem + "es",  # res
                    "Ngenpl": self._stem + "erum",  # rerum
                    "Ndatpl": self._stem + "ebus",  # rebus
                    "Nablpl": self._stem + "ebus",  # rebus
                }

            case _:  # pragma: no cover
                raise ValueError(
                    f"Declension {self.declension} not recognised"
                )

        if self.gender == "neuter":
            temp_endings["Naccsg"] = self.nominative  # templum
            temp_endings["Nvocsg"] = self.nominative  # templum

            if self.declension == 4:
                temp_endings["Nnompl"] = self._stem + "ua"  # cornua
                temp_endings["Naccpl"] = self._stem + "ua"  # cornua
                temp_endings["Nvocpl"] = self._stem + "ua"  # cornua
                temp_endings["Ndatsg"] = self._stem + "u"  # cornu
            elif self.declension == 5:
                raise InvalidInputError(
                    f"Fifth declension nouns cannot be neuter (noun '{self.nominative}')"
                )
            else:
                # For the other declensions
                temp_endings["Nnompl"] = self._stem + "a"  # templa
                temp_endings["Naccpl"] = self._stem + "a"  # templa
                temp_endings["Nvocpl"] = self._stem + "a"  # templa

        if self.plurale_tantum:
            temp_endings = {
                k: v for k, v in temp_endings.items() if not k.endswith("sg")
            }

        self.endings: Endings = temp_endings

    def get(self, *, case: str, number: str) -> Ending | None:
        """Returns the ending of the noun.
        The function returns None if no ending is found.

        Parameters
        ----------
        case, number : str

        Returns
        -------
        Ending
            The ending found.
        None
            If no ending is found.

        Raises
        ------
        InvalidInputError
            If the input is invalid.

        Examples
        --------
        >>> foo = Noun(nominative="ancilla", genitive="ancillae", \
        ...            gender="feminine", meaning="slavegirl")
        >>> foo.get(case="nominative", number="singular")
        "ancilla"

        Note that all arguments of get are keyword-only.
        """
        try:
            short_case: str = CASE_SHORTHAND[case]
            short_number: str = NUMBER_SHORTHAND[number]
        except KeyError:
            raise InvalidInputError(
                f"Case '{case}' or number '{number}' not recognised"
            )

        return self.endings.get(f"N{short_case}{short_number}")

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents = EndingComponents(
            case=key_from_value(CASE_SHORTHAND, key[1:4]),
            number=key_from_value(NUMBER_SHORTHAND, key[4:6]),
        )
        output.string = f"{output.case} {output.number}"
        return output

    def __repr__(self) -> str:
        return f"Noun({self.nominative}, {self.genitive}, {GENDER_SHORTHAND[self.gender]}, {self.meaning})"

    def __str__(self) -> str:
        match self.gender:
            case "masculine":
                return (
                    f"{self.meaning}: {self.nominative}, {self.genitive}, (m)"
                )
            case "feminine":
                return (
                    f"{self.meaning}: {self.nominative}, {self.genitive}, (f)"
                )
            case "neuter":
                return (
                    f"{self.meaning}: {self.nominative}, {self.genitive}, (n)"
                )
            case _:  # pragma: no cover
                raise ValueError(f"Gender {self.gender} not recognised")