from typing import Union

# fmt: off
NOUN_ENDINGS: tuple[Union[str, None], ...] = (
    None, None, "am", "ae", "ae", "a", "ae", "ae", "as", "arum", "is", "is",
    None, None, "um", "i", "o", "o", "i", "i", "os", "orum", "is", "is",
    None, None, "em", "is", "i", "e", "es", "es", "es", "um", "ibus", "ibus",
    None, None, "um", "us", "ui", "us", "us", "us", "us", "uum", "ibus", "ibus",
    None, None, "em", "ei", "ei", "e", "es", "es", "es", "erum", "ebus", "ebus"
)

ADJECTIVE1_ENDINGS = (
    None, None, "am", "ae", "ae", "a", "ae", "ae", "as", "arum", "is", "is"
)

ADJECTIVE2_ENDINGS = (
    None, "e", "um", "i", "o", "o", "i", "i", "os", "orum", "is", "is"
)

ADJECTIVE3_ENDINGS = (
    None, None, "em", "is", "i", "i", "es", "es", "es", "ium", "ibus", "ibus"
)  

ADJECTIVE2N_ENDINGS = (
    None, "e", "um", "i", "o", "o", "a", "a", "a", "orum", "is", "is"
)

ADJECTIVE3N_ENDINGS = (
    None, None, None, "is", "i", "i", "ia", "ia", "ia", "ium", "ibus", "ibus"
)

ADJECTIVE3C_ENDINGS = (
    None, None, "em", "is", "i", "e", "es", "es", "es", "um", "ibus", "ibus"
)  

ADJECTIVE3CN_ENDINGS = (
    None, None, None, "is", "i", "e", "a", "a", "a", "um", "ibus", "ibus"
)

# Same endings across conjugations: perfect, pluperfect, imperfect sbj, pluperfect sbj
def VERB_SAME_ENDINGS(*, per_stem: str, infinitive: str) -> dict[str, tuple[str, tuple[str, ...]]]: 
    return {
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


# Similar endings across conjugations: imperfect, present (kinda)
def VERB_SIMILAR_ENDINGS(*, inf_stem: str) -> dict[
    str, tuple[str, tuple[str, ...], tuple[Union[str, None], ...]]
]:
    return {
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

type EndingsTable = tuple[Union[str, None], ...]  # type: ignore
