from io import StringIO
from typing import Optional, Union
from functools import total_ordering
from dataclass import dataclass

from . import edge_cases
from .misc import MultipleOptions

SHORTHAND = {
    # Verbs
    "singular": "sg",
    "plural": "pl",
    "present": "pre",
    "imperfect": "imp",
    "future": "fut",
    "perfect": "per",
    "pluperfect": "plp",
    "future perfect": "fpr",
    "active": "act",
    "passive": "pas",
    "indicative": "ind",
    "infinitive": "inf",
    "imperative": "ipe",
    "subjunctive": "sbj",
    # Nouns
    "nominative": "nom",
    "vocative": "voc",
    "accusative": "acc",
    "genitive": "gen",
    "dative": "dat",
    "ablative": "abl",
    # Adjectives
    "masculine": "m",
    "feminine": "f",
    "neuter": "n",
    "positive": "pos",
    "comparative": "cmp",
    "superlative": "spr",
}


@dataclass
class Word:
    word: str
    meaning: Union[str, MultipleOptions]


@total_ordering
class LearningVerb:
    def __init__(
        self,
        pre: str,
        inf: str,
        per: str,
        ppp: Optional[str],
        meaning: Union[str, MultipleOptions],
    ) -> None:
        self.pre = pre
        self.inf = inf
        self.per = per
        self.ppp = ppp if ppp else False
        if isinstance(meaning, MultipleOptions):
            self.meaning = meaning
        else:
            self.meaning = MultipleOptions(meaning, [])

        self.first = pre

        # Conjugation edge cases
        if pre in edge_cases.THIRD_IO_VERBS:
            self.conjugation = 5
        elif pre in edge_cases.IRREGULAR_VERBS:
            self.endings = edge_cases.IRREGULAR_VERBS[pre]
            self.conjugation = "irregular"
            return

        # Find conjugation
        elif inf[-3:] == "are":
            self.conjugation = 1
        elif inf[-3:] == "ire":
            self.conjugation = 4
        elif inf[-3:] == "ere":
            if self.pre[-2:] == "eo":
                self.conjugation = 2
            else:
                self.conjugation = 3
        else:
            raise Exception("The infinitive is not valid (must end in are, ire or ere)")

        self.pre_stem = pre[:-1]
        self.inf_stem = inf[:-3]
        self.per_stem = per[:-1]

        match self.conjugation:
            # First conjugation
            case 1:
                self.endings = {
                    "Vpreactindsg1": self.pre,  # porto
                    "Vpreactindsg2": self.inf_stem + "as",  # portas
                    "Vpreactindsg3": self.inf_stem + "at",  # portat
                    "Vpreactindpl1": self.inf_stem + "amus",  # portamus
                    "Vpreactindpl2": self.inf_stem + "atis",  # portatis
                    "Vpreactindpl3": self.inf_stem + "ant",  # portant
                    "Vimpactindsg1": self.inf_stem + "abam",  # portabam
                    "Vimpactindsg2": self.inf_stem + "abas",  # portabas
                    "Vimpactindsg3": self.inf_stem + "abat",  # portabat
                    "Vimpactindpl1": self.inf_stem + "abamus",  # portabamus
                    "Vimpactindpl2": self.inf_stem + "abatis",  # portabatis
                    "Vimpactindpl3": self.inf_stem + "abant",  # portabant
                    "Vperactindsg1": self.per,  # portavi
                    "Vperactindsg2": self.per_stem + "isti",  # portavisti
                    "Vperactindsg3": self.per_stem + "it",  # portavit
                    "Vperactindpl1": self.per_stem + "imus",  # portavimus
                    "Vperactindpl2": self.per_stem + "istis",  # portavistis
                    "Vperactindpl3": self.per_stem + "erunt",  # portaverunt
                    "Vplpactindsg1": self.per_stem + "eram",  # portaveram
                    "Vplpactindsg2": self.per_stem + "eras",  # portaveras
                    "Vplpactindsg3": self.per_stem + "erat",  # portaverat
                    "Vplpactindpl1": self.per_stem + "eramus",  # portaveramus
                    "Vplpactindpl2": self.per_stem + "eratis",  # portaveratis
                    "Vplpactindpl3": self.per_stem + "erant",  # portaverant
                    "Vpreactinf   ": self.inf,  # portare
                    "Vpreactipesg2": self.inf_stem + "a",  # porta
                    "Vpreactipepl2": self.inf_stem + "ate",  # portate
                    "Vimpactsbjsg1": self.inf + "m",  # portarem
                    "Vimpactsbjsg2": self.inf + "s",  # portares
                    "Vimpactsbjsg3": self.inf + "t",  # portaret
                    "Vimpactsbjpl1": self.inf + "mus",  # portaremus
                    "Vimpactsbjpl2": self.inf + "tis",  # portaretis
                    "Vimpactsbjpl3": self.inf + "nt",  # portarent
                    "Vplpactsbjsg1": self.per_stem + "issem",  # portavissem
                    "Vplpactsbjsg2": self.per_stem + "isses",  # portavisses
                    "Vplpactsbjsg3": self.per_stem + "isset",  # portavisset
                    "Vplpactsbjpl1": self.per_stem + "issemus",  # portavissemus
                    "Vplpactsbjpl2": self.per_stem + "issetis",  # portavissetis
                    "Vplpactsbjpl3": self.per_stem + "issent",  # portavissent
                }

            # Second conjugation
            case 2:
                self.endings = {
                    "Vpreactindsg1": self.pre,  # doceo
                    "Vpreactindsg2": self.inf_stem + "es",  # doces
                    "Vpreactindsg3": self.inf_stem + "et",  # docet
                    "Vpreactindpl1": self.inf_stem + "emus",  # docemus
                    "Vpreactindpl2": self.inf_stem + "etis",  # docetis
                    "Vpreactindpl3": self.inf_stem + "ent",  # docent
                    "Vimpactindsg1": self.inf_stem + "ebam",  # docebam
                    "Vimpactindsg2": self.inf_stem + "ebas",  # docebas
                    "Vimpactindsg3": self.inf_stem + "ebat",  # docebat
                    "Vimpactindpl1": self.inf_stem + "ebamus",  # docebamus
                    "Vimpactindpl2": self.inf_stem + "ebatis",  # docebatis
                    "Vimpactindpl3": self.inf_stem + "ebant",  # docebant
                    "Vperactindsg1": self.per,  # docui
                    "Vperactindsg2": self.per_stem + "isti",  # docuisit
                    "Vperactindsg3": self.per_stem + "it",  # docuit
                    "Vperactindpl1": self.per_stem + "imus",  # docuimus
                    "Vperactindpl2": self.per_stem + "istis",  # docuistis
                    "Vperactindpl3": self.per_stem + "erunt",  # docuerunt
                    "Vplpactindsg1": self.per_stem + "eram",  # docueram
                    "Vplpactindsg2": self.per_stem + "eras",  # docueras
                    "Vplpactindsg3": self.per_stem + "erat",  # docuerat
                    "Vplpactindpl1": self.per_stem + "eramus",  # docueramus
                    "Vplpactindpl2": self.per_stem + "eratis",  # docueratis
                    "Vplpactindpl3": self.per_stem + "erant",  # docuerant
                    "Vpreactinf   ": self.inf,  # docere
                    "Vpreactipesg2": self.inf_stem + "e",  # doce
                    "Vpreactipepl2": self.inf_stem + "ete",  # docete
                    "Vimpactsbjsg1": self.inf + "m",  # docerem
                    "Vimpactsbjsg2": self.inf + "s",  # doceres
                    "Vimpactsbjsg3": self.inf + "t",  # doceret
                    "Vimpactsbjpl1": self.inf + "mus",  # doceremus
                    "Vimpactsbjpl2": self.inf + "tis",  # doceretis
                    "Vimpactsbjpl3": self.inf + "nt",  # docerent
                    "Vplpactsbjsg1": self.per_stem + "issem",  # docuissem
                    "Vplpactsbjsg2": self.per_stem + "isses",  # docuisses
                    "Vplpactsbjsg3": self.per_stem + "isset",  # docuisset
                    "Vplpactsbjpl1": self.per_stem + "issemus",  # docuissmus
                    "Vplpactsbjpl2": self.per_stem + "issetis",  # docuissetis
                    "Vplpactsbjpl3": self.per_stem + "issent",  # docuissent
                }

            # Third conjugation
            case 3:
                self.endings = {
                    "Vpreactindsg1": self.pre,  # traho
                    "Vpreactindsg2": self.inf_stem + "is",  # trahis
                    "Vpreactindsg3": self.inf_stem + "it",  # trahit
                    "Vpreactindpl1": self.inf_stem + "imus",  # trahimus
                    "Vpreactindpl2": self.inf_stem + "itis",  # trahitis
                    "Vpreactindpl3": self.inf_stem + "unt",  # trahunt
                    "Vimpactindsg1": self.inf_stem + "ebam",  # trahebam
                    "Vimpactindsg2": self.inf_stem + "ebas",  # trahebas
                    "Vimpactindsg3": self.inf_stem + "ebat",  # trahebat
                    "Vimpactindpl1": self.inf_stem + "ebamus",  # trahebamus
                    "Vimpactindpl2": self.inf_stem + "ebatis",  # trahebatis
                    "Vimpactindpl3": self.inf_stem + "ebant",  # trahebant
                    "Vperactindsg1": self.per,  # traxi
                    "Vperactindsg2": self.per_stem + "isti",  # traxisti
                    "Vperactindsg3": self.per_stem + "it",  # traxit
                    "Vperactindpl1": self.per_stem + "imus",  # traximus
                    "Vperactindpl2": self.per_stem + "istis",  # traxistis
                    "Vperactindpl3": self.per_stem + "erunt",  # traxerunt
                    "Vplpactindsg1": self.per_stem + "eram",  # traxeram
                    "Vplpactindsg2": self.per_stem + "eras",  # traxeras
                    "Vplpactindsg3": self.per_stem + "erat",  # traxerat
                    "Vplpactindpl1": self.per_stem + "eramus",  # traxeramus
                    "Vplpactindpl2": self.per_stem + "eratis",  # traxeratis
                    "Vplpactindpl3": self.per_stem + "erant",  # traxerant
                    "Vpreactinf   ": self.inf,  # trahere
                    "Vpreactipesg2": self.inf_stem + "e",  # trahe
                    "Vpreactipepl2": self.inf_stem + "ite",  # trahite
                    "Vimpactsbjsg1": self.inf + "m",  # traherem
                    "Vimpactsbjsg2": self.inf + "s",  # traheres
                    "Vimpactsbjsg3": self.inf + "t",  # traheret
                    "Vimpactsbjpl1": self.inf + "mus",  # traheremus
                    "Vimpactsbjpl2": self.inf + "tis",  # traheretis
                    "Vimpactsbjpl3": self.inf + "nt",  # traherent
                    "Vplpactsbjsg1": self.per_stem + "issem",  # traxissem
                    "Vplpactsbjsg2": self.per_stem + "isses",  # traxisses
                    "Vplpactsbjsg3": self.per_stem + "isset",  # traxisset
                    "Vplpactsbjpl1": self.per_stem + "issemus",  # traxissemus
                    "Vplpactsbjpl2": self.per_stem + "issetis",  # traxissetis
                    "Vplpactsbjpl3": self.per_stem + "issent",  # traxissent
                }

            # Fourth conjugation
            case 4:
                self.endings = {
                    "Vpreactindsg1": self.pre,  # audio
                    "Vpreactindsg2": self.inf_stem + "is",  # audis
                    "Vpreactindsg3": self.inf_stem + "it",  # audit
                    "Vpreactindpl1": self.inf_stem + "imus",  # audimus
                    "Vpreactindpl2": self.inf_stem + "itis",  # auditis
                    "Vpreactindpl3": self.inf_stem + "iunt",  # audiunt
                    "Vimpactindsg1": self.inf_stem + "iebam",  # audiebam
                    "Vimpactindsg2": self.inf_stem + "iebas",  # audiebas
                    "Vimpactindsg3": self.inf_stem + "iebat",  # audiebat
                    "Vimpactindpl1": self.inf_stem + "iebamus",  # audiebamus
                    "Vimpactindpl2": self.inf_stem + "iebatis",  # audiebatis
                    "Vimpactindpl3": self.inf_stem + "iebant",  # audiebant
                    "Vperactindsg1": self.per,  # audivi
                    "Vperactindsg2": self.per_stem + "isti",  # audivisti
                    "Vperactindsg3": self.per_stem + "it",  # audivit
                    "Vperactindpl1": self.per_stem + "imus",  # audivimus
                    "Vperactindpl2": self.per_stem + "istis",  # audivistis
                    "Vperactindpl3": self.per_stem + "erunt",  # audiverunt
                    "Vplpactindsg1": self.per_stem + "eram",  # audiveram
                    "Vplpactindsg2": self.per_stem + "eras",  # audiveras
                    "Vplpactindsg3": self.per_stem + "erat",  # audiverat
                    "Vplpactindpl1": self.per_stem + "eramus",  # audiveramus
                    "Vplpactindpl2": self.per_stem + "eratis",  # audiveratis
                    "Vplpactindpl3": self.per_stem + "erant",  # audiverant
                    "Vpreactinf   ": self.inf,  # audire
                    "Vpreactipesg2": self.inf_stem + "i",  # audi
                    "Vpreactipepl2": self.inf_stem + "ite",  # audite
                    "Vimpactsbjsg1": self.inf + "m",  # audirem
                    "Vimpactsbjsg2": self.inf + "s",  # audires
                    "Vimpactsbjsg3": self.inf + "t",  # audiret
                    "Vimpactsbjpl1": self.inf + "mus",  # audiremus
                    "Vimpactsbjpl2": self.inf + "tis",  # audiretis
                    "Vimpactsbjpl3": self.inf + "nt",  # audirent
                    "Vplpactsbjsg1": self.per_stem + "issem",  # audivissem
                    "Vplpactsbjsg2": self.per_stem + "isses",  # audivisses
                    "Vplpactsbjsg3": self.per_stem + "isset",  # audivisset
                    "Vplpactsbjpl1": self.per_stem + "issemus",  # audivissemus
                    "Vplpactsbjpl2": self.per_stem + "issetis",  # audivissetis
                    "Vplpactsbjpl3": self.per_stem + "issent",  # audivissent
                }

            # Third conjugation -io verbs
            case 5:
                self.endings = {
                    "Vpreactindsg1": self.pre,  # capio
                    "Vpreactindsg2": self.inf_stem + "is",  # capis
                    "Vpreactindsg3": self.inf_stem + "it",  # capit
                    "Vpreactindpl1": self.inf_stem + "imus",  # capimus
                    "Vpreactindpl2": self.inf_stem + "itis",  # capitis
                    "Vpreactindpl3": self.inf_stem + "unt",  # capiunt
                    "Vimpactindsg1": self.inf_stem + "iebam",  # capiebam
                    "Vimpactindsg2": self.inf_stem + "iebas",  # capiebas
                    "Vimpactindsg3": self.inf_stem + "iebat",  # capiebat
                    "Vimpactindpl1": self.inf_stem + "iebamus",  # capiebamus
                    "Vimpactindpl2": self.inf_stem + "iebatis",  # capiebatis
                    "Vimpactindpl3": self.inf_stem + "iebant",  # capiebant
                    "Vperactindsg1": self.per,  # cepi
                    "Vperactindsg2": self.per_stem + "isti",  # cepisti
                    "Vperactindsg3": self.per_stem + "it",  # cepit
                    "Vperactindpl1": self.per_stem + "imus",  # cepimus
                    "Vperactindpl2": self.per_stem + "istis",  # cepistis
                    "Vperactindpl3": self.per_stem + "erunt",  # ceperunt
                    "Vplpactindsg1": self.per_stem + "eram",  # ceperam
                    "Vplpactindsg2": self.per_stem + "eras",  # ceperas
                    "Vplpactindsg3": self.per_stem + "erat",  # ceperat
                    "Vplpactindpl1": self.per_stem + "eramus",  # ceperamus
                    "Vplpactindpl2": self.per_stem + "eratis",  # ceperatis
                    "Vplpactindpl3": self.per_stem + "erant",  # ceperant
                    "Vpreactinf   ": self.inf,  # capere
                    "Vpreactipesg2": self.inf_stem + "e",  # cape
                    "Vpreactipepl2": self.inf_stem + "ite",  # capite
                    "Vimpactsbjsg1": self.inf + "m",  # caperem
                    "Vimpactsbjsg2": self.inf + "s",  # caperes
                    "Vimpactsbjsg3": self.inf + "t",  # caperet
                    "Vimpactsbjpl1": self.inf + "mus",  # caperemus
                    "Vimpactsbjpl2": self.inf + "tis",  # caperetis
                    "Vimpactsbjpl3": self.inf + "nt",  # caperent
                    "Vplpactsbjsg1": self.per_stem + "issem",  # cepissem
                    "Vplpactsbjsg2": self.per_stem + "isses",  # cepisses
                    "Vplpactsbjsg3": self.per_stem + "isset",  # cepisset
                    "Vplpactsbjpl1": self.per_stem + "issemus",  # cepissemus
                    "Vplpactsbjpl2": self.per_stem + "issetis",  # cepissetis
                    "Vplpactsbjpl3": self.per_stem + "issent",  # cepissent
                }

            case _:
                raise ValueError("Conjugation not recognised")

    def get(
        self,
        person: Optional[int],
        number: Optional[str],
        tense: str,
        voice: str,
        mood: str,
    ):
        try:
            if mood == "infinitive":
                return self.endings[f"V{SHORTHAND[tense]}{SHORTHAND[voice]}inf   "]
            return self.endings[
                f"V{SHORTHAND[tense]}{SHORTHAND[voice]}{SHORTHAND[mood]}{SHORTHAND[number]}{person}"
            ]

        except KeyError:
            raise ValueError(
                f"No ending found for {person} {number} {tense} {voice} {mood}"
            )

    def __repr__(self) -> str:
        return f"LearningVerb({self.pre}, {self.inf}, {self.per}, {self.ppp}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(
            f"{self.meaning}: {self.pre}, {self.inf}, {self.per}, {self.ppp} ({self.conjugation})\n\n"
        )

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LearningVerb):
            return NotImplemented
        return self.endings == other.endings

    def __hash__(self) -> int:
        return hash((self.pre, self.inf, self.per, self.ppp, self.meaning))

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented


