import itertools
from dataclasses import dataclass
from functools import total_ordering
from io import StringIO
from typing import Literal, Optional, Union, NamedTuple

from . import edge_cases
from .custom_exceptions import InvalidInputError, NoMeaningError
from .misc import Ending, Endings, Meaning

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

    def __setitem__(self, key: str, value: Ending) -> None:
        self.endings[key] = value


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
            **LearningVerb._static_regular_endings(
                self.conjugation, self.present, self.infinitive, self.perfect
            ),
            **LearningVerb._same_regular_endings(
                self.present, self.infinitive, self.perfect
            ),
            **LearningVerb._similar_regular_endings(
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

        self.nom: str = nominative
        self.gen: str = genitive
        self.meaning: Meaning = meaning
        self.declension: int

        self.first = self.nom

        if self.nom in edge_cases.IRREGULAR_NOUNS:
            self.endings = edge_cases.IRREGULAR_NOUNS[nominative]
            self.declension = 0
            return

        # The ordering of this is strange because e.g. ending -ei ends in 'i' as well as 'ei'
        # so 5th declension check must come before 2nd declension check, etc.
        DECLENSION_MAP: dict[str, tuple[int, int, Optional[bool]]] = {
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
            if self.gen.endswith(ending):
                self.declension = declension
                self.stem: str = self.gen[:stem_slice]
                self.plurale_tantum: bool = bool(plurale_tantum)
                break
        else:
            raise InvalidInputError(f"Genitive form '{self.gen}' is not valid")

        self.endings = {
            **Noun._same_regular_endings(self.stem, self.declension),
            **Noun._static_regular_endings(
                self.nom, self.gen, self.stem, self.declension
            ),
        }

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

    @staticmethod
    def _same_regular_endings(stem: str, declension: int) -> Endings:
        CaseEnding: NamedTuple = NamedTuple(
            "CaseEnding", [("sg", Union[str, None]), ("pl", str)]
        )

        NOUN_ENDINGS: tuple[tuple[CaseEnding, ...], ...] = (
            (
                CaseEnding(None, "ae"),
                CaseEnding(None, "ae"),
                CaseEnding("am", "as"),
                CaseEnding(None, "arum"),
                CaseEnding("ae", "is"),
                CaseEnding("a", "is"),
            ),
            (
                CaseEnding(None, "i"),
                CaseEnding(None, "i"),
                CaseEnding("um", "os"),
                CaseEnding(None, "orum"),
                CaseEnding("o", "is"),
                CaseEnding("o", "is"),
            ),
            (
                CaseEnding(None, "es"),
                CaseEnding(None, "es"),
                CaseEnding("em", "es"),
                CaseEnding(None, "um"),
                CaseEnding("i", "ibus"),
                CaseEnding("e", "ibus"),
            ),
            (
                CaseEnding(None, "us"),
                CaseEnding(None, "us"),
                CaseEnding("um", "us"),
                CaseEnding(None, "uum"),
                CaseEnding("ui", "ibus"),
                CaseEnding("us", "ibus"),
            ),
            (
                CaseEnding(None, "es"),
                CaseEnding(None, "es"),
                CaseEnding("em", "es"),
                CaseEnding(None, "erum"),
                CaseEnding("ei", "ebus"),
                CaseEnding("e", "ebus"),
            ),
        )

        return {
            f"N{case}{number}": stem
            + getattr(NOUN_ENDINGS[declension - 1][count], number)
            for count, case in enumerate(CASE_SHORTHAND.values())
            for number in NUMBER_SHORTHAND.values()
            if getattr(NOUN_ENDINGS[declension - 1][count], number)
        }

    @staticmethod
    def _static_regular_endings(
        nom: str, gen: str, stem: str, declension: int
    ) -> Endings:
        match declension:
            case 1 | 3 | 4 | 5:
                return {
                    "Nnomsg": nom,  # puella
                    "Nvocsg": nom,  # puella
                    "Ngensg": gen,  # puellae
                }

            case 2:
                return {
                    "Nnomsg": nom,  # servus
                    "Nvocsg": nom if nom[-2:] == "er" else stem + "e",  # serve
                    "Ngensg": gen,  # servi
                }

            case _:
                raise ValueError(f"Declension {declension} not recognised")

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

                if not self.irregular_flag:
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
