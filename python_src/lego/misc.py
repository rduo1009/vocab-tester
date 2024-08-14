#!/usr/bin/env python3

from dataclasses import dataclass

import python_src

from .. import accido


@dataclass
class VocabList:
    vocab_list: list[accido.endings._Word]

    def __post_init__(self) -> None:
        self.version = python_src.__version__


key = b"vocab-tester"
