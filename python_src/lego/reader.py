#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions for reading vocabulary files."""

import sys

if sys.version_info >= (3, 10):
    from .._compat.latest.reader import (
        _generate_meaning as _generate_meaning,
    )
    from .._compat.latest.reader import _parse_line as _parse_line
    from .._compat.latest.reader import (
        _regenerate_vocab_list as _regenerate_vocab_list,
    )
    from .._compat.latest.reader import read_vocab_dump as read_vocab_dump
    from .._compat.latest.reader import read_vocab_file as read_vocab_file
else:
    from .._compat.py38.reader import _generate_meaning as _generate_meaning
    from .._compat.py38.reader import _parse_line as _parse_line
    from .._compat.py38.reader import (
        _regenerate_vocab_list as _regenerate_vocab_list,
    )
    from .._compat.py38.reader import read_vocab_dump as read_vocab_dump
    from .._compat.py38.reader import read_vocab_file as read_vocab_file
