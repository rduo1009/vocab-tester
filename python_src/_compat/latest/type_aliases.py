#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

import sys

assert sys.version_info >= (3, 12)

from ...accido.misc import MultipleEndings, MultipleMeanings

type Ending = str | MultipleEndings
type Endings = dict[str, Ending]
type Meaning = str | MultipleMeanings
