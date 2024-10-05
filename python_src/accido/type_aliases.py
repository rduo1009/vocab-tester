#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

from typing import Literal

from ..accido.misc import MultipleEndings, MultipleMeanings

type Ending = str | MultipleEndings
type Endings = dict[str, Ending]
type Meaning = str | MultipleMeanings

type NounDeclension = Literal[0, 1, 2, 3, 4, 5]
type AdjectiveDeclension = Literal["212", "3"]
type Conjugation = Literal[0, 1, 2, 3, 4, 5]
type Termination = Literal[1, 2, 3]
