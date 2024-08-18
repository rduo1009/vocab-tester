#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains a function for saving vocabulary files."""

from __future__ import annotations

import hashlib as hl
import hmac
from pathlib import Path
from warnings import warn

import dill as pickle

from .misc import KEY, VocabList


def save_vocab_dump(file_path: Path, vocab_list: VocabList) -> None:
    """Saves a vocabulary dump file.
    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the vocabulary dump file.

    vocab_list : VocabList
        The vocabulary to save.

    Raises
    ------
    FileNotFoundError
        If the directory of the file does not exist.

    Warnings
    --------
    UserWarning
        If the file already exists and has been overwritten.

    Examples
    --------
    >>> save_vocab_dump(Path("path_to_file.pickle"), VocabList(...))
    """
    file_path = Path(file_path)

    if not file_path.parent.exists():
        raise FileNotFoundError(
            f"The directory {file_path.parent} does not exist."
        )

    if file_path.exists():
        warn(
            f"The file {file_path} already exists and has been overwritten.",
            UserWarning,
        )

    pickled_data: bytes = pickle.dumps(vocab_list)

    signature = hmac.new(KEY, pickled_data, hl.sha256).hexdigest()

    with open(file_path, "wb") as file:
        file.write(pickled_data)
        file.write(signature.encode())
