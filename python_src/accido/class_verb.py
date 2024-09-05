#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representation of a Latin verb with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import Literal, Optional

from ..utils import key_from_value
from .class_word import _Word
from .edge_cases import check_io_verb, find_irregular_endings
from .exceptions import InvalidInputError
from .misc import (
    CASE_SHORTHAND,
    GENDER_SHORTHAND,
    MOOD_SHORTHAND,
    NUMBER_SHORTHAND,
    PERSON_SHORTHAND,
    TENSE_SHORTHAND,
    VOICE_SHORTHAND,
    Ending,
    EndingComponents,
    Meaning,
)


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
        """Initalises Verb and determines the conjugation and
        endings.

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
                f"Invalid present form: '{self.present}' (must end in '-o')"
            )

        if self.perfect[-1:] != "i":
            raise InvalidInputError(
                f"Invalid perfect form: '{self.perfect}' (must end in '-i')"
            )

        # Conjugation edge cases
        if irregular_endings := find_irregular_endings(self.present):
            self.endings = irregular_endings
            self.conjugation = 0
            return
        elif check_io_verb(self.present):
            self.conjugation = 5

        # Find conjugation
        elif self.infinitive[-3:] == "are":
            self.conjugation = 1
        elif self.infinitive[-3:] == "ire":
            self.conjugation = 4
        elif self.infinitive[-3:] == "ere":
            if self.present[-2:] == "eo":
                self.conjugation = 2
            else:
                self.conjugation = 3
        else:
            raise InvalidInputError(
                f"Invalid infinitive form: '{self.infinitive}'"
            )

        self._pre_stem: str = self.present[:-1]
        self._inf_stem: str = self.infinitive[:-3]
        self._per_stem: str = self.perfect[:-1]

        match self.conjugation:
            case 1:
                self.endings = {
                    "Vpreactindsg1": self.present,  # porto
                    "Vpreactindsg2": self._inf_stem + "as",  # portas
                    "Vpreactindsg3": self._inf_stem + "at",  # portat
                    "Vpreactindpl1": self._inf_stem + "amus",  # portamus
                    "Vpreactindpl2": self._inf_stem + "atis",  # portatis
                    "Vpreactindpl3": self._inf_stem + "ant",  # portant
                    "Vimpactindsg1": self._inf_stem + "abam",  # portabam
                    "Vimpactindsg2": self._inf_stem + "abas",  # portabas
                    "Vimpactindsg3": self._inf_stem + "abat",  # portabat
                    "Vimpactindpl1": self._inf_stem + "abamus",  # portabamus
                    "Vimpactindpl2": self._inf_stem + "abatis",  # portabatis
                    "Vimpactindpl3": self._inf_stem + "abant",  # portabant
                    "Vperactindsg1": self.perfect,  # portavi
                    "Vperactindsg2": self._per_stem + "isti",  # portavisti
                    "Vperactindsg3": self._per_stem + "it",  # portavit
                    "Vperactindpl1": self._per_stem + "imus",  # portavimus
                    "Vperactindpl2": self._per_stem + "istis",  # portavistis
                    "Vperactindpl3": self._per_stem + "erunt",  # portaverunt
                    "Vplpactindsg1": self._per_stem + "eram",  # portaveram
                    "Vplpactindsg2": self._per_stem + "eras",  # portaveras
                    "Vplpactindsg3": self._per_stem + "erat",  # portaverat
                    "Vplpactindpl1": self._per_stem + "eramus",  # portaveramus
                    "Vplpactindpl2": self._per_stem + "eratis",  # portaveratis
                    "Vplpactindpl3": self._per_stem + "erant",  # portaverant
                    "Vpreactinf   ": self.infinitive,  # portare
                    "Vpreactipesg2": self._inf_stem + "a",  # porta
                    "Vpreactipepl2": self._inf_stem + "ate",  # portate
                    "Vimpactsbjsg1": self.infinitive + "m",  # portarem
                    "Vimpactsbjsg2": self.infinitive + "s",  # portares
                    "Vimpactsbjsg3": self.infinitive + "t",  # portaret
                    "Vimpactsbjpl1": self.infinitive + "mus",  # portaremus
                    "Vimpactsbjpl2": self.infinitive + "tis",  # portaretis
                    "Vimpactsbjpl3": self.infinitive + "nt",  # portarent
                    "Vplpactsbjsg1": self._per_stem + "issem",  # portavissem
                    "Vplpactsbjsg2": self._per_stem + "isses",  # portavisses
                    "Vplpactsbjsg3": self._per_stem + "isset",  # portavisset
                    "Vplpactsbjpl1": self._per_stem + "issemus",  # portavissemus
                    "Vplpactsbjpl2": self._per_stem + "issetis",  # portavissetis
                    "Vplpactsbjpl3": self._per_stem + "issent",  # portavissent
                }  # fmt: skip

            case 2:
                self.endings = {
                    "Vpreactindsg1": self.present,  # doceo
                    "Vpreactindsg2": self._inf_stem + "es",  # doces
                    "Vpreactindsg3": self._inf_stem + "et",  # docet
                    "Vpreactindpl1": self._inf_stem + "emus",  # docemus
                    "Vpreactindpl2": self._inf_stem + "etis",  # docetis
                    "Vpreactindpl3": self._inf_stem + "ent",  # docent
                    "Vimpactindsg1": self._inf_stem + "ebam",  # docebam
                    "Vimpactindsg2": self._inf_stem + "ebas",  # docebas
                    "Vimpactindsg3": self._inf_stem + "ebat",  # docebat
                    "Vimpactindpl1": self._inf_stem + "ebamus",  # docebamus
                    "Vimpactindpl2": self._inf_stem + "ebatis",  # docebatis
                    "Vimpactindpl3": self._inf_stem + "ebant",  # docebant
                    "Vperactindsg1": self.perfect,  # docui
                    "Vperactindsg2": self._per_stem + "isti",  # docuisit
                    "Vperactindsg3": self._per_stem + "it",  # docuit
                    "Vperactindpl1": self._per_stem + "imus",  # docuimus
                    "Vperactindpl2": self._per_stem + "istis",  # docuistis
                    "Vperactindpl3": self._per_stem + "erunt",  # docuerunt
                    "Vplpactindsg1": self._per_stem + "eram",  # docueram
                    "Vplpactindsg2": self._per_stem + "eras",  # docueras
                    "Vplpactindsg3": self._per_stem + "erat",  # docuerat
                    "Vplpactindpl1": self._per_stem + "eramus",  # docueramus
                    "Vplpactindpl2": self._per_stem + "eratis",  # docueratis
                    "Vplpactindpl3": self._per_stem + "erant",  # docuerant
                    "Vpreactinf   ": self.infinitive,  # docere
                    "Vpreactipesg2": self._inf_stem + "e",  # doce
                    "Vpreactipepl2": self._inf_stem + "ete",  # docete
                    "Vimpactsbjsg1": self.infinitive + "m",  # docerem
                    "Vimpactsbjsg2": self.infinitive + "s",  # doceres
                    "Vimpactsbjsg3": self.infinitive + "t",  # doceret
                    "Vimpactsbjpl1": self.infinitive + "mus",  # doceremus
                    "Vimpactsbjpl2": self.infinitive + "tis",  # doceretis
                    "Vimpactsbjpl3": self.infinitive + "nt",  # docerent
                    "Vplpactsbjsg1": self._per_stem + "issem",  # docuissem
                    "Vplpactsbjsg2": self._per_stem + "isses",  # docuisses
                    "Vplpactsbjsg3": self._per_stem + "isset",  # docuisset
                    "Vplpactsbjpl1": self._per_stem + "issemus",  # docuissmus
                    "Vplpactsbjpl2": self._per_stem + "issetis",  # docuissetis
                    "Vplpactsbjpl3": self._per_stem + "issent",  # docuissent
                }  # fmt: skip

            case 3:
                self.endings = {
                    "Vpreactindsg1": self.present,  # traho
                    "Vpreactindsg2": self._inf_stem + "is",  # trahis
                    "Vpreactindsg3": self._inf_stem + "it",  # trahit
                    "Vpreactindpl1": self._inf_stem + "imus",  # trahimus
                    "Vpreactindpl2": self._inf_stem + "itis",  # trahitis
                    "Vpreactindpl3": self._inf_stem + "unt",  # trahunt
                    "Vimpactindsg1": self._inf_stem + "ebam",  # trahebam
                    "Vimpactindsg2": self._inf_stem + "ebas",  # trahebas
                    "Vimpactindsg3": self._inf_stem + "ebat",  # trahebat
                    "Vimpactindpl1": self._inf_stem + "ebamus",  # trahebamus
                    "Vimpactindpl2": self._inf_stem + "ebatis",  # trahebatis
                    "Vimpactindpl3": self._inf_stem + "ebant",  # trahebant
                    "Vperactindsg1": self.perfect,  # traxi
                    "Vperactindsg2": self._per_stem + "isti",  # traxisti
                    "Vperactindsg3": self._per_stem + "it",  # traxit
                    "Vperactindpl1": self._per_stem + "imus",  # traximus
                    "Vperactindpl2": self._per_stem + "istis",  # traxistis
                    "Vperactindpl3": self._per_stem + "erunt",  # traxerunt
                    "Vplpactindsg1": self._per_stem + "eram",  # traxeram
                    "Vplpactindsg2": self._per_stem + "eras",  # traxeras
                    "Vplpactindsg3": self._per_stem + "erat",  # traxerat
                    "Vplpactindpl1": self._per_stem + "eramus",  # traxeramus
                    "Vplpactindpl2": self._per_stem + "eratis",  # traxeratis
                    "Vplpactindpl3": self._per_stem + "erant",  # traxerant
                    "Vpreactinf   ": self.infinitive,  # trahere
                    "Vpreactipesg2": self._inf_stem + "e",  # trahe
                    "Vpreactipepl2": self._inf_stem + "ite",  # trahite
                    "Vimpactsbjsg1": self.infinitive + "m",  # traherem
                    "Vimpactsbjsg2": self.infinitive + "s",  # traheres
                    "Vimpactsbjsg3": self.infinitive + "t",  # traheret
                    "Vimpactsbjpl1": self.infinitive + "mus",  # traheremus
                    "Vimpactsbjpl2": self.infinitive + "tis",  # traheretis
                    "Vimpactsbjpl3": self.infinitive + "nt",  # traherent
                    "Vplpactsbjsg1": self._per_stem + "issem",  # traxissem
                    "Vplpactsbjsg2": self._per_stem + "isses",  # traxisses
                    "Vplpactsbjsg3": self._per_stem + "isset",  # traxisset
                    "Vplpactsbjpl1": self._per_stem + "issemus",  # traxissemus
                    "Vplpactsbjpl2": self._per_stem + "issetis",  # traxissetis
                    "Vplpactsbjpl3": self._per_stem + "issent",  # traxissent
                }  # fmt: skip

            case 4:
                self.endings = {
                    "Vpreactindsg1": self.present,  # audio
                    "Vpreactindsg2": self._inf_stem + "is",  # audis
                    "Vpreactindsg3": self._inf_stem + "it",  # audit
                    "Vpreactindpl1": self._inf_stem + "imus",  # audimus
                    "Vpreactindpl2": self._inf_stem + "itis",  # auditis
                    "Vpreactindpl3": self._inf_stem + "iunt",  # audiunt
                    "Vimpactindsg1": self._inf_stem + "iebam",  # audiebam
                    "Vimpactindsg2": self._inf_stem + "iebas",  # audiebas
                    "Vimpactindsg3": self._inf_stem + "iebat",  # audiebat
                    "Vimpactindpl1": self._inf_stem + "iebamus",  # audiebamus
                    "Vimpactindpl2": self._inf_stem + "iebatis",  # audiebatis
                    "Vimpactindpl3": self._inf_stem + "iebant",  # audiebant
                    "Vperactindsg1": self.perfect,  # audivi
                    "Vperactindsg2": self._per_stem + "isti",  # audivisti
                    "Vperactindsg3": self._per_stem + "it",  # audivit
                    "Vperactindpl1": self._per_stem + "imus",  # audivimus
                    "Vperactindpl2": self._per_stem + "istis",  # audivistis
                    "Vperactindpl3": self._per_stem + "erunt",  # audiverunt
                    "Vplpactindsg1": self._per_stem + "eram",  # audiveram
                    "Vplpactindsg2": self._per_stem + "eras",  # audiveras
                    "Vplpactindsg3": self._per_stem + "erat",  # audiverat
                    "Vplpactindpl1": self._per_stem + "eramus",  # audiveramus
                    "Vplpactindpl2": self._per_stem + "eratis",  # audiveratis
                    "Vplpactindpl3": self._per_stem + "erant",  # audiverant
                    "Vpreactinf   ": self.infinitive,  # audire
                    "Vpreactipesg2": self._inf_stem + "i",  # audi
                    "Vpreactipepl2": self._inf_stem + "ite",  # audite
                    "Vimpactsbjsg1": self.infinitive + "m",  # audirem
                    "Vimpactsbjsg2": self.infinitive + "s",  # audires
                    "Vimpactsbjsg3": self.infinitive + "t",  # audiret
                    "Vimpactsbjpl1": self.infinitive + "mus",  # audiremus
                    "Vimpactsbjpl2": self.infinitive + "tis",  # audiretis
                    "Vimpactsbjpl3": self.infinitive + "nt",  # audirent
                    "Vplpactsbjsg1": self._per_stem + "issem",  # audivissem
                    "Vplpactsbjsg2": self._per_stem + "isses",  # audivisses
                    "Vplpactsbjsg3": self._per_stem + "isset",  # audivisset
                    "Vplpactsbjpl1": self._per_stem + "issemus",  # audivissemus
                    "Vplpactsbjpl2": self._per_stem + "issetis",  # audivissetis
                    "Vplpactsbjpl3": self._per_stem + "issent",  # audivissent
                }  # fmt: skip

            case 5:
                self.endings = {
                    "Vpreactindsg1": self.present,  # capio
                    "Vpreactindsg2": self._inf_stem + "is",  # capis
                    "Vpreactindsg3": self._inf_stem + "it",  # capit
                    "Vpreactindpl1": self._inf_stem + "imus",  # capimus
                    "Vpreactindpl2": self._inf_stem + "itis",  # capitis
                    "Vpreactindpl3": self._inf_stem + "iunt",  # capiunt
                    "Vimpactindsg1": self._inf_stem + "iebam",  # capiebam
                    "Vimpactindsg2": self._inf_stem + "iebas",  # capiebas
                    "Vimpactindsg3": self._inf_stem + "iebat",  # capiebat
                    "Vimpactindpl1": self._inf_stem + "iebamus",  # capiebamus
                    "Vimpactindpl2": self._inf_stem + "iebatis",  # capiebatis
                    "Vimpactindpl3": self._inf_stem + "iebant",  # capiebant
                    "Vperactindsg1": self.perfect,  # cepi
                    "Vperactindsg2": self._per_stem + "isti",  # cepisti
                    "Vperactindsg3": self._per_stem + "it",  # cepit
                    "Vperactindpl1": self._per_stem + "imus",  # cepimus
                    "Vperactindpl2": self._per_stem + "istis",  # cepistis
                    "Vperactindpl3": self._per_stem + "erunt",  # ceperunt
                    "Vplpactindsg1": self._per_stem + "eram",  # ceperam
                    "Vplpactindsg2": self._per_stem + "eras",  # ceperas
                    "Vplpactindsg3": self._per_stem + "erat",  # ceperat
                    "Vplpactindpl1": self._per_stem + "eramus",  # ceperamus
                    "Vplpactindpl2": self._per_stem + "eratis",  # ceperatis
                    "Vplpactindpl3": self._per_stem + "erant",  # ceperant
                    "Vpreactinf   ": self.infinitive,  # capere
                    "Vpreactipesg2": self._inf_stem + "e",  # cape
                    "Vpreactipepl2": self._inf_stem + "ite",  # capite
                    "Vimpactsbjsg1": self.infinitive + "m",  # caperem
                    "Vimpactsbjsg2": self.infinitive + "s",  # caperes
                    "Vimpactsbjsg3": self.infinitive + "t",  # caperet
                    "Vimpactsbjpl1": self.infinitive + "mus",  # caperemus
                    "Vimpactsbjpl2": self.infinitive + "tis",  # caperetis
                    "Vimpactsbjpl3": self.infinitive + "nt",  # caperent
                    "Vplpactsbjsg1": self._per_stem + "issem",  # cepissem
                    "Vplpactsbjsg2": self._per_stem + "isses",  # cepisses
                    "Vplpactsbjsg3": self._per_stem + "isset",  # cepisset
                    "Vplpactsbjpl1": self._per_stem + "issemus",  # cepissemus
                    "Vplpactsbjpl2": self._per_stem + "issetis",  # cepissetis
                    "Vplpactsbjpl3": self._per_stem + "issent",  # cepissent
                }  # fmt: skip

            case _:  # pragma: no cover
                raise ValueError(
                    f"Conjugation {self.conjugation} not recognised"
                )

        # Participles
        if self.ppp:
            self._preptc_stem: str = self.infinitive[:-2]
            self._ppp_stem: str = self.ppp[:-2]
            self.endings = self.endings | {
                "Vpreactptcmnomsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcmvocsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcmaccsg": self._preptc_stem + "ntem",  # portantem
                "Vpreactptcmgensg": self._preptc_stem + "ntis",  # portantis
                "Vpreactptcmdatsg": self._preptc_stem + "nti",  # portanti
                "Vpreactptcmablsg": self._preptc_stem + "nte",  # portante
                "Vpreactptcmnompl": self._preptc_stem + "ntes",  # portantes
                "Vpreactptcmvocpl": self._preptc_stem + "ntes",  # portantes
                "Vpreactptcmaccpl": self._preptc_stem + "ntes",  # portantes
                "Vpreactptcmgenpl": self._preptc_stem + "ntium",  # portantium
                "Vpreactptcmdatpl": self._preptc_stem + "ntibus",  # portantibus
                "Vpreactptcmablpl": self._preptc_stem + "ntibus",  # portantibus
                "Vpreactptcfnomsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcfvocsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcfaccsg": self._preptc_stem + "ntem",  # portantem
                "Vpreactptcfgensg": self._preptc_stem + "ntis",  # portantis
                "Vpreactptcfdatsg": self._preptc_stem + "nti",  # portanti
                "Vpreactptcfablsg": self._preptc_stem + "nte",  # portante
                "Vpreactptcfnompl": self._preptc_stem + "ntes",  # portantes
                "Vpreactptcfvocpl": self._preptc_stem + "ntes",  # portantes
                "Vpreactptcfaccpl": self._preptc_stem + "ntes",  # portantes
                "Vpreactptcfgenpl": self._preptc_stem + "ntium",  # portantium
                "Vpreactptcfdatpl": self._preptc_stem + "ntibus",  # portantibus
                "Vpreactptcfablpl": self._preptc_stem + "ntibus",  # portantibus
                "Vpreactptcnnomsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcnvocsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcnaccsg": self._preptc_stem + "ns",  # portans
                "Vpreactptcngensg": self._preptc_stem + "ntis",  # portantis
                "Vpreactptcndatsg": self._preptc_stem + "nti",  # portanti
                "Vpreactptcnablsg": self._preptc_stem + "nte",  # portante
                "Vpreactptcnnompl": self._preptc_stem + "ntia",  # portantia
                "Vpreactptcnvocpl": self._preptc_stem + "ntia",  # portantia
                "Vpreactptcnaccpl": self._preptc_stem + "ntia",  # portantia
                "Vpreactptcngenpl": self._preptc_stem + "ntium",  # portantium
                "Vpreactptcndatpl": self._preptc_stem + "ntibus",  # portantibus
                "Vpreactptcnablpl": self._preptc_stem + "ntibus",  # portantibus
                "Vperpasptcmnomsg": self.ppp,  # portatus
                "Vperpasptcmvocsg": self._ppp_stem + "e",  # portate
                "Vperpasptcmaccsg": self._ppp_stem + "um",  # portatum
                "Vperpasptcmgensg": self._ppp_stem + "i",  # portati
                "Vperpasptcmdatsg": self._ppp_stem + "o",  # portato
                "Vperpasptcmablsg": self._ppp_stem + "o",  # portato
                "Vperpasptcmnompl": self._ppp_stem + "i",  # portati
                "Vperpasptcmvocpl": self._ppp_stem + "i",  # portati
                "Vperpasptcmaccpl": self._ppp_stem + "os",  # portatos
                "Vperpasptcmgenpl": self._ppp_stem + "orum",  # portatorum
                "Vperpasptcmdatpl": self._ppp_stem + "is",  # portatis
                "Vperpasptcmablpl": self._ppp_stem + "is",  # portatis
                "Vperpasptcfnomsg": self._ppp_stem + "a",  # portata
                "Vperpasptcfvocsg": self._ppp_stem + "a",  # portata
                "Vperpasptcfaccsg": self._ppp_stem + "am",  # portatam
                "Vperpasptcfgensg": self._ppp_stem + "ae",  # portatae
                "Vperpasptcfdatsg": self._ppp_stem + "ae",  # portatae
                "Vperpasptcfablsg": self._ppp_stem + "a",  # portata
                "Vperpasptcfnompl": self._ppp_stem + "ae",  # portatae
                "Vperpasptcfvocpl": self._ppp_stem + "ae",  # portatae
                "Vperpasptcfaccpl": self._ppp_stem + "as",  # portatas
                "Vperpasptcfgenpl": self._ppp_stem + "arum",  # portarum
                "Vperpasptcfdatpl": self._ppp_stem + "is",  # portatis
                "Vperpasptcfablpl": self._ppp_stem + "is",  # portatis
                "Vperpasptcnnomsg": self._ppp_stem + "um",  # portatum
                "Vperpasptcnvocsg": self._ppp_stem + "um",  # portatum
                "Vperpasptcnaccsg": self._ppp_stem + "um",  # portatum
                "Vperpasptcngensg": self._ppp_stem + "i",  # portati
                "Vperpasptcndatsg": self._ppp_stem + "o",  # portato
                "Vperpasptcnablsg": self._ppp_stem + "o",  # portato
                "Vperpasptcnnompl": self._ppp_stem + "a",  # portata
                "Vperpasptcnvocpl": self._ppp_stem + "a",  # portata
                "Vperpasptcnaccpl": self._ppp_stem + "a",  # portata
                "Vperpasptcngenpl": self._ppp_stem + "orum",  # portatorum
                "Vperpasptcndatpl": self._ppp_stem + "is",  # portatis
                "Vperpasptcnablpl": self._ppp_stem + "is",  # portatis
            }  # fmt: skip

    def get(
        self,
        *,
        person: Optional[int] = None,
        number: Optional[str] = None,
        tense: str,
        voice: str,
        mood: str,
        participle_gender: Optional[str] = None,
        participle_case: Optional[str] = None,
    ) -> Ending | None:
        """Returns the ending of the verb.
        The function returns None if no ending is found.

        Parameters
        ----------
        person : Optional[int], default = None
            The person of the ending, if applicable (not participle).
        number : Optional[str], default = None
            The number of the ending, if applicable (not participle).
        tense, voice, mood : str
            The tense, voice and mood of the ending.
        participle_gender, participle_case : Optional[str], default = None
            The case and gender of the ending, if applicable (participle).

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
        ...     number="singular",
        ...     tense="present",
        ...     voice="active",
        ...     mood="indicative",
        ... )
        'celo'

        Note that all arguments of get are keyword-only.

        >>> foo.get(
        ...     number="singular",
        ...     tense="perfect",
        ...     voice="passive",
        ...     mood="participle",
        ...     participle_gender="masculine",
        ...     participle_case="nominative",
        ... )
        'celatus'

        Similar with participle endings.
        """
        short_tense: str
        short_voice: str
        short_mood: str
        short_number: str

        if tense not in TENSE_SHORTHAND:
            raise InvalidInputError(f"Invalid tense: '{tense}'")

        if voice not in VOICE_SHORTHAND:
            raise InvalidInputError(f"Invalid voice: '{voice}'")

        if mood == "participle":
            if person:
                raise InvalidInputError(
                    f"Participle cannot have a person (person '{person}')"
                )

            if not participle_case:
                raise InvalidInputError("Case not given")

            if not participle_gender:
                raise InvalidInputError("Gender not given")

            if not number:
                raise InvalidInputError("Number not given")

            if participle_case not in CASE_SHORTHAND:
                raise InvalidInputError(f"Invalid case: '{participle_case}'")

            if participle_gender not in GENDER_SHORTHAND:
                raise InvalidInputError(
                    f"Invalid gender: '{participle_gender}'"
                )

            if number not in NUMBER_SHORTHAND:
                raise InvalidInputError(f"Invalid number: '{number}'")

            short_tense = TENSE_SHORTHAND[tense]
            short_voice = VOICE_SHORTHAND[voice]
            short_number = NUMBER_SHORTHAND[number]
            short_gender: str = GENDER_SHORTHAND[participle_gender]
            short_case: str = CASE_SHORTHAND[participle_case]

            return self.endings.get(
                f"V{short_tense}{short_voice}ptc{short_gender}{short_case}{short_number}"
            )

        if mood not in MOOD_SHORTHAND:
            raise InvalidInputError(f"Invalid mood: '{mood}'")

        if number and number not in NUMBER_SHORTHAND:
            raise InvalidInputError(f"Invalid number: '{number}'")

        if person and person not in {1, 2, 3}:
            raise InvalidInputError(f"Invalid person: '{person}'")

        short_tense = TENSE_SHORTHAND[tense]
        short_voice = VOICE_SHORTHAND[voice]
        short_mood = MOOD_SHORTHAND[mood]
        if number:
            short_number = NUMBER_SHORTHAND[number]

        if mood == "infinitive":
            return self.endings.get(f"V{short_tense}{short_voice}inf   ")
        return self.endings.get(
            f"V{short_tense}{short_voice}{short_mood}{short_number}{person}"
        )

    @staticmethod
    def _create_namespace(key: str) -> EndingComponents:
        output: EndingComponents
        if len(key) == 13:
            output = EndingComponents(
                tense=key_from_value(TENSE_SHORTHAND, key[1:4]),
                voice=key_from_value(VOICE_SHORTHAND, key[4:7]),
                mood=key_from_value(MOOD_SHORTHAND, key[7:10]),
                number=key_from_value(NUMBER_SHORTHAND, key[10:12]),
                person=PERSON_SHORTHAND[int(key[12])],
            )
            output.string = f"{output.tense} {output.voice} {output.mood} {output.number} {output.person}"
            return output
        elif len(key) == 16 and key[7:10] == "ptc":
            output = EndingComponents(
                tense=key_from_value(TENSE_SHORTHAND, key[1:4]),
                voice=key_from_value(VOICE_SHORTHAND, key[4:7]),
                mood="participle",
                gender=key_from_value(GENDER_SHORTHAND, key[10]),
                case=key_from_value(CASE_SHORTHAND, key[11:14]),
                number=key_from_value(NUMBER_SHORTHAND, key[14:16]),
            )
            output.string = f"{output.tense} {output.voice} participle {output.gender} {output.case} {output.number}"
            return output
        else:  # pragma: no cover # this should never happen
            raise InvalidInputError(f"Key '{key}' is invalid")

    def __repr__(self) -> str:
        return f"Verb({self.present}, {self.infinitive}, {self.perfect}, {self.ppp}, {self.meaning})"

    def __str__(self) -> str:
        if self.ppp:
            return f"{self.meaning}: {self.present}, {self.infinitive}, {self.perfect}, {self.ppp}"
        return f"{self.meaning}: {self.present}, {self.infinitive}, {self.perfect}"
