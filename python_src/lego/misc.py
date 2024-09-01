#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains miscellaneous constants and classes used by lego."""

from __future__ import annotations

import ctypes
from dataclasses import dataclass
from typing import Final

import python_src as src

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
    >>> x = VocabList([Noun(nominative="ancilla", genitive="ancillae", \
    ...                     gender="feminine", meaning="slavegirl")], 
    This will create a VocabList with a single Noun object in it.
    """

    vocab: list[accido.endings._Word]

    def __post_init__(self) -> None:
        # Set the version using the package version.
        self.version: str = src.__version__


# Imports the c++ library containing the key. This is used to sign the
# vocabulary pickle files for additional security.
# Frankly, considering the code for all of this is public, this is a bit
# on the useless side. I guess it would help if someone tried to make
# an attack without knowledge of the source code or something.
libkey: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
libkey.get_key.restype = ctypes.c_char_p

"""The key used to sign vocabulary pickle files."""
KEY: Final[bytes] = libkey.get_key()
