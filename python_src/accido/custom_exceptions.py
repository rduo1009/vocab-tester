#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""custom_exceptions.py
Contains custom exceptions used by accido.
"""


class NoEndingError(Exception):
    """An error that is raised when no ending is found for a given input to
    Word.get()

    Parameters
    ----------
    error : str
        The error message to be displayed
    """

    pass


class InvalidInputError(Exception):
    """An error that is raised when an invalid input is given to a
    accido class.

    Parameters
    ----------
    error : str
        The error message to be displayed
    """

    pass
