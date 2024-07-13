"""misc.py
Contains miscellaneous functions and classes used by grammatica.
"""

from dataclasses import dataclass, field
from typing import Union


@dataclass(init=True)
class MultipleMeanings:
    """Represents multiple meanings, with a best meaning and other meanings.
    If there is only one meaning, the other_meanings list will be empty.

    Attributes
    ----------
    best_meaning : str
        The best meaning.
    other_meanings : list[str], str
        Other meanings.

    Notes
    -----
    This class allows for there to be several English definitions of one Latin word. This means for
    translating-to-English questions, synonyms can be accepted, but not vice versa.

    The other_meanings list is intended to be ordered from better to worse meanings.
    For example, callidus -> MultipleMeanings("clever", ["cunning", "callid"])
    'Callid' is technically correct, but not a very commonly used word, so it is put later in the
    list.
    """

    best_meaning: str
    other_meanings: Union[list[str], str] = field(default_factory=list)

    def __str__(self) -> str:
        """Returns the best meaning as a representation of the MultipleMeanings object."""
        return self.best_meaning

    def __repr__(self) -> str:
        """Returns a representation of the MultipleMeanings object."""
        return f"MultipleMeanings({self.best_meaning}, {self.other_meanings})"

    def __post_init__(self) -> None:
        """If other_meanings is a string, convert it to a list."""
        if isinstance(self.other_meanings, str):
            self.other_meanings: list = [self.other_meanings]
