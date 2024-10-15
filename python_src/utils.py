#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""General functions used by vocab-tester and its tests."""

import sys

if sys.version_info >= (3, 13):
    from .utils_latest import compare as compare
else:
    from ._compat.py312.utils import compare as compare
