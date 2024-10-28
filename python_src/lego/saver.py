#!/usr/bin/env python3

"""Contains a function for saving vocabulary files."""

import hashlib
import hmac
import warnings
from pathlib import Path

import dill as pickle
import lz4.frame  # type: ignore[import-untyped]

from .exceptions import MisleadingFilenameWarning
from .misc import KEY, VocabList


def save_vocab_dump(
    file_path: Path, vocab_list: VocabList, *, compress: bool = False
) -> None:
    """Save a vocabulary dump file.

    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with.
    The files can also be compressed using LZ4 compression. If this is the
    case, the files will be saved with the .lz4 extension, unless the user
    has put the .lz4 extension in the file path already.

    Parameters
    ----------
    file_path : Path
        The path to the vocabulary dump file.
    vocab_list : VocabList
        The vocabulary to save.
    compress : bool, default = False
        Whether to compress the pickle file.

    Raises
    ------
    FileNotFoundError
        If the directory of the file does not exist.

    Warnings
    --------
    UserWarning
        If the file already exists and has been overwritten.
    MisleadingFilenameWarning
        If the file path does not end in .lz4 and the file is being
        compressed, or if the file path ends in .lz4 and the file is not
        being compressed.

    Examples
    --------
    >>> save_vocab_dump(
    ...     Path("path_to_file.pickle"), VocabList()
    ... )  # doctest: +SKIP
    """
    if not file_path.parent.exists():
        raise FileNotFoundError(
            f"The directory '{file_path.parent}' does not exist",
        )

    if file_path.exists():
        warnings.warn(
            f"The file '{file_path}' already exists and has been overwritten",
            stacklevel=2,
        )

    pickled_data: bytes = pickle.dumps(vocab_list)
    signature: str = hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest()

    if compress:
        # Add lz4 extension if it is not already there
        if file_path.suffix != ".lz4":
            warnings.warn(
                f"The file '{file_path}' is being compressed, "
                "but the '.lz4' extension is not present and is being added.",
                category=MisleadingFilenameWarning,
                stacklevel=2,
            )
            file_path = file_path.with_suffix(f"{file_path.suffix}.lz4")

        with lz4.frame.open(file_path, "wb") as file:
            file.write(pickled_data)
            file.write(signature.encode())
        return

    if file_path.suffix == ".lz4":
        warnings.warn(
            f"The file '{file_path}' is not being compressed, "
            "but the file extension ('.lz4') suggests it is.",
            category=MisleadingFilenameWarning,
            stacklevel=2,
        )

    with open(file_path, "wb") as file:
        file.write(pickled_data)
        file.write(signature.encode())
