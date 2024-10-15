#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

import sys
from typing import Dict

assert sys.version_info <= (3, 10)

from typing import Literal, Union

from ...accido.misc import MultipleEndings, MultipleMeanings

Ending = Union[str, MultipleEndings]
Endings = Dict[str, Ending]
Meaning = Union[str, MultipleMeanings]

NounDeclension = Literal[0, 1, 2, 3, 4, 5]
AdjectiveDeclension = Literal["212", "3"]
Conjugation = Literal[0, 1, 2, 3, 4, 5]
Termination = Literal[1, 2, 3]
Person = Literal[1, 2, 3]
