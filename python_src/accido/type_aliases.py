#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

import sys

if sys.version_info >= (3, 12):
    from .type_aliases_latest import AdjectiveDeclension as AdjectiveDeclension
    from .type_aliases_latest import Conjugation as Conjugation
    from .type_aliases_latest import Ending as Ending
    from .type_aliases_latest import Endings as Endings
    from .type_aliases_latest import Meaning as Meaning
    from .type_aliases_latest import NounDeclension as NounDeclension
    from .type_aliases_latest import Person as Person
    from .type_aliases_latest import Termination as Termination
    from .type_aliases_latest import is_person as is_person
    from .type_aliases_latest import is_termination as is_termination

elif sys.version_info >= (3, 10):
    from .._compat.py310.type_aliases import (
        AdjectiveDeclension as AdjectiveDeclension,
    )
    from .._compat.py310.type_aliases import Conjugation as Conjugation
    from .._compat.py310.type_aliases import Ending as Ending
    from .._compat.py310.type_aliases import Endings as Endings
    from .._compat.py310.type_aliases import Meaning as Meaning
    from .._compat.py310.type_aliases import NounDeclension as NounDeclension
    from .._compat.py310.type_aliases import Person as Person

else:  # pragma: no cover
    from .._compat.py38.type_aliases import Ending as Ending
    from .._compat.py38.type_aliases import Endings as Endings
    from .._compat.py38.type_aliases import Meaning as Meaning
