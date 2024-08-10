#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""endings.py
Representations of Latin words with their endings calculated.
"""

from abc import ABC, abstractmethod
from functools import total_ordering
from io import StringIO
from random import choice
from types import SimpleNamespace
from typing import Any, Final, Literal, Optional

from frozendict import deepfreeze, frozendict

from . import edge_cases
from .custom_exceptions import InvalidInputError, NoEndingError
from .misc import Ending, Endings, Meaning, MultipleEndings, key_from_value

NUMBER_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "singular": "sg",
    "plural": "pl",
})  # fmt: skip

TENSE_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "present": "pre",
    "imperfect": "imp",
    "future": "fut",
    "perfect": "per",
    "pluperfect": "plp",
    # "future perfect": "fpr",
})  # fmt: skip

VOICE_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "active": "act",
    "passive": "pas",
})  # fmt: skip

MOOD_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "indicative": "ind",
    "infinitive": "inf",
    "imperative": "ipe",
    "subjunctive": "sbj",
    "participle": "ptc",
})  # fmt: skip

CASE_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "nominative": "nom",
    "vocative": "voc",
    "accusative": "acc",
    "genitive": "gen",
    "dative": "dat",
    "ablative": "abl",
})  # fmt: skip

GENDER_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "masculine": "m",
    "feminine": "f",
    "neuter": "n",
})  # fmt: skip

DEGREE_SHORTHAND: Final[frozendict[str, str]] = frozendict({
    "positive": "pos",
    "comparative": "cmp",
    "superlative": "spr",
})  # fmt: skip

PERSON_SHORTHAND: Final[frozendict[int, str]] = frozendict({
    1: "1st person",
    2: "2nd person",
    3: "3rd person",
})  # fmt: skip


@total_ordering
class _Word(ABC):
    """Representation of an word.
    This class is not intended to be used by the user. Rather, all of the
    other classes inherit from this class.

    Attributes
    ----------
    endings : Ending
    _first : str
        The first principal part. Used so that the word classes can be
        alphabetically sorted.
    """

    def __init__(self) -> None:
        self.endings: Endings
        self._first: str
        self._unique_endings: set[Ending] = set()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _Word):
            return NotImplemented
        return self.endings == other.endings

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, _Word):
            return NotImplemented
        return self._first < other._first

    def __getitem__(self, key: str) -> Ending:
        return self.endings[key]

    def _find_unique_endings(self) -> None:
        self._unique_endings = set(self.endings.values())

    def pick(self) -> Ending:
        """Returns a random ending from the endings.
        Note that this method chooses from unique endings, so that the same
        endings (e.g. puella is both nominative and ablative singular) do
        not skew the results.

        Returns
        -------
        Ending
            The ending chosen.

        Raises
        ------
        ValueError
            If the _unique_endings set has not been created. This error
            should never occur.
        """
        if self._unique_endings == set():
            raise ValueError
        return choice(tuple(self._unique_endings))

    def find(self, form: str) -> list[SimpleNamespace]:
        """Finds the accidol properties that match the given form.

        Attributes
        ----------
        form : str
            The form to search for.

        Returns
        -------
        list[SimpleNamespace]
            The list of SimpleNamespace objects that represent the endings 
            that match the given form.
        """  # fmt: skip

        results = []
        for key, value in self.endings.items():
            if isinstance(value, MultipleEndings):
                if form in value.get_all():
                    results.append(self._create_namespace(key))
            elif value == form:
                results.append(self._create_namespace(key))
        return results

    # Force implementation of these methods
    @abstractmethod
    def get(self, *args: Any, **kwargs: Any) -> Ending:
        pass

    @staticmethod
    @abstractmethod
    def _create_namespace(key: str) -> SimpleNamespace:
        pass


@total_ordering
class RegularWord(_Word):
    """Representation of a Latin word that is undeclinable.

    Attributes
    ----------
    word : str
    meaning : Meaning

    Examples
    --------
    >>> foo = RegularWord(word="sed", meaning="but")
    >>> foo.endings
    {"": "sed"}
    """  # fmt: skip

    def __init__(self, word: str, meaning: Meaning):
        self.word: str = word
        self.meaning: Meaning = meaning
        self.endings: Endings = frozendict({"": self.word})
        self._find_unique_endings()

    def get(self) -> str:
        """Returns the word.

        Returns
        -------
        str
            The word.
        
        Examples
        --------
        >>> foo = RegularWord(word="sed", meaning="but")
        >>> foo.get()
        "sed"
        """  # fmt: skip
        return self.word

    @staticmethod
    def _create_namespace(key: str) -> SimpleNamespace:
        return NotImplemented

    def __repr__(self) -> str:
        return f"RegularWord({self.word}, {self.meaning})"


@total_ordering
class LearningVerb(_Word):
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
    >>> foo = LearningVerb(present="celo", infinitive="celare", \
    ...       perfect="celavi", ppp="celatus", \
    ...       meaning="hide")
    >>> foo.endings
    {"Vpreactindsg1": "celo", "Vpreactindsg2": "celas", ...}

    Note that all arguments of LearningVerb are keyword-only.
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
        """Initalises LearningVerb and determines the conjugation and
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
            raise InvalidInputError(f"Present {self.present} is not valid")

        if self.perfect[-1:] != "i":
            raise InvalidInputError(f"Perfect '{self.perfect}' is not valid")

        # Conjugation edge cases
        if irregular_endings := edge_cases.find_irregular_endings(
            self.present
        ):
            self.endings = irregular_endings
            self.conjugation = 0
            return
        elif edge_cases.check_io_verb(self.present):
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
                f"Infinitive '{self.infinitive}' is not valid"
            )

        self._pre_stem: str = self.present[:-1]
        self._inf_stem: str = self.infinitive[:-3]
        self._per_stem: str = self.perfect[:-1]

        match self.conjugation:
            case 1:
                self.endings = frozendict({
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
                })  # fmt: skip

            case 2:
                self.endings = frozendict({
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
                })  # fmt: skip

            case 3:
                self.endings = frozendict({
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
                })  # fmt: skip

            case 4:
                self.endings = frozendict({
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
                })  # fmt: skip

            case 5:
                self.endings = frozendict({
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
                })  # fmt: skip

            # case _:
            #     raise ValueError(f"Conjugation {self.conjugation} not recognised")

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

        self._endings = deepfreeze(self.endings)
        self._find_unique_endings()

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
    ) -> Ending:
        """Returns the ending of the verb.
        The function raises an error if the ending cannot be found, as it
        is intended for the method to always find an ending.

        Parameters
        ----------
        person : Optional[int], default = None
            The person of the ending, if applicable (not participle).
        number : Optional[str], default = None
            The number of the ending, if applicable (not participle).
        tense, voice, mood : str
            The tense, voice and mood of the ending.
        participle_gender, participle_case : Optional[str]
            The case and gender of the ending, if applicable (participle).

        Returns
        -------
        Ending
            The ending found

        Raises
        ------
        InvalidInputError
            If the inputs are not valid. Note that the inputs must be the
            full words, e.g. 'singular', 'plural', 'masculine', 'feminine'.
        NoEndingError
            If the ending cannot be found.
        

        Examples
        --------
        >>> foo = LearningVerb(present="celo", infinitive="celare", \
        ...                    perfect="celavi", ppp="celatus", \
        ...                    meaning="hide")
        >>> foo.get(person=1, number="singular", tense="present", \
        ...         voice="active", mood="indicative")
        "celo"

        Note that all arguments of get are keyword-only.

        >>> foo.get(number="singular", tense="perfect", voice="passive", \
        ...         mood="participle", participle_gender="masculine", \
        ...         participle_case="nominative")
        "celatus"

        Similar with participle endings.
        """
        short_tense: str
        short_voice: str
        short_mood: str
        short_number: str

        if mood == "participle":
            try:
                short_tense = TENSE_SHORTHAND[tense]
                short_voice = VOICE_SHORTHAND[voice]
                if number:
                    short_number = NUMBER_SHORTHAND[number]
                else:
                    raise InvalidInputError("Number not given")
                if participle_case and participle_gender:
                    short_gender: str = GENDER_SHORTHAND[participle_gender]
                    short_case: str = CASE_SHORTHAND[participle_case]
                else:
                    raise InvalidInputError("Gender or case not given")
            except KeyError:
                raise InvalidInputError(
                    f"Tense '{tense}', voice '{voice}', gender '{participle_gender}', case '{participle_case}', or number '{number}' not recognised"
                )

            if person:
                raise InvalidInputError(
                    f"Participle cannot have a person (person '{person}')"
                )

            try:
                return self.endings[
                    f"V{short_tense}{short_voice}ptc{short_gender}{short_case}{short_number}"
                ]
            except KeyError:
                raise NoEndingError(
                    f"No ending found for {participle_case} {number} {participle_gender} {tense} {voice} participle"
                )

        try:
            short_tense = TENSE_SHORTHAND[tense]
            short_voice = VOICE_SHORTHAND[voice]
            short_mood = MOOD_SHORTHAND[mood]
            if number:
                short_number = NUMBER_SHORTHAND[number]
        except KeyError:
            raise InvalidInputError(
                f"Tense '{tense}', voice '{voice}', mood '{mood}', or number '{number}' not recognised"
            )

        if person and person not in {1, 2, 3}:
            raise InvalidInputError(f"Person '{person}' not recognised")

        try:
            if mood == "infinitive":
                return self.endings[f"V{short_tense}{short_voice}inf   "]
            return self.endings[
                f"V{short_tense}{short_voice}{short_mood}{short_number}{person}"
            ]
        except KeyError:
            raise NoEndingError(
                f"No ending found for {person} {number} {tense} {voice} {mood}"
            )

    @staticmethod
    def _create_namespace(key: str) -> SimpleNamespace:
        output: SimpleNamespace = SimpleNamespace(
            tense=key_from_value(TENSE_SHORTHAND, key[1:4]),
            voice=key_from_value(VOICE_SHORTHAND, key[4:7]),
            mood=key_from_value(MOOD_SHORTHAND, key[7:10]),
            number=key_from_value(NUMBER_SHORTHAND, key[10:12]),
            person=PERSON_SHORTHAND[int(key[12])],
        )
        output.string = f"{output.tense} {output.voice} {output.mood} {output.number} {output.person}"
        return output

    def __repr__(self) -> str:
        return f"LearningVerb({self.present}, {self.infinitive}, {self.perfect}, {self.ppp}, {self.meaning})"

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(
            f"{self.meaning}: {self.present}, {self.infinitive}, {self.perfect}, {self.ppp} ({self.conjugation})\n\n"
        )

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()


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
    """  # fmt: skip

    def __init__(
        self,
        *,
        nominative: str,
        genitive: str,
        gender: str,
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

        if gender not in GENDER_SHORTHAND:
            raise InvalidInputError(f"Gender '{gender}' not recognised")
        self.gender: str = gender

        self.nominative: str = nominative
        self.genitive: str = genitive
        self.meaning: Meaning = meaning
        self.plurale_tantum: bool = False

        self._first = self.nominative
        self.declension: Literal[0, 1, 2, 3, 4, 5]
        self._stem: str

        if self.nominative in edge_cases.IRREGULAR_NOUNS:
            self.endings = edge_cases.IRREGULAR_NOUNS[nominative]
            self.declension = 0
            return

        # The ordering of this is strange because e.g. ending -ei ends in 'i' as well as 'ei'
        # so 5th declension check must come before 2nd declension check, etc.
        if self.genitive[-2:] == "ei":
            self.declension = 5
            self._stem = self.genitive[:-2]  # diei > di-
        elif self.genitive[-2:] == "um":
            self.declension = 3
            self._stem = self.genitive[:-2]  # canum -> can-
            self.plurale_tantum = True
        elif self.genitive[-2:] == "ae":
            self.declension = 1
            self._stem = self.genitive[:-2]  # puellae -> puell-
        elif self.genitive[-1:] == "i":
            self.declension = 2
            self._stem = self.genitive[:-1]  # servi -> serv-
        elif self.genitive[-2:] == "is":
            self.declension = 3
            self._stem = self.genitive[:-2]  # canis -> can-
        elif genitive[-2:] == "us":
            self.declension = 4
            self._stem = self.genitive[:-2]  # manus -> man-

        elif self.genitive[-4:] == "uum":
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
        elif self.genitive[-4:] == "erum":
            self.declension = 5
            self._stem = self.genitive[:-4]  # dierum > di-
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

            case _:
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
                temp_endings["Ndatpl"] = self._stem + "ua"  # cornua
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

        self.endings = deepfreeze(temp_endings)
        self._find_unique_endings()

    def get(self, *, case: str, number: str) -> Ending:
        """Returns the ending of the noun.
        The function raises an error if the ending cannot be found, as it
        is intended for the method to always find an ending.

        Parameters
        ----------
        case, number : str

        Returns
        -------
        Ending
            The ending found.

        Raises
        ------
        InvalidInputError
            If the input is invalid.
        NoEndingError
            If an ending cannot be found.

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

        try:
            return self.endings[f"N{short_case}{short_number}"]
        except KeyError:
            raise NoEndingError(
                f"No ending found for case '{case}' and number '{number}'"
            )

    @staticmethod
    def _create_namespace(key: str) -> SimpleNamespace:
        output: SimpleNamespace = SimpleNamespace(
            case=key_from_value(CASE_SHORTHAND, key[1:4]),
            number=key_from_value(NUMBER_SHORTHAND, key[4:6]),
        )
        output.string = f"{output.case} {output.number}"
        return output

    def __repr__(self) -> str:
        return f"Noun({self.nominative}, {self.genitive}, {GENDER_SHORTHAND[self.gender]}, {self.meaning})"

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(
            f"{self.meaning}: {self.nominative}, {self.genitive} ({self.declension})"
        )

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()


