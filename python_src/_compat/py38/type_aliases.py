#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

from ...accido.misc import MultipleEndings, MultipleMeanings

Ending = str | MultipleEndings
Endings = dict[str, Ending]
Meaning = str | MultipleMeanings
