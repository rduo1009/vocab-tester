from dataclasses import dataclass
from functools import total_ordering
from io import StringIO
from typing import Optional

from . import edge_cases
from .custom_exceptions import InvalidInputError, NoMeaningError
from .misc import Meaning, Ending, Endings

NUMBER_SHORTHAND: dict[str, str] = {
    "singular": "sg",
    "plural": "pl",
}

TENSE_SHORTHAND: dict[str, str] = {
    "present": "pre",
    "imperfect": "imp",
    "future": "fut",
    "perfect": "per",
    "pluperfect": "plp",
    "future perfect": "fpr",
}

VOICE_SHORTHAND: dict[str, str] = {
    "active": "act",
    "passive": "pas",
}

MOOD_SHORTHAND: dict[str, str] = {
    "indicative": "ind",
    "infinitive": "inf",
    "imperative": "ipe",
    "subjunctive": "sbj",
    "participle": "ptc",
}

CASE_SHORTHAND: dict[str, str] = {
    "nominative": "nom",
    "vocative": "voc",
    "accusative": "acc",
    "genitive": "gen",
    "dative": "dat",
    "ablative": "abl",
}

GENDER_SHORTHAND: dict[str, str] = {
    "masculine": "m",
    "feminine": "f",
    "neuter": "n",
}

DEGREE_SHORTHAND: dict[str, str] = {
    "positive": "pos",
    "comparative": "cmp",
    "superlative": "spr",
}


@total_ordering
class Word:
    def __init__(self) -> None:
        self.endings: Endings
        self.first: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Word):
            return NotImplemented
        return self.endings == other.endings

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Word):
            return NotImplemented
        return self.first < other.first  # type: ignore

    def __hash__(self) -> int:
        return hash(self.endings)


@dataclass
class BasicWord(Word):
    word: str
    meaning: Meaning

    def __post_init__(self) -> None:
        self.endings: Endings = {"": self.word}

    def get(self) -> str:
        return self.word


