#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ctypes
from dataclasses import dataclass

import python_src

from .. import accido


@dataclass
class VocabList:
    vocab: list[accido.endings._Word]

    def __post_init__(self) -> None:
        self.version: str = python_src.__version__


libkey: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
libkey.get_key.restype = ctypes.c_char_p
key: bytes = libkey.get_key()
