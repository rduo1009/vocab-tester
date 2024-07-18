"""misc.py
Contains miscellaneous functions and classes used by grammatica.
"""

from dataclasses import dataclass
from typing import TypeAlias

Endings: TypeAlias = dict[str, str]


@dataclass(init=True)
class MultipleMeanings:
    """Represents multiple meanings, with a best meaning and other meanings.

    Attributes
    ----------
    meanings : list[str]
        The meanings, the input of the class
    best_meaning : str
        The best meaning.
    other_meanings : list[str], str
        Other meanings.

    Notes
    -----
    This class allows for there to be several English definitions of one Latin word. This means for
    translating-to-English questions, synonyms can be accepted, but not vice versa.

    The meanings and other_meanings list is intended to be ordered from better to worse meanings.
    For example, meanings = ["clever", "cunning", "callid"]
    'Callid' is technically correct, but not a very commonly used word, so it is put later in the
    list.
    """

    meanings: list[str]

    def __str__(self) -> str:
        """Returns the best meaning as a representation of the MultipleMeanings object."""
        return self.best_meaning

    def __repr__(self) -> str:
        """Returns a representation of the MultipleMeanings object."""
        return f"MultipleMeanings({",".join(self.meanings)})"

    def __post_init__(self) -> None:
        """If other_meanings is a string, convert it to a list."""
        self.best_meaning: str = self.meanings[0]
        self.other_meanings: list[str] = self.meanings[1:]
