#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin adjective with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import Optional

from .class_word import _Word
from .custom_exceptions import InvalidInputError
from .edge_cases import IRREGULAR_ADJECTIVES, LIS_ADJECTIVES
from .misc import (
    CASE_SHORTHAND,
    DEGREE_SHORTHAND,
    GENDER_SHORTHAND,
    NUMBER_SHORTHAND,
    Ending,
    EndingComponents,
    Meaning,
    key_from_value,
)


@total_ordering
class Adjective(_Word):
    """Representation of a Latin adjective with endings.

    Attributes
    ----------
    meaning : Meaning
    endings : Endings
    declension : {"212", "3"}
        The declension of the adjective. "212" represents a 2-1-2
        adjective, while "3" represents a third declension adjective.
    termination : Optional[int]
        The termination of the adjective if applicable (only third
        declension adjectives).
    irregular_flag : bool

    Examples
    --------
    >>> foo = Adjective("laetus", "laeta", "laetum", declension="212", \
    ...                  meaning="happy")
    >>> foo.endings
    {"Aposmnomsg": "laetus", "Aposmvocsg": "laete", ...}

    Note that the declension and meaning arguments of Adjectives are 
    keyword-only.

    >>> foo = Adjective("egens", "egentis", termination=1, \
    ...                 declension="3", meaning="poor")

    The same can be said with the termination argument for third declension
    adjectives.
    """  # fmt: skip

    def __init__(
        self,
        *principal_parts: str,
        termination: Optional[int] = None,
        declension: str,
        meaning: Meaning,
    ) -> None:
        """Initialises Adjective and determines the endings.

        Parameters
        ----------
        *principal_parts : str
            The principal parts of the adjective.
        termination : Optional[int], default = None
            The termination of the adjective if applicable (only third
            declension adjectives).
        declension : {"212", "3"}
            The declension of the adjective. "212" represents a 2-1-2
            adjective, while "3" represents a third declension adjective.
        meaning: Meaning

        Raises
        ------
        InvalidInputError
            If the input is invalid.
        """
        super().__init__()

        self._principal_parts: tuple[str, ...] = principal_parts
        self._mascnom: str = self._principal_parts[0]
        self._femnom: str
        self._neutnom: str

        self._pos_stem: str

        self._first = self._principal_parts[0]
        self.meaning: Meaning = meaning
        self.declension: str = declension
        self.termination: Optional[int] = termination
        self.irregular_flag: bool = False
        self.adverb_flag: bool = True

        self._cmp_stem: str
        self._spr_stem: str

        self._irregular_posadv: str
        self._irregular_cmpadv: str
        self._irregular_spradv: str

        if self._mascnom in IRREGULAR_ADJECTIVES:
            self.irregular_flag = True
            irregular_data = IRREGULAR_ADJECTIVES[self._mascnom]

            self._cmp_stem = irregular_data[0]  # type: ignore
            self._spr_stem = irregular_data[1]  # type: ignore

            if None not in irregular_data[2:]:
                (
                    self._irregular_posadv,
                    self._irregular_cmpadv,
                    self._irregular_spradv,
                ) = irregular_data[2:]  # type: ignore
            else:
                self.adverb_flag = False

        match self.declension:
            case "212":
                if self.termination:
                    raise InvalidInputError(
                        f"2-1-2 adjectives cannot have a termination (termination {self.termination} given)"
                    )
                if len(self._principal_parts) != 3:
                    raise InvalidInputError(
                        f"2-1-2 adjectives must have 3 principal parts (adjective '{self._first}' given)"
                    )
                self._femnom = self._principal_parts[1]
                self._neutnom = self._principal_parts[2]

                self._pos_stem = self._femnom[:-1]  # cara -> car-

                if self._mascnom not in IRREGULAR_ADJECTIVES:
                    self._cmp_stem = self._pos_stem + "ior"  # car- -> carior-
                    if self._mascnom[-2:] == "er":  # pragma: no cover
                        self._spr_stem = (
                            self._mascnom + "rim"  # miser- -> miserrim-
                        )
                    elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                        self._spr_stem = (
                            self._pos_stem + "lim"  # facil- -> facillim-
                        )
                    else:
                        self._spr_stem = (
                            self._pos_stem + "issim"  # car- -> carissim-
                        )

                self.endings = {
                    "Aposmnomsg": self._mascnom,  # carus
                    "Aposmvocsg": self._pos_stem + "e",  # care
                    "Aposmaccsg": self._pos_stem + "um",  # carum
                    "Aposmgensg": self._pos_stem + "i",  # cari
                    "Aposmdatsg": self._pos_stem + "o",  # caro
                    "Aposmablsg": self._pos_stem + "o",  # caro
                    "Aposmnompl": self._pos_stem + "i",  # cari
                    "Aposmvocpl": self._pos_stem + "i",  # cari
                    "Aposmaccpl": self._pos_stem + "os",  # caros
                    "Aposmgenpl": self._pos_stem + "orum",  # carorum
                    "Aposmdatpl": self._pos_stem + "is",  # caris
                    "Aposmablpl": self._pos_stem + "is",  # caris
                    "Aposfnomsg": self._femnom,  # cara
                    "Aposfvocsg": self._femnom,  # cara
                    "Aposfaccsg": self._pos_stem + "am",  # caram
                    "Aposfgensg": self._pos_stem + "ae",  # carae
                    "Aposfdatsg": self._pos_stem + "ae",  # carae
                    "Aposfablsg": self._pos_stem + "a",  # cara
                    "Aposfnompl": self._pos_stem + "ae",  # carae
                    "Aposfvocpl": self._pos_stem + "ae",  # carae
                    "Aposfaccpl": self._pos_stem + "as",  # caras
                    "Aposfgenpl": self._pos_stem + "arum",  # cararum
                    "Aposfdatpl": self._pos_stem + "is",  # caris
                    "Aposfablpl": self._pos_stem + "is",  # caris
                    "Aposnnomsg": self._neutnom,  # carum
                    "Aposnvocsg": self._neutnom,  # carum
                    "Aposnaccsg": self._neutnom,  # carum
                    "Aposngensg": self._pos_stem + "i",  # cari
                    "Aposndatsg": self._pos_stem + "o",  # caro
                    "Aposnablsg": self._pos_stem + "o",  # caro
                    "Aposnnompl": self._pos_stem + "a",  # cara
                    "Aposnvocpl": self._pos_stem + "a",  # cara
                    "Aposnaccpl": self._pos_stem + "a",  # cara
                    "Aposngenpl": self._pos_stem + "orum",  # carorum
                    "Aposndatpl": self._pos_stem + "is",  # caris
                    "Aposnablpl": self._pos_stem + "is",  # caris
                    "Acmpmnomsg": self._cmp_stem,  # carior
                    "Acmpmvocsg": self._cmp_stem,  # carior
                    "Acmpmaccsg": self._cmp_stem + "em",  # cariorem
                    "Acmpmgensg": self._cmp_stem + "is",  # carioris
                    "Acmpmdatsg": self._cmp_stem + "i",  # cariori
                    "Acmpmablsg": self._cmp_stem + "e",  # cariore
                    "Acmpmnompl": self._cmp_stem + "es",  # cariores
                    "Acmpmvocpl": self._cmp_stem + "es",  # cariores
                    "Acmpmaccpl": self._cmp_stem + "es",  # cariores
                    "Acmpmgenpl": self._cmp_stem + "um",  # cariorum
                    "Acmpmdatpl": self._cmp_stem + "ibus",  # carioribus
                    "Acmpmablpl": self._cmp_stem + "ibus",  # carioribus
                    "Acmpfnomsg": self._cmp_stem,  # carior
                    "Acmpfvocsg": self._cmp_stem,  # carior
                    "Acmpfaccsg": self._cmp_stem + "em",  # cariorem
                    "Acmpfgensg": self._cmp_stem + "is",  # carioris
                    "Acmpfdatsg": self._cmp_stem + "i",  # cariori
                    "Acmpfablsg": self._cmp_stem + "e",  # cariore
                    "Acmpfnompl": self._cmp_stem + "es",  # cariores
                    "Acmpfvocpl": self._cmp_stem + "es",  # cariores
                    "Acmpfaccpl": self._cmp_stem + "es",  # cariores
                    "Acmpfgenpl": self._cmp_stem + "um",  # cariorum
                    "Acmpfdatpl": self._cmp_stem + "ibus",  # carioribus
                    "Acmpfablpl": self._cmp_stem + "ibus",  # carioribus
                    "Acmpnnomsg": self._cmp_stem[:-3] + "ius",  # carius
                    "Acmpnvocsg": self._cmp_stem[:-3] + "ius",  # carius
                    "Acmpnaccsg": self._cmp_stem[:-3] + "ius",  # carius
                    "Acmpngensg": self._cmp_stem + "is",  # carioris
                    "Acmpndatsg": self._cmp_stem + "i",  # cariori
                    "Acmpnablsg": self._cmp_stem + "e",  # cariore
                    "Acmpnnompl": self._cmp_stem + "a",  # cariora
                    "Acmpnvocpl": self._cmp_stem + "a",  # cariora
                    "Acmpnaccpl": self._cmp_stem + "a",  # cariora
                    "Acmpngenpl": self._cmp_stem + "um",  # cariorum
                    "Acmpndatpl": self._cmp_stem + "ibus",  # carioribus
                    "Acmpnablpl": self._cmp_stem + "ibus",  # carioribus
                    "Asprmnomsg": self._spr_stem + "us",  # carrissimus
                    "Asprmvocsg": self._spr_stem + "e",  # carrissime
                    "Asprmaccsg": self._spr_stem + "um",  # carrissimum
                    "Asprmgensg": self._spr_stem + "i",  # carrissimi
                    "Asprmdatsg": self._spr_stem + "o",  # carrissimo
                    "Asprmablsg": self._spr_stem + "o",  # carrissimo
                    "Asprmnompl": self._spr_stem + "i",  # carrissimi
                    "Asprmvocpl": self._spr_stem + "i",  # carrissimi
                    "Asprmaccpl": self._spr_stem + "os",  # carrissimos
                    "Asprmgenpl": self._spr_stem + "orum",  # carrissimorum
                    "Asprmdatpl": self._spr_stem + "is",  # carrissimis
                    "Asprmablpl": self._spr_stem + "is",  # carrissimis
                    "Asprfnomsg": self._spr_stem + "a",  # carrissima
                    "Asprfvocsg": self._spr_stem + "a",  # carrissima
                    "Asprfaccsg": self._spr_stem + "am",  # carrissimam
                    "Asprfgensg": self._spr_stem + "ae",  # carrissimae
                    "Asprfdatsg": self._spr_stem + "ae",  # crrissimae
                    "Asprfablsg": self._spr_stem + "a",  # carrissima
                    "Asprfnompl": self._spr_stem + "ae",  # carrissimae
                    "Asprfvocpl": self._spr_stem + "ae",  # carrissimae
                    "Asprfaccpl": self._spr_stem + "as",  # carrissimas
                    "Asprfgenpl": self._spr_stem + "arum",  # carrissimarum
                    "Asprfdatpl": self._spr_stem + "is",  # carrissimis
                    "Asprfablpl": self._spr_stem + "is",  # carrissimis
                    "Asprnnomsg": self._spr_stem + "um",  # carrissimum
                    "Asprnvocsg": self._spr_stem + "um",  # carrissimum
                    "Asprnaccsg": self._spr_stem + "um",  # carrissimum
                    "Asprngensg": self._spr_stem + "i",  # carrissimi
                    "Asprndatsg": self._spr_stem + "o",  # carrissimo
                    "Asprnablsg": self._spr_stem + "o",  # carrissimo
                    "Asprnnompl": self._spr_stem + "a",  # carrissima
                    "Asprnvocpl": self._spr_stem + "a",  # carrissima
                    "Asprnaccpl": self._spr_stem + "a",  # carrissima
                    "Asprngenpl": self._spr_stem + "orum",  # carrissimorum
                    "Asprndatpl": self._spr_stem + "is",  # carrissimis
                    "Asprnablpl": self._spr_stem + "is",  # carrissimis
                }  # fmt: skip

                if self.adverb_flag:
                    self.endings = self.endings | {
                        "Dpos": self._irregular_posadv
                        if self.irregular_flag
                        else self._pos_stem + "e",  # laete
                        "Dcmp": self._irregular_cmpadv
                        if self.irregular_flag
                        else self._pos_stem + "ius",  # laetius
                        "Dspr": self._irregular_spradv
                        if self.irregular_flag
                        else self._spr_stem + "e",  # laetissime
                    }

            case "3":
                match self.termination:
                    case 1:
                        # ingens, ingentis
                        if len(self._principal_parts) != 2:
                            raise InvalidInputError(
                                f"First-termination adjectives must have 2 principal parts (adjective '{self._first}')"
                            )

                        self._mascgen: str = self._principal_parts[1]

                        if self._mascgen[-2:] != "is":
                            raise InvalidInputError(
                                f"Genitive '{self._mascgen}' not recognised"
                            )
                        self._pos_stem = self._mascgen[
                            :-2  # ingentis -> ingent-
                        ]

                        if not self.irregular_flag:
                            self._cmp_stem = (
                                self._pos_stem + "ior"
                            )  # ingent- > ingentior-
                            if self._mascnom[-2:] == "er":
                                self._spr_stem = (
                                    self._mascnom + "rim"
                                )  # miser- -> miserrim-
                            elif (
                                self._mascnom in LIS_ADJECTIVES
                            ):  # pragma: no cover
                                self._spr_stem = (
                                    self._pos_stem
                                    + "lim"  # facil- -> facillim-
                                )
                            else:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "issim"  # ingent- -> ingentissim-
                                )

                        self.endings = {
                            "Aposmnomsg": self._mascnom,  # ingens
                            "Aposmvocsg": self._mascnom,  # ingens
                            "Aposmaccsg": self._pos_stem + "em",  # ingentem
                            "Aposmgensg": self._mascgen,  # ingentis
                            "Aposmdatsg": self._pos_stem + "i",  # ingenti
                            "Aposmablsg": self._pos_stem + "i",  # ingenti
                            "Aposmnompl": self._pos_stem + "es",  # ingentes
                            "Aposmvocpl": self._pos_stem + "es",  # ingentes
                            "Aposmaccpl": self._pos_stem + "es",  # ingentes
                            "Aposmgenpl": self._pos_stem + "ium",  # ingentium
                            "Aposmdatpl": self._pos_stem + "ibus",  # ingentibus
                            "Aposmablpl": self._pos_stem + "ibus",  # ingentibus
                            "Aposfnomsg": self._mascnom,  # ingens
                            "Aposfvocsg": self._mascnom,  # ingens
                            "Aposfaccsg": self._pos_stem + "em",  # ingentem
                            "Aposfgensg": self._mascgen,  # ingentis
                            "Aposfdatsg": self._pos_stem + "i",  # ingenti
                            "Aposfablsg": self._pos_stem + "i",  # ingenti
                            "Aposfnompl": self._pos_stem + "es",  # ingentes
                            "Aposfvocpl": self._pos_stem + "es",  # ingentes
                            "Aposfaccpl": self._pos_stem + "es",  # ingentes
                            "Aposfgenpl": self._pos_stem + "ium",  # ingentium
                            "Aposfdatpl": self._pos_stem + "ibus",  # ingentibus
                            "Aposfablpl": self._pos_stem + "ibus",  # ingentibus
                            "Aposnnomsg": self._mascnom,  # ingens
                            "Aposnvocsg": self._mascnom,  # ingens
                            "Aposnaccsg": self._mascnom,  # ingens
                            "Aposngensg": self._mascgen,  # ingentis
                            "Aposndatsg": self._pos_stem + "i",  # ingenti
                            "Aposnablsg": self._pos_stem + "i",  # ingenti
                            "Aposnnompl": self._pos_stem + "ia",  # ingentia
                            "Aposnvocpl": self._pos_stem + "ia",  # ingentia
                            "Aposnaccpl": self._pos_stem + "ia",  # ingentia
                            "Aposngenpl": self._pos_stem + "ium",  # ingentium
                            "Aposndatpl": self._pos_stem + "ibus",  # ingentibus
                            "Aposnablpl": self._pos_stem + "ibus",  # ingentibus
                            "Acmpmnomsg": self._cmp_stem,  # ingentior
                            "Acmpmvocsg": self._cmp_stem,  # ingentior
                            "Acmpmaccsg": self._cmp_stem + "em",  # ingentiorem
                            "Acmpmgensg": self._cmp_stem + "is",  # ingentioris
                            "Acmpmdatsg": self._cmp_stem + "i",  # ingentiori
                            "Acmpmablsg": self._cmp_stem + "e",  # ingentiore
                            "Acmpmnompl": self._cmp_stem + "es",  # ingentiores
                            "Acmpmvocpl": self._cmp_stem + "es",  # ingentiores
                            "Acmpmaccpl": self._cmp_stem + "es",  # ingentiores
                            "Acmpmgenpl": self._cmp_stem + "um",  # ingentiorum
                            "Acmpmdatpl": self._cmp_stem + "ibus",  # ingentioribus
                            "Acmpmablpl": self._cmp_stem + "ibus",  # ingentioribus
                            "Acmpfnomsg": self._cmp_stem,  # ingentior
                            "Acmpfvocsg": self._cmp_stem,  # ingentior
                            "Acmpfaccsg": self._cmp_stem + "em",  # ingentiorem
                            "Acmpfgensg": self._cmp_stem + "is",  # ingentioris
                            "Acmpfdatsg": self._cmp_stem + "i",  # ingentiori
                            "Acmpfablsg": self._cmp_stem + "e",  # ingentiore
                            "Acmpfnompl": self._cmp_stem + "es",  # ingentiores
                            "Acmpfvocpl": self._cmp_stem + "es",  # ingentiores
                            "Acmpfaccpl": self._cmp_stem + "es",  # ingentiores
                            "Acmpfgenpl": self._cmp_stem + "um",  # ingentiorum
                            "Acmpfdatpl": self._cmp_stem + "ibus",  # ingentioribus
                            "Acmpfablpl": self._cmp_stem + "ibus",  # ingentioribus
                            "Acmpnnomsg": self._cmp_stem[:-3] + "ius",  # ingentius
                            "Acmpnvocsg": self._cmp_stem[:-3] + "ius",  # ingentius
                            "Acmpnaccsg": self._cmp_stem[:-3] + "ius",  # ingentius
                            "Acmpngensg": self._cmp_stem + "is",  # ingentioris
                            "Acmpndatsg": self._cmp_stem + "i",  # ingentiori
                            "Acmpnablsg": self._cmp_stem + "e",  # ingentiore
                            "Acmpnnompl": self._cmp_stem + "a",  # ingentiora
                            "Acmpnvocpl": self._cmp_stem + "a",  # ingentiora
                            "Acmpnaccpl": self._cmp_stem + "a",  # ingentiora
                            "Acmpngenpl": self._cmp_stem + "um",  # ingentiorum
                            "Acmpndatpl": self._cmp_stem + "ibus",  # ingentioribus
                            "Acmpnablpl": self._cmp_stem + "ibus",  # ingentioribus
                            "Asprmnomsg": self._spr_stem + "us",  # ingentissimus
                            "Asprmvocsg": self._spr_stem + "e",  # ingentissime
                            "Asprmaccsg": self._spr_stem + "um",  # ingentissimum
                            "Asprmgensg": self._spr_stem + "i",  # ingentissimi
                            "Asprmdatsg": self._spr_stem + "o",  # ingentissimo
                            "Asprmablsg": self._spr_stem + "o",  # ingentissimo
                            "Asprmnompl": self._spr_stem + "i",  # ingentissimi
                            "Asprmvocpl": self._spr_stem + "i",  # ingentissimi
                            "Asprmaccpl": self._spr_stem + "os",  # ingentissimos
                            "Asprmgenpl": self._spr_stem + "orum",  # ingentissimorum
                            "Asprmdatpl": self._spr_stem + "is",  # ingentissimis
                            "Asprmablpl": self._spr_stem + "is",  # ingentissimis
                            "Asprfnomsg": self._spr_stem + "a",  # ingentissima
                            "Asprfvocsg": self._spr_stem + "a",  # ingentissima
                            "Asprfaccsg": self._spr_stem + "am",  # ingentissimam
                            "Asprfgensg": self._spr_stem + "ae",  # ingentissimae
                            "Asprfdatsg": self._spr_stem + "ae",  # ingentissimae
                            "Asprfablsg": self._spr_stem + "a",  # ingentissima
                            "Asprfnompl": self._spr_stem + "ae",  # ingentissimae
                            "Asprfvocpl": self._spr_stem + "ae",  # ingentissimae
                            "Asprfaccpl": self._spr_stem + "as",  # ingentissimas
                            "Asprfgenpl": self._spr_stem + "arum",  # ingentissimarum
                            "Asprfdatpl": self._spr_stem + "is",  # ingentissimis
                            "Asprfablpl": self._spr_stem + "is",  # ingentissimis
                            "Asprnnomsg": self._spr_stem + "um",  # ingentissimum
                            "Asprnvocsg": self._spr_stem + "um",  # ingentissimum
                            "Asprnaccsg": self._spr_stem + "um",  # ingentissimum
                            "Asprngensg": self._spr_stem + "i",  # ingentissimi
                            "Asprndatsg": self._spr_stem + "o",  # ingentissimo
                            "Asprnablsg": self._spr_stem + "o",  # ingentissimo
                            "Asprnnompl": self._spr_stem + "a",  # ingentissima
                            "Asprnvocpl": self._spr_stem + "a",  # ingentissima
                            "Asprnaccpl": self._spr_stem + "a",  # ingentissima
                            "Asprngenpl": self._spr_stem + "orum",  # ingentissimorum
                            "Asprndatpl": self._spr_stem + "is",  # ingentissimis
                            "Asprnablpl": self._spr_stem + "is",  # ingentissimis
                        }  # fmt: skip

                        if self.adverb_flag:
                            self.endings = self.endings | {
                                "Dpos": self._irregular_posadv
                                if self.irregular_flag
                                else self._pos_stem + "er",  # atrociter
                                "Dcmp": self._irregular_cmpadv
                                if self.irregular_flag
                                else self._pos_stem + "ius",  # atrocius
                                "Dspr": self._irregular_spradv
                                if self.irregular_flag
                                else self._spr_stem + "e",  # atrocissime
                            }

                    case 2:
                        # fortis, forte
                        if len(self._principal_parts) != 2:
                            raise InvalidInputError(
                                f"Second-termination adjectives must have 2 principal parts (adjective '{self._first}')"
                            )

                        self._neutnom = self._principal_parts[1]

                        self._pos_stem = self._mascnom[:-2]  # fortis -> fort-
                        if not self.irregular_flag:
                            self._cmp_stem = (
                                self._pos_stem + "ior"
                            )  # fort- -> fortior-
                            if self._mascnom[-2:] == "er":  # pragma: no cover
                                self._spr_stem = (
                                    self._mascnom
                                    + "rim"  # miser- -> miserrim-
                                )
                            elif self._mascnom in LIS_ADJECTIVES:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "lim"  # facil- -> facillim-
                                )
                            else:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "issim"  # fort- -> fortissim-
                                )

                        self.endings = {
                            "Aposmnomsg": self._mascnom,  # fortis
                            "Aposmvocsg": self._mascnom,  # fortis
                            "Aposmaccsg": self._pos_stem + "em",  # fortem
                            "Aposmgensg": self._pos_stem + "is",  # fortis
                            "Aposmdatsg": self._pos_stem + "i",  # forti
                            "Aposmablsg": self._pos_stem + "i",  # forti
                            "Aposmnompl": self._pos_stem + "es",  # fortes
                            "Aposmvocpl": self._pos_stem + "es",  # fortes
                            "Aposmaccpl": self._pos_stem + "es",  # fortes
                            "Aposmgenpl": self._pos_stem + "ium",  # fortium
                            "Aposmdatpl": self._pos_stem + "ibus",  # fortibus
                            "Aposmablpl": self._pos_stem + "ibus",  # fortibus
                            "Aposfnomsg": self._mascnom,  # fortis
                            "Aposfvocsg": self._mascnom,  # fortis
                            "Aposfaccsg": self._pos_stem + "em",  # fortem
                            "Aposfgensg": self._pos_stem + "is",  # fortis
                            "Aposfdatsg": self._pos_stem + "i",  # forti
                            "Aposfablsg": self._pos_stem + "i",  # forti
                            "Aposfnompl": self._pos_stem + "es",  # fortes
                            "Aposfvocpl": self._pos_stem + "es",  # fortes
                            "Aposfaccpl": self._pos_stem + "es",  # fortes
                            "Aposfgenpl": self._pos_stem + "ium",  # fortium
                            "Aposfdatpl": self._pos_stem + "ibus",  # fortibus
                            "Aposfablpl": self._pos_stem + "ibus",  # fortibus
                            "Aposnnomsg": self._neutnom,  # forte
                            "Aposnvocsg": self._neutnom,  # forte
                            "Aposnaccsg": self._neutnom,  # forte
                            "Aposngensg": self._pos_stem + "is",  # fortis
                            "Aposndatsg": self._pos_stem + "i",  # fortibus
                            "Aposnablsg": self._pos_stem + "i",  # fortibus
                            "Aposnnompl": self._pos_stem + "ia",  # fortia
                            "Aposnvocpl": self._pos_stem + "ia",  # fortia
                            "Aposnaccpl": self._pos_stem + "ia",  # fortia
                            "Aposngenpl": self._pos_stem + "ium",  # fortium
                            "Aposndatpl": self._pos_stem + "ibus",  # fortibus
                            "Aposnablpl": self._pos_stem + "ibus",  # fortibus
                            "Acmpmnomsg": self._cmp_stem,  # fortior
                            "Acmpmvocsg": self._cmp_stem,  # fortior
                            "Acmpmaccsg": self._cmp_stem + "em",  # fortiorem
                            "Acmpmgensg": self._cmp_stem + "is",  # fortioris
                            "Acmpmdatsg": self._cmp_stem + "i",  # fortiori
                            "Acmpmablsg": self._cmp_stem + "e",  # fortiore
                            "Acmpmnompl": self._cmp_stem + "es",  # fortiores
                            "Acmpmvocpl": self._cmp_stem + "es",  # fortiores
                            "Acmpmaccpl": self._cmp_stem + "es",  # fortiores
                            "Acmpmgenpl": self._cmp_stem + "um",  # fortiorum
                            "Acmpmdatpl": self._cmp_stem + "ibus",  # fortioribus
                            "Acmpmablpl": self._cmp_stem + "ibus",  # fortioribus
                            "Acmpfnomsg": self._cmp_stem,  # fortior
                            "Acmpfvocsg": self._cmp_stem,  # fortior
                            "Acmpfaccsg": self._cmp_stem + "em",  # fortiorem
                            "Acmpfgensg": self._cmp_stem + "is",  # fortioris
                            "Acmpfdatsg": self._cmp_stem + "i",  # fortiori
                            "Acmpfablsg": self._cmp_stem + "e",  # fortiore
                            "Acmpfnompl": self._cmp_stem + "es",  # fortiores
                            "Acmpfvocpl": self._cmp_stem + "es",  # fortiores
                            "Acmpfaccpl": self._cmp_stem + "es",  # fortiores
                            "Acmpfgenpl": self._cmp_stem + "um",  # fortiorum
                            "Acmpfdatpl": self._cmp_stem + "ibus",  # fortioribus
                            "Acmpfablpl": self._cmp_stem + "ibus",  # fortioribus
                            "Acmpnnomsg": self._cmp_stem[:-3] + "ius",  # fortius
                            "Acmpnvocsg": self._cmp_stem[:-3] + "ius",  # fortius
                            "Acmpnaccsg": self._cmp_stem[:-3] + "ius",  # fortius
                            "Acmpngensg": self._cmp_stem + "is",  # fortioris
                            "Acmpndatsg": self._cmp_stem + "i",  # fortiori
                            "Acmpnablsg": self._cmp_stem + "e",  # fortiore
                            "Acmpnnompl": self._cmp_stem + "a",  # fortiora
                            "Acmpnvocpl": self._cmp_stem + "a",  # fortiora
                            "Acmpnaccpl": self._cmp_stem + "a",  # fortiora
                            "Acmpngenpl": self._cmp_stem + "um",  # fortiorum
                            "Acmpndatpl": self._cmp_stem + "ibus",  # fortioribus
                            "Acmpnablpl": self._cmp_stem + "ibus",  # fortioribus
                            "Asprmnomsg": self._spr_stem + "us",  # fortissimus
                            "Asprmvocsg": self._spr_stem + "e",  # fortissime
                            "Asprmaccsg": self._spr_stem + "um",  # fortissimum
                            "Asprmgensg": self._spr_stem + "i",  # fortissimi
                            "Asprmdatsg": self._spr_stem + "o",  # fortissimo
                            "Asprmablsg": self._spr_stem + "o",  # fortissimo
                            "Asprmnompl": self._spr_stem + "i",  # fortissimi
                            "Asprmvocpl": self._spr_stem + "i",  # fortissimi
                            "Asprmaccpl": self._spr_stem + "os",  # fortissimi
                            "Asprmgenpl": self._spr_stem + "orum",  # fortissimorum
                            "Asprmdatpl": self._spr_stem + "is",  # fortissimis
                            "Asprmablpl": self._spr_stem + "is",  # fortissimis
                            "Asprfnomsg": self._spr_stem + "a",  # fortissima
                            "Asprfvocsg": self._spr_stem + "a",  # fortissima
                            "Asprfaccsg": self._spr_stem + "am",  # fortissimam
                            "Asprfgensg": self._spr_stem + "ae",  # fortissimae
                            "Asprfdatsg": self._spr_stem + "ae",  # crrissimae
                            "Asprfablsg": self._spr_stem + "a",  # fortissima
                            "Asprfnompl": self._spr_stem + "ae",  # fortissimae
                            "Asprfvocpl": self._spr_stem + "ae",  # fortissimae
                            "Asprfaccpl": self._spr_stem + "as",  # fortissimas
                            "Asprfgenpl": self._spr_stem + "arum",  # fortissimarum
                            "Asprfdatpl": self._spr_stem + "is",  # fortissimis
                            "Asprfablpl": self._spr_stem + "is",  # fortissimis
                            "Asprnnomsg": self._spr_stem + "um",  # fortissimum
                            "Asprnvocsg": self._spr_stem + "um",  # fortissimum
                            "Asprnaccsg": self._spr_stem + "um",  # fortissimum
                            "Asprngensg": self._spr_stem + "i",  # fortissimi
                            "Asprndatsg": self._spr_stem + "o",  # fortissimo
                            "Asprnablsg": self._spr_stem + "o",  # fortissimo
                            "Asprnnompl": self._spr_stem + "a",  # fortissima
                            "Asprnvocpl": self._spr_stem + "a",  # fortissima
                            "Asprnaccpl": self._spr_stem + "a",  # fortissima
                            "Asprngenpl": self._spr_stem + "orum",  # fortissimorum
                            "Asprndatpl": self._spr_stem + "is",  # fortissimis
                            "Asprnablpl": self._spr_stem + "is",  # fortissimis
                        }  # fmt: skip

                        if self.adverb_flag:
                            self.endings = self.endings | {
                                "Dpos": self._irregular_posadv
                                if self.irregular_flag
                                else self._pos_stem + "iter",  # fortiter
                                "Dcmp": self._irregular_cmpadv
                                if self.irregular_flag
                                else self._pos_stem + "ius",  # fortius
                                "Dspr": self._irregular_spradv
                                if self.irregular_flag
                                else self._spr_stem + "e",  # fortissime
                            }

                    case 3:
                        # acer, acris, acre
                        if len(self._principal_parts) != 3:
                            raise InvalidInputError(
                                f"Third-termination adjectives must have 3 principal parts (adjective '{self._first}')"
                            )

                        self._mascnom = self._principal_parts[0]
                        self._femnom = self._principal_parts[1]
                        self._neutnom = self._principal_parts[2]

                        self._pos_stem = self._femnom[:-2]  # acris -> acr-
                        if not self.irregular_flag:
                            self._cmp_stem = (
                                self._pos_stem + "ior"
                            )  # acr- -> acrior-
                            if self._mascnom[-2:] == "er":
                                self._spr_stem = (
                                    self._mascnom + "rim"
                                )  # cer- -> acerrim-
                            elif (
                                self._mascnom in LIS_ADJECTIVES
                            ):  # pragma: no cover
                                self._spr_stem = (
                                    self._pos_stem
                                    + "lim"  # facil- -> facillim-
                                )
                            else:  # pragma: no cover
                                self._spr_stem = (
                                    self._pos_stem
                                    + "issim"  # levis -> levissim-
                                )

                        self.endings = {
                            "Aposmnomsg": self._mascnom,  # acer
                            "Aposmvocsg": self._mascnom,  # acer
                            "Aposmaccsg": self._pos_stem + "em",  # acrem
                            "Aposmgensg": self._pos_stem + "is",  # acris
                            "Aposmdatsg": self._pos_stem + "i",  # acri
                            "Aposmablsg": self._pos_stem + "i",  # acri
                            "Aposmnompl": self._pos_stem + "es",  # acres
                            "Aposmvocpl": self._pos_stem + "es",  # acres
                            "Aposmaccpl": self._pos_stem + "es",  # acres
                            "Aposmgenpl": self._pos_stem + "ium",  # acrium
                            "Aposmdatpl": self._pos_stem + "ibus",  # acribus
                            "Aposmablpl": self._pos_stem + "ibus",  # acribus
                            "Aposfnomsg": self._femnom,  # acris
                            "Aposfvocsg": self._femnom,  # acris
                            "Aposfaccsg": self._pos_stem + "em",  # acrem
                            "Aposfgensg": self._pos_stem + "is",  # acris
                            "Aposfdatsg": self._pos_stem + "i",  # acri
                            "Aposfablsg": self._pos_stem + "i",  # acri
                            "Aposfnompl": self._pos_stem + "es",  # acres
                            "Aposfvocpl": self._pos_stem + "es",  # acres
                            "Aposfaccpl": self._pos_stem + "es",  # acres
                            "Aposfgenpl": self._pos_stem + "ium",  # acrium
                            "Aposfdatpl": self._pos_stem + "ibus",  # acribus
                            "Aposfablpl": self._pos_stem + "ibus",  # acribus
                            "Aposnnomsg": self._neutnom,  # acre
                            "Aposnvocsg": self._neutnom,  # acre
                            "Aposnaccsg": self._neutnom,  # acre
                            "Aposngensg": self._pos_stem + "is",  # acris
                            "Aposndatsg": self._pos_stem + "i",  # acri
                            "Aposnablsg": self._pos_stem + "i",  # acri
                            "Aposnnompl": self._pos_stem + "ia",  # acria
                            "Aposnvocpl": self._pos_stem + "ia",  # acria
                            "Aposnaccpl": self._pos_stem + "ia",  # acria
                            "Aposngenpl": self._pos_stem + "ium",  # acrium
                            "Aposndatpl": self._pos_stem + "ibus",  # acribus
                            "Aposnablpl": self._pos_stem + "ibus",  # acribus
                            "Acmpmnomsg": self._cmp_stem,  # acrior
                            "Acmpmvocsg": self._cmp_stem,  # acrior
                            "Acmpmaccsg": self._cmp_stem + "em",  # acriorem
                            "Acmpmgensg": self._cmp_stem + "is",  # acrioris
                            "Acmpmdatsg": self._cmp_stem + "i",  # acriori
                            "Acmpmablsg": self._cmp_stem + "e",  # acriore
                            "Acmpmnompl": self._cmp_stem + "es",  # acriores
                            "Acmpmvocpl": self._cmp_stem + "es",  # acriores
                            "Acmpmaccpl": self._cmp_stem + "es",  # acriores
                            "Acmpmgenpl": self._cmp_stem + "um",  # acriorum
                            "Acmpmdatpl": self._cmp_stem + "ibus",  # acrioribus
                            "Acmpmablpl": self._cmp_stem + "ibus",  # acrioribus
                            "Acmpfnomsg": self._cmp_stem,  # acrior
                            "Acmpfvocsg": self._cmp_stem,  # acrior
                            "Acmpfaccsg": self._cmp_stem + "em",  # acriorem
                            "Acmpfgensg": self._cmp_stem + "is",  # acrioris
                            "Acmpfdatsg": self._cmp_stem + "i",  # acriori
                            "Acmpfablsg": self._cmp_stem + "e",  # acriore
                            "Acmpfnompl": self._cmp_stem + "es",  # acriores
                            "Acmpfvocpl": self._cmp_stem + "es",  # acriores
                            "Acmpfaccpl": self._cmp_stem + "es",  # acriores
                            "Acmpfgenpl": self._cmp_stem + "um",  # acriorum
                            "Acmpfdatpl": self._cmp_stem + "ibus",  # acrioribus
                            "Acmpfablpl": self._cmp_stem + "ibus",  # acrioribus
                            "Acmpnnomsg": self._cmp_stem[:-3] + "ius",  # acrius
                            "Acmpnvocsg": self._cmp_stem[:-3] + "ius",  # acrius
                            "Acmpnaccsg": self._cmp_stem[:-3] + "ius",  # acrius
                            "Acmpngensg": self._cmp_stem + "is",  # acrioris
                            "Acmpndatsg": self._cmp_stem + "i",  # acriori
                            "Acmpnablsg": self._cmp_stem + "e",  # acriore
                            "Acmpnnompl": self._cmp_stem + "a",  # acriora
                            "Acmpnvocpl": self._cmp_stem + "a",  # acriora
                            "Acmpnaccpl": self._cmp_stem + "a",  # acriora
                            "Acmpngenpl": self._cmp_stem + "um",  # acriorum
                            "Acmpndatpl": self._cmp_stem + "ibus",  # acrioribus
                            "Acmpnablpl": self._cmp_stem + "ibus",  # acrioribus
                            "Asprmnomsg": self._spr_stem + "us",  # acerrimus
                            "Asprmvocsg": self._spr_stem + "e",  # acerrime
                            "Asprmaccsg": self._spr_stem + "um",  # acerrimum
                            "Asprmgensg": self._spr_stem + "i",  # acerrimi
                            "Asprmdatsg": self._spr_stem + "o",  # acerrimo
                            "Asprmablsg": self._spr_stem + "o",  # acerrimo
                            "Asprmnompl": self._spr_stem + "i",  # acerrimi
                            "Asprmvocpl": self._spr_stem + "i",  # acerrimi
                            "Asprmaccpl": self._spr_stem + "os",  # acerrimos
                            "Asprmgenpl": self._spr_stem + "orum",  # acerrimorum
                            "Asprmdatpl": self._spr_stem + "is",  # acerrimis
                            "Asprmablpl": self._spr_stem + "is",  # acerrimis
                            "Asprfnomsg": self._spr_stem + "a",  # acerrima
                            "Asprfvocsg": self._spr_stem + "a",  # acerrima
                            "Asprfaccsg": self._spr_stem + "am",  # acerrimam
                            "Asprfgensg": self._spr_stem + "ae",  # acerrimae
                            "Asprfdatsg": self._spr_stem + "ae",  # crrissimae
                            "Asprfablsg": self._spr_stem + "a",  # acerrima
                            "Asprfnompl": self._spr_stem + "ae",  # acerrimae
                            "Asprfvocpl": self._spr_stem + "ae",  # acerrimae
                            "Asprfaccpl": self._spr_stem + "as",  # acerrimas
                            "Asprfgenpl": self._spr_stem + "arum",  # acerrimarum
                            "Asprfdatpl": self._spr_stem + "is",  # acerrimis
                            "Asprfablpl": self._spr_stem + "is",  # acerrimis
                            "Asprnnomsg": self._spr_stem + "um",  # acerrimum
                            "Asprnvocsg": self._spr_stem + "um",  # acerrimum
                            "Asprnaccsg": self._spr_stem + "um",  # acerrimum
                            "Asprngensg": self._spr_stem + "i",  # acerrimi
                            "Asprndatsg": self._spr_stem + "o",  # acerrimo
                            "Asprnablsg": self._spr_stem + "o",  # acerrimo
                            "Asprnnompl": self._spr_stem + "a",  # acerrima
                            "Asprnvocpl": self._spr_stem + "a",  # acerrima
                            "Asprnaccpl": self._spr_stem + "a",  # acerrima
                            "Asprngenpl": self._spr_stem + "orum",  # acerrimorum
                            "Asprndatpl": self._spr_stem + "is",  # acerrimis
                            "Asprnablpl": self._spr_stem + "is",  # acerrimis
                        }  # fmt: skip

                        if self.adverb_flag:
                            self.endings = self.endings | {
                                "Dpos": self._irregular_posadv
                                if self.irregular_flag
                                else self._pos_stem + "iter",  # acriter
                                "Dcmp": self._irregular_cmpadv
                                if self.irregular_flag
                                else self._pos_stem + "ius",  # acrius
                                "Dspr": self._irregular_spradv
                                if self.irregular_flag
                                else self._spr_stem + "e",  # acerrime
                            }

                    case _:
                        raise InvalidInputError(
                            f"Termination must be 1, 2 or 3 (given {self.termination})"
                        )

            case _:
                raise InvalidInputError(
                    f"Declension {self.declension} not recognised"
                )

    def get(
        self,
        *,
        degree: str,
        gender: Optional[str] = None,
        case: Optional[str] = None,
        number: Optional[str] = None,
        adverb: bool = False,
    ) -> Ending | None:
        """Returns the ending of the adjective.
        The function returns None if no ending is found.

        Parameters
        ----------
        degree : str
        gender, case, number : Optional[str], default = None
            The gender, case and number of the ending, if applicable (not
            an adverb).
        adverb : bool, default = False
            Whether the queried ending is an adverb or not.

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
        >>> foo = Adjective("egens", "egentis", termination=1, \
        ...                 declension="3", meaning="poor")
        >>> foo.get(degree="positive", gender="masculine", \
        ...         case="nominative", number="singular")
        "egens"

        Note that the arguments of get are keyword-only.
        """  # fmt: skip
        short_degree: str

        if adverb:
            if gender or case or number:
                raise InvalidInputError(
                    f"Adverbs do not have gender, case or number (given '{gender}', '{case}' and '{number}')"
                )
            try:
                short_degree = DEGREE_SHORTHAND[degree]
            except KeyError:
                raise InvalidInputError(f"Degree '{degree}' not recognised")

            return self.endings.get(f"D{short_degree}")

        try:
            short_degree = DEGREE_SHORTHAND[degree]
            if gender and case and number:
                short_gender: str = GENDER_SHORTHAND[gender]
                short_case: str = CASE_SHORTHAND[case]
                short_number: str = NUMBER_SHORTHAND[number]
        except KeyError:
            raise InvalidInputError(
                f"Degree '{degree}', gender '{gender}', case '{case}' or number '{number}' not recognised"
            )

        return self.endings.get(
            f"A{short_degree}{short_gender}{short_case}{short_number}"
        )

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents = EndingComponents(
            degree=key_from_value(DEGREE_SHORTHAND, key[1:4]),
            gender=key_from_value(GENDER_SHORTHAND, key[4]),
            case=key_from_value(CASE_SHORTHAND, key[5:8]),
            number=key_from_value(NUMBER_SHORTHAND, key[8:10]),
        )
        output.string = (
            f"{output.degree} {output.case} {output.number} {output.gender}"
        )
        return output

    def __str__(self) -> str:
        if self.declension == "3":
            return f"{self.meaning}: {', '.join(self._principal_parts)}, ({self.declension}-{self.termination})"
        return f"{self.meaning}: {', '.join(self._principal_parts)}, (2-1-2)"

    def __repr__(self) -> str:
        return f"Adjective({', '.join(self._principal_parts)}, {self.termination}, {self.declension}, {self.meaning})"
