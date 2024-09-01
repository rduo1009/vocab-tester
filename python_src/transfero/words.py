#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English words."""

from .adj_to_adv import adj_to_adv as adj_to_adv
from .adjective_inflection import (
    find_adjective_inflections as find_adjective_inflections,
)
from .adverb_inflection import (
    find_adverb_inflections as find_adverb_inflections,
)
from .noun_inflection import find_noun_inflections as find_noun_inflections
from .verb_inflection import find_verb_inflections as find_verb_inflections
