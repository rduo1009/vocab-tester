#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains custom exceptions used by lego."""


class InvalidVocabFileFormatError(Exception):
    """An error that is raised when a vocab file has the incorrect format."""

    pass


class InvalidVocabDumpError(Exception):
    """An error that is raised when a vocab dump is invalid.
    This could be due to the file being corrupted or being tampered with,
    or if the file is not a vocab dump."""

    pass
