#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type hints for accido, to be used with python3.12 and above."""

from frozendict import frozendict

from .misc import MultipleEndings, MultipleMeanings

type Ending = str | MultipleEndings
type Endings = frozendict[str, Ending]
type Meaning = str | MultipleMeanings
