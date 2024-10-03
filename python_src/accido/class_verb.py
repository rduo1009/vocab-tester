#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin verb with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, Literal

from .class_word import _Word
from .edge_cases import check_io_verb, find_irregular_endings
from .exceptions import InvalidInputError
from .misc import (
    PERSON_SHORTHAND,
    Case,
    EndingComponents,
    Gender,
    Mood,
    Number,
    Person,
    Tense,
    Voice,
)

if TYPE_CHECKING:
    from .type_aliases import Ending, Endings, Meaning


@total_ordering
class Verb(_Word):
    """Representation of a Latin verb with endings.

    Attributes
    ----------
    present, infinitive, perfect : str
    ppp : str
        The present perfect participle form of the verb. If the verb does
        not have participle endings, ppp is an empty string.
    meaning : Meaning
    conjugation : {0, 1, 2, 3, 4, 5}
        The conjugation of the verb. The value 5 represents the third
        declension -io verbs, and the value 0 represents an irregular
        conjugation.
    endings : Endings

    Examples
    --------
    >>> foo = Verb(
    ...     present="celo",
    ...     infinitive="celare",
    ...     perfect="celavi",
    ...     ppp="celatus",
    ...     meaning="hide",
    ... )
    >>> foo["Vpreactindsg1"]
    'celo'

    Note that all arguments of Verb are keyword-only.
    """

    def __init__(
        self,
        *,
        present: str,
        infinitive: str,
        perfect: str,
        ppp: str = "",
        meaning: Meaning,
    ) -> None:
        """Initialises Verb and determines the conjugation and endings.

        Parameters
        ----------
        present, infinitive, perfect : str
        ppp : str, default = ""
            The ppp ending of the verb. If the verb does not have
            participle endings, ppp is an empty string.
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the input is invalid (incorrect perfect or infinitive).
        """
        super().__init__()

        self.present: str = present
        self.infinitive: str = infinitive
        self.perfect: str = perfect
        self.ppp: str = ppp
        self.meaning: Meaning = meaning

        self._first = self.present
        self.conjugation: Literal[0, 1, 2, 3, 4, 5]

        if self.present[-1:] != "o":
            raise InvalidInputError(
                f"Invalid present form: '{self.present}' (must end in '-o')",
            )

        if self.perfect[-1:] != "i":
            raise InvalidInputError(
                f"Invalid perfect form: '{self.perfect}' (must end in '-i')",
            )

        # Conjugation edge cases
        if irregular_endings := find_irregular_endings(self.present):
            self.endings = irregular_endings
            self.conjugation = 0
            return
        if check_io_verb(self.present):
            self.conjugation = 5

        elif self.infinitive.endswith("are"):
            self.conjugation = 1
        elif self.infinitive.endswith("ire"):
            self.conjugation = 4
        elif self.infinitive.endswith("ere"):
            self.conjugation = 2 if self.present.endswith("eo") else 3
        else:
            raise InvalidInputError(
                f"Invalid infinitive form: '{self.infinitive}'",
            )

        self._pre_stem: str = self.present[:-1]
        self._inf_stem: str = self.infinitive[:-3]
        self._per_stem: str = self.perfect[:-1]

        match self.conjugation:
            case 1:
                self.endings = self._first_conjugation()

            case 2:
                self.endings = self._second_conjugation()

            case 3:
                self.endings = self._third_conjugation()

            case 4:
                self.endings = self._fourth_conjugation()

            case 5:
                self.endings = self._third_io_conjugation()

            case _:  # pragma: no cover
                raise ValueError(  # noqa: DOC501
                    f"Conjugation {self.conjugation} not recognised",
                )

        if self.ppp:
            self.endings |= self._participles()

    def _first_conjugation(self) -> Endings:
        return {
            "Vpreactindsg1": self.present,  # porto
            "Vpreactindsg2": f"{self._inf_stem}as",  # portas
            "Vpreactindsg3": f"{self._inf_stem}at",  # portat
            "Vpreactindpl1": f"{self._inf_stem}amus",  # portamus
            "Vpreactindpl2": f"{self._inf_stem}atis",  # portatis
            "Vpreactindpl3": f"{self._inf_stem}ant",  # portant
            "Vimpactindsg1": f"{self._inf_stem}abam",  # portabam
            "Vimpactindsg2": f"{self._inf_stem}abas",  # portabas
            "Vimpactindsg3": f"{self._inf_stem}abat",  # portabat
            "Vimpactindpl1": f"{self._inf_stem}abamus",  # portabamus
            "Vimpactindpl2": f"{self._inf_stem}abatis",  # portabatis
            "Vimpactindpl3": f"{self._inf_stem}abant",  # portabant
            "Vperactindsg1": self.perfect,  # portavi
            "Vperactindsg2": f"{self._per_stem}isti",  # portavisti
            "Vperactindsg3": f"{self._per_stem}it",  # portavit
            "Vperactindpl1": f"{self._per_stem}imus",  # portavimus
            "Vperactindpl2": f"{self._per_stem}istis",  # portavistis
            "Vperactindpl3": f"{self._per_stem}erunt",  # portaverunt
            "Vplpactindsg1": f"{self._per_stem}eram",  # portaveram
            "Vplpactindsg2": f"{self._per_stem}eras",  # portaveras
            "Vplpactindsg3": f"{self._per_stem}erat",  # portaverat
            "Vplpactindpl1": f"{self._per_stem}eramus",  # portaveramus
            "Vplpactindpl2": f"{self._per_stem}eratis",  # portaveratis
            "Vplpactindpl3": f"{self._per_stem}erant",  # portaverant
            "Vpreactinf   ": self.infinitive,  # portare
            "Vpreactipesg2": f"{self._inf_stem}a",  # porta
            "Vpreactipepl2": f"{self._inf_stem}ate",  # portate
            "Vimpactsbjsg1": f"{self.infinitive}m",  # portarem
            "Vimpactsbjsg2": f"{self.infinitive}s",  # portares
            "Vimpactsbjsg3": f"{self.infinitive}t",  # portaret
            "Vimpactsbjpl1": f"{self.infinitive}mus",  # portaremus
            "Vimpactsbjpl2": f"{self.infinitive}tis",  # portaretis
            "Vimpactsbjpl3": f"{self.infinitive}nt",  # portarent
            "Vplpactsbjsg1": f"{self._per_stem}issem",  # portavissem
            "Vplpactsbjsg2": f"{self._per_stem}isses",  # portavisses
            "Vplpactsbjsg3": f"{self._per_stem}isset",  # portavisset
            "Vplpactsbjpl1": f"{self._per_stem}issemus",  # portavissemus
            "Vplpactsbjpl2": f"{self._per_stem}issetis",  # portavissetis
            "Vplpactsbjpl3": f"{self._per_stem}issent",  # portavissent
        }

    def _second_conjugation(self) -> Endings:
        return {
            "Vpreactindsg1": self.present,  # doceo
            "Vpreactindsg2": f"{self._inf_stem}es",  # doces
            "Vpreactindsg3": f"{self._inf_stem}et",  # docet
            "Vpreactindpl1": f"{self._inf_stem}emus",  # docemus
            "Vpreactindpl2": f"{self._inf_stem}etis",  # docetis
            "Vpreactindpl3": f"{self._inf_stem}ent",  # docent
            "Vimpactindsg1": f"{self._inf_stem}ebam",  # docebam
            "Vimpactindsg2": f"{self._inf_stem}ebas",  # docebas
            "Vimpactindsg3": f"{self._inf_stem}ebat",  # docebat
            "Vimpactindpl1": f"{self._inf_stem}ebamus",  # docebamus
            "Vimpactindpl2": f"{self._inf_stem}ebatis",  # docebatis
            "Vimpactindpl3": f"{self._inf_stem}ebant",  # docebant
            "Vperactindsg1": self.perfect,  # docui
            "Vperactindsg2": f"{self._per_stem}isti",  # docuisit
            "Vperactindsg3": f"{self._per_stem}it",  # docuit
            "Vperactindpl1": f"{self._per_stem}imus",  # docuimus
            "Vperactindpl2": f"{self._per_stem}istis",  # docuistis
            "Vperactindpl3": f"{self._per_stem}erunt",  # docuerunt
            "Vplpactindsg1": f"{self._per_stem}eram",  # docueram
            "Vplpactindsg2": f"{self._per_stem}eras",  # docueras
            "Vplpactindsg3": f"{self._per_stem}erat",  # docuerat
            "Vplpactindpl1": f"{self._per_stem}eramus",  # docueramus
            "Vplpactindpl2": f"{self._per_stem}eratis",  # docueratis
            "Vplpactindpl3": f"{self._per_stem}erant",  # docuerant
            "Vpreactinf   ": self.infinitive,  # docere
            "Vpreactipesg2": f"{self._inf_stem}e",  # doce
            "Vpreactipepl2": f"{self._inf_stem}ete",  # docete
            "Vimpactsbjsg1": f"{self.infinitive}m",  # docerem
            "Vimpactsbjsg2": f"{self.infinitive}s",  # doceres
            "Vimpactsbjsg3": f"{self.infinitive}t",  # doceret
            "Vimpactsbjpl1": f"{self.infinitive}mus",  # doceremus
            "Vimpactsbjpl2": f"{self.infinitive}tis",  # doceretis
            "Vimpactsbjpl3": f"{self.infinitive}nt",  # docerent
            "Vplpactsbjsg1": f"{self._per_stem}issem",  # docuissem
            "Vplpactsbjsg2": f"{self._per_stem}isses",  # docuisses
            "Vplpactsbjsg3": f"{self._per_stem}isset",  # docuisset
            "Vplpactsbjpl1": f"{self._per_stem}issemus",  # docuissmus
            "Vplpactsbjpl2": f"{self._per_stem}issetis",  # docuissetis
            "Vplpactsbjpl3": f"{self._per_stem}issent",  # docuissent
        }

    def _third_conjugation(self) -> Endings:
        return {
            "Vpreactindsg1": self.present,  # traho
            "Vpreactindsg2": f"{self._inf_stem}is",  # trahis
            "Vpreactindsg3": f"{self._inf_stem}it",  # trahit
            "Vpreactindpl1": f"{self._inf_stem}imus",  # trahimus
            "Vpreactindpl2": f"{self._inf_stem}itis",  # trahitis
            "Vpreactindpl3": f"{self._inf_stem}unt",  # trahunt
            "Vimpactindsg1": f"{self._inf_stem}ebam",  # trahebam
            "Vimpactindsg2": f"{self._inf_stem}ebas",  # trahebas
            "Vimpactindsg3": f"{self._inf_stem}ebat",  # trahebat
            "Vimpactindpl1": f"{self._inf_stem}ebamus",  # trahebamus
            "Vimpactindpl2": f"{self._inf_stem}ebatis",  # trahebatis
            "Vimpactindpl3": f"{self._inf_stem}ebant",  # trahebant
            "Vperactindsg1": self.perfect,  # traxi
            "Vperactindsg2": f"{self._per_stem}isti",  # traxisti
            "Vperactindsg3": f"{self._per_stem}it",  # traxit
            "Vperactindpl1": f"{self._per_stem}imus",  # traximus
            "Vperactindpl2": f"{self._per_stem}istis",  # traxistis
            "Vperactindpl3": f"{self._per_stem}erunt",  # traxerunt
            "Vplpactindsg1": f"{self._per_stem}eram",  # traxeram
            "Vplpactindsg2": f"{self._per_stem}eras",  # traxeras
            "Vplpactindsg3": f"{self._per_stem}erat",  # traxerat
            "Vplpactindpl1": f"{self._per_stem}eramus",  # traxeramus
            "Vplpactindpl2": f"{self._per_stem}eratis",  # traxeratis
            "Vplpactindpl3": f"{self._per_stem}erant",  # traxerant
            "Vpreactinf   ": self.infinitive,  # trahere
            "Vpreactipesg2": f"{self._inf_stem}e",  # trahe
            "Vpreactipepl2": f"{self._inf_stem}ite",  # trahite
            "Vimpactsbjsg1": f"{self.infinitive}m",  # traherem
            "Vimpactsbjsg2": f"{self.infinitive}s",  # traheres
            "Vimpactsbjsg3": f"{self.infinitive}t",  # traheret
            "Vimpactsbjpl1": f"{self.infinitive}mus",  # traheremus
            "Vimpactsbjpl2": f"{self.infinitive}tis",  # traheretis
            "Vimpactsbjpl3": f"{self.infinitive}nt",  # traherent
            "Vplpactsbjsg1": f"{self._per_stem}issem",  # traxissem
            "Vplpactsbjsg2": f"{self._per_stem}isses",  # traxisses
            "Vplpactsbjsg3": f"{self._per_stem}isset",  # traxisset
            "Vplpactsbjpl1": f"{self._per_stem}issemus",  # traxissemus
            "Vplpactsbjpl2": f"{self._per_stem}issetis",  # traxissetis
            "Vplpactsbjpl3": f"{self._per_stem}issent",  # traxissent
        }

    def _fourth_conjugation(self) -> Endings:
        return {
            "Vpreactindsg1": self.present,  # audio
            "Vpreactindsg2": f"{self._inf_stem}is",  # audis
            "Vpreactindsg3": f"{self._inf_stem}it",  # audit
            "Vpreactindpl1": f"{self._inf_stem}imus",  # audimus
            "Vpreactindpl2": f"{self._inf_stem}itis",  # auditis
            "Vpreactindpl3": f"{self._inf_stem}iunt",  # audiunt
            "Vimpactindsg1": f"{self._inf_stem}iebam",  # audiebam
            "Vimpactindsg2": f"{self._inf_stem}iebas",  # audiebas
            "Vimpactindsg3": f"{self._inf_stem}iebat",  # audiebat
            "Vimpactindpl1": f"{self._inf_stem}iebamus",  # audiebamus
            "Vimpactindpl2": f"{self._inf_stem}iebatis",  # audiebatis
            "Vimpactindpl3": f"{self._inf_stem}iebant",  # audiebant
            "Vperactindsg1": self.perfect,  # audivi
            "Vperactindsg2": f"{self._per_stem}isti",  # audivisti
            "Vperactindsg3": f"{self._per_stem}it",  # audivit
            "Vperactindpl1": f"{self._per_stem}imus",  # audivimus
            "Vperactindpl2": f"{self._per_stem}istis",  # audivistis
            "Vperactindpl3": f"{self._per_stem}erunt",  # audiverunt
            "Vplpactindsg1": f"{self._per_stem}eram",  # audiveram
            "Vplpactindsg2": f"{self._per_stem}eras",  # audiveras
            "Vplpactindsg3": f"{self._per_stem}erat",  # audiverat
            "Vplpactindpl1": f"{self._per_stem}eramus",  # audiveramus
            "Vplpactindpl2": f"{self._per_stem}eratis",  # audiveratis
            "Vplpactindpl3": f"{self._per_stem}erant",  # audiverant
            "Vpreactinf   ": self.infinitive,  # audire
            "Vpreactipesg2": f"{self._inf_stem}i",  # audi
            "Vpreactipepl2": f"{self._inf_stem}ite",  # audite
            "Vimpactsbjsg1": f"{self.infinitive}m",  # audirem
            "Vimpactsbjsg2": f"{self.infinitive}s",  # audires
            "Vimpactsbjsg3": f"{self.infinitive}t",  # audiret
            "Vimpactsbjpl1": f"{self.infinitive}mus",  # audiremus
            "Vimpactsbjpl2": f"{self.infinitive}tis",  # audiretis
            "Vimpactsbjpl3": f"{self.infinitive}nt",  # audirent
            "Vplpactsbjsg1": f"{self._per_stem}issem",  # audivissem
            "Vplpactsbjsg2": f"{self._per_stem}isses",  # audivisses
            "Vplpactsbjsg3": f"{self._per_stem}isset",  # audivisset
            "Vplpactsbjpl1": f"{self._per_stem}issemus",  # audivissemus
            "Vplpactsbjpl2": f"{self._per_stem}issetis",  # audivissetis
            "Vplpactsbjpl3": f"{self._per_stem}issent",  # audivissent
        }

    def _third_io_conjugation(self) -> Endings:
        return {
            "Vpreactindsg1": self.present,  # capio
            "Vpreactindsg2": f"{self._inf_stem}is",  # capis
            "Vpreactindsg3": f"{self._inf_stem}it",  # capit
            "Vpreactindpl1": f"{self._inf_stem}imus",  # capimus
            "Vpreactindpl2": f"{self._inf_stem}itis",  # capitis
            "Vpreactindpl3": f"{self._inf_stem}iunt",  # capiunt
            "Vimpactindsg1": f"{self._inf_stem}iebam",  # capiebam
            "Vimpactindsg2": f"{self._inf_stem}iebas",  # capiebas
            "Vimpactindsg3": f"{self._inf_stem}iebat",  # capiebat
            "Vimpactindpl1": f"{self._inf_stem}iebamus",  # capiebamus
            "Vimpactindpl2": f"{self._inf_stem}iebatis",  # capiebatis
            "Vimpactindpl3": f"{self._inf_stem}iebant",  # capiebant
            "Vperactindsg1": self.perfect,  # cepi
            "Vperactindsg2": f"{self._per_stem}isti",  # cepisti
            "Vperactindsg3": f"{self._per_stem}it",  # cepit
            "Vperactindpl1": f"{self._per_stem}imus",  # cepimus
            "Vperactindpl2": f"{self._per_stem}istis",  # cepistis
            "Vperactindpl3": f"{self._per_stem}erunt",  # ceperunt
            "Vplpactindsg1": f"{self._per_stem}eram",  # ceperam
            "Vplpactindsg2": f"{self._per_stem}eras",  # ceperas
            "Vplpactindsg3": f"{self._per_stem}erat",  # ceperat
            "Vplpactindpl1": f"{self._per_stem}eramus",  # ceperamus
            "Vplpactindpl2": f"{self._per_stem}eratis",  # ceperatis
            "Vplpactindpl3": f"{self._per_stem}erant",  # ceperant
            "Vpreactinf   ": self.infinitive,  # capere
            "Vpreactipesg2": f"{self._inf_stem}e",  # cape
            "Vpreactipepl2": f"{self._inf_stem}ite",  # capite
            "Vimpactsbjsg1": f"{self.infinitive}m",  # caperem
            "Vimpactsbjsg2": f"{self.infinitive}s",  # caperes
            "Vimpactsbjsg3": f"{self.infinitive}t",  # caperet
            "Vimpactsbjpl1": f"{self.infinitive}mus",  # caperemus
            "Vimpactsbjpl2": f"{self.infinitive}tis",  # caperetis
            "Vimpactsbjpl3": f"{self.infinitive}nt",  # caperent
            "Vplpactsbjsg1": f"{self._per_stem}issem",  # cepissem
            "Vplpactsbjsg2": f"{self._per_stem}isses",  # cepisses
            "Vplpactsbjsg3": f"{self._per_stem}isset",  # cepisset
            "Vplpactsbjpl1": f"{self._per_stem}issemus",  # cepissemus
            "Vplpactsbjpl2": f"{self._per_stem}issetis",  # cepissetis
            "Vplpactsbjpl3": f"{self._per_stem}issent",  # cepissent
        }

    def _participles(self) -> Endings:
        self._preptc_stem: str = self.infinitive[:-2]
        self._ppp_stem: str = self.ppp[:-2]
        return {
            "Vpreactptcmnomsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcmvocsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcmaccsg": f"{self._preptc_stem}ntem",  # portantem
            "Vpreactptcmgensg": f"{self._preptc_stem}ntis",  # portantis
            "Vpreactptcmdatsg": f"{self._preptc_stem}nti",  # portanti
            "Vpreactptcmablsg": f"{self._preptc_stem}nte",  # portante
            "Vpreactptcmnompl": f"{self._preptc_stem}ntes",  # portantes
            "Vpreactptcmvocpl": f"{self._preptc_stem}ntes",  # portantes
            "Vpreactptcmaccpl": f"{self._preptc_stem}ntes",  # portantes
            "Vpreactptcmgenpl": f"{self._preptc_stem}ntium",  # portantium
            "Vpreactptcmdatpl": f"{self._preptc_stem}ntibus",  # portantibus
            "Vpreactptcmablpl": f"{self._preptc_stem}ntibus",  # portantibus
            "Vpreactptcfnomsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcfvocsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcfaccsg": f"{self._preptc_stem}ntem",  # portantem
            "Vpreactptcfgensg": f"{self._preptc_stem}ntis",  # portantis
            "Vpreactptcfdatsg": f"{self._preptc_stem}nti",  # portanti
            "Vpreactptcfablsg": f"{self._preptc_stem}nte",  # portante
            "Vpreactptcfnompl": f"{self._preptc_stem}ntes",  # portantes
            "Vpreactptcfvocpl": f"{self._preptc_stem}ntes",  # portantes
            "Vpreactptcfaccpl": f"{self._preptc_stem}ntes",  # portantes
            "Vpreactptcfgenpl": f"{self._preptc_stem}ntium",  # portantium
            "Vpreactptcfdatpl": f"{self._preptc_stem}ntibus",  # portantibus
            "Vpreactptcfablpl": f"{self._preptc_stem}ntibus",  # portantibus
            "Vpreactptcnnomsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcnvocsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcnaccsg": f"{self._preptc_stem}ns",  # portans
            "Vpreactptcngensg": f"{self._preptc_stem}ntis",  # portantis
            "Vpreactptcndatsg": f"{self._preptc_stem}nti",  # portanti
            "Vpreactptcnablsg": f"{self._preptc_stem}nte",  # portante
            "Vpreactptcnnompl": f"{self._preptc_stem}ntia",  # portantia
            "Vpreactptcnvocpl": f"{self._preptc_stem}ntia",  # portantia
            "Vpreactptcnaccpl": f"{self._preptc_stem}ntia",  # portantia
            "Vpreactptcngenpl": f"{self._preptc_stem}ntium",  # portantium
            "Vpreactptcndatpl": f"{self._preptc_stem}ntibus",  # portantibus
            "Vpreactptcnablpl": f"{self._preptc_stem}ntibus",  # portantibus
            "Vperpasptcmnomsg": self.ppp,  # portatustus
            "Vperpasptcmvocsg": f"{self._ppp_stem}e",  # portate
            "Vperpasptcmaccsg": f"{self._ppp_stem}um",  # portatum
            "Vperpasptcmgensg": f"{self._ppp_stem}i",  # portati
            "Vperpasptcmdatsg": f"{self._ppp_stem}o",  # portato
            "Vperpasptcmablsg": f"{self._ppp_stem}o",  # portato
            "Vperpasptcmnompl": f"{self._ppp_stem}i",  # portati
            "Vperpasptcmvocpl": f"{self._ppp_stem}i",  # portati
            "Vperpasptcmaccpl": f"{self._ppp_stem}os",  # portatos
            "Vperpasptcmgenpl": f"{self._ppp_stem}orum",  # portatorum
            "Vperpasptcmdatpl": f"{self._ppp_stem}is",  # portatis
            "Vperpasptcmablpl": f"{self._ppp_stem}is",  # portatis
            "Vperpasptcfnomsg": f"{self._ppp_stem}a",  # portata
            "Vperpasptcfvocsg": f"{self._ppp_stem}a",  # portata
            "Vperpasptcfaccsg": f"{self._ppp_stem}am",  # portatam
            "Vperpasptcfgensg": f"{self._ppp_stem}ae",  # portatae
            "Vperpasptcfdatsg": f"{self._ppp_stem}ae",  # portatae
            "Vperpasptcfablsg": f"{self._ppp_stem}a",  # portata
            "Vperpasptcfnompl": f"{self._ppp_stem}ae",  # portatae
            "Vperpasptcfvocpl": f"{self._ppp_stem}ae",  # portatae
            "Vperpasptcfaccpl": f"{self._ppp_stem}as",  # portatas
            "Vperpasptcfgenpl": f"{self._ppp_stem}arum",  # portarum
            "Vperpasptcfdatpl": f"{self._ppp_stem}is",  # portatis
            "Vperpasptcfablpl": f"{self._ppp_stem}is",  # portatis
            "Vperpasptcnnomsg": f"{self._ppp_stem}um",  # portatum
            "Vperpasptcnvocsg": f"{self._ppp_stem}um",  # portatum
            "Vperpasptcnaccsg": f"{self._ppp_stem}um",  # portatum
            "Vperpasptcngensg": f"{self._ppp_stem}i",  # portati
            "Vperpasptcndatsg": f"{self._ppp_stem}o",  # portato
            "Vperpasptcnablsg": f"{self._ppp_stem}o",  # portato
            "Vperpasptcnnompl": f"{self._ppp_stem}a",  # portata
            "Vperpasptcnvocpl": f"{self._ppp_stem}a",  # portata
            "Vperpasptcnaccpl": f"{self._ppp_stem}a",  # portata
            "Vperpasptcngenpl": f"{self._ppp_stem}orum",  # portatorum
            "Vperpasptcndatpl": f"{self._ppp_stem}is",  # portatis
            "Vperpasptcnablpl": f"{self._ppp_stem}is",  # portatis
        }

    def get(
        self,
        *,
        person: Person | None = None,
        number: Number | None = None,
        tense: Tense,
        voice: Voice,
        mood: Mood,
        participle_gender: Gender | None = None,
        participle_case: Case | None = None,
    ) -> Ending | None:
        """Returns the ending of the verb.

        The function returns None if no ending is found.

        Parameters
        ----------
        person : Optional[Person], default = None
            The person of the ending, if applicable (not participle).
        number : Optional[Number], default = None
            The number of the ending, if applicable (not participle).
        tense : Tense
            The tense of the ending.
        voice : Voice
            The voice of the ending.
        mood : Mood
            The mood of the ending.
        participle_gender : Optional[Gender], default = None
            The gender of the participle, if applicable.
        participle_case : Optional[Case], default = None
            The case of the participle, if applicable.

        Returns
        -------
        Ending
            The ending found
        None
            If no ending is found

        Raises
        ------
        InvalidInputError
            If the inputs are not valid. Note that the inputs must be the
            full words, e.g. 'singular', 'plural', 'masculine', 'feminine'.

            If the ending cannot be found.


        Examples
        --------
        >>> foo = Verb(
        ...     present="celo",
        ...     infinitive="celare",
        ...     perfect="celavi",
        ...     ppp="celatus",
        ...     meaning="hide",
        ... )
        >>> foo.get(
        ...     person=1,
        ...     number=Number.SINGULAR,
        ...     tense=Tense.PRESENT,
        ...     voice=Voice.ACTIVE,
        ...     mood=Mood.INDICATIVE,
        ... )
        'celo'

        Note that all arguments of get are keyword-only.

        >>> foo.get(
        ...     number=Number.SINGULAR,
        ...     tense=Tense.PERFECT,
        ...     voice=Voice.PASSIVE,
        ...     mood=Mood.PARTICIPLE,
        ...     participle_gender=Gender.MASCULINE,
        ...     participle_case=Case.NOMINATIVE,
        ... )
        'celatus'

        Similar with participle endings.
        """
        short_tense: str
        short_voice: str
        short_mood: str
        short_number: str

        if isinstance(tense, str):
            try:
                tense = Tense(tense.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid tense: '{tense}'") from e

        if isinstance(voice, str):
            try:
                voice = Voice(voice.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid voice: '{voice}'") from e

        if isinstance(mood, str):
            try:
                mood = Mood(mood.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid mood: '{mood}'") from e

        if mood == Mood.PARTICIPLE:
            if person:
                raise InvalidInputError(
                    f"Participle cannot have a person (person '{person}')",
                )

            if not participle_case:
                raise InvalidInputError("Case not given")

            if not participle_gender:
                raise InvalidInputError("Gender not given")

            if not number:
                raise InvalidInputError("Number not given")

            return self._get_participle(
                tense=tense,
                voice=voice,
                number=number,
                participle_gender=participle_gender,
                participle_case=participle_case,
            )

        if number and isinstance(number, str):
            try:
                number = Number(number.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid number: '{number}'") from e

        short_tense = tense.shorthand
        short_voice = voice.shorthand
        short_mood = mood.shorthand
        if number:
            assert isinstance(number, Number)
            short_number = number.shorthand

        if mood == Mood.INFINITIVE:
            return self.endings.get(f"V{short_tense}{short_voice}inf   ")
        return self.endings.get(
            f"V{short_tense}{short_voice}{short_mood}{short_number}{person}",
        )

    def _get_participle(
        self,
        *,
        tense: Tense,
        voice: Voice,
        number: Number,
        participle_gender: Gender,
        participle_case: Case,
    ) -> Ending | None:
        if isinstance(participle_case, str):
            try:
                participle_case = Case(participle_case.lower())
            except ValueError as e:
                raise InvalidInputError(
                    f"Invalid case: '{participle_case}'"
                ) from e

        if isinstance(participle_gender, str):
            try:
                participle_gender = Gender(participle_gender.lower())
            except ValueError as e:
                raise InvalidInputError(
                    f"Invalid gender: '{participle_gender}'"
                ) from e

        if isinstance(number, str):
            try:
                number = Number(number.lower())
            except ValueError as e:
                raise InvalidInputError(f"Invalid number: '{number}'") from e

        short_tense = tense.shorthand
        short_voice = voice.shorthand
        short_number = number.shorthand
        short_gender: str = participle_gender.shorthand
        short_case: str = participle_case.shorthand

        return self.endings.get(
            f"V{short_tense}{short_voice}ptc{short_gender}{short_case}{short_number}",
        )

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents
        if len(key) == 13 and key[7:10] == "inf":
            output = EndingComponents(
                tense=Tense(key[1:4]),
                voice=Voice(key[4:7]),
                mood=Mood(key[7:10]),
            )
            output.string = (
                f"{output.tense.regular} {output.voice.regular} "
                f"{output.mood.regular}"
            )
            return output

        if len(key) == 13:
            output = EndingComponents(
                tense=Tense(key[1:4]),
                voice=Voice(key[4:7]),
                mood=Mood(key[7:10]),
                number=Number(key[10:12]),
                person=int(key[12]),
            )
            output.string = (
                f"{output.tense.regular} {output.voice.regular} "
                f"{output.mood.regular} {output.number.regular} "
                f"{PERSON_SHORTHAND[int(key[12])]}"
            )
            return output

        if len(key) == 16 and key[7:10] == "ptc":
            output = EndingComponents(
                tense=Tense(key[1:4]),
                voice=Voice(key[4:7]),
                mood=Mood.PARTICIPLE,
                gender=Gender(key[10]),
                case=Case(key[11:14]),
                number=Number(key[14:16]),
            )
            output.string = (
                f"{output.tense.regular} {output.voice.regular} participle "
                f"{output.gender.regular} {output.case.regular} "
                f"{output.number.regular}"
            )
            return output

        raise InvalidInputError(
            f"Key '{key}' is invalid"
        )  # pragma: no cover # this should never happen

    def __repr__(self) -> str:
        return (
            f"Verb({self.present}, {self.infinitive}, {self.perfect}, "
            f"{self.ppp}, {self.meaning})"
        )

    def __str__(self) -> str:
        if self.ppp:
            return (
                f"{self.meaning}: {self.present}, {self.infinitive}, "
                f"{self.perfect}, {self.ppp}"
            )
        return (
            f"{self.meaning}: {self.present}, "
            f"{self.infinitive}, {self.perfect}"
        )
