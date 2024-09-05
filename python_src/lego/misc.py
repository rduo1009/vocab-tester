#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous constants and classes used by lego."""

from __future__ import annotations

import ctypes
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

import python_src as src

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
    ...         nominative="ancilla",
    ...         genitive="ancillae",
    ...         gender="feminine",
    ...         meaning="slavegirl",
    ...     )
    ... ])  # doctest: +SKIP
    This will create a VocabList with a single Noun object in it.
    """

    vocab: list[accido.endings._Word]

    def __post_init__(self) -> None:
        # Set the version using the package version.
        self.version: str = src.__version__


LIBKEY: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
LIBKEY.get_key.restype = ctypes.c_char_p

"""The key used to sign vocabulary pickle files."""
KEY: Final[bytes] = LIBKEY.get_key()
