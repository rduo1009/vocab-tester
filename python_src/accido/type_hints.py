#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type hints for accido, to be used with python3.12 and above.

Ideally this would be part of the misc module, but that would lead to a
syntax error in python3.11 and below.
"""

from .misc import MultipleEndings, MultipleMeanings

type Ending = str | MultipleEndings
type Endings = dict[str, Ending]
type Meaning = str | MultipleMeanings