@total_ordering
class Noun:
    def __init__(
        self, nom: str, gen: str, gender: str, meaning: Union[str, MultipleOptions]
    ) -> None:
        if gender not in ("m", "f", "n"):
            raise ValueError("Gender not recognised")

        self.nom = nom
        self.gen = gen
        self.gender = gender
        if isinstance(meaning, MultipleOptions):
            self.meaning = meaning
        else:
            self.meaning = MultipleOptions(meaning, [])

        self.first = nom

        # Find declension
        if nom in edge_cases.IRREGULAR_NOUNS:
            self.endings = edge_cases.IRREGULAR_NOUNS[nom]
            self.declension = "irregular"
            return

        if gen[-2:] == "ae":
            self.declension = 1
            self.stem = self.gen[:-2]  # puellae -> puell-
        elif gen[-1:] == "i":
            self.declension = 2
            self.stem = self.gen[:-1]  # servi -> serv-
        elif gen[-2:] == "is":
            self.declension = 3
            self.stem = self.gen[:-2]  # canis -> can-
        elif gen[-2:] == "us":
            self.declension = 4
            self.stem = self.gen[:-2]  # manus -> man-
        elif gen[-2:] == "ei":
            self.declension = 5
            self.stem = self.gen[:-2]  # diei > di-

        elif gen[-4:] == "arum":
            self.declension = 11
            self.stem = self.gen[:-4]  # puellarum -> puell-
        elif gen[-4:] == "orum":
            self.declension = 12
            self.stem = self.gen[:-4]  # servorum -> serv-
        elif gen[-2:] == "um":
            self.declension = 13
            self.stem = self.gen[:-2]  # canum -> can-
        elif gen[-4:] == "uum":
            self.declension = 14
            self.stem = self.gen[:-3]  # manuum -> man-
        elif gen[-4:] == "erum":
            self.declension = 15
            self.stem = self.gen[:-4]  # dierum > di-

        else:
            raise ValueError(
                "The genitive form is not valid (must end in ae, i, is, us, ei, arum, orum, um, uum, or erum)"
            )

        match self.declension:
            # First declension
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

            # Second declension
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

            # Third declension
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

            # Fourth declension
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

            # Fifth declension
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

            # First declension plural only
            case 11:
                self.endings = {
                    "Nnompl": self.stem + "ae",  # insidiae
                    "Nvocpl": self.stem + "ae",  # insidiae
                    "Naccpl": self.stem + "as",  # insidias
                    "Ngenpl": self.stem + "arum",  # insidiarum
                    "Ndatpl": self.stem + "is",  # insidiis
                    "Nablpl": self.stem + "is",  # insidiis
                }

            # Second declension plural only
            case 12:
                self.endings = {
                    "Nnompl": self.stem + "i",  # liberi
                    "Nvocpl": self.stem + "i",  # liberi
                    "Naccpl": self.stem + "os",  # liberos
                    "Ngenpl": self.stem + "orum",  # liberorum
                    "Ndatpl": self.stem + "is",  # liberis
                    "Nablpl": self.stem + "is",  # liberis
                }

            # Third declension plural only
            case 13:
                self.endings = {
                    "Nnompl": self.stem + "es",  # manes
                    "Nvocpl": self.stem + "es",  # manes
                    "Naccpl": self.stem + "es",  # manes
                    "Ngenpl": self.stem + "um",  # manium
                    "Ndatpl": self.stem + "ibus",  # manibus
                    "Nablpl": self.stem + "ibus",  # manibus
                }

            # Fourth declension plural only
            case 14:
                self.endings = {
                    "Nnompl": self.stem + "us",  # idus
                    "Nvocpl": self.stem + "us",  # idus
                    "Naccpl": self.stem + "us",  # idus
                    "Ngenpl": self.stem + "uum",  # iduum
                    "Ndatpl": self.stem + "ibus",  # idibus
                    "Nablpl": self.stem + "ibus",  # idibus
                }

            # Fifth declension plural only
            # NOTE  not sure if this actually exists, implemented anyway
            case 15:
                self.endings = {
                    "Nnompl": self.stem + "es",
                    "Nvocpl": self.stem + "es",
                    "Naccpl": self.stem + "es",
                    "Ngenpl": self.stem + "erum",
                    "Ndatpl": self.stem + "ebus",
                    "Nablpl": self.stem + "ebus",
                }

            case _:
                raise ValueError("Declension not recognised")

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
                raise ValueError(
                    f"Fifth declension nouns cannot be neuter (noun {self.nom})"
                )

            # For the other declensions
            self.endings["Nnompl"] = self.stem + "a"
            self.endings["Naccpl"] = self.stem + "a"
            self.endings["Nvocpl"] = self.stem + "a"

    def get(self, case: str, number: str) -> str:
        try:
            return self.endings[f"N{SHORTHAND[case]}{SHORTHAND[number]}"]
        except KeyError:
            raise ValueError(f"No ending found for case {case} or number {number}")

    def __repr__(self) -> str:
        return f"Noun({self.nom}, {self.gen}, {self.declension}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(f"{self.meaning}: {self.nom}, {self.gen} ({self.declension})")

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Noun):
            return NotImplemented
        return self.endings == other.endings

    def __hash__(self) -> int:
        return hash((self.nom, self.gen, self.gender, self.meaning))

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented


