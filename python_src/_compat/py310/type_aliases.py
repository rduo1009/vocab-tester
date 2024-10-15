#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

import sys

assert sys.version_info >= (3, 10)
assert sys.version_info < (3, 12)

from typing import Literal, TypeAlias

from ...accido.misc import MultipleEndings, MultipleMeanings

Ending: TypeAlias = str | MultipleEndings
Endings: TypeAlias = dict[str, Ending]
Meaning: TypeAlias = str | MultipleMeanings

NounDeclension: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
AdjectiveDeclension: TypeAlias = Literal["212", "3"]
Conjugation: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
Termination: TypeAlias = Literal[1, 2, 3]
Person: TypeAlias = Literal[1, 2, 3]
