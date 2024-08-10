#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InvalidVocabFileFormat(Exception):
    """An error that is raised when a vocab file has the incorrect format.

    Parameters
    ----------
    error : str
        The error message to be displayed
    """

    pass


class InvalidVocabDump(Exception):
    """An error that is raised when a vocab dump is invalid.
    This could be due to the file being corrupted or being tampered with,
    or if the file is not a vocab dump.

    Parameters
    ----------
    error : str
        The error message to be displayed
    """
