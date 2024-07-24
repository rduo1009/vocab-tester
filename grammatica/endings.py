import itertools
from dataclasses import dataclass
from functools import total_ordering
from io import StringIO
from typing import Literal, Optional, Union

from . import edge_cases
from .custom_exceptions import InvalidInputError, NoEndingError
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
class _Word:
    def __init__(self) -> None:
        self.endings: Endings
        self._first: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _Word):
            return NotImplemented
        return self.endings == other.endings

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, _Word):
            return NotImplemented
        return self._first < other._first  # type: ignore

    def __hash__(self) -> int:
        return hash(self.endings)

    def __getitem__(self, key: str) -> Ending:
        return self.endings[key]


@dataclass
class BasicWord(_Word):
    word: str
    meaning: Meaning

    def __post_init__(self) -> None:
        self.endings: Endings = {"": self.word}

    def get(self) -> str:
        return self.word


@total_ordering
class LearningVerb(_Word):
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

        self._first = self.present
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

        self.endings = LearningVerb._same_regular_endings(
            self.present, self.infinitive, self.perfect
        )

        self.endings.update(
            LearningVerb._similar_regular_endings(
                self.conjugation, self.present, self.infinitive, self.perfect
            )
        )
        self.endings.update(
            LearningVerb._static_regular_endings(
                self.conjugation, self.present, self.infinitive, self.perfect
            )
        )

        if self.ppp:
            self.endings.update(
                LearningVerb._participle_endings(self.ppp, self.infinitive)
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
        preptc_stem: str = infinitive[:-2]
        ppp_stem: str = ppp[:-2]
        return {
                "Vpreactptcmnomsg": preptc_stem + "ns",
                "Vpreactptcmvocsg": preptc_stem + "ns",
                "Vpreactptcmaccsg": preptc_stem + "ntem",
                "Vpreactptcmgensg": preptc_stem + "ntis",
                "Vpreactptcmdatsg": preptc_stem + "nti",
                "Vpreactptcmablsg": preptc_stem + "nte",
                "Vpreactptcmnompl": preptc_stem + "ntes",
                "Vpreactptcmvocpl": preptc_stem + "ntes",
                "Vpreactptcmaccpl": preptc_stem + "ntes",
                "Vpreactptcmgenpl": preptc_stem + "ntium",
                "Vpreactptcmdatpl": preptc_stem + "ntibus",
                "Vpreactptcmablpl": preptc_stem + "ntibus",
                "Vpreactptcfnomsg": preptc_stem + "ns",
                "Vpreactptcfvocsg": preptc_stem + "ns",
                "Vpreactptcfaccsg": preptc_stem + "ntem",
                "Vpreactptcfgensg": preptc_stem + "ntis",
                "Vpreactptcfdatsg": preptc_stem + "nti",
                "Vpreactptcfablsg": preptc_stem + "nte",
                "Vpreactptcfnompl": preptc_stem + "ntes",
                "Vpreactptcfvocpl": preptc_stem + "ntes",
                "Vpreactptcfaccpl": preptc_stem + "ntes",
                "Vpreactptcfgenpl": preptc_stem + "ntium",
                "Vpreactptcfdatpl": preptc_stem + "ntibus",
                "Vpreactptcfablpl": preptc_stem + "ntibus",
                "Vpreactptcnnomsg": preptc_stem + "ns",
                "Vpreactptcnvocsg": preptc_stem + "ns",
                "Vpreactptcnaccsg": preptc_stem + "ns",
                "Vpreactptcngensg": preptc_stem + "ntis",
                "Vpreactptcndatsg": preptc_stem + "nti",
                "Vpreactptcnablsg": preptc_stem + "nte",
                "Vpreactptcnnompl": preptc_stem + "ntia",
                "Vpreactptcnvocpl": preptc_stem + "ntia",
                "Vpreactptcnaccpl": preptc_stem + "ntia",
                "Vpreactptcngenpl": preptc_stem + "ntium",
                "Vpreactptcndatpl": preptc_stem + "ntibus",
                "Vpreactptcnablpl": preptc_stem + "ntibus",
                "Vperpasptcmnomsg": ppp,
                "Vperpasptcmvocsg": ppp_stem + "e",
                "Vperpasptcmaccsg": ppp_stem + "um",
                "Vperpasptcmgensg": ppp_stem + "i",
                "Vperpasptcmdatsg": ppp_stem + "o",
                "Vperpasptcmablsg": ppp_stem + "o",
                "Vperpasptcmnompl": ppp_stem + "i",
                "Vperpasptcmvocpl": ppp_stem + "i",
                "Vperpasptcmaccpl": ppp_stem + "os",
                "Vperpasptcmgenpl": ppp_stem + "orum",
                "Vperpasptcmdatpl": ppp_stem + "is",
                "Vperpasptcmablpl": ppp_stem + "is",
                "Vperpasptcfnomsg": ppp_stem + "a",
                "Vperpasptcfvocsg": ppp_stem + "a",
                "Vperpasptcfaccsg": ppp_stem + "am",
                "Vperpasptcfgensg": ppp_stem + "ae",
                "Vperpasptcfdatsg": ppp_stem + "ae",
                "Vperpasptcfablsg": ppp_stem + "a",
                "Vperpasptcfnompl": ppp_stem + "ae",
                "Vperpasptcfvocpl": ppp_stem + "ae",
                "Vperpasptcfaccpl": ppp_stem + "as",
                "Vperpasptcfgenpl": ppp_stem + "arum",
                "Vperpasptcfdatpl": ppp_stem + "is",
                "Vperpasptcfablpl": ppp_stem + "is",
                "Vperpasptcnnomsg": ppp_stem + "um",
                "Vperpasptcnvocsg": ppp_stem + "um",
                "Vperpasptcnaccsg": ppp_stem + "um",
                "Vperpasptcngensg": ppp_stem + "i",
                "Vperpasptcndatsg": ppp_stem + "o",
                "Vperpasptcnablsg": ppp_stem + "o",
                "Vperpasptcnnompl": ppp_stem + "a",
                "Vperpasptcnvocpl": ppp_stem + "a",
                "Vperpasptcnaccpl": ppp_stem + "a",
                "Vperpasptcngenpl": ppp_stem + "orum",
                "Vperpasptcndatpl": ppp_stem + "is",
                "Vperpasptcnablpl": ppp_stem + "is",
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
                raise NoEndingError(
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
                raise NoEndingError(
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
class Noun(_Word):
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

        if gender not in GENDER_SHORTHAND:
            raise InvalidInputError(f"Gender '{gender}' not recognised")
        self.gender: str = GENDER_SHORTHAND[gender]

        self.nominative: str = nominative
        self.genitive: str = genitive
        self.meaning: Meaning = meaning
        self.declension: Literal[0, 1, 2, 3, 4, 5]

        self._first = self.nominative

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
                self._stem: str = self.genitive[:stem_slice]
                self.plurale_tantum: bool = bool(plurale_tantum)
                break
        else:
            raise InvalidInputError(f"Genitive form '{self.genitive}' is not valid")

        self.endings = Noun._same_regular_endings(self._stem, self.declension)
        self.endings.update(
            Noun._static_regular_endings(
                self.nominative, self.genitive, self._stem, self.declension
            )
        )

        if self.gender == "n":
            self.endings["Naccsg"] = self.nominative
            self.endings["Nvocsg"] = self.nominative

            if self.declension == 4:
                self.endings["Nnompl"] = self._stem + "ua"  # cornua
                self.endings["Naccpl"] = self._stem + "ua"  # cornua
                self.endings["Nvocpl"] = self._stem + "ua"  # cornua
                self.endings["Ndatpl"] = self._stem + "ua"  # cornua
                return
            elif self.declension == 5:
                raise InvalidInputError(
                    f"Fifth declension nouns cannot be neuter (noun '{self.nominative}')"
                )

            # For the other declensions
            self.endings["Nnompl"] = self._stem + "a"
            self.endings["Naccpl"] = self._stem + "a"
            self.endings["Nvocpl"] = self._stem + "a"

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
            raise NoEndingError(
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
class Adjective(_Word):
    def __init__(
        self,
        *principal_parts: str,
        termination: Optional[int] = None,
        declension: Literal["212", "3"],
        meaning: Meaning,
    ) -> None:
        super().__init__()

        self._principal_parts: tuple[str, ...] = principal_parts
        self._mascnom: str = self._principal_parts[0]
        self._femnom: str
        self._neutnom: str

        self._pos_stem: str

        self._first = self._principal_parts[0]
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
                if len(self._principal_parts) != 3:
                    raise InvalidInputError(
                        f"2-1-2 adjectives must have 3 principal parts (adjective '{self._first}' given)"
                    )
                self._femnom = self._principal_parts[1]
                self._neutnom = self._principal_parts[2]

                self._pos_stem = self._femnom[:-1]  # cara -> car-
                Adjective._comparative_stem(self)

                self.endings = Adjective._endings_from_table(
                    ADJECTIVE2_ENDINGS, self._pos_stem, "pos", "m"
                )
                self.endings.update(
                    Adjective._endings_from_table(
                        ADJECTIVE1_ENDINGS, self._pos_stem, "pos", "f"
                    )
                )
                self.endings.update(
                    Adjective._endings_from_table(
                        ADJECTIVE2N_ENDINGS, self._pos_stem, "pos", "n"
                    )
                )
                self.endings.update(
                    {
                        "Aposmnomsg": self._mascnom,  # carus
                        "Aposfnomsg": self._femnom,  # cara
                        "Aposfvocsg": self._femnom,  # cara
                        "Aposnnomsg": self._neutnom,  # carum
                        "Aposnvocsg": self._neutnom,  # carum
                        "Aposnaccsg": self._neutnom,  # carum
                        "Dpos": self._irregular_posadv
                        if self.irregular_flag
                        else self._pos_stem + "e",
                        "Dcmp": self._irregular_cmpadv
                        if self.irregular_flag
                        else self._pos_stem + "ius",
                        "Dspr": self._irregular_spradv
                        if self.irregular_flag
                        else self._spr_stem + "e",
                    },
                )

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

                        self._pos_stem = self._mascgen[:-2]  # ingentis -> ingent-
                        Adjective._comparative_stem(self)

                        self.endings = {
                            "Aposmnomsg": self._mascnom,  # ingens
                            "Aposmvocsg": self._mascnom,  # ingens
                            "Aposfnomsg": self._mascnom,  # ingens
                            "Aposfvocsg": self._mascnom,  # ingens
                            "Aposnnomsg": self._mascnom,  # ingens
                            "Aposnvocsg": self._mascnom,  # ingens
                            "Aposnaccsg": self._mascnom,  # ingens
                            "Dpos": self._irregular_posadv
                            if self.irregular_flag
                            else self._pos_stem + "er",
                            "Dcmp": self._irregular_cmpadv
                            if self.irregular_flag
                            else self._pos_stem + "ius",
                            "Dspr": self._irregular_spradv
                            if self.irregular_flag
                            else self._spr_stem + "e",
                        }

                    case 2:
                        # fortis, forte
                        if len(self._principal_parts) != 2:
                            raise InvalidInputError(
                                f"Second-termination adjectives must have 2 principal parts (adjective '{self._first}')"
                            )

                        self._neutnom = self._principal_parts[1]

                        self._pos_stem = self._mascnom[:-2]  # fortis -> fort-
                        Adjective._comparative_stem(self)

                        self.endings = {
                            "Aposmnomsg": self._mascnom,  # fortis
                            "Aposmvocsg": self._mascnom,  # fortis
                            "Aposfnomsg": self._mascnom,  # fortis
                            "Aposfvocsg": self._mascnom,  # fortis
                            "Aposnnomsg": self._neutnom,  # forte
                            "Aposnvocsg": self._neutnom,  # forte
                            "Aposnaccsg": self._neutnom,  # forte
                            "Dpos": self._irregular_posadv
                            if self.irregular_flag
                            else self._pos_stem + "iter",
                            "Dcmp": self._irregular_cmpadv
                            if self.irregular_flag
                            else self._pos_stem + "ius",
                            "Dspr": self._irregular_spradv
                            if self.irregular_flag
                            else self._spr_stem + "e",
                        }

                    case 3:
                        # acer, acris, acre
                        if len(self._principal_parts) != 3:
                            raise InvalidInputError(
                                f"Third-termination adjectives must have 3 principal parts (adjective '{self._first}')"
                            )

                        self._femnom = self._principal_parts[1]
                        self._neutnom = self._principal_parts[2]

                        self._pos_stem = self._femnom[:-2]  # acris -> acr-
                        Adjective._comparative_stem(self)

                        self.endings = {
                            "Aposmnomsg": self._mascnom,  # acer
                            "Aposmvocsg": self._mascnom,  # acer
                            "Aposfnomsg": self._femnom,  # acris
                            "Aposfvocsg": self._femnom,  # acris
                            "Aposnnomsg": self._neutnom,  # acre
                            "Aposnvocsg": self._neutnom,  # acre
                            "Aposnaccsg": self._neutnom,  # acre
                            "Dpos": self._irregular_posadv
                            if self.irregular_flag
                            else self._pos_stem + "iter",
                            "Dcmp": self._irregular_cmpadv
                            if self.irregular_flag
                            else self._pos_stem + "ius",
                            "Dspr": self._irregular_spradv
                            if self.irregular_flag
                            else self._spr_stem + "e",
                        }

                    case _:
                        raise InvalidInputError(
                            f"Termination must be 1, 2 or 3 (given {self.termination})"
                        )

                self.endings.update(
                    Adjective._endings_from_table(
                        ADJECTIVE3_ENDINGS, self._pos_stem, "pos", "m"
                    )
                )
                self.endings.update(
                    Adjective._endings_from_table(
                        ADJECTIVE3_ENDINGS, self._pos_stem, "pos", "f"
                    )
                )
                self.endings.update(
                    Adjective._endings_from_table(
                        ADJECTIVE3N_ENDINGS, self._pos_stem, "pos", "n"
                    ),
                )
            case _:
                raise InvalidInputError(f"Declension {self.declension} not recognised")

        self.endings.update(
            Adjective._endings_from_table(
                ADJECTIVE3C_ENDINGS, self._cmp_stem, "cmp", "m"
            )
        )
        self.endings.update(
            Adjective._endings_from_table(
                ADJECTIVE3C_ENDINGS, self._cmp_stem, "cmp", "f"
            )
        )
        self.endings.update(
            Adjective._endings_from_table(
                ADJECTIVE3CN_ENDINGS, self._cmp_stem, "cmp", "n"
            )
        )

        self.endings.update(
            {
                "Acmpmnomsg": self._cmp_stem,  # carior
                "Acmpmvocsg": self._cmp_stem,  # carior
                "Acmpfnomsg": self._cmp_stem,  # carior
                "Acmpfvocsg": self._cmp_stem,  # carior
                "Acmpnnomsg": self._cmp_stem[:-3] + "ius",  # carius
                "Acmpnvocsg": self._cmp_stem[:-3] + "ius",  # carius
                "Acmpnaccsg": self._cmp_stem[:-3] + "ius",  # carius
            }
        )

        self.endings.update(
            Adjective._endings_from_table(
                ADJECTIVE2_ENDINGS, self._spr_stem, "spr", "m"
            )
        )
        self.endings.update(
            Adjective._endings_from_table(
                ADJECTIVE1_ENDINGS, self._spr_stem, "spr", "f"
            )
        )
        self.endings.update(
            Adjective._endings_from_table(
                ADJECTIVE2N_ENDINGS, self._spr_stem, "spr", "n"
            )
        )
        self.endings.update(
            {
                "Asprmnomsg": self._spr_stem + "us",  # carrissimus
                "Asprfnomsg": self._spr_stem + "a",  # carrissima
                "Asprfvocsg": self._spr_stem + "a",  # carrissima
                "Asprnnomsg": self._spr_stem + "um",  # carrissimum
                "Asprnvocsg": self._spr_stem + "um",  # carrissimum
                "Asprnaccsg": self._spr_stem + "um",  # carrissimum})
            }
        )

    def _comparative_stem(self) -> None:
        # FIXME: some adjectives don't have adverbs!
        #        bug probably to be left in, a bit complicated to fix
        self.irregular_flag: bool = False

        if self._mascnom in edge_cases.IRREGULAR_COMPARATIVES:
            self._cmp_stem: str = edge_cases.IRREGULAR_COMPARATIVES[self._mascnom][0]
            self._spr_stem: str = edge_cases.IRREGULAR_COMPARATIVES[self._mascnom][1]
            self._irregular_posadv: str = edge_cases.IRREGULAR_COMPARATIVES[
                self._mascnom
            ][2]
            self._irregular_cmpadv: str = edge_cases.IRREGULAR_COMPARATIVES[
                self._mascnom
            ][3]
            self._irregular_spradv: str = edge_cases.IRREGULAR_COMPARATIVES[
                self._mascnom
            ][4]
            self.irregular_flag = True
            return

        self._cmp_stem = self._pos_stem + "ior"  # car- -> carior-
        if self._mascnom[-2:] == "er":
            self._spr_stem = self._mascnom + "rim"  # miser- -> miserrim-
        elif self._mascnom in edge_cases.LIS_ADJECTIVES:
            self._spr_stem = self._pos_stem + "lim"  # facil- -> facillim-
        else:
            self._spr_stem = self._pos_stem + "issim"  # car- -> carissim-

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
    def __init__(self, *, pronoun: str, meaning: Meaning):
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
            raise NoEndingError(
                f"No ending found for gender '{gender}', case '{case}' and number '{number}'"
            )

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