@total_ordering
class LearningVerb(Word):
    def __init__(
        self,
        *,
        present: str,
        infinitive: str,
        perfect: str,
        ppp: str = "",
        meaning: Meaning,
    ) -> None:
        super().__init__()
        self.present: str = present
        self.infinitive: str = infinitive
        self.perfect: str = perfect
        self.ppp: str = ppp
        self.meaning: Meaning = meaning

        self.first = self.present
        self.conjugation: int

        # Conjugation edge cases
        if irregular_endings := edge_cases.find_irregular_endings(self.present):
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
            raise InvalidInputError(f"Infinitive '{self.infinitive}' is not valid")

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
                }

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
                }

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
                }

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
                }

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
                }

            # case _:
            #     raise ValueError(f"Conjugation {self.conjugation} not recognised")

        # Participles
        if self.ppp:
            self.endings.update(self._participle_endings(self.ppp, self.infinitive))

    def _participle_endings(self, ppp: str, infinitive: str) -> Endings:
        self._preptc_stem: str = infinitive[:-2]
        self._ppp_stem: str = ppp[:-2]
        return {
                "Vpreactptcmnomsg": self._preptc_stem + "ns",
                "Vpreactptcmvocsg": self._preptc_stem + "ns",
                "Vpreactptcmaccsg": self._preptc_stem + "ntem",
                "Vpreactptcmgensg": self._preptc_stem + "ntis",
                "Vpreactptcmdatsg": self._preptc_stem + "nti",
                "Vpreactptcmablsg": self._preptc_stem + "nte",
                "Vpreactptcmnompl": self._preptc_stem + "ntes",
                "Vpreactptcmvocpl": self._preptc_stem + "ntes",
                "Vpreactptcmaccpl": self._preptc_stem + "ntes",
                "Vpreactptcmgenpl": self._preptc_stem + "ntium",
                "Vpreactptcmdatpl": self._preptc_stem + "ntibus",
                "Vpreactptcmablpl": self._preptc_stem + "ntibus",
                "Vpreactptcfnomsg": self._preptc_stem + "ns",
                "Vpreactptcfvocsg": self._preptc_stem + "ns",
                "Vpreactptcfaccsg": self._preptc_stem + "ntem",
                "Vpreactptcfgensg": self._preptc_stem + "ntis",
                "Vpreactptcfdatsg": self._preptc_stem + "nti",
                "Vpreactptcfablsg": self._preptc_stem + "nte",
                "Vpreactptcfnompl": self._preptc_stem + "ntes",
                "Vpreactptcfvocpl": self._preptc_stem + "ntes",
                "Vpreactptcfaccpl": self._preptc_stem + "ntes",
                "Vpreactptcfgenpl": self._preptc_stem + "ntium",
                "Vpreactptcfdatpl": self._preptc_stem + "ntibus",
                "Vpreactptcfablpl": self._preptc_stem + "ntibus",
                "Vpreactptcnnomsg": self._preptc_stem + "ns",
                "Vpreactptcnvocsg": self._preptc_stem + "ns",
                "Vpreactptcnaccsg": self._preptc_stem + "ns",
                "Vpreactptcngensg": self._preptc_stem + "ntis",
                "Vpreactptcndatsg": self._preptc_stem + "nti",
                "Vpreactptcnablsg": self._preptc_stem + "nte",
                "Vpreactptcnnompl": self._preptc_stem + "ntia",
                "Vpreactptcnvocpl": self._preptc_stem + "ntia",
                "Vpreactptcnaccpl": self._preptc_stem + "ntia",
                "Vpreactptcngenpl": self._preptc_stem + "ntium",
                "Vpreactptcndatpl": self._preptc_stem + "ntibus",
                "Vpreactptcnablpl": self._preptc_stem + "ntibus",
                "Vperpasptcmnomsg": self.ppp,
                "Vperpasptcmvocsg": self._ppp_stem + "e",
                "Vperpasptcmaccsg": self._ppp_stem + "um",
                "Vperpasptcmgensg": self._ppp_stem + "i",
                "Vperpasptcmdatsg": self._ppp_stem + "o",
                "Vperpasptcmablsg": self._ppp_stem + "o",
                "Vperpasptcmnompl": self._ppp_stem + "i",
                "Vperpasptcmvocpl": self._ppp_stem + "i",
                "Vperpasptcmaccpl": self._ppp_stem + "os",
                "Vperpasptcmgenpl": self._ppp_stem + "orum",
                "Vperpasptcmdatpl": self._ppp_stem + "is",
                "Vperpasptcmablpl": self._ppp_stem + "is",
                "Vperpasptcfnomsg": self._ppp_stem + "a",
                "Vperpasptcfvocsg": self._ppp_stem + "a",
                "Vperpasptcfaccsg": self._ppp_stem + "am",
                "Vperpasptcfgensg": self._ppp_stem + "ae",
                "Vperpasptcfdatsg": self._ppp_stem + "ae",
                "Vperpasptcfablsg": self._ppp_stem + "a",
                "Vperpasptcfnompl": self._ppp_stem + "ae",
                "Vperpasptcfvocpl": self._ppp_stem + "ae",
                "Vperpasptcfaccpl": self._ppp_stem + "as",
                "Vperpasptcfgenpl": self._ppp_stem + "arum",
                "Vperpasptcfdatpl": self._ppp_stem + "is",
                "Vperpasptcfablpl": self._ppp_stem + "is",
                "Vperpasptcnnomsg": self._ppp_stem + "um",
                "Vperpasptcnvocsg": self._ppp_stem + "um",
                "Vperpasptcnaccsg": self._ppp_stem + "um",
                "Vperpasptcngensg": self._ppp_stem + "i",
                "Vperpasptcndatsg": self._ppp_stem + "o",
                "Vperpasptcnablsg": self._ppp_stem + "o",
                "Vperpasptcnnompl": self._ppp_stem + "a",
                "Vperpasptcnvocpl": self._ppp_stem + "a",
                "Vperpasptcnaccpl": self._ppp_stem + "a",
                "Vperpasptcngenpl": self._ppp_stem + "orum",
                "Vperpasptcndatpl": self._ppp_stem + "is",
                "Vperpasptcnablpl": self._ppp_stem + "is",
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
    ) -> Ending:
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
                raise NoMeaningError(
                    f"No ending found for {participle_case} {number} {participle_gender} {tense} {voice} participle"
                )

        else:
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
                raise NoMeaningError(
                    f"No ending found for {person} {number} {tense} {voice} {mood}"
                )

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
class Noun(Word):
    def __init__(
        self,
        *,
        nominative: str,
        genitive: str,
        gender: str,
        meaning: Meaning,
    ) -> None:
        super().__init__()

        self.gender: str
        if gender not in {"m", "f", "n"}:
            if gender not in {"masculine", "feminine", "neuter"}:
                raise InvalidInputError(f"Gender '{gender}' not recognised")
            self.gender = GENDER_SHORTHAND[gender]
        else:
            self.gender = gender

        self.nom: str = nominative
        self.gen: str = genitive
        self.meaning: Meaning = meaning
        self.plurale_tantum: bool = False

        self.first = self.nom
        self.declension: int
        self.stem: str

        if self.nom in edge_cases.IRREGULAR_NOUNS:
            self.endings = edge_cases.IRREGULAR_NOUNS[nominative]
            self.declension = 0
            return

        # The ordering of this is strange because e.g. ending -ei ends in 'i' as well as 'ei'
        # so 5th declension check must come before 2nd declension check, etc.

        DECLENSION_MAP = {
            "ei": (5, -2),
            "ae": (1, -2),
            "i": (2, -1),
            "is": (3, -2),
            "us": (4, -2),
            "uum": (4, -3, True),
            "arum": (1, -4, True),
            "orum": (2, -4, True),
            "erum": (5, -4, True),
            "um": (3, -2, True),
        }

        for ending, (declension, stem_slice, *plurale_tantum) in DECLENSION_MAP.items():
            if genitive.endswith(ending):
                self.declension = declension
                self.stem = self.gen[:stem_slice]
                self.plurale_tantum = bool(plurale_tantum)
                break
        else:
            raise InvalidInputError(f"Genitive form '{self.gen}' is not valid")

        match self.declension:
            case 1:
                self.endings = {
                    "Nnomsg": self.nom,  # puella
                    "Nvocsg": self.nom,  # puella
                    "Naccsg": self.stem + "am",  # puellam
                    "Ngensg": self.gen,  # puellae
                    "Ndatsg": self.stem + "ae",  # puellae
                    "Nablsg": self.stem + "a",  # puella
                    "Nnompl": self.stem + "ae",  # puellae
                    "Nvocpl": self.stem + "ae",  # puellae
                    "Naccpl": self.stem + "as",  # puellas
                    "Ngenpl": self.stem + "arum",  # puellarum
                    "Ndatpl": self.stem + "is",  # puellis
                    "Nablpl": self.stem + "is",  # puellis
                }

            case 2:
                self.endings = {
                    "Nnomsg": self.nom,  # servus
                    "Nvocsg": self.nom
                    if self.nom[-2:] == "er"
                    else self.stem + "e",  # serve
                    "Naccsg": self.stem + "um",  # servum
                    "Ngensg": self.gen,  # servi
                    "Ndatsg": self.stem + "o",  # servo
                    "Nablsg": self.stem + "o",  # servo
                    "Nnompl": self.stem + "i",  # servi
                    "Nvocpl": self.stem + "i",  # servi
                    "Naccpl": self.stem + "os",  # servos
                    "Ngenpl": self.stem + "orum",  # servorum
                    "Ndatpl": self.stem + "is",  # servis
                    "Nablpl": self.stem + "is",  # servis
                }

            case 3:
                self.endings = {
                    "Nnomsg": self.nom,  # mercator
                    "Nvocsg": self.nom,  # mercator
                    "Naccsg": self.stem + "em",  # mercatorem
                    "Ngensg": self.gen,  # mercatoris
                    "Ndatsg": self.stem + "i",  # mercatori
                    "Nablsg": self.stem + "e",  # mercatore
                    "Nnompl": self.stem + "es",  # mercatores
                    "Nvocpl": self.stem + "es",  # mercatores
                    "Naccpl": self.stem + "es",  # mercatores
                    "Ngenpl": self.stem + "um",  # mercatorum
                    "Ndatpl": self.stem + "ibus",  # mercatoribus
                    "Nablpl": self.stem + "ibus",  # mercatoribus
                }

            case 4:
                self.endings = {
                    "Nnomsg": self.nom,  # manus
                    "Nvocsg": self.nom,  # manus
                    "Naccsg": self.stem + "um",  # manum
                    "Ngensg": self.stem + "us",  # manus
                    "Ndatsg": self.stem + "ui",  # manui
                    "Nablsg": self.stem + "u",  # manu
                    "Nnompl": self.stem + "us",  # manus
                    "Nvocpl": self.stem + "us",  # manus
                    "Naccpl": self.stem + "us",  # manus
                    "Ngenpl": self.stem + "uum",  # manuum
                    "Ndatpl": self.stem + "ibus",  # manibus
                    "Nablpl": self.stem + "ibus",  # manibus
                }

            case 5:
                self.endings = {
                    "Nnomsg": self.nom,  # res
                    "Nvocsg": self.nom,  # res
                    "Naccsg": self.stem + "em",  # rem
                    "Ngensg": self.stem + "ei",  # rei
                    "Ndatsg": self.stem + "ei",  # rei
                    "Nablsg": self.stem + "e",  # re
                    "Nnompl": self.stem + "es",  # res
                    "Nvocpl": self.stem + "es",  # res
                    "Naccpl": self.stem + "es",  # res
                    "Ngenpl": self.stem + "erum",  # rerum
                    "Ndatpl": self.stem + "ebus",  # rebus
                    "Nablpl": self.stem + "ebus",  # rebus
                }

            case _:
                raise ValueError(f"Declension {self.declension} not recognised")

        if self.gender == "n":
            self.endings["Naccsg"] = self.nom
            self.endings["Nvocsg"] = self.nom

            if self.declension == 4:
                self.endings["Nnompl"] = self.stem + "ua"  # cornua
                self.endings["Naccpl"] = self.stem + "ua"  # cornua
                self.endings["Nvocpl"] = self.stem + "ua"  # cornua
                self.endings["Ndatpl"] = self.stem + "ua"  # cornua
                return
            elif self.declension == 5:
                raise InvalidInputError(
                    f"Fifth declension nouns cannot be neuter (noun '{self.nom}')"
                )

            # For the other declensions
            self.endings["Nnompl"] = self.stem + "a"
            self.endings["Naccpl"] = self.stem + "a"
            self.endings["Nvocpl"] = self.stem + "a"

        if self.plurale_tantum:
            self.endings = {
                k: v for k, v in self.endings.items() if not k.endswith("sg")
            }

    def get(self, *, case: str, number: str) -> Ending:
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
            raise NoMeaningError(
                f"No ending found for case '{case}' and number '{number}'"
            )

    def __repr__(self) -> str:
        return f"Noun({self.nom}, {self.gen}, {self.gender}, {self.meaning})"

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(f"{self.meaning}: {self.nom}, {self.gen} ({self.declension})")

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()


