#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A package for reading from a vocabulary list and creating a Python list
containing the words. Also, it can save the word list to a pickle file.
"""  # noqa: D205

from . import cache, exceptions, reader, saver

__all__ = [
    "cache",
    "exceptions",
    "reader",
    "saver",
]
