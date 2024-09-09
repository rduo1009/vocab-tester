#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

import sys
from typing import Dict

assert sys.version_info <= (3, 10)

from typing import Union

from ...accido.misc import MultipleEndings, MultipleMeanings

Ending = Union[str, MultipleEndings]
Endings = Dict[str, Ending]
Meaning = Union[str, MultipleMeanings]