class Adjective:
    def get(self, comparison: str, gender: str, case: str, number: str) -> str:
        try:
            return self.endings[
                f"A{SHORTHAND[comparison]}{SHORTHAND[gender]}{SHORTHAND[case]}{SHORTHAND[number]}"
            ]
        except KeyError:
            raise ValueError(
                f"No ending found for comparison {comparison}, gender {gender}, case {case} or number {number}"
            )

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Adjective):
            return NotImplemented
        return self.endings == other.endings


@total_ordering
class Adjective212(Adjective):
    def __init__(
        self,
        mascnom: str,
        femnom: str,
        neutnom: str,
        meaning: Union[str, MultipleOptions],
    ) -> None:
        self.mascnom = mascnom
        self.femnom = femnom
        self.neutnom = neutnom
        if isinstance(meaning, MultipleOptions):
            self.meaning = meaning
        else:
            self.meaning = MultipleOptions(meaning, [])

        self.first = mascnom

        self.pos_stem = self.femnom[:-1]  # cara -> car-
        self.cmp_stem = self.pos_stem + "ior"  # car- -> carior-

        self.endings = {
            "Aposmnomsg": self.mascnom,  # carus
            "Aposmvocsg": self.pos_stem + "e",  # care
            "Aposmaccsg": self.pos_stem + "um",  # carum
            "Aposmgensg": self.pos_stem + "i",  # cari
            "Aposmdatsg": self.pos_stem + "o",  # caro
            "Aposmablsg": self.pos_stem + "o",  # caro
            "Aposmnompl": self.pos_stem + "i",  # cari
            "Aposmvocpl": self.pos_stem + "i",  # cari
            "Aposmaccpl": self.pos_stem + "i",  # caros
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
            "Acmpnnomsg": self.pos_stem + "ius",  # carius
            "Acmpnvocsg": self.pos_stem + "ius",  # carius
            "Acmpnaccsg": self.pos_stem + "ius",  # carius
            "Acmpngensg": self.cmp_stem + "is",  # carioris
            "Acmpndatsg": self.cmp_stem + "i",  # cariori
            "Acmpnablsg": self.cmp_stem + "e",  # cariore
            "Acmpnnompl": self.cmp_stem + "a",  # cariora
            "Acmpnvocpl": self.cmp_stem + "a",  # cariora
            "Acmpnaccpl": self.cmp_stem + "a",  # cariora
            "Acmpngenpl": self.cmp_stem + "um",  # cariorum
            "Acmpndatpl": self.cmp_stem + "ibus",  # carioribus
            "Acmpnablpl": self.cmp_stem + "ibus",  # carioribus
        }

    def __repr__(self) -> str:
        return f"Adjective212({self.mascnom}, {self.femnom}, {self.neutnom}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(f"{self.meaning}: {self.mascnom}, {self.femnom}, {self.neutnom}")

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()

    def __hash__(self) -> int:
        return hash((self.mascnom, self.femnom, self.neutnom, self.meaning))


