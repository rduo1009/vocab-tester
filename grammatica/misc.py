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

    """

    best_option: str
    other_options: Union[list[str], str] = field(default_factory=list)

    def __repr__(self) -> str:
        """Returns the best option as a respresentation of the MultipleOptions object."""
        return self.best_option

    def __post_init__(self):
        """If other_options is a string, convert it to a list."""
        if isinstance(self.other_options, str):
            self.other_options = [self.other_options]
