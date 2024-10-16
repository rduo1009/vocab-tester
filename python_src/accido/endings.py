#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Representations of Latin words with their endings calculated.

A wrapper for the classes.
"""

import sys

if sys.version_info >= (3, 10):
    from .class_adjective import Adjective as Adjective
    from .class_noun import Noun as Noun
    from .class_verb import Verb as Verb
else:
    from .._compat.py39.accido.class_adjective import Adjective as Adjective
    from .._compat.py39.accido.class_noun import Noun as Noun
    from .._compat.py39.accido.class_verb import Verb as Verb

from .class_pronoun import Pronoun as Pronoun
from .class_regularword import RegularWord as RegularWord
from .class_word import _Word as _Word
