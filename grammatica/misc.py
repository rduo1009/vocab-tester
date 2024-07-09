"""misc.py
Contains miscellaneous functions and classes used by grammatica.
"""

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, init=True)
class MultipleOptions:
    best_option: str
    other_options: Union[list[str], str]

    def __post_init__(self):
        if isinstance(self.other_options, str):
            self.other_options = [self.other_options]
