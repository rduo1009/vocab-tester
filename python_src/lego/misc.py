#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass

import python_src

from .. import accido


@dataclass
class VocabList:
    vocab: list[accido.endings._Word]

    def __post_init__(self) -> None:
        self.version: str = python_src.__version__


key: bytes = b"vocab-tester"
