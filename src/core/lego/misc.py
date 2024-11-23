"""Contains miscellaneous constants and classes used by lego."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

import src

from ...utils import compact

if TYPE_CHECKING:
    from .. import accido


@dataclass
class VocabList:
    """Represents a list of Latin vocabulary.

    Each piece of vocabulary is represented by the classes in the accido
    package.

    Attributes
    ----------
    vocab : list[accido.endings._Word]
        The vocabulary in the list.
    version : str
        The version of the package. Used to regenerate the endings if the
        version of the package is different (e.g. if the package is updated).

    Examples
    --------
    >>> foo = VocabList([
    ...     Noun(
    ...         "ancilla",
    ...         "ancillae",
    ...         gender="feminine",
    ...         meaning="slavegirl",
    ...     )
    ... ])  # doctest: +SKIP
    This will create a VocabList with a single Noun object in it.
    """

    vocab: list[accido.endings._Word]

    def __post_init__(self) -> None:
        self.vocab = compact(self.vocab)

        # Set the version using the package version.
        self.version: str = src.__version__

    def __repr__(self) -> str:
        object_reprs: str = ", ".join(repr(word) for word in self.vocab)
        return f"VocabList([{object_reprs}], version={self.version})"

    def __add__(self, other: object) -> VocabList:
        if not isinstance(other, VocabList) or self.version != other.version:
            return NotImplemented

        return VocabList(self.vocab + other.vocab)


"""The key used to sign vocabulary pickle files."""
KEY: Final[bytes] = b"vocab-tester-key"
