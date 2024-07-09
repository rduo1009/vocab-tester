"""misc.py
Contains miscellaneous functions and classes used by grammatica.
"""

from dataclasses import dataclass, field
from typing import Union


@dataclass(frozen=True, init=True)
class MultipleOptions:
    """Represents multiple options, with a best option and other options.
    If there is only one option, the other_options list will be empty.

    Attributes
    ----------
    best_option : str
        The best option.
    other_options : list[str], str
        Other options.

    Notes
    -----
    This class allows for there to be several English definitions of one Latin word. This means for
    translating-to-English questions, synonyms can be accepted, but not vice versa.

    The other_options list is intended to be ordered from better to worse options.
    For example, callidus -> MultipleOptions("clever", ["cunning", "callid"])
    'Callid' is technically correct, but not a very commonly used word, so it is put later in the
    list.
    """

    best_option: str
    other_options: Union[list[str], str] = field(default_factory=list)

    def __repr__(self) -> str:
        """Returns the best option as a respresentation of the MultipleOptions object."""
        return self.best_option

    def __post_init__(self) -> None:
        """If other_options is a string, convert it to a list."""
        if isinstance(self.other_options, str):
            self.other_options = [self.other_options]
