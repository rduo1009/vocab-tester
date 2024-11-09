#!/usr/bin/env python3

"""Contains custom exceptions used by transfero."""


class InvalidWordError(Exception):
    """An error that is raised when an invalid word is given to a transfero function."""


class InvalidComponentsError(Exception):
    """An error that is raised when invalid components are given to a transfero function."""
