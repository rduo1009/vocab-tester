"""custom_exceptions.py
Contains custom exceptions used by grammatica.
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
    grammatica class.

    Parameters
    ----------
    error : str
        The error message to be displayed
    """

    pass
