import itertools
from dataclasses import dataclass
from functools import total_ordering
from io import StringIO
from typing import Literal, Optional, Union

from . import edge_cases
from .custom_exceptions import InvalidInputError, NoMeaningError
from .misc import Ending, Endings, Meaning, replace_at_index, CaseEnding, EndingTable

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
    # "future perfect": "fpr",
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

    def __getitem__(self, key: str) -> Ending:
        return self.endings[key]


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
        self.conjugation: Literal[0, 1, 2, 3, 4, 5]

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

        self.endings = {
            **LearningVerb._same_regular_endings(
                self.present, self.infinitive, self.perfect
            ),
            **LearningVerb._similar_regular_endings(
                self.conjugation, self.present, self.infinitive, self.perfect
            ),
            **LearningVerb._static_regular_endings(
                self.conjugation, self.present, self.infinitive, self.perfect
            ),
        }

        if self.ppp:
            self.endings.update(
                **LearningVerb._participle_endings(self.ppp, self.infinitive),
            )

    @staticmethod
    def _static_regular_endings(
        conjugation: Literal[1, 2, 3, 4, 5], present: str, infinitive: str, perfect: str
    ) -> Endings:
        # pre_stem: str = present[:-1]
        inf_stem: str = infinitive[:-3]
        # per_stem: str = perfect[:-1]

        match conjugation:
            case 1:
                return {
                    "Vpreactindsg1": present,  # porto
                    "Vpreactindpl3": inf_stem + "ant",  # portant
                    "Vpreactinf   ": infinitive,  # portare
                    "Vpreactipesg2": inf_stem + "a",  # porta
                    "Vpreactipepl2": inf_stem + "ate",  # portate
                }  # fmt: skip

            case 2:
                return {
                    "Vpreactindsg1": present,  # doceo
                    "Vpreactindpl3": inf_stem + "ent",  # docent
                    "Vpreactinf   ": infinitive,  # docere
                    "Vpreactipesg2": inf_stem + "e",  # doce
                    "Vpreactipepl2": inf_stem + "ete",  # docete
                }  # fmt: skip

            case 3:
                return {
                    "Vpreactindsg1": present,  # traho
                    "Vpreactindpl3": inf_stem + "unt",  # trahunt
                    "Vpreactinf   ": infinitive,  # trahere
                    "Vpreactipesg2": inf_stem + "e",  # trahe
                    "Vpreactipepl2": inf_stem + "ite",  # trahite
                }  # fmt: skip

            case 4:
                return {
                    "Vpreactindsg1": present,  # audio
                    "Vpreactindpl3": inf_stem + "iunt",  # audiunt
                    "Vpreactinf   ": infinitive,  # audire
                    "Vpreactipesg2": inf_stem + "i",  # audi
                    "Vpreactipepl2": inf_stem + "ite",  # audite
                }  # fmt: skip

            case 5:
                return {
                    "Vpreactindsg1": present,  # capio
                    "Vpreactindpl3": inf_stem + "iunt",  # capiunt
                    "Vpreactinf   ": infinitive,  # capere
                    "Vpreactipesg2": inf_stem + "e",  # cape
                    "Vpreactipepl2": inf_stem + "ite",  # capite
                }  # fmt: skip

            # case _:
            #    raise ValueError(f"Conjugation {conjugation} not recognised")

    @staticmethod
    def _same_regular_endings(present: str, infinitive: str, perfect: str) -> Endings:
        # pre_stem: str = present[:-1]
        # inf_stem: str = infinitive[:-3]
        per_stem: str = perfect[:-1]

        # Same endings across conjugations: perfect, pluperfect, imperfect sbj, pluperfect sbj
        SAME_ENDINGS: dict[str, tuple[str, tuple[str, ...]]] = {
            "peractind": (
                per_stem,
                ("i", "isti", "it", "imus", "istis", "erunt"),
            ),
            "plpactind": (
                per_stem,
                ("eram", "eras", "erat", "eramus", "eratis", "erant"),
            ),
            "impactsbj": (  # fmt: skip
                infinitive,
                ("m", "s", "t", "mus", "tis", "nt"),
            ),
            "plpactsbj": (
                per_stem,
                ("issem", "isses", "isset", "issemus", "issetis", "issent"),
            ),
        }

        return {
            f"V{tense}{voice}{mood}{number}{person}": SAME_ENDINGS[
                f"{tense}{voice}{mood}"
            ][0]
            + SAME_ENDINGS[f"{tense}{voice}{mood}"][1][i]
            for voice, (tense, mood), (i, (number, person)) in itertools.product(
                VOICE_SHORTHAND.values(),
                [("per", "ind"), ("plp", "ind"), ("imp", "sbj"), ("plp", "sbj")],
                enumerate(itertools.product(NUMBER_SHORTHAND.values(), range(1, 4))),
            )
            if f"{tense}{voice}{mood}" in SAME_ENDINGS
        }

    @staticmethod
    def _similar_regular_endings(
        conjugation: Literal[1, 2, 3, 4, 5], present: str, infinitive: str, perfect: str
    ) -> Endings:
        # pre_stem: str = present[:-1]
        inf_stem: str = infinitive[:-3]
        # per_stem: str = perfect[:-1]

        # Similar endings across conjugations: imperfect, present (kinda)
        SIMILAR_ENDINGS: dict[
            str, tuple[str, tuple[str, ...], tuple[Union[str, None], ...]]
        ] = {
            "impactind": (
                inf_stem,
                ("a", "e", "e", "ie", "ie"),
                ("bam", "bas", "bat", "bamus", "batis", "bant"),
            ),
            "preactind": (
                inf_stem,
                ("a", "e", "i", "i", "i"),
                (None, "s", "t", "mus", "tis", None),
            ),
        }

        return {
            f"V{tense}{voice}{mood}{number}{person}": SIMILAR_ENDINGS[  # type: ignore
                f"{tense}{voice}{mood}"
            ][0]
            + SIMILAR_ENDINGS[f"{tense}{voice}{mood}"][1][conjugation - 1]
            + suffix
            for voice, (tense, mood), (i, (number, person)) in itertools.product(
                VOICE_SHORTHAND.values(),
                [("imp", "ind"), ("pre", "ind")],
                enumerate(itertools.product(NUMBER_SHORTHAND.values(), range(1, 4))),
            )
            if f"{tense}{voice}{mood}" in SIMILAR_ENDINGS
            and (suffix := SIMILAR_ENDINGS[f"{tense}{voice}{mood}"][2][i])
        }

    @staticmethod
    def _participle_endings(ppp: str, infinitive: str) -> Endings:
        _preptc_stem: str = infinitive[:-2]
        _ppp_stem: str = ppp[:-2]
        return {
                "Vpreactptcmnomsg": _preptc_stem + "ns",
                "Vpreactptcmvocsg": _preptc_stem + "ns",
                "Vpreactptcmaccsg": _preptc_stem + "ntem",
                "Vpreactptcmgensg": _preptc_stem + "ntis",
                "Vpreactptcmdatsg": _preptc_stem + "nti",
                "Vpreactptcmablsg": _preptc_stem + "nte",
                "Vpreactptcmnompl": _preptc_stem + "ntes",
                "Vpreactptcmvocpl": _preptc_stem + "ntes",
                "Vpreactptcmaccpl": _preptc_stem + "ntes",
                "Vpreactptcmgenpl": _preptc_stem + "ntium",
                "Vpreactptcmdatpl": _preptc_stem + "ntibus",
                "Vpreactptcmablpl": _preptc_stem + "ntibus",
                "Vpreactptcfnomsg": _preptc_stem + "ns",
                "Vpreactptcfvocsg": _preptc_stem + "ns",
                "Vpreactptcfaccsg": _preptc_stem + "ntem",
                "Vpreactptcfgensg": _preptc_stem + "ntis",
                "Vpreactptcfdatsg": _preptc_stem + "nti",
                "Vpreactptcfablsg": _preptc_stem + "nte",
                "Vpreactptcfnompl": _preptc_stem + "ntes",
                "Vpreactptcfvocpl": _preptc_stem + "ntes",
                "Vpreactptcfaccpl": _preptc_stem + "ntes",
                "Vpreactptcfgenpl": _preptc_stem + "ntium",
                "Vpreactptcfdatpl": _preptc_stem + "ntibus",
                "Vpreactptcfablpl": _preptc_stem + "ntibus",
                "Vpreactptcnnomsg": _preptc_stem + "ns",
                "Vpreactptcnvocsg": _preptc_stem + "ns",
                "Vpreactptcnaccsg": _preptc_stem + "ns",
                "Vpreactptcngensg": _preptc_stem + "ntis",
                "Vpreactptcndatsg": _preptc_stem + "nti",
                "Vpreactptcnablsg": _preptc_stem + "nte",
                "Vpreactptcnnompl": _preptc_stem + "ntia",
                "Vpreactptcnvocpl": _preptc_stem + "ntia",
                "Vpreactptcnaccpl": _preptc_stem + "ntia",
                "Vpreactptcngenpl": _preptc_stem + "ntium",
                "Vpreactptcndatpl": _preptc_stem + "ntibus",
                "Vpreactptcnablpl": _preptc_stem + "ntibus",
                "Vperpasptcmnomsg": ppp,
                "Vperpasptcmvocsg": _ppp_stem + "e",
                "Vperpasptcmaccsg": _ppp_stem + "um",
                "Vperpasptcmgensg": _ppp_stem + "i",
                "Vperpasptcmdatsg": _ppp_stem + "o",
                "Vperpasptcmablsg": _ppp_stem + "o",
                "Vperpasptcmnompl": _ppp_stem + "i",
                "Vperpasptcmvocpl": _ppp_stem + "i",
                "Vperpasptcmaccpl": _ppp_stem + "os",
                "Vperpasptcmgenpl": _ppp_stem + "orum",
                "Vperpasptcmdatpl": _ppp_stem + "is",
                "Vperpasptcmablpl": _ppp_stem + "is",
                "Vperpasptcfnomsg": _ppp_stem + "a",
                "Vperpasptcfvocsg": _ppp_stem + "a",
                "Vperpasptcfaccsg": _ppp_stem + "am",
                "Vperpasptcfgensg": _ppp_stem + "ae",
                "Vperpasptcfdatsg": _ppp_stem + "ae",
                "Vperpasptcfablsg": _ppp_stem + "a",
                "Vperpasptcfnompl": _ppp_stem + "ae",
                "Vperpasptcfvocpl": _ppp_stem + "ae",
                "Vperpasptcfaccpl": _ppp_stem + "as",
                "Vperpasptcfgenpl": _ppp_stem + "arum",
                "Vperpasptcfdatpl": _ppp_stem + "is",
                "Vperpasptcfablpl": _ppp_stem + "is",
                "Vperpasptcnnomsg": _ppp_stem + "um",
                "Vperpasptcnvocsg": _ppp_stem + "um",
                "Vperpasptcnaccsg": _ppp_stem + "um",
                "Vperpasptcngensg": _ppp_stem + "i",
                "Vperpasptcndatsg": _ppp_stem + "o",
                "Vperpasptcnablsg": _ppp_stem + "o",
                "Vperpasptcnnompl": _ppp_stem + "a",
                "Vperpasptcnvocpl": _ppp_stem + "a",
                "Vperpasptcnaccpl": _ppp_stem + "a",
                "Vperpasptcngenpl": _ppp_stem + "orum",
                "Vperpasptcndatpl": _ppp_stem + "is",
                "Vperpasptcnablpl": _ppp_stem + "is",
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
    NOUN_ENDINGS: tuple[EndingTable, ...] = (
        (
            CaseEnding(None, "ae"),
            CaseEnding(None, "ae"),
            CaseEnding("am", "as"),
            CaseEnding("ae", "arum"),
            CaseEnding("ae", "is"),
            CaseEnding("a", "is"),
        ),
        (
            CaseEnding(None, "i"),
            CaseEnding(None, "i"),
            CaseEnding("um", "os"),
            CaseEnding("i", "orum"),
            CaseEnding("o", "is"),
            CaseEnding("o", "is"),
        ),
        (
            CaseEnding(None, "es"),
            CaseEnding(None, "es"),
            CaseEnding("em", "es"),
            CaseEnding("is", "um"),
            CaseEnding("i", "ibus"),
            CaseEnding("e", "ibus"),
        ),
        (
            CaseEnding(None, "us"),
            CaseEnding(None, "us"),
            CaseEnding("um", "us"),
            CaseEnding("us", "uum"),
            CaseEnding("ui", "ibus"),
            CaseEnding("us", "ibus"),
        ),
        (
            CaseEnding(None, "es"),
            CaseEnding(None, "es"),
            CaseEnding("em", "es"),
            CaseEnding("ei", "erum"),
            CaseEnding("ei", "ebus"),
            CaseEnding("e", "ebus"),
        ),
    )

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
        if gender not in GENDER_SHORTHAND.values():
            if gender not in GENDER_SHORTHAND:
                raise InvalidInputError(f"Gender '{gender}' not recognised")
            self.gender = GENDER_SHORTHAND[gender]
        else:
            self.gender = gender

        self.nominative: str = nominative
        self.genitive: str = genitive
        self.meaning: Meaning = meaning
        self.declension: Literal[0, 1, 2, 3, 4, 5]

        self.first = self.nominative

        if self.nominative in edge_cases.IRREGULAR_NOUNS:
            self.endings = edge_cases.IRREGULAR_NOUNS[nominative]
            self.declension = 0
            return

        # The ordering of this is strange because e.g. ending -ei ends in 'i' as well as 'ei'
        # so 5th declension check must come before 2nd declension check, etc.
        DECLENSION_MAP: dict[
            str, tuple[Literal[1, 2, 3, 4, 5], int, Optional[bool]]
        ] = {
            "ei": (5, -2, None),
            "ae": (1, -2, None),
            "i": (2, -1, None),
            "is": (3, -2, None),
            "us": (4, -2, None),
            "uum": (4, -3, True),
            "arum": (1, -4, True),
            "orum": (2, -4, True),
            "erum": (5, -4, True),
            "um": (3, -2, True),
        }

        for ending, (declension, stem_slice, plurale_tantum) in DECLENSION_MAP.items():
            if self.genitive.endswith(ending):
                self.declension = declension
                self.stem: str = self.genitive[:stem_slice]
                self.plurale_tantum: bool = bool(plurale_tantum)
                break
        else:
            raise InvalidInputError(f"Genitive form '{self.genitive}' is not valid")

        self.endings = {
            **Noun._same_regular_endings(self.stem, self.declension),
            **Noun._static_regular_endings(
                self.nominative, self.genitive, self.stem, self.declension
            ),
        }

        if self.gender == "n":
            self.endings["Naccsg"] = self.nominative
            self.endings["Nvocsg"] = self.nominative

            if self.declension == 4:
                self.endings["Nnompl"] = self.stem + "ua"  # cornua
                self.endings["Naccpl"] = self.stem + "ua"  # cornua
                self.endings["Nvocpl"] = self.stem + "ua"  # cornua
                self.endings["Ndatpl"] = self.stem + "ua"  # cornua
                return
            elif self.declension == 5:
                raise InvalidInputError(
                    f"Fifth declension nouns cannot be neuter (noun '{self.nominative}')"
                )

            # For the other declensions
            self.endings["Nnompl"] = self.stem + "a"
            self.endings["Naccpl"] = self.stem + "a"
            self.endings["Nvocpl"] = self.stem + "a"

        if self.plurale_tantum:
            self.endings = {
                k: v for k, v in self.endings.items() if not k.endswith("sg")
            }

    @staticmethod
    def _same_regular_endings(stem: str, declension: Literal[1, 2, 3, 4, 5]) -> Endings:
        return {
            f"N{case}{number}": stem
            + getattr(Noun.NOUN_ENDINGS[declension - 1][count], number)
            for count, case in enumerate(CASE_SHORTHAND.values())
            for number in NUMBER_SHORTHAND.values()
            if getattr(Noun.NOUN_ENDINGS[declension - 1][count], number)
        }

    @staticmethod
    def _static_regular_endings(
        nom: str, gen: str, stem: str, declension: Literal[1, 2, 3, 4, 5]
    ) -> Endings:
        match declension:
            case 1 | 3 | 4 | 5:
                return {
                    "Nnomsg": nom,  # puella
                    "Nvocsg": nom,  # puella
                }

            case 2:
                return {
                    "Nnomsg": nom,  # servus
                    "Nvocsg": nom if nom[-2:] == "er" else stem + "e",  # serve
                }

            # case _:
            #    raise ValueError(f"Declension {declension} not recognised")

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
        return (
            f"Noun({self.nominative}, {self.genitive}, {self.gender}, {self.meaning})"
        )

    def __str__(self) -> str:
        output: StringIO = StringIO()
        output.write(
            f"{self.meaning}: {self.nominative}, {self.genitive} ({self.declension})"
        )

        for _, item in self.endings.items():
            output.write(item + "\n")

        return output.getvalue()


@total_ordering
class Adjective(Word):
    def __init__(
        self,
        *principal_parts: str,
        termination: Optional[int] = None,
        declension: Literal["212", "3"],
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
        self.declension: Literal["212", "3"] = declension
        self.termination: Optional[int] = termination

        ADJECTIVE1_ENDINGS: EndingTable = Noun.NOUN_ENDINGS[0]

        ADJECTIVE2_ENDINGS: EndingTable = replace_at_index(
            Noun.NOUN_ENDINGS[1],  # type: ignore
            1,
            CaseEnding("e", "i"),
        )

        ADJECTIVE3_ENDINGS: EndingTable = (
            CaseEnding(None, "es"),
            CaseEnding(None, "es"),
            CaseEnding("em", "es"),
            CaseEnding("is", "ium"),
            CaseEnding("i", "ibus"),
            CaseEnding("i", "ibus"),
        )

        ADJECTIVE2N_ENDINGS: EndingTable = Noun.NOUN_ENDINGS[1]
        for i in range(3):
            ADJECTIVE2N_ENDINGS = replace_at_index(
                ADJECTIVE2N_ENDINGS, i, CaseEnding(None, "a")
            )

        ADJECTIVE3N_ENDINGS: EndingTable = (
            CaseEnding(None, "ia"),
            CaseEnding(None, "ia"),
            CaseEnding(None, "ia"),
            CaseEnding("is", "ium"),
            CaseEnding("i", "ibus"),
            CaseEnding("i", "ibus"),
        )

        ADJECTIVE3C_ENDINGS: EndingTable = Noun.NOUN_ENDINGS[2]
        ADJECTIVE3CN_ENDINGS: EndingTable = ADJECTIVE3C_ENDINGS
        for i in range(3):
            ADJECTIVE3CN_ENDINGS = replace_at_index(
                ADJECTIVE3CN_ENDINGS, i, CaseEnding(None, "a")
            )

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
                Adjective._comparative_stem(self)

                self.endings = {
                    **Adjective._endings_from_table(
                        ADJECTIVE2_ENDINGS, self.pos_stem, "pos", "m"
                    ),
                    **Adjective._endings_from_table(
                        ADJECTIVE1_ENDINGS, self.pos_stem, "pos", "f"
                    ),
                    **Adjective._endings_from_table(
                        ADJECTIVE2N_ENDINGS, self.pos_stem, "pos", "n"
                    ),
                    **{
                        "Aposmnomsg": self.mascnom,  # carus
                        "Aposfnomsg": self.femnom,  # cara
                        "Aposfvocsg": self.femnom,  # cara
                        "Aposnnomsg": self.neutnom,  # carum
                        "Aposnvocsg": self.neutnom,  # carum
                        "Aposnaccsg": self.neutnom,  # carum
                        "Dpos": self.irregular_posadv
                        if self.irregular_flag
                        else self.pos_stem + "e",
                        "Dcmp": self.irregular_cmpadv
                        if self.irregular_flag
                        else self.pos_stem + "ius",
                        "Dspr": self.irregular_spradv
                        if self.irregular_flag
                        else self.spr_stem + "e",
                    },
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
                        Adjective._comparative_stem(self)

                        self.endings = {
                            "Aposmnomsg": self.mascnom,  # ingens
                            "Aposmvocsg": self.mascnom,  # ingens
                            "Aposfnomsg": self.mascnom,  # ingens
                            "Aposfvocsg": self.mascnom,  # ingens
                            "Aposnnomsg": self.mascnom,  # ingens
                            "Aposnvocsg": self.mascnom,  # ingens
                            "Aposnaccsg": self.mascnom,  # ingens
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
                        Adjective._comparative_stem(self)

                        self.endings = {
                            "Aposmnomsg": self.mascnom,  # fortis
                            "Aposmvocsg": self.mascnom,  # fortis
                            "Aposfnomsg": self.mascnom,  # fortis
                            "Aposfvocsg": self.mascnom,  # fortis
                            "Aposnnomsg": self.neutnom,  # forte
                            "Aposnvocsg": self.neutnom,  # forte
                            "Aposnaccsg": self.neutnom,  # forte
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

                        self.femnom = self.principal_parts[1]
                        self.neutnom = self.principal_parts[2]

                        self.pos_stem = self.femnom[:-2]  # acris -> acr-
                        Adjective._comparative_stem(self)

                        self.endings = {
                            "Aposmnomsg": self.mascnom,  # acer
                            "Aposmvocsg": self.mascnom,  # acer
                            "Aposfnomsg": self.femnom,  # acris
                            "Aposfvocsg": self.femnom,  # acris
                            "Aposnnomsg": self.neutnom,  # acre
                            "Aposnvocsg": self.neutnom,  # acre
                            "Aposnaccsg": self.neutnom,  # acre
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

                self.endings.update(
                    {
                        **Adjective._endings_from_table(
                            ADJECTIVE3_ENDINGS, self.pos_stem, "pos", "m"
                        ),
                        **Adjective._endings_from_table(
                            ADJECTIVE3_ENDINGS, self.pos_stem, "pos", "f"
                        ),
                        **Adjective._endings_from_table(
                            ADJECTIVE3N_ENDINGS, self.pos_stem, "pos", "n"
                        ),
                    }
                )
            case _:
                raise InvalidInputError(f"Declension {self.declension} not recognised")

        self.endings.update(
            {
                **Adjective._endings_from_table(
                    ADJECTIVE3C_ENDINGS, self.cmp_stem, "cmp", "m"
                ),
                **Adjective._endings_from_table(
                    ADJECTIVE3C_ENDINGS, self.cmp_stem, "cmp", "f"
                ),
                **Adjective._endings_from_table(
                    ADJECTIVE3CN_ENDINGS, self.cmp_stem, "cmp", "n"
                ),
                "Acmpmnomsg": self.cmp_stem,  # carior
                "Acmpmvocsg": self.cmp_stem,  # carior
                "Acmpfnomsg": self.cmp_stem,  # carior
                "Acmpfvocsg": self.cmp_stem,  # carior
                "Acmpnnomsg": self.cmp_stem[:-3] + "ius",  # carius
                "Acmpnvocsg": self.cmp_stem[:-3] + "ius",  # carius
                "Acmpnaccsg": self.cmp_stem[:-3] + "ius",  # carius
                **Adjective._endings_from_table(
                    ADJECTIVE2_ENDINGS, self.spr_stem, "spr", "m"
                ),
                **Adjective._endings_from_table(
                    ADJECTIVE1_ENDINGS, self.spr_stem, "spr", "f"
                ),
                **Adjective._endings_from_table(
                    ADJECTIVE2N_ENDINGS, self.spr_stem, "spr", "n"
                ),
                "Asprmnomsg": self.spr_stem + "us",  # carrissimus
                "Asprfnomsg": self.spr_stem + "a",  # carrissima
                "Asprfvocsg": self.spr_stem + "a",  # carrissima
                "Asprnnomsg": self.spr_stem + "um",  # carrissimum
                "Asprnvocsg": self.spr_stem + "um",  # carrissimum
                "Asprnaccsg": self.spr_stem + "um",  # carrissimum
            }
        )

    def _comparative_stem(self) -> None:
        # FIXME: some adjectives don't have adverbs!
        #        bug probably to be left in, a bit complicated to fix
        self.irregular_flag: bool = False

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
            return

        self.cmp_stem = self.pos_stem + "ior"  # car- -> carior-
        if self.mascnom[-2:] == "er":
            self.spr_stem = self.mascnom + "rim"  # miser- -> miserrim-
        elif self.mascnom in edge_cases.LIS_ADJECTIVES:
            self.spr_stem = self.pos_stem + "lim"  # facil- -> facillim-
        else:
            self.spr_stem = self.pos_stem + "issim"  # car- -> carissim-

    @staticmethod
    def _endings_from_table(
        endings_table: EndingTable,
        stem: str,
        degree: Literal["pos", "cmp", "spr"],
        gender: Literal["m", "f", "n"],
    ) -> Endings:
        if (degree not in {"pos", "cmp", "spr"}) or (gender not in {"m", "f", "n"}):
            raise ValueError

        return {
            f"A{degree}{gender}{case}{number}": stem
            + getattr(endings_table[count], number)
            for count, case in enumerate(CASE_SHORTHAND.values())
            for number in NUMBER_SHORTHAND.values()
            if getattr(endings_table[count], number)
        }

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