# HACK  Very messy, but third declension adjectives are complicated
@total_ordering
class Adjective3(Adjective):
    def __init__(
        self,
        *principle_parts: str,
        termination: int,
        meaning: Union[str, MultipleOptions],
    ) -> None:
        self.principle_parts = principle_parts
        self.termination = termination
        if isinstance(meaning, MultipleOptions):
            self.meaning = meaning
        else:
            self.meaning = MultipleOptions(meaning, [])

        self.first = self.principle_parts[0]

        match termination:
            # First termination adjectives
            case 1:
                # ingens, ingentis
                if len(self.principle_parts) != 2:
                    raise ValueError(
                        "First-termination adjectives must have 2 principle parts"
                    )

                self.nom = self.principle_parts[0]
                self.gen = self.principle_parts[1]
                self.pos_stem = self.gen[:-2]  # ingentis -> ingent-
                self.cmp_stem = self.pos_stem + "ior"  # ingent- > ingentior-

                self.endings = {
                    "Aposmnomsg": self.nom,  # ingens
                    "Aposmvocsg": self.nom,  # ingens
                    "Aposmaccsg": self.pos_stem + "em",  # ingentem
                    "Aposmgensg": self.gen,  # ingentis
                    "Aposmdatsg": self.pos_stem + "i",  # ingenti
                    "Aposmablsg": self.pos_stem + "i",  # ingenti
                    "Aposmnompl": self.pos_stem + "es",  # ingentes
                    "Aposmvocpl": self.pos_stem + "es",  # ingentes
                    "Aposmaccpl": self.pos_stem + "es",  # ingentes
                    "Aposmgenpl": self.pos_stem + "ium",  # ingentium
                    "Aposmdatpl": self.pos_stem + "ibus",  # ingentibus
                    "Aposmablpl": self.pos_stem + "ibus",  # ingentibus
                    "Aposfnomsg": self.nom,  # ingens
                    "Aposfvocsg": self.nom,  # ingens
                    "Aposfaccsg": self.pos_stem + "em",  # ingentem
                    "Aposfgensg": self.gen,  # ingentis
                    "Aposfdatsg": self.pos_stem + "i",  # ingenti
                    "Aposfablsg": self.pos_stem + "i",  # ingenti
                    "Aposfnompl": self.pos_stem + "es",  # ingentes
                    "Aposfvocpl": self.pos_stem + "es",  # ingentes
                    "Aposfaccpl": self.pos_stem + "es",  # ingentes
                    "Aposfgenpl": self.pos_stem + "ium",  # ingentium
                    "Aposfdatpl": self.pos_stem + "ibus",  # ingentibus
                    "Aposfablpl": self.pos_stem + "ibus",  # ingentibus
                    "Aposnnomsg": self.nom,  # ingens
                    "Aposnvocsg": self.nom,  # ingens
                    "Aposnaccsg": self.nom,  # ingens
                    "Aposngensg": self.gen,  # ingentis
                    "Aposndatsg": self.pos_stem + "i",  # ingenti
                    "Aposnablsg": self.pos_stem + "i",  # ingenti
                    "Aposnnompl": self.pos_stem + "a",  # ingentia
                    "Aposnvocpl": self.pos_stem + "a",  # ingentia
                    "Aposnaccpl": self.pos_stem + "a",  # ingentia
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
                    "Acmpnnomsg": self.pos_stem + "ius",  # ingentius
                    "Acmpnvocsg": self.pos_stem + "ius",  # ingentius
                    "Acmpnaccsg": self.pos_stem + "ius",  # ingentius
                    "Acmpngensg": self.cmp_stem + "is",  # ingentioris
                    "Acmpndatsg": self.cmp_stem + "i",  # ingentiori
                    "Acmpnablsg": self.cmp_stem + "e",  # ingentiore
                    "Acmpnnompl": self.cmp_stem + "a",  # ingentiora
                    "Acmpnvocpl": self.cmp_stem + "a",  # ingentiora
                    "Acmpnaccpl": self.cmp_stem + "a",  # ingentiora
                    "Acmpngenpl": self.cmp_stem + "um",  # ingentiorum
                    "Acmpndatpl": self.cmp_stem + "ibus",  # ingentioribus
                    "Acmpnablpl": self.cmp_stem + "ibus",  # ingentioribus
                }

            # Second termination adjectives
            case 2:
                # fortis, forte
                if len(self.principle_parts) != 2:
                    raise ValueError(
                        "Second-termination adjectives must have 2 principle parts"
                    )

                self.mascnom = self.principle_parts[0]
                self.neutnom = self.principle_parts[1]
                self.pos_stem = self.mascnom[:-2]  # fortis -> fort-
                self.cmp_stem = self.pos_stem + "ior"  # fort- -> fortior-

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
                    "Aposngensg": self.pos_stem + "ium",  # fortium
                    "Aposndatsg": self.pos_stem + "ibus",  # fortibus
                    "Aposnablsg": self.pos_stem + "ibus",  # fortibus
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
                    "Acmpnnomsg": self.pos_stem + "ius",  # fortius
                    "Acmpnvocsg": self.pos_stem + "ius",  # fortius
                    "Acmpnaccsg": self.pos_stem + "ius",  # fortius
                    "Acmpngensg": self.cmp_stem + "is",  # fortioris
                    "Acmpndatsg": self.cmp_stem + "i",  # fortiori
                    "Acmpnablsg": self.cmp_stem + "e",  # fortiore
                    "Acmpnnompl": self.cmp_stem + "a",  # fortiora
                    "Acmpnvocpl": self.cmp_stem + "a",  # fortiora
                    "Acmpnaccpl": self.cmp_stem + "a",  # fortiora
                    "Acmpngenpl": self.cmp_stem + "um",  # fortiorum
                    "Acmpndatpl": self.cmp_stem + "ibus",  # fortioribus
                    "Acmpnablpl": self.cmp_stem + "ibus",  # fortioribus
                }

            # Third termination adjectives
            case 3:
                # acer, acris, acre
                if len(self.principle_parts) != 3:
                    raise ValueError(
                        "Third-termination adjectives must have 3 principle parts"
                    )

                self.mascnom = self.principle_parts[0]
                self.femnom = self.principle_parts[1]
                self.neutnom = self.principle_parts[2]
                self.pos_stem = self.femnom[:-2]  # acris -> acr-
                self.cmp_stem = self.pos_stem + "ior"  # acr- -> acrior-

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
                    "Acmpnnomsg": self.pos_stem + "ius",  # acrius
                    "Acmpnvocsg": self.pos_stem + "ius",  # acrius
                    "Acmpnaccsg": self.pos_stem + "ius",  # acrius
                    "Acmpngensg": self.cmp_stem + "is",  # acrioris
                    "Acmpndatsg": self.cmp_stem + "i",  # acriori
                    "Acmpnablsg": self.cmp_stem + "e",  # acriore
                    "Acmpnnompl": self.cmp_stem + "a",  # acriora
                    "Acmpnvocpl": self.cmp_stem + "a",  # acriora
                    "Acmpnaccpl": self.cmp_stem + "a",  # acriora
                    "Acmpngenpl": self.cmp_stem + "um",  # acriorum
                    "Acmpndatpl": self.cmp_stem + "ibus",  # acrioribus
                    "Acmpnablpl": self.cmp_stem + "ibus",  # acrioribus
                }

            case _:
                raise ValueError("Termination must be 1, 2 or 3")

    def __repr__(self) -> str:
        return f"Adjective3({", ".join(self.principle_parts)}, {self.termination}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(f"{self.meaning}: {", ".join(self.principle_parts)}\n")
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()

    def __hash__(self) -> int:
        return hash((self.principle_parts, self.termination, self.meaning))


@total_ordering
class Pronoun:
    def __init__(self, pronoun: str, meaning: str):
        try:
            self.endings = edge_cases.PRONOUNS[pronoun]
        except KeyError:
            raise ValueError(f"Pronoun {pronoun} not recognised")

        self.pronoun = pronoun
        self.first = self.pronoun
        self.meaning = meaning

        self.mascnom = self.endings["Pmnomsg"]
        self.femnom = self.endings["Pfnomsg"]
        self.neutnom = self.endings["Pnnomsg"]

    def get(self, gender: str, case: str, number: str):
        try:
            return self.endings[
                f"P{SHORTHAND[gender]}{SHORTHAND[case]}{SHORTHAND[number]}"
            ]
        except KeyError:
            raise ValueError(
                f"No ending found for gender {gender}, case {case} or number {number}"
            )

    def __repr__(self) -> str:
        return f"Pronoun({self.pronoun}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(f"{self.meaning}: {self.mascnom}, {self.femnom}, {self.neutnom}\n")
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()

    def __hash__(self) -> int:
        return hash((self.pronoun, self.meaning))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pronoun):
            return NotImplemented
        return self.endings == other.endings

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented
