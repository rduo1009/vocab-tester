#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains type aliases used by accido."""

import sys

if sys.version_info >= (3, 12):
    from .._compat.latest.type_aliases import Ending as Ending
    from .._compat.latest.type_aliases import Endings as Endings
    from .._compat.latest.type_aliases import Meaning as Meaning

elif sys.version_info >= (3, 10):
    from .._compat.py310.type_aliases import Ending as Ending
    from .._compat.py310.type_aliases import Endings as Endings
    from .._compat.py310.type_aliases import Meaning as Meaning

else:  # pragma: no cover
    from .._compat.py38.type_aliases import Ending as Ending
    from .._compat.py38.type_aliases import Endings as Endings
    from .._compat.py38.type_aliases import Meaning as Meaning