@total_ordering
class Adjective(_Word):
    """Representaiton of a Latin adjective with endings.

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

        if self._mascnom in edge_cases.IRREGULAR_COMPARATIVES:
            self.irregular_flag = True
            irregular_data = edge_cases.IRREGULAR_COMPARATIVES[self._mascnom]

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

                if self._mascnom not in edge_cases.IRREGULAR_COMPARATIVES:
                    self._cmp_stem = self._pos_stem + "ior"  # car- -> carior-
                    if self._mascnom[:2] == "er":
                        self._spr_stem = (
                            self._mascnom + "rim"  # miser- -> miserrim-
                        )
                    elif self._mascnom in edge_cases.LIS_ADJECTIVES:
                        self._spr_stem = (
                            self._pos_stem + "lim"  # facil- -> facillim-
                        )
                    else:
                        self._spr_stem = (
                            self._pos_stem + "issim"  # car- -> carissim-
                        )

                self.endings = frozendict({
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
                })  # fmt: skip

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
                            if self._mascnom[:2] == "er":
                                self._spr_stem = (
                                    self._mascnom + "rim"
                                )  # miser- -> miserrim-
                            elif self._mascnom in edge_cases.LIS_ADJECTIVES:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "lim"  # facil- -> facillim-
                                )
                            else:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "issim"  # ingent- -> ingentissim-
                                )

                        self.endings = frozendict({
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
                        })  # fmt: skip

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
                            if self._mascnom[:2] == "er":
                                self._spr_stem = (
                                    self._mascnom
                                    + "rim"  # miser- -> miserrim-
                                )
                            elif self._mascnom in edge_cases.LIS_ADJECTIVES:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "lim"  # facil- -> facillim-
                                )
                            else:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "issim"  # fort- -> fortissim-
                                )

                        self.endings = frozendict({
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
                        })  # fmt: skip

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
                            elif self._mascnom in edge_cases.LIS_ADJECTIVES:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "lim"  # facil- -> facillim-
                                )
                            else:
                                self._spr_stem = (
                                    self._pos_stem
                                    + "issim"  # levis -> levissim-
                                )

                        self.endings = frozendict({
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
                        })  # fmt: skip

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

        self._endings = deepfreeze(self.endings)
        self._find_unique_endings()

    def get(
        self,
        *,
        degree: str,
        gender: Optional[str] = None,
        case: Optional[str] = None,
        number: Optional[str] = None,
        adverb: bool = False,
    ) -> Ending:
        """Returns the ending of the adjective.
        The function raises an error if the ending cannot be found, as it
        is intended for the method to always find an ending.

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

        Raises
        ------
        InvalidInputError
            If the input is invalid.
        NoEndingError
            If an ending cannot be found.
        
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

            try:
                return self.endings[f"D{short_degree}"]
            except KeyError:
                raise NoEndingError(f"No ending found for degree '{degree}'")

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

        try:
            return self.endings[
                f"A{short_degree}{short_gender}{short_case}{short_number}"
            ]
        except KeyError:
            raise NoEndingError(
                f"No ending found for degree '{degree}', gender '{gender}', case '{case}' and number '{number}'"
            )

    @staticmethod
    def _create_namespace(key: str) -> SimpleNamespace:
        output: SimpleNamespace = SimpleNamespace(
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
        output: StringIO = StringIO()
        output.write(f"{self.meaning}: {', '.join(self._principal_parts)}\n")
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()

    def __repr__(self) -> str:
        return f"Adjective({', '.join(self._principal_parts)}, {self.termination}, {self.declension}, {self.meaning})"


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
            self.endings = edge_cases.PRONOUNS[pronoun]
        except KeyError:
            raise InvalidInputError(f"Pronoun '{pronoun}' not recognised")

        self.pronoun: str = pronoun
        self._first = self.pronoun
        self.meaning: Meaning = meaning

        self._mascnom: Ending = self.endings["Pmnomsg"]
        self._femnom: Ending = self.endings["Pfnomsg"]
        self._neutnom: Ending = self.endings["Pnnomsg"]

        self._endings = deepfreeze(self.endings)
        self._find_unique_endings()

    def get(self, *, gender: str, case: str, number: str) -> Ending:
        """Returns the ending of the pronoun.
        The function raises an error if an ending cannot be found, as it
        is intended for the method to always find an ending.

        Parameters
        ----------
        gender, case, number : str

        Returns
        -------
        Ending
            The ending found.

        Raises
        ------
        InvalidInputError
            If the input is invalid.
        NoEndingError
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

        try:
            return self.endings[f"P{short_gender}{short_case}{short_number}"]
        except KeyError:
            raise NoEndingError(
                f"No ending found for gender '{gender}', case '{case}' and number '{number}'"
            )

    @staticmethod
    def _create_namespace(key: str) -> SimpleNamespace:
        output: SimpleNamespace = SimpleNamespace(
            gender=key_from_value(GENDER_SHORTHAND, key[1]),
            case=key_from_value(CASE_SHORTHAND, key[2:5]),
            number=key_from_value(NUMBER_SHORTHAND, key[5:7]),
        )
        output.string = f"{output.case} {output.number} {output.gender}"
        return output

    def __repr__(self) -> str:
        return f"Pronoun({self.pronoun}, {self.meaning})"

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(
            f"{self.meaning}: {self._mascnom}, {self._femnom}, {self._neutnom}\n"
        )
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()
