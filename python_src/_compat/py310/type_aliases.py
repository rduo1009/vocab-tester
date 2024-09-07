#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from __future__ import annotations

from typing import TypeAlias

from ...accido.misc import MultipleEndings, MultipleMeanings

Ending: TypeAlias = str | MultipleEndings
Endings: TypeAlias = dict[str, Ending]
Meaning: TypeAlias = str | MultipleMeanings
