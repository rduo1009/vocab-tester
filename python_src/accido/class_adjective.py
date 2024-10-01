#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin adjective with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING

from .class_word import _Word
from .edge_cases import IRREGULAR_ADJECTIVES, LIS_ADJECTIVES
from .exceptions import InvalidInputError
from .misc import (
    Case,
    Degree,
    EndingComponents,
    Gender,
    Number,
)

if TYPE_CHECKING:
    from .type_aliases import Ending, Endings, Meaning


@total_ordering
class Adjective(_Word):
    """Representation of a Latin adjective with endings.

    Attributes
    ----------
    meaning : Meaning
    endings : Endings
    declension : str
        The declension of the adjective. "212" represents a 2-1-2
        adjective, while "3" represents a third declension adjective.
    termination : Optional[int]
        The termination of the adjective if applicable (only third
        declension adjectives).
    irregular_flag : bool

    Examples
    --------
    >>> foo = Adjective(
    ...     "laetus", "laeta", "laetum", declension="212", meaning="happy"
    ... )
    >>> foo["Aposmnomsg"]
    'laetus'

    Note that the declension and meaning arguments of Adjectives are
    keyword-only.

    >>> bar = Adjective(
    ...     "egens", "egentis", termination=1, declension="3", meaning="poor"
    ... )
    >>> bar["Aposmnomsg"]
    'egens'

    The same can be said with the termination argument for third declension
    adjectives.
    """

    def __init__(
        self,
        *principal_parts: str,
        termination: int | None = None,
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
        declension : str
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

        self._first = self._principal_parts[0]
        self.meaning: Meaning = meaning
        self.declension: str = declension
        self.termination: int | None = termination
        self.irregular_flag: bool = False
        self.adverb_flag: bool = True

        self._pos_stem: str
        self._cmp_stem: str
        self._spr_stem: str

        if self._mascnom in IRREGULAR_ADJECTIVES:
            self.irregular_flag = True
            irregular_data = IRREGULAR_ADJECTIVES[self._mascnom]

            assert irregular_data[0] is not None
            assert irregular_data[1] is not None

            self._cmp_stem = irregular_data[0]
            self._spr_stem = irregular_data[1]

            if None not in irregular_data[2:]:
                assert irregular_data[2] is not None
                assert irregular_data[3] is not None
                assert irregular_data[4] is not None

                self._irregular_posadv: str = irregular_data[2]
                self._irregular_cmpadv: str = irregular_data[3]
                self._irregular_spradv: str = irregular_data[4]
            else:
                self.adverb_flag = False

        match self.declension:
            case "212":
                self.endings = self._212_endings()

            case "3":
                match self.termination:
                    case 1:
                        self.endings = self._31_endings()

                    case 2:
                        self.endings = self._32_endings()

                    case 3:
                        self.endings = self._33_endings()

                    case _:
                        raise InvalidInputError(
                            "Termination must be 1, 2 or 3 "
                            f"(given '{self.termination}')",
                        )

            case _:
                raise InvalidInputError(
                    f"Invalid declension: '{self.declension}'",
                )

    def _212_endings(self) -> Endings:
        if self.termination:
            raise InvalidInputError(
                "2-1-2 adjectives cannot have a termination "
                f"(termination '{self.termination}' given)",
            )

        if len(self._principal_parts) != 3:
            raise InvalidInputError(
                "2-1-2 adjectives must have 3 principal parts "
                f"(adjective '{self._first}' given)",
            )

        self._femnom = self._principal_parts[1]
        self._neutnom = self._principal_parts[2]

        self._pos_stem = self._femnom[:-1]  # cara -> car-

        if self._mascnom not in IRREGULAR_ADJECTIVES:
            self._cmp_stem = f"{self._pos_stem}ior"  # car- -> carior-
            if self._mascnom.endswith(
                "er",
            ):  # pragma: no cover
                self._spr_stem = f"{self._mascnom}rim"  # miser- -> miserrim-
            elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:
                self._spr_stem = f"{self._pos_stem}issim"  # car- -> carissim-

        endings: Endings
        endings = {
            "Aposmnomsg": self._mascnom,  # carus
            "Aposmvocsg": f"{self._pos_stem}e",  # care
            "Aposmaccsg": f"{self._pos_stem}um",  # carum
            "Aposmgensg": f"{self._pos_stem}i",  # cari
            "Aposmdatsg": f"{self._pos_stem}o",  # caro
            "Aposmablsg": f"{self._pos_stem}o",  # caro
            "Aposmnompl": f"{self._pos_stem}i",  # cari
            "Aposmvocpl": f"{self._pos_stem}i",  # cari
            "Aposmaccpl": f"{self._pos_stem}os",  # caros
            "Aposmgenpl": f"{self._pos_stem}orum",  # carorum
            "Aposmdatpl": f"{self._pos_stem}is",  # caris
            "Aposmablpl": f"{self._pos_stem}is",  # caris
            "Aposfnomsg": self._femnom,  # cara
            "Aposfvocsg": self._femnom,  # cara
            "Aposfaccsg": f"{self._pos_stem}am",  # caram
            "Aposfgensg": f"{self._pos_stem}ae",  # carae
            "Aposfdatsg": f"{self._pos_stem}ae",  # carae
            "Aposfablsg": f"{self._pos_stem}a",  # cara
            "Aposfnompl": f"{self._pos_stem}ae",  # carae
            "Aposfvocpl": f"{self._pos_stem}ae",  # carae
            "Aposfaccpl": f"{self._pos_stem}as",  # caras
            "Aposfgenpl": f"{self._pos_stem}arum",  # cararum
            "Aposfdatpl": f"{self._pos_stem}is",  # caris
            "Aposfablpl": f"{self._pos_stem}is",  # caris
            "Aposnnomsg": self._neutnom,  # carum
            "Aposnvocsg": self._neutnom,  # carum
            "Aposnaccsg": self._neutnom,  # carum
            "Aposngensg": f"{self._pos_stem}i",  # cari
            "Aposndatsg": f"{self._pos_stem}o",  # caro
            "Aposnablsg": f"{self._pos_stem}o",  # caro
            "Aposnnompl": f"{self._pos_stem}a",  # cara
            "Aposnvocpl": f"{self._pos_stem}a",  # cara
            "Aposnaccpl": f"{self._pos_stem}a",  # cara
            "Aposngenpl": f"{self._pos_stem}orum",  # carorum
            "Aposndatpl": f"{self._pos_stem}is",  # caris
            "Aposnablpl": f"{self._pos_stem}is",  # caris
            "Acmpmnomsg": self._cmp_stem,  # carior
            "Acmpmvocsg": self._cmp_stem,  # carior
            "Acmpmaccsg": f"{self._cmp_stem}em",  # cariorem
            "Acmpmgensg": f"{self._cmp_stem}is",  # carioris
            "Acmpmdatsg": f"{self._cmp_stem}i",  # cariori
            "Acmpmablsg": f"{self._cmp_stem}e",  # cariore
            "Acmpmnompl": f"{self._cmp_stem}es",  # cariores
            "Acmpmvocpl": f"{self._cmp_stem}es",  # cariores
            "Acmpmaccpl": f"{self._cmp_stem}es",  # cariores
            "Acmpmgenpl": f"{self._cmp_stem}um",  # cariorum
            "Acmpmdatpl": f"{self._cmp_stem}ibus",  # carioribus
            "Acmpmablpl": f"{self._cmp_stem}ibus",  # carioribus
            "Acmpfnomsg": self._cmp_stem,  # carior
            "Acmpfvocsg": self._cmp_stem,  # carior
            "Acmpfaccsg": f"{self._cmp_stem}em",  # cariorem
            "Acmpfgensg": f"{self._cmp_stem}is",  # carioris
            "Acmpfdatsg": f"{self._cmp_stem}i",  # cariori
            "Acmpfablsg": f"{self._cmp_stem}e",  # cariore
            "Acmpfnompl": f"{self._cmp_stem}es",  # cariores
            "Acmpfvocpl": f"{self._cmp_stem}es",  # cariores
            "Acmpfaccpl": f"{self._cmp_stem}es",  # cariores
            "Acmpfgenpl": f"{self._cmp_stem}um",  # cariorum
            "Acmpfdatpl": f"{self._cmp_stem}ibus",  # carioribus
            "Acmpfablpl": f"{self._cmp_stem}ibus",  # carioribus
            "Acmpnnomsg": f"{self._cmp_stem[:-3]}ius",  # carius
            "Acmpnvocsg": f"{self._cmp_stem[:-3]}ius",  # carius
            "Acmpnaccsg": f"{self._cmp_stem[:-3]}ius",  # carius
            "Acmpngensg": f"{self._cmp_stem}is",  # carioris
            "Acmpndatsg": f"{self._cmp_stem}i",  # cariori
            "Acmpnablsg": f"{self._cmp_stem}e",  # cariore
            "Acmpnnompl": f"{self._cmp_stem}a",  # cariora
            "Acmpnvocpl": f"{self._cmp_stem}a",  # cariora
            "Acmpnaccpl": f"{self._cmp_stem}a",  # cariora
            "Acmpngenpl": f"{self._cmp_stem}um",  # cariorum
            "Acmpndatpl": f"{self._cmp_stem}ibus",  # carioribus
            "Acmpnablpl": f"{self._cmp_stem}ibus",  # carioribus
            "Asprmnomsg": f"{self._spr_stem}us",  # carrissimus
            "Asprmvocsg": f"{self._spr_stem}e",  # carrissime
            "Asprmaccsg": f"{self._spr_stem}um",  # carrissimum
            "Asprmgensg": f"{self._spr_stem}i",  # carrissimi
            "Asprmdatsg": f"{self._spr_stem}o",  # carrissimo
            "Asprmablsg": f"{self._spr_stem}o",  # carrissimo
            "Asprmnompl": f"{self._spr_stem}i",  # carrissimi
            "Asprmvocpl": f"{self._spr_stem}i",  # carrissimi
            "Asprmaccpl": f"{self._spr_stem}os",  # carrissimos
            "Asprmgenpl": f"{self._spr_stem}orum",  # carrissimorum
            "Asprmdatpl": f"{self._spr_stem}is",  # carrissimis
            "Asprmablpl": f"{self._spr_stem}is",  # carrissimis
            "Asprfnomsg": f"{self._spr_stem}a",  # carrissima
            "Asprfvocsg": f"{self._spr_stem}a",  # carrissima
            "Asprfaccsg": f"{self._spr_stem}am",  # carrissimam
            "Asprfgensg": f"{self._spr_stem}ae",  # carrissimae
            "Asprfdatsg": f"{self._spr_stem}ae",  # crrissimae
            "Asprfablsg": f"{self._spr_stem}a",  # carrissima
            "Asprfnompl": f"{self._spr_stem}ae",  # carrissimae
            "Asprfvocpl": f"{self._spr_stem}ae",  # carrissimae
            "Asprfaccpl": f"{self._spr_stem}as",  # carrissimas
            "Asprfgenpl": f"{self._spr_stem}arum",  # carrissimarum
            "Asprfdatpl": f"{self._spr_stem}is",  # carrissimis
            "Asprfablpl": f"{self._spr_stem}is",  # carrissimis
            "Asprnnomsg": f"{self._spr_stem}um",  # carrissimum
            "Asprnvocsg": f"{self._spr_stem}um",  # carrissimum
            "Asprnaccsg": f"{self._spr_stem}um",  # carrissimum
            "Asprngensg": f"{self._spr_stem}i",  # carrissimi
            "Asprndatsg": f"{self._spr_stem}o",  # carrissimo
            "Asprnablsg": f"{self._spr_stem}o",  # carrissimo
            "Asprnnompl": f"{self._spr_stem}a",  # carrissima
            "Asprnvocpl": f"{self._spr_stem}a",  # carrissima
            "Asprnaccpl": f"{self._spr_stem}a",  # carrissima
            "Asprngenpl": f"{self._spr_stem}orum",  # carrissimorum
            "Asprndatpl": f"{self._spr_stem}is",  # carrissimis
            "Asprnablpl": f"{self._spr_stem}is",  # carrissimis
        }

        if self.adverb_flag:
            endings |= {
                "Dpos": (
                    self._irregular_posadv
                    if self.irregular_flag
                    else f"{self._pos_stem}e"
                ),  # laete
                "Dcmp": (
                    self._irregular_cmpadv
                    if self.irregular_flag
                    else f"{self._pos_stem}ius"
                ),  # laetius
                "Dspr": (
                    self._irregular_spradv
                    if self.irregular_flag
                    else f"{self._spr_stem}e"
                ),  # laetissime
            }

        return endings

    def _31_endings(self) -> Endings:
        if len(self._principal_parts) != 2:
            raise InvalidInputError(
                "First-termination adjectives must have 2 principal parts "
                f"(adjective '{self._first}' given)",
            )

        self._mascgen: str = self._principal_parts[1]

        if self._mascgen[-2:] != "is":
            raise InvalidInputError(
                f"Invalid genitive form: '{self._mascgen}' "
                "(must end in '-is')",
            )

        self._pos_stem = self._mascgen[:-2]  # ingentis -> ingent-

        if not self.irregular_flag:
            self._cmp_stem = f"{self._pos_stem}ior"  # ingent- > ingentior-
            if self._mascnom.endswith("er"):
                self._spr_stem = f"{self._mascnom}rim"  # miser- -> miserrim-
            elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:
                self._spr_stem = (
                    f"{self._pos_stem}issim"  # ingent- -> ingentissim-
                )

        endings: Endings
        endings = {
            "Aposmnomsg": self._mascnom,  # ingens
            "Aposmvocsg": self._mascnom,  # ingens
            "Aposmaccsg": f"{self._pos_stem}em",  # ingentem
            "Aposmgensg": self._mascgen,  # ingentis
            "Aposmdatsg": f"{self._pos_stem}i",  # ingenti
            "Aposmablsg": f"{self._pos_stem}i",  # ingenti
            "Aposmnompl": f"{self._pos_stem}es",  # ingentes
            "Aposmvocpl": f"{self._pos_stem}es",  # ingentes
            "Aposmaccpl": f"{self._pos_stem}es",  # ingentes
            "Aposmgenpl": f"{self._pos_stem}ium",  # ingentium
            "Aposmdatpl": f"{self._pos_stem}ibus",  # ingentibus
            "Aposmablpl": f"{self._pos_stem}ibus",  # ingentibus
            "Aposfnomsg": self._mascnom,  # ingens
            "Aposfvocsg": self._mascnom,  # ingens
            "Aposfaccsg": f"{self._pos_stem}em",  # ingentem
            "Aposfgensg": self._mascgen,  # ingentis
            "Aposfdatsg": f"{self._pos_stem}i",  # ingenti
            "Aposfablsg": f"{self._pos_stem}i",  # ingenti
            "Aposfnompl": f"{self._pos_stem}es",  # ingentes
            "Aposfvocpl": f"{self._pos_stem}es",  # ingentes
            "Aposfaccpl": f"{self._pos_stem}es",  # ingentes
            "Aposfgenpl": f"{self._pos_stem}ium",  # ingentium
            "Aposfdatpl": f"{self._pos_stem}ibus",  # ingentibus
            "Aposfablpl": f"{self._pos_stem}ibus",  # ingentibus
            "Aposnnomsg": self._mascnom,  # ingens
            "Aposnvocsg": self._mascnom,  # ingens
            "Aposnaccsg": self._mascnom,  # ingens
            "Aposngensg": self._mascgen,  # ingentis
            "Aposndatsg": f"{self._pos_stem}i",  # ingenti
            "Aposnablsg": f"{self._pos_stem}i",  # ingenti
            "Aposnnompl": f"{self._pos_stem}ia",  # ingentia
            "Aposnvocpl": f"{self._pos_stem}ia",  # ingentia
            "Aposnaccpl": f"{self._pos_stem}ia",  # ingentia
            "Aposngenpl": f"{self._pos_stem}ium",  # ingentium
            "Aposndatpl": f"{self._pos_stem}ibus",  # ingentibus
            "Aposnablpl": f"{self._pos_stem}ibus",  # ingentibus
            "Acmpmnomsg": self._cmp_stem,  # ingentior
            "Acmpmvocsg": self._cmp_stem,  # ingentior
            "Acmpmaccsg": f"{self._cmp_stem}em",  # ingentiorem
            "Acmpmgensg": f"{self._cmp_stem}is",  # ingentioris
            "Acmpmdatsg": f"{self._cmp_stem}i",  # ingentiori
            "Acmpmablsg": f"{self._cmp_stem}e",  # ingentiore
            "Acmpmnompl": f"{self._cmp_stem}es",  # ingentiores
            "Acmpmvocpl": f"{self._cmp_stem}es",  # ingentiores
            "Acmpmaccpl": f"{self._cmp_stem}es",  # ingentiores
            "Acmpmgenpl": f"{self._cmp_stem}um",  # ingentiorum
            "Acmpmdatpl": f"{self._cmp_stem}ibus",  # ingentioribus
            "Acmpmablpl": f"{self._cmp_stem}ibus",  # ingentioribus
            "Acmpfnomsg": self._cmp_stem,  # ingentior
            "Acmpfvocsg": self._cmp_stem,  # ingentior
            "Acmpfaccsg": f"{self._cmp_stem}em",  # ingentiorem
            "Acmpfgensg": f"{self._cmp_stem}is",  # ingentioris
            "Acmpfdatsg": f"{self._cmp_stem}i",  # ingentiori
            "Acmpfablsg": f"{self._cmp_stem}e",  # ingentiore
            "Acmpfnompl": f"{self._cmp_stem}es",  # ingentiores
            "Acmpfvocpl": f"{self._cmp_stem}es",  # ingentiores
            "Acmpfaccpl": f"{self._cmp_stem}es",  # ingentiores
            "Acmpfgenpl": f"{self._cmp_stem}um",  # ingentiorum
            "Acmpfdatpl": f"{self._cmp_stem}ibus",  # ingentioribus
            "Acmpfablpl": f"{self._cmp_stem}ibus",  # ingentioribus
            "Acmpnnomsg": f"{self._cmp_stem[:-3]}ius",  # ingentius
            "Acmpnvocsg": f"{self._cmp_stem[:-3]}ius",  # ingentius
            "Acmpnaccsg": f"{self._cmp_stem[:-3]}ius",  # ingentius
            "Acmpngensg": f"{self._cmp_stem}is",  # ingentioris
            "Acmpndatsg": f"{self._cmp_stem}i",  # ingentiori
            "Acmpnablsg": f"{self._cmp_stem}e",  # ingentiore
            "Acmpnnompl": f"{self._cmp_stem}a",  # ingentiora
            "Acmpnvocpl": f"{self._cmp_stem}a",  # ingentiora
            "Acmpnaccpl": f"{self._cmp_stem}a",  # ingentiora
            "Acmpngenpl": f"{self._cmp_stem}um",  # ingentiorum
            "Acmpndatpl": f"{self._cmp_stem}ibus",  # ingentioribus
            "Acmpnablpl": f"{self._cmp_stem}ibus",  # ingentioribus
            "Asprmnomsg": f"{self._spr_stem}us",  # ingentissimus
            "Asprmvocsg": f"{self._spr_stem}e",  # ingentissime
            "Asprmaccsg": f"{self._spr_stem}um",  # ingentissimum
            "Asprmgensg": f"{self._spr_stem}i",  # ingentissimi
            "Asprmdatsg": f"{self._spr_stem}o",  # ingentissimo
            "Asprmablsg": f"{self._spr_stem}o",  # ingentissimo
            "Asprmnompl": f"{self._spr_stem}i",  # ingentissimi
            "Asprmvocpl": f"{self._spr_stem}i",  # ingentissimi
            "Asprmaccpl": f"{self._spr_stem}os",  # ingentissimos
            "Asprmgenpl": f"{self._spr_stem}orum",  # ingentissimorum
            "Asprmdatpl": f"{self._spr_stem}is",  # ingentissimis
            "Asprmablpl": f"{self._spr_stem}is",  # ingentissimis
            "Asprfnomsg": f"{self._spr_stem}a",  # ingentissima
            "Asprfvocsg": f"{self._spr_stem}a",  # ingentissima
            "Asprfaccsg": f"{self._spr_stem}am",  # ingentissimam
            "Asprfgensg": f"{self._spr_stem}ae",  # ingentissimae
            "Asprfdatsg": f"{self._spr_stem}ae",  # ingentissimae
            "Asprfablsg": f"{self._spr_stem}a",  # ingentissima
            "Asprfnompl": f"{self._spr_stem}ae",  # ingentissimae
            "Asprfvocpl": f"{self._spr_stem}ae",  # ingentissimae
            "Asprfaccpl": f"{self._spr_stem}as",  # ingentissimas
            "Asprfgenpl": f"{self._spr_stem}arum",  # ingentissimarum
            "Asprfdatpl": f"{self._spr_stem}is",  # ingentissimis
            "Asprfablpl": f"{self._spr_stem}is",  # ingentissimis
            "Asprnnomsg": f"{self._spr_stem}um",  # ingentissimum
            "Asprnvocsg": f"{self._spr_stem}um",  # ingentissimum
            "Asprnaccsg": f"{self._spr_stem}um",  # ingentissimum
            "Asprngensg": f"{self._spr_stem}i",  # ingentissimi
            "Asprndatsg": f"{self._spr_stem}o",  # ingentissimo
            "Asprnablsg": f"{self._spr_stem}o",  # ingentissimo
            "Asprnnompl": f"{self._spr_stem}a",  # ingentissima
            "Asprnvocpl": f"{self._spr_stem}a",  # ingentissima
            "Asprnaccpl": f"{self._spr_stem}a",  # ingentissima
            "Asprngenpl": f"{self._spr_stem}orum",  # ingentissimorum
            "Asprndatpl": f"{self._spr_stem}is",  # ingentissimis
            "Asprnablpl": f"{self._spr_stem}is",  # ingentissimis
        }

        if self.adverb_flag:
            endings |= {
                "Dpos": (
                    self._irregular_posadv
                    if self.irregular_flag
                    else f"{self._pos_stem}er"
                ),  # atrociter
                "Dcmp": (
                    self._irregular_cmpadv
                    if self.irregular_flag
                    else f"{self._pos_stem}ius"
                ),  # atrocius
                "Dspr": (
                    self._irregular_spradv
                    if self.irregular_flag
                    else f"{self._spr_stem}e"
                ),  # atrocissime
            }

        return endings

    def _32_endings(self) -> Endings:
        if len(self._principal_parts) != 2:
            raise InvalidInputError(
                "Second-termination adjectives must have 2 principal parts "
                f"(adjective '{self._first}' given)",
            )

        self._neutnom = self._principal_parts[1]

        self._pos_stem = self._mascnom[:-2]  # fortis -> fort-
        if not self.irregular_flag:
            self._cmp_stem = f"{self._pos_stem}ior"  # fort- -> fortior-
            if self._mascnom[-2:] == "er":  # pragma: no cover
                self._spr_stem = f"{self._mascnom}rim"  # miser- -> miserrim-
            elif self._mascnom in LIS_ADJECTIVES:
                self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:
                self._spr_stem = (
                    f"{self._pos_stem}issim"  # fort- -> fortissim-
                )

        endings: Endings
        endings = {
            "Aposmnomsg": self._mascnom,  # fortis
            "Aposmvocsg": self._mascnom,  # fortis
            "Aposmaccsg": f"{self._pos_stem}em",  # fortem
            "Aposmgensg": f"{self._pos_stem}is",  # fortis
            "Aposmdatsg": f"{self._pos_stem}i",  # forti
            "Aposmablsg": f"{self._pos_stem}i",  # forti
            "Aposmnompl": f"{self._pos_stem}es",  # fortes
            "Aposmvocpl": f"{self._pos_stem}es",  # fortes
            "Aposmaccpl": f"{self._pos_stem}es",  # fortes
            "Aposmgenpl": f"{self._pos_stem}ium",  # fortium
            "Aposmdatpl": f"{self._pos_stem}ibus",  # fortibus
            "Aposmablpl": f"{self._pos_stem}ibus",  # fortibus
            "Aposfnomsg": self._mascnom,  # fortis
            "Aposfvocsg": self._mascnom,  # fortis
            "Aposfaccsg": f"{self._pos_stem}em",  # fortem
            "Aposfgensg": f"{self._pos_stem}is",  # fortis
            "Aposfdatsg": f"{self._pos_stem}i",  # forti
            "Aposfablsg": f"{self._pos_stem}i",  # forti
            "Aposfnompl": f"{self._pos_stem}es",  # fortes
            "Aposfvocpl": f"{self._pos_stem}es",  # fortes
            "Aposfaccpl": f"{self._pos_stem}es",  # fortes
            "Aposfgenpl": f"{self._pos_stem}ium",  # fortium
            "Aposfdatpl": f"{self._pos_stem}ibus",  # fortibus
            "Aposfablpl": f"{self._pos_stem}ibus",  # fortibus
            "Aposnnomsg": self._neutnom,  # forte
            "Aposnvocsg": self._neutnom,  # forte
            "Aposnaccsg": self._neutnom,  # forte
            "Aposngensg": f"{self._pos_stem}is",  # fortis
            "Aposndatsg": f"{self._pos_stem}i",  # fortibus
            "Aposnablsg": f"{self._pos_stem}i",  # fortibus
            "Aposnnompl": f"{self._pos_stem}ia",  # fortia
            "Aposnvocpl": f"{self._pos_stem}ia",  # fortia
            "Aposnaccpl": f"{self._pos_stem}ia",  # fortia
            "Aposngenpl": f"{self._pos_stem}ium",  # fortium
            "Aposndatpl": f"{self._pos_stem}ibus",  # fortibus
            "Aposnablpl": f"{self._pos_stem}ibus",  # fortibus
            "Acmpmnomsg": self._cmp_stem,  # fortior
            "Acmpmvocsg": self._cmp_stem,  # fortior
            "Acmpmaccsg": f"{self._cmp_stem}em",  # fortiorem
            "Acmpmgensg": f"{self._cmp_stem}is",  # fortioris
            "Acmpmdatsg": f"{self._cmp_stem}i",  # fortiori
            "Acmpmablsg": f"{self._cmp_stem}e",  # fortiore
            "Acmpmnompl": f"{self._cmp_stem}es",  # fortiores
            "Acmpmvocpl": f"{self._cmp_stem}es",  # fortiores
            "Acmpmaccpl": f"{self._cmp_stem}es",  # fortiores
            "Acmpmgenpl": f"{self._cmp_stem}um",  # fortiorum
            "Acmpmdatpl": f"{self._cmp_stem}ibus",  # fortioribus
            "Acmpmablpl": f"{self._cmp_stem}ibus",  # fortioribus
            "Acmpfnomsg": self._cmp_stem,  # fortior
            "Acmpfvocsg": self._cmp_stem,  # fortior
            "Acmpfaccsg": f"{self._cmp_stem}em",  # fortiorem
            "Acmpfgensg": f"{self._cmp_stem}is",  # fortioris
            "Acmpfdatsg": f"{self._cmp_stem}i",  # fortiori
            "Acmpfablsg": f"{self._cmp_stem}e",  # fortiore
            "Acmpfnompl": f"{self._cmp_stem}es",  # fortiores
            "Acmpfvocpl": f"{self._cmp_stem}es",  # fortiores
            "Acmpfaccpl": f"{self._cmp_stem}es",  # fortiores
            "Acmpfgenpl": f"{self._cmp_stem}um",  # fortiorum
            "Acmpfdatpl": f"{self._cmp_stem}ibus",  # fortioribus
            "Acmpfablpl": f"{self._cmp_stem}ibus",  # fortioribus
            "Acmpnnomsg": f"{self._cmp_stem[:-3]}ius",  # fortius
            "Acmpnvocsg": f"{self._cmp_stem[:-3]}ius",  # fortius
            "Acmpnaccsg": f"{self._cmp_stem[:-3]}ius",  # fortius
            "Acmpngensg": f"{self._cmp_stem}is",  # fortioris
            "Acmpndatsg": f"{self._cmp_stem}i",  # fortiori
            "Acmpnablsg": f"{self._cmp_stem}e",  # fortiore
            "Acmpnnompl": f"{self._cmp_stem}a",  # fortiora
            "Acmpnvocpl": f"{self._cmp_stem}a",  # fortiora
            "Acmpnaccpl": f"{self._cmp_stem}a",  # fortiora
            "Acmpngenpl": f"{self._cmp_stem}um",  # fortiorum
            "Acmpndatpl": f"{self._cmp_stem}ibus",  # fortioribus
            "Acmpnablpl": f"{self._cmp_stem}ibus",  # fortioribus
            "Asprmnomsg": f"{self._spr_stem}us",  # fortissimus
            "Asprmvocsg": f"{self._spr_stem}e",  # fortissime
            "Asprmaccsg": f"{self._spr_stem}um",  # fortissimum
            "Asprmgensg": f"{self._spr_stem}i",  # fortissimi
            "Asprmdatsg": f"{self._spr_stem}o",  # fortissimo
            "Asprmablsg": f"{self._spr_stem}o",  # fortissimo
            "Asprmnompl": f"{self._spr_stem}i",  # fortissimi
            "Asprmvocpl": f"{self._spr_stem}i",  # fortissimi
            "Asprmaccpl": f"{self._spr_stem}os",  # fortissimi
            "Asprmgenpl": f"{self._spr_stem}orum",  # fortissimorum
            "Asprmdatpl": f"{self._spr_stem}is",  # fortissimis
            "Asprmablpl": f"{self._spr_stem}is",  # fortissimis
            "Asprfnomsg": f"{self._spr_stem}a",  # fortissima
            "Asprfvocsg": f"{self._spr_stem}a",  # fortissima
            "Asprfaccsg": f"{self._spr_stem}am",  # fortissimam
            "Asprfgensg": f"{self._spr_stem}ae",  # fortissimae
            "Asprfdatsg": f"{self._spr_stem}ae",  # crrissimae
            "Asprfablsg": f"{self._spr_stem}a",  # fortissima
            "Asprfnompl": f"{self._spr_stem}ae",  # fortissimae
            "Asprfvocpl": f"{self._spr_stem}ae",  # fortissimae
            "Asprfaccpl": f"{self._spr_stem}as",  # fortissimas
            "Asprfgenpl": f"{self._spr_stem}arum",  # fortissimarum
            "Asprfdatpl": f"{self._spr_stem}is",  # fortissimis
            "Asprfablpl": f"{self._spr_stem}is",  # fortissimis
            "Asprnnomsg": f"{self._spr_stem}um",  # fortissimum
            "Asprnvocsg": f"{self._spr_stem}um",  # fortissimum
            "Asprnaccsg": f"{self._spr_stem}um",  # fortissimum
            "Asprngensg": f"{self._spr_stem}i",  # fortissimi
            "Asprndatsg": f"{self._spr_stem}o",  # fortissimo
            "Asprnablsg": f"{self._spr_stem}o",  # fortissimo
            "Asprnnompl": f"{self._spr_stem}a",  # fortissima
            "Asprnvocpl": f"{self._spr_stem}a",  # fortissima
            "Asprnaccpl": f"{self._spr_stem}a",  # fortissima
            "Asprngenpl": f"{self._spr_stem}orum",  # fortissimorum
            "Asprndatpl": f"{self._spr_stem}is",  # fortissimis
            "Asprnablpl": f"{self._spr_stem}is",  # fortissimis
        }

        if self.adverb_flag:
            endings |= {
                "Dpos": (
                    self._irregular_posadv
                    if self.irregular_flag
                    else f"{self._pos_stem}iter"
                ),  # fortiter
                "Dcmp": (
                    self._irregular_cmpadv
                    if self.irregular_flag
                    else f"{self._pos_stem}ius"
                ),  # fortius
                "Dspr": (
                    self._irregular_spradv
                    if self.irregular_flag
                    else f"{self._spr_stem}e"
                ),  # fortissime
            }

        return endings

    def _33_endings(self) -> Endings:
        if len(self._principal_parts) != 3:
            raise InvalidInputError(
                "Third-termination adjectives must have 3 principal parts "
                f"(adjective '{self._first}' given)",
            )

        self._mascnom = self._principal_parts[0]
        self._femnom = self._principal_parts[1]
        self._neutnom = self._principal_parts[2]

        self._pos_stem = self._femnom[:-2]  # acris -> acr-
        if not self.irregular_flag:
            self._cmp_stem = f"{self._pos_stem}ior"  # acr- -> acrior-
            if self._mascnom[-2:] == "er":
                self._spr_stem = f"{self._mascnom}rim"  # cer- -> acerrim-
            elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:  # pragma: no cover
                self._spr_stem = f"{self._pos_stem}issim"  # levis -> levissim-

        endings: Endings
        endings = {
            "Aposmnomsg": self._mascnom,  # acer
            "Aposmvocsg": self._mascnom,  # acer
            "Aposmaccsg": f"{self._pos_stem}em",  # acrem
            "Aposmgensg": f"{self._pos_stem}is",  # acris
            "Aposmdatsg": f"{self._pos_stem}i",  # acri
            "Aposmablsg": f"{self._pos_stem}i",  # acri
            "Aposmnompl": f"{self._pos_stem}es",  # acres
            "Aposmvocpl": f"{self._pos_stem}es",  # acres
            "Aposmaccpl": f"{self._pos_stem}es",  # acres
            "Aposmgenpl": f"{self._pos_stem}ium",  # acrium
            "Aposmdatpl": f"{self._pos_stem}ibus",  # acribus
            "Aposmablpl": f"{self._pos_stem}ibus",  # acribus
            "Aposfnomsg": self._femnom,  # acris
            "Aposfvocsg": self._femnom,  # acris
            "Aposfaccsg": f"{self._pos_stem}em",  # acrem
            "Aposfgensg": f"{self._pos_stem}is",  # acris
            "Aposfdatsg": f"{self._pos_stem}i",  # acri
            "Aposfablsg": f"{self._pos_stem}i",  # acri
            "Aposfnompl": f"{self._pos_stem}es",  # acres
            "Aposfvocpl": f"{self._pos_stem}es",  # acres
            "Aposfaccpl": f"{self._pos_stem}es",  # acres
            "Aposfgenpl": f"{self._pos_stem}ium",  # acrium
            "Aposfdatpl": f"{self._pos_stem}ibus",  # acribus
            "Aposfablpl": f"{self._pos_stem}ibus",  # acribus
            "Aposnnomsg": self._neutnom,  # acre
            "Aposnvocsg": self._neutnom,  # acre
            "Aposnaccsg": self._neutnom,  # acre
            "Aposngensg": f"{self._pos_stem}is",  # acris
            "Aposndatsg": f"{self._pos_stem}i",  # acri
            "Aposnablsg": f"{self._pos_stem}i",  # acri
            "Aposnnompl": f"{self._pos_stem}ia",  # acria
            "Aposnvocpl": f"{self._pos_stem}ia",  # acria
            "Aposnaccpl": f"{self._pos_stem}ia",  # acria
            "Aposngenpl": f"{self._pos_stem}ium",  # acrium
            "Aposndatpl": f"{self._pos_stem}ibus",  # acribus
            "Aposnablpl": f"{self._pos_stem}ibus",  # acribus
            "Acmpmnomsg": self._cmp_stem,  # acrior
            "Acmpmvocsg": self._cmp_stem,  # acrior
            "Acmpmaccsg": f"{self._cmp_stem}em",  # acriorem
            "Acmpmgensg": f"{self._cmp_stem}is",  # acrioris
            "Acmpmdatsg": f"{self._cmp_stem}i",  # acriori
            "Acmpmablsg": f"{self._cmp_stem}e",  # acriore
            "Acmpmnompl": f"{self._cmp_stem}es",  # acriores
            "Acmpmvocpl": f"{self._cmp_stem}es",  # acriores
            "Acmpmaccpl": f"{self._cmp_stem}es",  # acriores
            "Acmpmgenpl": f"{self._cmp_stem}um",  # acriorum
            "Acmpmdatpl": f"{self._cmp_stem}ibus",  # acrioribus
            "Acmpmablpl": f"{self._cmp_stem}ibus",  # acrioribus
            "Acmpfnomsg": self._cmp_stem,  # acrior
            "Acmpfvocsg": self._cmp_stem,  # acrior
            "Acmpfaccsg": f"{self._cmp_stem}em",  # acriorem
            "Acmpfgensg": f"{self._cmp_stem}is",  # acrioris
            "Acmpfdatsg": f"{self._cmp_stem}i",  # acriori
            "Acmpfablsg": f"{self._cmp_stem}e",  # acriore
            "Acmpfnompl": f"{self._cmp_stem}es",  # acriores
            "Acmpfvocpl": f"{self._cmp_stem}es",  # acriores
            "Acmpfaccpl": f"{self._cmp_stem}es",  # acriores
            "Acmpfgenpl": f"{self._cmp_stem}um",  # acriorum
            "Acmpfdatpl": f"{self._cmp_stem}ibus",  # acrioribus
            "Acmpfablpl": f"{self._cmp_stem}ibus",  # acrioribus
            "Acmpnnomsg": f"{self._cmp_stem[:-3]}ius",  # acrius
            "Acmpnvocsg": f"{self._cmp_stem[:-3]}ius",  # acrius
            "Acmpnaccsg": f"{self._cmp_stem[:-3]}ius",  # acrius
            "Acmpngensg": f"{self._cmp_stem}is",  # acrioris
            "Acmpndatsg": f"{self._cmp_stem}i",  # acriori
            "Acmpnablsg": f"{self._cmp_stem}e",  # acriore
            "Acmpnnompl": f"{self._cmp_stem}a",  # acriora
            "Acmpnvocpl": f"{self._cmp_stem}a",  # acriora
            "Acmpnaccpl": f"{self._cmp_stem}a",  # acriora
            "Acmpngenpl": f"{self._cmp_stem}um",  # acriorum
            "Acmpndatpl": f"{self._cmp_stem}ibus",  # acrioribus
            "Acmpnablpl": f"{self._cmp_stem}ibus",  # acrioribus
            "Asprmnomsg": f"{self._spr_stem}us",  # acerrimus
            "Asprmvocsg": f"{self._spr_stem}e",  # acerrime
            "Asprmaccsg": f"{self._spr_stem}um",  # acerrimum
            "Asprmgensg": f"{self._spr_stem}i",  # acerrimi
            "Asprmdatsg": f"{self._spr_stem}o",  # acerrimo
            "Asprmablsg": f"{self._spr_stem}o",  # acerrimo
            "Asprmnompl": f"{self._spr_stem}i",  # acerrimi
            "Asprmvocpl": f"{self._spr_stem}i",  # acerrimi
            "Asprmaccpl": f"{self._spr_stem}os",  # acerrimos
            "Asprmgenpl": f"{self._spr_stem}orum",  # acerrimorum
            "Asprmdatpl": f"{self._spr_stem}is",  # acerrimis
            "Asprmablpl": f"{self._spr_stem}is",  # acerrimis
            "Asprfnomsg": f"{self._spr_stem}a",  # acerrima
            "Asprfvocsg": f"{self._spr_stem}a",  # acerrima
            "Asprfaccsg": f"{self._spr_stem}am",  # acerrimam
            "Asprfgensg": f"{self._spr_stem}ae",  # acerrimae
            "Asprfdatsg": f"{self._spr_stem}ae",  # crrissimae
            "Asprfablsg": f"{self._spr_stem}a",  # acerrima
            "Asprfnompl": f"{self._spr_stem}ae",  # acerrimae
            "Asprfvocpl": f"{self._spr_stem}ae",  # acerrimae
            "Asprfaccpl": f"{self._spr_stem}as",  # acerrimas
            "Asprfgenpl": f"{self._spr_stem}arum",  # acerrimarum
            "Asprfdatpl": f"{self._spr_stem}is",  # acerrimis
            "Asprfablpl": f"{self._spr_stem}is",  # acerrimis
            "Asprnnomsg": f"{self._spr_stem}um",  # acerrimum
            "Asprnvocsg": f"{self._spr_stem}um",  # acerrimum
            "Asprnaccsg": f"{self._spr_stem}um",  # acerrimum
            "Asprngensg": f"{self._spr_stem}i",  # acerrimi
            "Asprndatsg": f"{self._spr_stem}o",  # acerrimo
            "Asprnablsg": f"{self._spr_stem}o",  # acerrimo
            "Asprnnompl": f"{self._spr_stem}a",  # acerrima
            "Asprnvocpl": f"{self._spr_stem}a",  # acerrima
            "Asprnaccpl": f"{self._spr_stem}a",  # acerrima
            "Asprngenpl": f"{self._spr_stem}orum",  # acerrimorum
            "Asprndatpl": f"{self._spr_stem}is",  # acerrimis
            "Asprnablpl": f"{self._spr_stem}is",  # acerrimis
        }

        if self.adverb_flag:
            endings |= {
                "Dpos": (
                    self._irregular_posadv
                    if self.irregular_flag
                    else f"{self._pos_stem}iter"
                ),  # acriter
                "Dcmp": (
                    self._irregular_cmpadv
                    if self.irregular_flag
                    else f"{self._pos_stem}ius"
                ),  # acrius
                "Dspr": (
                    self._irregular_spradv
                    if self.irregular_flag
                    else f"{self._spr_stem}e"
                ),  # acerrime
            }

        return endings

    def get(
        self,
        *,
        degree: Degree | str,
        gender: Gender | str | None = None,
        case: Case | str | None = None,
        number: Number | str | None = None,
        adverb: bool = False,
    ) -> Ending | None:
        """Returns the ending of the adjective.

        The function returns None if no ending is found.

        Parameters
        ----------
        degree : Degree | str
            The degree of the adjective.
        gender : Optional[Gender | str], default = None
            The gender of the ending, if applicable (not an adverb).
        case : Optional[Case | str], default = None
            The case of the ending, if applicable (not an adverb).
        number : Optional[Number | str], default = None
            The number of the ending, if applicable (not an adverb).
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
        >>> foo = Adjective(
        ...     "egens", "egentis", termination=1, declension="3", meaning="poor"
        ... )
        >>> foo.get(
        ...     degree="positive",
        ...     gender="masculine",
        ...     case="nominative",
        ...     number="singular",
        ... )
        'egens'

        Note that the arguments of get are keyword-only.
        """  # noqa: E501
        short_degree: str

        if adverb:
            if gender or case or number:
                raise InvalidInputError(
                    "Adverbs do not have gender, case or number "
                    f"(given '{gender}', '{case}' and '{number}')",
                )

            try:
                degree = Degree(degree)
            except ValueError as e:
                raise InvalidInputError(f"Invalid degree: '{degree}'") from e
            short_degree = degree.shorthand
            return self.endings.get(f"D{short_degree}")

        if not gender:
            raise InvalidInputError("Gender not given")
        if not case:
            raise InvalidInputError("Case not given")
        if not number:
            raise InvalidInputError("Number not given")

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

        if isinstance(degree, str):
            try:
                degree = Degree(degree.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid degree: '{degree}'") from e

        short_degree = degree.shorthand
        short_gender: str = gender.shorthand
        short_case: str = case.shorthand
        short_number: str = number.shorthand

        return self.endings.get(
            f"A{short_degree}{short_gender}{short_case}{short_number}",
        )

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents

        if key[0] == "A":
            output = EndingComponents(
                degree=Degree(key[1:4]).regular,
                gender=Gender(key[4]).regular,
                case=Case(key[5:8]).regular,
                number=Number(key[8:10]).regular,
            )
            output.string = (
                f"{output.degree} {output.case} "
                f"{output.number} {output.gender}"
            )

        else:
            output = EndingComponents(
                degree=Degree(key[1:4]).regular,
            )
            output.string = output.degree

        return output

    def __str__(self) -> str:
        if self.declension == "3":
            return (
                f"{self.meaning}: {', '.join(self._principal_parts)}, "
                f"({self.declension}-{self.termination})"
            )
        return f"{self.meaning}: {', '.join(self._principal_parts)}, (2-1-2)"

    def __repr__(self) -> str:
        return (
            f"Adjective({', '.join(self._principal_parts)}, "
            f"{self.termination}, {self.declension}, {self.meaning})"
        )