@total_ordering
class Adjective(Word):
    def __init__(
        self,
        *principal_parts: str,
        termination: Optional[int] = None,
        declension: str,
        meaning: Meaning,
    ) -> None:
        super().__init__()

        self.principal_parts: tuple[str, ...] = principal_parts
        self.mascnom: str = self.principal_parts[0]
        self.femnom: str
        self.neutnom: str

        self.pos_stem: str

        self.first = self.principal_parts[0]
        self.meaning: Meaning = meaning
        self.declension: str = declension
        self.termination: Optional[int] = termination
        self.irregular_flag: bool = False

        # FIXME: some adjectives don't have adverbs!
        #        bug probably to be left in, a bit complicated to fix
        if self.mascnom in edge_cases.IRREGULAR_COMPARATIVES:
            self.cmp_stem: str = edge_cases.IRREGULAR_COMPARATIVES[self.mascnom][0]
            self.spr_stem: str = edge_cases.IRREGULAR_COMPARATIVES[self.mascnom][1]
            self.irregular_posadv: str = edge_cases.IRREGULAR_COMPARATIVES[
                self.mascnom
            ][2]
            self.irregular_cmpadv: str = edge_cases.IRREGULAR_COMPARATIVES[
                self.mascnom
            ][3]
            self.irregular_spradv: str = edge_cases.IRREGULAR_COMPARATIVES[
                self.mascnom
            ][4]
            self.irregular_flag = True

        match self.declension:
            case "212":
                if self.termination:
                    raise InvalidInputError(
                        f"2-1-2 adjectives cannot have a termination (termination {self.termination} given)"
                    )
                if len(self.principal_parts) != 3:
                    raise InvalidInputError(
                        f"2-1-2 adjectives must have 3 principal parts (adjective '{self.first}' given)"
                    )
                self.femnom = self.principal_parts[1]
                self.neutnom = self.principal_parts[2]

                self.pos_stem = self.femnom[:-1]  # cara -> car-

                if self.mascnom not in edge_cases.IRREGULAR_COMPARATIVES:
                    self.cmp_stem = self.pos_stem + "ior"  # car- -> carior-
                    if self.mascnom[:2] == "er":
                        self.spr_stem = self.mascnom + "rim"  # miser- -> miserrim-
                    elif self.mascnom in edge_cases.LIS_ADJECTIVES:
                        self.spr_stem = self.pos_stem + "lim"  # facil- -> facillim-
                    else:
                        self.spr_stem = self.pos_stem + "issim"  # car- -> carissim-

                self.endings = {
                    "Aposmnomsg": self.mascnom,  # carus
                    "Aposmvocsg": self.pos_stem + "e",  # care
                    "Aposmaccsg": self.pos_stem + "um",  # carum
                    "Aposmgensg": self.pos_stem + "i",  # cari
                    "Aposmdatsg": self.pos_stem + "o",  # caro
                    "Aposmablsg": self.pos_stem + "o",  # caro
                    "Aposmnompl": self.pos_stem + "i",  # cari
                    "Aposmvocpl": self.pos_stem + "i",  # cari
                    "Aposmaccpl": self.pos_stem + "os",  # caros
                    "Aposmgenpl": self.pos_stem + "orum",  # carorum
                    "Aposmdatpl": self.pos_stem + "is",  # caris
                    "Aposmablpl": self.pos_stem + "is",  # caris
                    "Aposfnomsg": self.femnom,  # cara
                    "Aposfvocsg": self.femnom,  # cara
                    "Aposfaccsg": self.pos_stem + "am",  # caram
                    "Aposfgensg": self.pos_stem + "ae",  # carae
                    "Aposfdatsg": self.pos_stem + "ae",  # carae
                    "Aposfablsg": self.pos_stem + "a",  # cara
                    "Aposfnompl": self.pos_stem + "ae",  # carae
                    "Aposfvocpl": self.pos_stem + "ae",  # carae
                    "Aposfaccpl": self.pos_stem + "as",  # caras
                    "Aposfgenpl": self.pos_stem + "arum",  # cararum
                    "Aposfdatpl": self.pos_stem + "is",  # caris
                    "Aposfablpl": self.pos_stem + "is",  # caris
                    "Aposnnomsg": self.neutnom,  # carum
                    "Aposnvocsg": self.neutnom,  # carum
                    "Aposnaccsg": self.neutnom,  # carum
                    "Aposngensg": self.pos_stem + "i",  # cari
                    "Aposndatsg": self.pos_stem + "o",  # caro
                    "Aposnablsg": self.pos_stem + "o",  # caro
                    "Aposnnompl": self.pos_stem + "a",  # cara
                    "Aposnvocpl": self.pos_stem + "a",  # cara
                    "Aposnaccpl": self.pos_stem + "a",  # cara
                    "Aposngenpl": self.pos_stem + "orum",  # carorum
                    "Aposndatpl": self.pos_stem + "is",  # caris
                    "Aposnablpl": self.pos_stem + "is",  # caris
                    "Acmpmnomsg": self.cmp_stem,  # carior
                    "Acmpmvocsg": self.cmp_stem,  # carior
                    "Acmpmaccsg": self.cmp_stem + "em",  # cariorem
                    "Acmpmgensg": self.cmp_stem + "is",  # carioris
                    "Acmpmdatsg": self.cmp_stem + "i",  # cariori
                    "Acmpmablsg": self.cmp_stem + "e",  # cariore
                    "Acmpmnompl": self.cmp_stem + "es",  # cariores
                    "Acmpmvocpl": self.cmp_stem + "es",  # cariores
                    "Acmpmaccpl": self.cmp_stem + "es",  # cariores
                    "Acmpmgenpl": self.cmp_stem + "um",  # cariorum
                    "Acmpmdatpl": self.cmp_stem + "ibus",  # carioribus
                    "Acmpmablpl": self.cmp_stem + "ibus",  # carioribus
                    "Acmpfnomsg": self.cmp_stem,  # carior
                    "Acmpfvocsg": self.cmp_stem,  # carior
                    "Acmpfaccsg": self.cmp_stem + "em",  # cariorem
                    "Acmpfgensg": self.cmp_stem + "is",  # carioris
                    "Acmpfdatsg": self.cmp_stem + "i",  # cariori
                    "Acmpfablsg": self.cmp_stem + "e",  # cariore
                    "Acmpfnompl": self.cmp_stem + "es",  # cariores
                    "Acmpfvocpl": self.cmp_stem + "es",  # cariores
                    "Acmpfaccpl": self.cmp_stem + "es",  # cariores
                    "Acmpfgenpl": self.cmp_stem + "um",  # cariorum
                    "Acmpfdatpl": self.cmp_stem + "ibus",  # carioribus
                    "Acmpfablpl": self.cmp_stem + "ibus",  # carioribus
                    "Acmpnnomsg": self.cmp_stem[:-3] + "ius",  # carius
                    "Acmpnvocsg": self.cmp_stem[:-3] + "ius",  # carius
                    "Acmpnaccsg": self.cmp_stem[:-3] + "ius",  # carius
                    "Acmpngensg": self.cmp_stem + "is",  # carioris
                    "Acmpndatsg": self.cmp_stem + "i",  # cariori
                    "Acmpnablsg": self.cmp_stem + "e",  # cariore
                    "Acmpnnompl": self.cmp_stem + "a",  # cariora
                    "Acmpnvocpl": self.cmp_stem + "a",  # cariora
                    "Acmpnaccpl": self.cmp_stem + "a",  # cariora
                    "Acmpngenpl": self.cmp_stem + "um",  # cariorum
                    "Acmpndatpl": self.cmp_stem + "ibus",  # carioribus
                    "Acmpnablpl": self.cmp_stem + "ibus",  # carioribus
                    "Asprmnomsg": self.spr_stem + "us",  # carrissimus
                    "Asprmvocsg": self.spr_stem + "e",  # carrissime
                    "Asprmaccsg": self.spr_stem + "um",  # carrissimum
                    "Asprmgensg": self.spr_stem + "i",  # carrissimi
                    "Asprmdatsg": self.spr_stem + "o",  # carrissimo
                    "Asprmablsg": self.spr_stem + "o",  # carrissimo
                    "Asprmnompl": self.spr_stem + "i",  # carrissimi
                    "Asprmvocpl": self.spr_stem + "i",  # carrissimi
                    "Asprmaccpl": self.spr_stem + "os",  # carrissimos
                    "Asprmgenpl": self.spr_stem + "orum",  # carrissimorum
                    "Asprmdatpl": self.spr_stem + "is",  # carrissimis
                    "Asprmablpl": self.spr_stem + "is",  # carrissimis
                    "Asprfnomsg": self.spr_stem + "a",  # carrissima
                    "Asprfvocsg": self.spr_stem + "a",  # carrissima
                    "Asprfaccsg": self.spr_stem + "am",  # carrissimam
                    "Asprfgensg": self.spr_stem + "ae",  # carrissimae
                    "Asprfdatsg": self.spr_stem + "ae",  # crrissimae
                    "Asprfablsg": self.spr_stem + "a",  # carrissima
                    "Asprfnompl": self.spr_stem + "ae",  # carrissimae
                    "Asprfvocpl": self.spr_stem + "ae",  # carrissimae
                    "Asprfaccpl": self.spr_stem + "as",  # carrissimas
                    "Asprfgenpl": self.spr_stem + "arum",  # carrissimarum
                    "Asprfdatpl": self.spr_stem + "is",  # carrissimis
                    "Asprfablpl": self.spr_stem + "is",  # carrissimis
                    "Asprnnomsg": self.spr_stem + "um",  # carrissimum
                    "Asprnvocsg": self.spr_stem + "um",  # carrissimum
                    "Asprnaccsg": self.spr_stem + "um",  # carrissimum
                    "Asprngensg": self.spr_stem + "i",  # carrissimi
                    "Asprndatsg": self.spr_stem + "o",  # carrissimo
                    "Asprnablsg": self.spr_stem + "o",  # carrissimo
                    "Asprnnompl": self.spr_stem + "a",  # carrissima
                    "Asprnvocpl": self.spr_stem + "a",  # carrissima
                    "Asprnaccpl": self.spr_stem + "a",  # carrissima
                    "Asprngenpl": self.spr_stem + "orum",  # carrissimorum
                    "Asprndatpl": self.spr_stem + "is",  # carrissimis
                    "Asprnablpl": self.spr_stem + "is",  # carrissimis
                    "Dpos": self.irregular_posadv
                    if self.irregular_flag
                    else self.pos_stem + "e",
                    "Dcmp": self.irregular_cmpadv
                    if self.irregular_flag
                    else self.pos_stem + "ius",
                    "Dspr": self.irregular_spradv
                    if self.irregular_flag
                    else self.spr_stem + "e",
                }

            case "3":
                match self.termination:
                    case 1:
                        # ingens, ingentis
                        if len(self.principal_parts) != 2:
                            raise InvalidInputError(
                                f"First-termination adjectives must have 2 principal parts (adjective '{self.first}')"
                            )

                        self.mascgen: str = self.principal_parts[1]

                        if self.mascgen[-2:] != "is":
                            raise InvalidInputError(
                                f"Genitive '{self.mascgen}' not recognised"
                            )
                        self.pos_stem = self.mascgen[:-2]  # ingentis -> ingent-

                        if not self.irregular_flag:
                            self.cmp_stem = (
                                self.pos_stem + "ior"
                            )  # ingent- > ingentior-
                            if self.mascnom[:2] == "er":
                                self.spr_stem = (
                                    self.mascnom + "rim"
                                )  # miser- -> miserrim-
                            elif self.mascnom in edge_cases.LIS_ADJECTIVES:
                                self.spr_stem = (
                                    self.pos_stem + "lim"  # facil- -> facillim-
                                )
                            else:
                                self.spr_stem = (
                                    self.pos_stem + "issim"  # ingent- -> ingentissim-
                                )

                        self.endings = {
                            "Aposmnomsg": self.mascnom,  # ingens
                            "Aposmvocsg": self.mascnom,  # ingens
                            "Aposmaccsg": self.pos_stem + "em",  # ingentem
                            "Aposmgensg": self.mascgen,  # ingentis
                            "Aposmdatsg": self.pos_stem + "i",  # ingenti
                            "Aposmablsg": self.pos_stem + "i",  # ingenti
                            "Aposmnompl": self.pos_stem + "es",  # ingentes
                            "Aposmvocpl": self.pos_stem + "es",  # ingentes
                            "Aposmaccpl": self.pos_stem + "es",  # ingentes
                            "Aposmgenpl": self.pos_stem + "ium",  # ingentium
                            "Aposmdatpl": self.pos_stem + "ibus",  # ingentibus
                            "Aposmablpl": self.pos_stem + "ibus",  # ingentibus
                            "Aposfnomsg": self.mascnom,  # ingens
                            "Aposfvocsg": self.mascnom,  # ingens
                            "Aposfaccsg": self.pos_stem + "em",  # ingentem
                            "Aposfgensg": self.mascgen,  # ingentis
                            "Aposfdatsg": self.pos_stem + "i",  # ingenti
                            "Aposfablsg": self.pos_stem + "i",  # ingenti
                            "Aposfnompl": self.pos_stem + "es",  # ingentes
                            "Aposfvocpl": self.pos_stem + "es",  # ingentes
                            "Aposfaccpl": self.pos_stem + "es",  # ingentes
                            "Aposfgenpl": self.pos_stem + "ium",  # ingentium
                            "Aposfdatpl": self.pos_stem + "ibus",  # ingentibus
                            "Aposfablpl": self.pos_stem + "ibus",  # ingentibus
                            "Aposnnomsg": self.mascnom,  # ingens
                            "Aposnvocsg": self.mascnom,  # ingens
                            "Aposnaccsg": self.mascnom,  # ingens
                            "Aposngensg": self.mascgen,  # ingentis
                            "Aposndatsg": self.pos_stem + "i",  # ingenti
                            "Aposnablsg": self.pos_stem + "i",  # ingenti
                            "Aposnnompl": self.pos_stem + "ia",  # ingentia
                            "Aposnvocpl": self.pos_stem + "ia",  # ingentia
                            "Aposnaccpl": self.pos_stem + "ia",  # ingentia
                            "Aposngenpl": self.pos_stem + "ium",  # ingentium
                            "Aposndatpl": self.pos_stem + "ibus",  # ingentibus
                            "Aposnablpl": self.pos_stem + "ibus",  # ingentibus
                            "Acmpmnomsg": self.cmp_stem,  # ingentior
                            "Acmpmvocsg": self.cmp_stem,  # ingentior
                            "Acmpmaccsg": self.cmp_stem + "em",  # ingentiorem
                            "Acmpmgensg": self.cmp_stem + "is",  # ingentioris
                            "Acmpmdatsg": self.cmp_stem + "i",  # ingentiori
                            "Acmpmablsg": self.cmp_stem + "e",  # ingentiore
                            "Acmpmnompl": self.cmp_stem + "es",  # ingentiores
                            "Acmpmvocpl": self.cmp_stem + "es",  # ingentiores
                            "Acmpmaccpl": self.cmp_stem + "es",  # ingentiores
                            "Acmpmgenpl": self.cmp_stem + "um",  # ingentiorum
                            "Acmpmdatpl": self.cmp_stem + "ibus",  # ingentioribus
                            "Acmpmablpl": self.cmp_stem + "ibus",  # ingentioribus
                            "Acmpfnomsg": self.cmp_stem,  # ingentior
                            "Acmpfvocsg": self.cmp_stem,  # ingentior
                            "Acmpfaccsg": self.cmp_stem + "em",  # ingentiorem
                            "Acmpfgensg": self.cmp_stem + "is",  # ingentioris
                            "Acmpfdatsg": self.cmp_stem + "i",  # ingentiori
                            "Acmpfablsg": self.cmp_stem + "e",  # ingentiore
                            "Acmpfnompl": self.cmp_stem + "es",  # ingentiores
                            "Acmpfvocpl": self.cmp_stem + "es",  # ingentiores
                            "Acmpfaccpl": self.cmp_stem + "es",  # ingentiores
                            "Acmpfgenpl": self.cmp_stem + "um",  # ingentiorum
                            "Acmpfdatpl": self.cmp_stem + "ibus",  # ingentioribus
                            "Acmpfablpl": self.cmp_stem + "ibus",  # ingentioribus
                            "Acmpnnomsg": self.cmp_stem[:-3] + "ius",  # ingentius
                            "Acmpnvocsg": self.cmp_stem[:-3] + "ius",  # ingentius
                            "Acmpnaccsg": self.cmp_stem[:-3] + "ius",  # ingentius
                            "Acmpngensg": self.cmp_stem + "is",  # ingentioris
                            "Acmpndatsg": self.cmp_stem + "i",  # ingentiori
                            "Acmpnablsg": self.cmp_stem + "e",  # ingentiore
                            "Acmpnnompl": self.cmp_stem + "a",  # ingentiora
                            "Acmpnvocpl": self.cmp_stem + "a",  # ingentiora
                            "Acmpnaccpl": self.cmp_stem + "a",  # ingentiora
                            "Acmpngenpl": self.cmp_stem + "um",  # ingentiorum
                            "Acmpndatpl": self.cmp_stem + "ibus",  # ingentioribus
                            "Acmpnablpl": self.cmp_stem + "ibus",  # ingentioribus
                            "Asprmnomsg": self.spr_stem + "us",  # ingentissimus
                            "Asprmvocsg": self.spr_stem + "e",  # ingentissime
                            "Asprmaccsg": self.spr_stem + "um",  # ingentissimum
                            "Asprmgensg": self.spr_stem + "i",  # ingentissimi
                            "Asprmdatsg": self.spr_stem + "o",  # ingentissimo
                            "Asprmablsg": self.spr_stem + "o",  # ingentissimo
                            "Asprmnompl": self.spr_stem + "i",  # ingentissimi
                            "Asprmvocpl": self.spr_stem + "i",  # ingentissimi
                            "Asprmaccpl": self.spr_stem + "os",  # ingentissimos
                            "Asprmgenpl": self.spr_stem + "orum",  # ingentissimorum
                            "Asprmdatpl": self.spr_stem + "is",  # ingentissimis
                            "Asprmablpl": self.spr_stem + "is",  # ingentissimis
                            "Asprfnomsg": self.spr_stem + "a",  # ingentissima
                            "Asprfvocsg": self.spr_stem + "a",  # ingentissima
                            "Asprfaccsg": self.spr_stem + "am",  # ingentissimam
                            "Asprfgensg": self.spr_stem + "ae",  # ingentissimae
                            "Asprfdatsg": self.spr_stem + "ae",  # ingentissimae
                            "Asprfablsg": self.spr_stem + "a",  # ingentissima
                            "Asprfnompl": self.spr_stem + "ae",  # ingentissimae
                            "Asprfvocpl": self.spr_stem + "ae",  # ingentissimae
                            "Asprfaccpl": self.spr_stem + "as",  # ingentissimas
                            "Asprfgenpl": self.spr_stem + "arum",  # ingentissimarum
                            "Asprfdatpl": self.spr_stem + "is",  # ingentissimis
                            "Asprfablpl": self.spr_stem + "is",  # ingentissimis
                            "Asprnnomsg": self.spr_stem + "um",  # ingentissimum
                            "Asprnvocsg": self.spr_stem + "um",  # ingentissimum
                            "Asprnaccsg": self.spr_stem + "um",  # ingentissimum
                            "Asprngensg": self.spr_stem + "i",  # ingentissimi
                            "Asprndatsg": self.spr_stem + "o",  # ingentissimo
                            "Asprnablsg": self.spr_stem + "o",  # ingentissimo
                            "Asprnnompl": self.spr_stem + "a",  # ingentissima
                            "Asprnvocpl": self.spr_stem + "a",  # ingentissima
                            "Asprnaccpl": self.spr_stem + "a",  # ingentissima
                            "Asprngenpl": self.spr_stem + "orum",  # ingentissimorum
                            "Asprndatpl": self.spr_stem + "is",  # ingentissimis
                            "Asprnablpl": self.spr_stem + "is",  # ingentissimis
                            "Dpos": self.irregular_posadv
                            if self.irregular_flag
                            else self.pos_stem + "er",
                            "Dcmp": self.irregular_cmpadv
                            if self.irregular_flag
                            else self.pos_stem + "ius",
                            "Dspr": self.irregular_spradv
                            if self.irregular_flag
                            else self.spr_stem + "e",
                        }

                    case 2:
                        # fortis, forte
                        if len(self.principal_parts) != 2:
                            raise InvalidInputError(
                                f"Second-termination adjectives must have 2 principal parts (adjective '{self.first}')"
                            )

                        self.neutnom = self.principal_parts[1]

                        self.pos_stem = self.mascnom[:-2]  # fortis -> fort-
                        if not self.irregular_flag:
                            self.cmp_stem = self.pos_stem + "ior"  # fort- -> fortior-
                            if self.mascnom[:2] == "er":
                                self.spr_stem = (
                                    self.mascnom + "rim"  # miser- -> miserrim-
                                )
                            elif self.mascnom in edge_cases.LIS_ADJECTIVES:
                                self.spr_stem = (
                                    self.pos_stem + "lim"  # facil- -> facillim-
                                )
                            else:
                                self.spr_stem = (
                                    self.pos_stem + "issim"  # fort- -> fortissim-
                                )

                        self.endings = {
                            "Aposmnomsg": self.mascnom,  # fortis
                            "Aposmvocsg": self.mascnom,  # fortis
                            "Aposmaccsg": self.pos_stem + "em",  # fortem
                            "Aposmgensg": self.pos_stem + "is",  # fortis
                            "Aposmdatsg": self.pos_stem + "i",  # forti
                            "Aposmablsg": self.pos_stem + "i",  # forti
                            "Aposmnompl": self.pos_stem + "es",  # fortes
                            "Aposmvocpl": self.pos_stem + "es",  # fortes
                            "Aposmaccpl": self.pos_stem + "es",  # fortes
                            "Aposmgenpl": self.pos_stem + "ium",  # fortium
                            "Aposmdatpl": self.pos_stem + "ibus",  # fortibus
                            "Aposmablpl": self.pos_stem + "ibus",  # fortibus
                            "Aposfnomsg": self.mascnom,  # fortis
                            "Aposfvocsg": self.mascnom,  # fortis
                            "Aposfaccsg": self.pos_stem + "em",  # fortem
                            "Aposfgensg": self.pos_stem + "is",  # fortis
                            "Aposfdatsg": self.pos_stem + "i",  # forti
                            "Aposfablsg": self.pos_stem + "i",  # forti
                            "Aposfnompl": self.pos_stem + "es",  # fortes
                            "Aposfvocpl": self.pos_stem + "es",  # fortes
                            "Aposfaccpl": self.pos_stem + "es",  # fortes
                            "Aposfgenpl": self.pos_stem + "ium",  # fortium
                            "Aposfdatpl": self.pos_stem + "ibus",  # fortibus
                            "Aposfablpl": self.pos_stem + "ibus",  # fortibus
                            "Aposnnomsg": self.neutnom,  # forte
                            "Aposnvocsg": self.neutnom,  # forte
                            "Aposnaccsg": self.neutnom,  # forte
                            "Aposngensg": self.pos_stem + "is",  # fortis
                            "Aposndatsg": self.pos_stem + "i",  # fortibus
                            "Aposnablsg": self.pos_stem + "i",  # fortibus
                            "Aposnnompl": self.pos_stem + "ia",  # fortia
                            "Aposnvocpl": self.pos_stem + "ia",  # fortia
                            "Aposnaccpl": self.pos_stem + "ia",  # fortia
                            "Aposngenpl": self.pos_stem + "ium",  # fortium
                            "Aposndatpl": self.pos_stem + "ibus",  # fortibus
                            "Aposnablpl": self.pos_stem + "ibus",  # fortibus
                            "Acmpmnomsg": self.cmp_stem,  # fortior
                            "Acmpmvocsg": self.cmp_stem,  # fortior
                            "Acmpmaccsg": self.cmp_stem + "em",  # fortiorem
                            "Acmpmgensg": self.cmp_stem + "is",  # fortioris
                            "Acmpmdatsg": self.cmp_stem + "i",  # fortiori
                            "Acmpmablsg": self.cmp_stem + "e",  # fortiore
                            "Acmpmnompl": self.cmp_stem + "es",  # fortiores
                            "Acmpmvocpl": self.cmp_stem + "es",  # fortiores
                            "Acmpmaccpl": self.cmp_stem + "es",  # fortiores
                            "Acmpmgenpl": self.cmp_stem + "um",  # fortiorum
                            "Acmpmdatpl": self.cmp_stem + "ibus",  # fortioribus
                            "Acmpmablpl": self.cmp_stem + "ibus",  # fortioribus
                            "Acmpfnomsg": self.cmp_stem,  # fortior
                            "Acmpfvocsg": self.cmp_stem,  # fortior
                            "Acmpfaccsg": self.cmp_stem + "em",  # fortiorem
                            "Acmpfgensg": self.cmp_stem + "is",  # fortioris
                            "Acmpfdatsg": self.cmp_stem + "i",  # fortiori
                            "Acmpfablsg": self.cmp_stem + "e",  # fortiore
                            "Acmpfnompl": self.cmp_stem + "es",  # fortiores
                            "Acmpfvocpl": self.cmp_stem + "es",  # fortiores
                            "Acmpfaccpl": self.cmp_stem + "es",  # fortiores
                            "Acmpfgenpl": self.cmp_stem + "um",  # fortiorum
                            "Acmpfdatpl": self.cmp_stem + "ibus",  # fortioribus
                            "Acmpfablpl": self.cmp_stem + "ibus",  # fortioribus
                            "Acmpnnomsg": self.cmp_stem[:-3] + "ius",  # fortius
                            "Acmpnvocsg": self.cmp_stem[:-3] + "ius",  # fortius
                            "Acmpnaccsg": self.cmp_stem[:-3] + "ius",  # fortius
                            "Acmpngensg": self.cmp_stem + "is",  # fortioris
                            "Acmpndatsg": self.cmp_stem + "i",  # fortiori
                            "Acmpnablsg": self.cmp_stem + "e",  # fortiore
                            "Acmpnnompl": self.cmp_stem + "a",  # fortiora
                            "Acmpnvocpl": self.cmp_stem + "a",  # fortiora
                            "Acmpnaccpl": self.cmp_stem + "a",  # fortiora
                            "Acmpngenpl": self.cmp_stem + "um",  # fortiorum
                            "Acmpndatpl": self.cmp_stem + "ibus",  # fortioribus
                            "Acmpnablpl": self.cmp_stem + "ibus",  # fortioribus
                            "Asprmnomsg": self.spr_stem + "us",  # fortissimus
                            "Asprmvocsg": self.spr_stem + "e",  # fortissime
                            "Asprmaccsg": self.spr_stem + "um",  # fortissimum
                            "Asprmgensg": self.spr_stem + "i",  # fortissimi
                            "Asprmdatsg": self.spr_stem + "o",  # fortissimo
                            "Asprmablsg": self.spr_stem + "o",  # fortissimo
                            "Asprmnompl": self.spr_stem + "i",  # fortissimi
                            "Asprmvocpl": self.spr_stem + "i",  # fortissimi
                            "Asprmaccpl": self.spr_stem + "os",  # fortissimi
                            "Asprmgenpl": self.spr_stem + "orum",  # fortissimorum
                            "Asprmdatpl": self.spr_stem + "is",  # fortissimis
                            "Asprmablpl": self.spr_stem + "is",  # fortissimis
                            "Asprfnomsg": self.spr_stem + "a",  # fortissima
                            "Asprfvocsg": self.spr_stem + "a",  # fortissima
                            "Asprfaccsg": self.spr_stem + "am",  # fortissimam
                            "Asprfgensg": self.spr_stem + "ae",  # fortissimae
                            "Asprfdatsg": self.spr_stem + "ae",  # crrissimae
                            "Asprfablsg": self.spr_stem + "a",  # fortissima
                            "Asprfnompl": self.spr_stem + "ae",  # fortissimae
                            "Asprfvocpl": self.spr_stem + "ae",  # fortissimae
                            "Asprfaccpl": self.spr_stem + "as",  # fortissimas
                            "Asprfgenpl": self.spr_stem + "arum",  # fortissimarum
                            "Asprfdatpl": self.spr_stem + "is",  # fortissimis
                            "Asprfablpl": self.spr_stem + "is",  # fortissimis
                            "Asprnnomsg": self.spr_stem + "um",  # fortissimum
                            "Asprnvocsg": self.spr_stem + "um",  # fortissimum
                            "Asprnaccsg": self.spr_stem + "um",  # fortissimum
                            "Asprngensg": self.spr_stem + "i",  # fortissimi
                            "Asprndatsg": self.spr_stem + "o",  # fortissimo
                            "Asprnablsg": self.spr_stem + "o",  # fortissimo
                            "Asprnnompl": self.spr_stem + "a",  # fortissima
                            "Asprnvocpl": self.spr_stem + "a",  # fortissima
                            "Asprnaccpl": self.spr_stem + "a",  # fortissima
                            "Asprngenpl": self.spr_stem + "orum",  # fortissimorum
                            "Asprndatpl": self.spr_stem + "is",  # fortissimis
                            "Asprnablpl": self.spr_stem + "is",  # fortissimis
                            "Dpos": self.irregular_posadv
                            if self.irregular_flag
                            else self.pos_stem + "iter",
                            "Dcmp": self.irregular_cmpadv
                            if self.irregular_flag
                            else self.pos_stem + "ius",
                            "Dspr": self.irregular_spradv
                            if self.irregular_flag
                            else self.spr_stem + "e",
                        }

                    case 3:
                        # acer, acris, acre
                        if len(self.principal_parts) != 3:
                            raise InvalidInputError(
                                f"Third-termination adjectives must have 3 principal parts (adjective '{self.first}')"
                            )

                        self.mascnom = self.principal_parts[0]
                        self.femnom = self.principal_parts[1]
                        self.neutnom = self.principal_parts[2]

                        self.pos_stem = self.femnom[:-2]  # acris -> acr-
                        if not self.irregular_flag:
                            self.cmp_stem = self.pos_stem + "ior"  # acr- -> acrior-
                            if self.mascnom[-2:] == "er":
                                self.spr_stem = (
                                    self.mascnom + "rim"
                                )  # acer- -> acerrim-
                            elif self.mascnom in edge_cases.LIS_ADJECTIVES:
                                self.spr_stem = (
                                    self.pos_stem + "lim"  # facil- -> facillim-
                                )
                            else:
                                self.spr_stem = (
                                    self.pos_stem + "issim"  # levis -> levissim-
                                )

                        self.endings = {
                            "Aposmnomsg": self.mascnom,  # acer
                            "Aposmvocsg": self.mascnom,  # acer
                            "Aposmaccsg": self.pos_stem + "em",  # acrem
                            "Aposmgensg": self.pos_stem + "is",  # acris
                            "Aposmdatsg": self.pos_stem + "i",  # acri
                            "Aposmablsg": self.pos_stem + "i",  # acri
                            "Aposmnompl": self.pos_stem + "es",  # acres
                            "Aposmvocpl": self.pos_stem + "es",  # acres
                            "Aposmaccpl": self.pos_stem + "es",  # acres
                            "Aposmgenpl": self.pos_stem + "ium",  # acrium
                            "Aposmdatpl": self.pos_stem + "ibus",  # acribus
                            "Aposmablpl": self.pos_stem + "ibus",  # acribus
                            "Aposfnomsg": self.femnom,  # acris
                            "Aposfvocsg": self.femnom,  # acris
                            "Aposfaccsg": self.pos_stem + "em",  # acrem
                            "Aposfgensg": self.pos_stem + "is",  # acris
                            "Aposfdatsg": self.pos_stem + "i",  # acri
                            "Aposfablsg": self.pos_stem + "i",  # acri
                            "Aposfnompl": self.pos_stem + "es",  # acres
                            "Aposfvocpl": self.pos_stem + "es",  # acres
                            "Aposfaccpl": self.pos_stem + "es",  # acres
                            "Aposfgenpl": self.pos_stem + "ium",  # acrium
                            "Aposfdatpl": self.pos_stem + "ibus",  # acribus
                            "Aposfablpl": self.pos_stem + "ibus",  # acribus
                            "Aposnnomsg": self.neutnom,  # acre
                            "Aposnvocsg": self.neutnom,  # acre
                            "Aposnaccsg": self.neutnom,  # acre
                            "Aposngensg": self.pos_stem + "is",  # acris
                            "Aposndatsg": self.pos_stem + "i",  # acri
                            "Aposnablsg": self.pos_stem + "i",  # acri
                            "Aposnnompl": self.pos_stem + "ia",  # acria
                            "Aposnvocpl": self.pos_stem + "ia",  # acria
                            "Aposnaccpl": self.pos_stem + "ia",  # acria
                            "Aposngenpl": self.pos_stem + "ium",  # acrium
                            "Aposndatpl": self.pos_stem + "ibus",  # acribus
                            "Aposnablpl": self.pos_stem + "ibus",  # acribus
                            "Acmpmnomsg": self.cmp_stem,  # acrior
                            "Acmpmvocsg": self.cmp_stem,  # acrior
                            "Acmpmaccsg": self.cmp_stem + "em",  # acriorem
                            "Acmpmgensg": self.cmp_stem + "is",  # acrioris
                            "Acmpmdatsg": self.cmp_stem + "i",  # acriori
                            "Acmpmablsg": self.cmp_stem + "e",  # acriore
                            "Acmpmnompl": self.cmp_stem + "es",  # acriores
                            "Acmpmvocpl": self.cmp_stem + "es",  # acriores
                            "Acmpmaccpl": self.cmp_stem + "es",  # acriores
                            "Acmpmgenpl": self.cmp_stem + "um",  # acriorum
                            "Acmpmdatpl": self.cmp_stem + "ibus",  # acrioribus
                            "Acmpmablpl": self.cmp_stem + "ibus",  # acrioribus
                            "Acmpfnomsg": self.cmp_stem,  # acrior
                            "Acmpfvocsg": self.cmp_stem,  # acrior
                            "Acmpfaccsg": self.cmp_stem + "em",  # acriorem
                            "Acmpfgensg": self.cmp_stem + "is",  # acrioris
                            "Acmpfdatsg": self.cmp_stem + "i",  # acriori
                            "Acmpfablsg": self.cmp_stem + "e",  # acriore
                            "Acmpfnompl": self.cmp_stem + "es",  # acriores
                            "Acmpfvocpl": self.cmp_stem + "es",  # acriores
                            "Acmpfaccpl": self.cmp_stem + "es",  # acriores
                            "Acmpfgenpl": self.cmp_stem + "um",  # acriorum
                            "Acmpfdatpl": self.cmp_stem + "ibus",  # acrioribus
                            "Acmpfablpl": self.cmp_stem + "ibus",  # acrioribus
                            "Acmpnnomsg": self.cmp_stem[:-3] + "ius",  # acrius
                            "Acmpnvocsg": self.cmp_stem[:-3] + "ius",  # acrius
                            "Acmpnaccsg": self.cmp_stem[:-3] + "ius",  # acrius
                            "Acmpngensg": self.cmp_stem + "is",  # acrioris
                            "Acmpndatsg": self.cmp_stem + "i",  # acriori
                            "Acmpnablsg": self.cmp_stem + "e",  # acriore
                            "Acmpnnompl": self.cmp_stem + "a",  # acriora
                            "Acmpnvocpl": self.cmp_stem + "a",  # acriora
                            "Acmpnaccpl": self.cmp_stem + "a",  # acriora
                            "Acmpngenpl": self.cmp_stem + "um",  # acriorum
                            "Acmpndatpl": self.cmp_stem + "ibus",  # acrioribus
                            "Acmpnablpl": self.cmp_stem + "ibus",  # acrioribus
                            "Asprmnomsg": self.spr_stem + "us",  # acerrimus
                            "Asprmvocsg": self.spr_stem + "e",  # acerrime
                            "Asprmaccsg": self.spr_stem + "um",  # acerrimum
                            "Asprmgensg": self.spr_stem + "i",  # acerrimi
                            "Asprmdatsg": self.spr_stem + "o",  # acerrimo
                            "Asprmablsg": self.spr_stem + "o",  # acerrimo
                            "Asprmnompl": self.spr_stem + "i",  # acerrimi
                            "Asprmvocpl": self.spr_stem + "i",  # acerrimi
                            "Asprmaccpl": self.spr_stem + "os",  # acerrimos
                            "Asprmgenpl": self.spr_stem + "orum",  # acerrimorum
                            "Asprmdatpl": self.spr_stem + "is",  # acerrimis
                            "Asprmablpl": self.spr_stem + "is",  # acerrimis
                            "Asprfnomsg": self.spr_stem + "a",  # acerrima
                            "Asprfvocsg": self.spr_stem + "a",  # acerrima
                            "Asprfaccsg": self.spr_stem + "am",  # acerrimam
                            "Asprfgensg": self.spr_stem + "ae",  # acerrimae
                            "Asprfdatsg": self.spr_stem + "ae",  # crrissimae
                            "Asprfablsg": self.spr_stem + "a",  # acerrima
                            "Asprfnompl": self.spr_stem + "ae",  # acerrimae
                            "Asprfvocpl": self.spr_stem + "ae",  # acerrimae
                            "Asprfaccpl": self.spr_stem + "as",  # acerrimas
                            "Asprfgenpl": self.spr_stem + "arum",  # acerrimarum
                            "Asprfdatpl": self.spr_stem + "is",  # acerrimis
                            "Asprfablpl": self.spr_stem + "is",  # acerrimis
                            "Asprnnomsg": self.spr_stem + "um",  # acerrimum
                            "Asprnvocsg": self.spr_stem + "um",  # acerrimum
                            "Asprnaccsg": self.spr_stem + "um",  # acerrimum
                            "Asprngensg": self.spr_stem + "i",  # acerrimi
                            "Asprndatsg": self.spr_stem + "o",  # acerrimo
                            "Asprnablsg": self.spr_stem + "o",  # acerrimo
                            "Asprnnompl": self.spr_stem + "a",  # acerrima
                            "Asprnvocpl": self.spr_stem + "a",  # acerrima
                            "Asprnaccpl": self.spr_stem + "a",  # acerrima
                            "Asprngenpl": self.spr_stem + "orum",  # acerrimorum
                            "Asprndatpl": self.spr_stem + "is",  # acerrimis
                            "Asprnablpl": self.spr_stem + "is",  # acerrimis
                            "Dpos": self.irregular_posadv
                            if self.irregular_flag
                            else self.pos_stem + "iter",
                            "Dcmp": self.irregular_cmpadv
                            if self.irregular_flag
                            else self.pos_stem + "ius",
                            "Dspr": self.irregular_spradv
                            if self.irregular_flag
                            else self.spr_stem + "e",
                        }

                    case _:
                        raise InvalidInputError(
                            f"Termination must be 1, 2 or 3 (given {self.termination})"
                        )

            case _:
                raise InvalidInputError(f"Declension {self.declension} not recognised")

    def get(
        self,
        *,
        degree: str,
        gender: Optional[str] = None,
        case: Optional[str] = None,
        number: Optional[str] = None,
        adverb: bool = False,
    ) -> Ending:
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
                raise NoMeaningError(f"No ending found for degree '{degree}'")

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
            raise NoMeaningError(
                f"No ending found for degree '{degree}', gender '{gender}', case '{case}' and number '{number}'"
            )

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(f"{self.meaning}: {', '.join(self.principal_parts)}\n")
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()

    def __repr__(self) -> str:
        return f"Adjective({', '.join(self.principal_parts)}, {self.termination}, {self.declension}, {self.meaning})"


@total_ordering
class Pronoun(Word):
    def __init__(self, *, pronoun: str, meaning: Meaning):
        super().__init__()
        try:
            self.endings = edge_cases.PRONOUNS[pronoun]
        except KeyError:
            raise InvalidInputError(f"Pronoun '{pronoun}' not recognised")

        self.pronoun: str = pronoun
        self.first = self.pronoun
        self.meaning: Meaning = meaning

        self.mascnom: Ending = self.endings["Pmnomsg"]
        self.femnom: Ending = self.endings["Pfnomsg"]
        self.neutnom: Ending = self.endings["Pnnomsg"]

    def get(self, gender: str, case: str, number: str) -> Ending:
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
            raise NoMeaningError(
                f"No ending found for gender '{gender}', case '{case}' and number '{number}'"
            )

    def __repr__(self) -> str:
        return f"Pronoun({self.pronoun}, {self.meaning})"

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(f"{self.meaning}: {self.mascnom}, {self.femnom}, {self.neutnom}\n")
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()
