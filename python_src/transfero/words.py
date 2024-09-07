#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions that inflect English words."""

import sys

if sys.version_info >= (3, 10):
    from .adj_to_adv import adj_to_adv as adj_to_adv
    from .adjective_inflection import (
        find_adjective_inflections as find_adjective_inflections,
    )
    from .adverb_inflection import (
        find_adverb_inflections as find_adverb_inflections,
    )
    from .noun_inflection import find_noun_inflections as find_noun_inflections
    from .verb_inflection import find_verb_inflections as find_verb_inflections
else:
    from .._compat.py38.adjective_inflection import (
        find_adjective_inflections as find_adjective_inflections,
    )
    from .._compat.py38.adverb_inflection import (
        find_adverb_inflections as find_adverb_inflections,
    )
    from .._compat.py38.noun_inflection import (
        find_noun_inflections as find_noun_inflections,
    )
    from .._compat.py38.verb_inflection import (
        find_verb_inflections as find_verb_inflections,
    )
    from .adj_to_adv import adj_to_adv as adj_to_adv
