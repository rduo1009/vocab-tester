#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains custom exceptions used by lego."""


class InvalidVocabFileFormatError(Exception):
    """An error that is raised when a vocab file has the incorrect format."""


class InvalidVocabDumpError(Exception):
    """An error that is raised when a vocab dump is invalid.

    This could be due to the file being corrupted or being tampered with,
    or if the file is not a vocab dump.
    """


class MisleadingFilenameWarning(
    UserWarning
):  # sourcery skip: errors-named-error
    """A warning that is raised when a filename is misleading.

    For example, if a file ends in .lz4 but it is not a compressed file.
    """
