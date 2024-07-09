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
        return (
            self.pre,
            self.inf,
            self.per,
            self.ppp,
            self.meaning,
        ) == (
            other.pre,
            other.inf,
            other.per,
            other.ppp,
            other.meaning,
        )

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
        if not isinstance(other, LearningVerb):
            return NotImplemented
        return (self.nom, self.gen, self.gender, self.meaning) == (
            other.nom,
            other.gen,
            other.gender,
            other.meaning,
        )

    def __hash__(self) -> int:
        return hash((self.nom, self.gen, self.gender, self.meaning))

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented


@total_ordering
class Adjective212:
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

        self.stem = self.femnom[:-1]  # bona -> bon-

        self.endings = {
            "Amnomsg": self.mascnom,  # bonus
            "Amvocsg": self.stem + "e",  # bone
            "Amaccsg": self.stem + "um",  # bonum
            "Amgensg": self.stem + "i",  # boni
            "Amdatsg": self.stem + "o",  # bono
            "Amablsg": self.stem + "o",  # bono
            "Amnompl": self.stem + "i",  # boni
            "Amvocpl": self.stem + "i",  # boni
            "Amaccpl": self.stem + "i",  # bonos
            "Amgenpl": self.stem + "orum",  # bonorum
            "Amdatpl": self.stem + "is",  # bonis
            "Amablpl": self.stem + "is",  # bonis
            "Afnomsg": self.femnom,  # bona
            "Afvocsg": self.femnom,  # bona
            "Afaccsg": self.stem + "am",  # bonam
            "Afgensg": self.stem + "ae",  # bonae
            "Afdatsg": self.stem + "ae",  # bonae
            "Afablsg": self.stem + "a",  # bona
            "Afnompl": self.stem + "ae",  # bonae
            "Afvocpl": self.stem + "ae",  # bonae
            "Afaccpl": self.stem + "as",  # bonas
            "Afgenpl": self.stem + "arum",  # bonarum
            "Afdatpl": self.stem + "is",  # bonis
            "Afablpl": self.stem + "is",  # bonis
            "Annomsg": self.neutnom,  # bonum
            "Anvocsg": self.neutnom,  # bonum
            "Anaccsg": self.neutnom,  # bonum
            "Angensg": self.stem + "i",  # boni
            "Andatsg": self.stem + "o",  # bono
            "Anablsg": self.stem + "o",  # bono
            "Annompl": self.stem + "a",  # bona
            "Anvocpl": self.stem + "a",  # bona
            "Anaccpl": self.stem + "a",  # bona
            "Angenpl": self.stem + "orum",  # bonorum
            "Andatpl": self.stem + "is",  # bonis
            "Anablpl": self.stem + "is",  # bonis
        }

    def get(self, gender: str, case: str, number: str) -> str:
        try:
            return self.endings[
                f"A{SHORTHAND[gender]}{SHORTHAND[case]}{SHORTHAND[number]}"
            ]
        except KeyError:
            raise ValueError(
                f"No ending found for gender {gender}, case {case} or number {number}"
            )

    def __repr__(self) -> str:
        return f"Adjective212({self.mascnom}, {self.femnom}, {self.neutnom}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(f"{self.meaning}: {self.mascnom}, {self.femnom}, {self.neutnom}")

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LearningVerb):
            return NotImplemented
        return (self.mascnom, self.femnom, self.neutnom, self.meaning) == (
            other.mascnom,
            other.femnom,
            other.neutnom,
            other.meaning,
        )

    def __hash__(self) -> int:
        return hash((self.mascnom, self.femnom, self.neutnom, self.meaning))

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented


# HACK  Very messy, but third declension adjectives are complicated
@total_ordering
class Adjective3:
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
                self.stem = self.gen[:-2]  # ingentis -> ingent-

                self.endings = {
                    "Amnomsg": self.nom,  # ingens
                    "Amvocsg": self.nom,  # ingens
                    "Amaccsg": self.stem + "em",  # ingentem
                    "Amgensg": self.gen,  # ingentis
                    "Amdatsg": self.stem + "i",  # ingenti
                    "Amablsg": self.stem + "i",  # ingenti  TODO  is this right?
                    "Amnompl": self.stem + "es",  # ingentes
                    "Amvocpl": self.stem + "es",  # ingentes
                    "Amaccpl": self.stem + "es",  # ingentes
                    "Amgenpl": self.stem + "ium",  # ingentium
                    "Amdatpl": self.stem + "ibus",  # ingentibus
                    "Amablpl": self.stem + "ibus",  # ingentibus
                    "Afnomsg": self.nom,  # ingens
                    "Afvocsg": self.nom,  # ingens
                    "Afaccsg": self.stem + "em",  # ingentem
                    "Afgensg": self.gen,  # ingentis
                    "Afdatsg": self.stem + "i",  # ingenti
                    "Afablsg": self.stem + "i",  # ingenti
                    "Afnompl": self.stem + "es",  # ingentes
                    "Afvocpl": self.stem + "es",  # ingentes
                    "Afaccpl": self.stem + "es",  # ingentes
                    "Afgenpl": self.stem + "ium",  # ingentium
                    "Afdatpl": self.stem + "ibus",  # ingentibus
                    "Afablpl": self.stem + "ibus",  # ingentibus
                    "Annomsg": self.nom,  # ingens
                    "Anvocsg": self.nom,  # ingens
                    "Anaccsg": self.nom,  # ingens
                    "Angensg": self.gen,  # ingentis
                    "Andatsg": self.stem + "i",  # ingenti
                    "Anablsg": self.stem + "i",  # ingenti
                    "Annompl": self.stem + "a",  # ingentia
                    "Anvocpl": self.stem + "a",  # ingentia
                    "Anaccpl": self.stem + "a",  # ingentia
                    "Angenpl": self.stem + "ium",  # ingentium
                    "Andatpl": self.stem + "ibus",  # ingentibus
                    "Anablpl": self.stem + "ibus",  # ingentibus
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
                self.stem = self.mascnom[:-2]  # fortis -> fort-

                self.endings = {
                    "Amnomsg": self.mascnom,  # fortis
                    "Amvocsg": self.mascnom,  # fortis
                    "Amaccsg": self.stem + "em",  # fortem
                    "Amgensg": self.stem + "is",  # fortis
                    "Amdatsg": self.stem + "i",  # forti
                    "Amablsg": self.stem + "i",  # forti
                    "Amnompl": self.stem + "es",  # fortes
                    "Amvocpl": self.stem + "es",  # fortes
                    "Amaccpl": self.stem + "es",  # fortes
                    "Amgenpl": self.stem + "ium",  # fortium
                    "Amdatpl": self.stem + "ibus",  # fortibus
                    "Amablpl": self.stem + "ibus",  # fortibus
                    "Afnomsg": self.mascnom,  # fortis
                    "Afvocsg": self.mascnom,  # fortis
                    "Afaccsg": self.stem + "em",  # fortem
                    "Afgensg": self.stem + "is",  # fortis
                    "Afdatsg": self.stem + "i",  # forti
                    "Afablsg": self.stem + "i",  # forti
                    "Afnompl": self.stem + "es",  # fortes
                    "Afvocpl": self.stem + "es",  # fortes
                    "Afaccpl": self.stem + "es",  # fortes
                    "Afgenpl": self.stem + "ium",  # fortium
                    "Afdatpl": self.stem + "ibus",  # fortibus
                    "Afablpl": self.stem + "ibus",  # fortibus
                    "Annomsg": self.neutnom,  # forte
                    "Anvocsg": self.neutnom,  # forte
                    "Anaccsg": self.neutnom,  # forte
                    "Angensg": self.stem + "ium",  # fortium
                    "Andatsg": self.stem + "ibus",  # fortibus
                    "Anablsg": self.stem + "ibus",  # fortibus
                    "Annompl": self.stem + "ia",  # fortia
                    "Anvocpl": self.stem + "ia",  # fortia
                    "Anaccpl": self.stem + "ia",  # fortia
                    "Angenpl": self.stem + "ium",  # fortium
                    "Andatpl": self.stem + "ibus",  # fortibus
                    "Anablpl": self.stem + "ibus",  # fortibus
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
                self.stem = self.mascnom[:-2]  # acer -> ac-

                self.endings = {
                    "Amnomsg": self.mascnom,  # acer
                    "Amvocsg": self.mascnom,  # acer
                    "Amaccsg": self.stem + "em",  # acrem
                    "Amgensg": self.stem + "is",  # acris
                    "Amdatsg": self.stem + "i",  # acri
                    "Amablsg": self.stem + "i",  # acri
                    "Amnompl": self.stem + "es",  # acres
                    "Amvocpl": self.stem + "es",  # acres
                    "Amaccpl": self.stem + "es",  # acres
                    "Amgenpl": self.stem + "ium",  # acrium
                    "Amdatpl": self.stem + "ibus",  # acribus
                    "Amablpl": self.stem + "ibus",  # acribus
                    "Afnomsg": self.femnom,  # acris
                    "Afvocsg": self.femnom,  # acris
                    "Afaccsg": self.stem + "em",  # acrem
                    "Afgensg": self.stem + "is",  # acris
                    "Afdatsg": self.stem + "i",  # acri
                    "Afablsg": self.stem + "i",  # acri
                    "Afnompl": self.stem + "es",  # acres
                    "Afvocpl": self.stem + "es",  # acres
                    "Afaccpl": self.stem + "es",  # acres
                    "Afgenpl": self.stem + "ium",  # acrium
                    "Afdatpl": self.stem + "ibus",  # acribus
                    "Afablpl": self.stem + "ibus",  # acribus
                    "Annomsg": self.neutnom,  # acre
                    "Anvocsg": self.neutnom,  # acre
                    "Anaccsg": self.neutnom,  # acre
                    "Angensg": self.stem + "is",  # acris
                    "Andatsg": self.stem + "i",  # acri
                    "Anablsg": self.stem + "i",  # acri
                    "Annompl": self.stem + "ia",  # acria
                    "Anvocpl": self.stem + "ia",  # acria
                    "Anaccpl": self.stem + "ia",  # acria
                    "Angenpl": self.stem + "ium",  # acrium
                    "Andatpl": self.stem + "ibus",  # acribus
                    "Anablpl": self.stem + "ibus",  # acribus
                }

            case _:
                raise ValueError("Termination must be 1, 2 or 3")

    def get(self, gender: str, case: str, number: str) -> str:
        try:
            return self.endings[
                f"A{SHORTHAND[gender]}{SHORTHAND[case]}{SHORTHAND[number]}"
            ]
        except KeyError:
            raise ValueError(
                f"No ending found for gender {gender}, case {case} or number {number}"
            )

    def __repr__(self) -> str:
        return f"Adjective3({", ".join(self.principle_parts)}, {self.termination}, {self.meaning})"

    def __str__(self) -> str:
        output = StringIO()
        output.write(f"{self.meaning}: {self.nom}, {self.gen}\n")
        for _, item in self.endings.items():
            output.write(item + "\n")
        return output.getvalue()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Adjective3):
            return NotImplemented
        return (self.principle_parts, self.termination, self.meaning) == (
            other.principle_parts,
            other.termination,
            other.meaning,
        )

    def __hash__(self) -> int:
        return hash((self.principle_parts, self.termination, self.meaning))

    def __lt__(self, other: object) -> bool:
        try:
            return self.first < other.first
        except AttributeError:
            return NotImplemented
