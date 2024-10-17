#!/usr/bin/env python3

"""Contains a function for caching vocabulary files in a cache folder."""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import TYPE_CHECKING

from .reader import read_vocab_dump, read_vocab_file
from .saver import save_vocab_dump

if TYPE_CHECKING:
    from .misc import VocabList
import hashlib


def _sha256sum(filename: Path) -> str:
    """Hashes a file.

    Parameters
    ----------
    filename : Path
        The file to hash.

    Returns
    -------
    str
        The hash as a string.

    Notes
    -----
    Code taken from https://stackoverflow.com/a/44873382
    """
    with open(filename, "rb", buffering=0) as file:
        return hashlib.file_digest(
            file,  # type: ignore[arg-type] # mypy cannot handle this
            "sha256",
        ).hexdigest()


def cache_vocab_file(
    cache_folder: Path, vocab_file_path: Path
) -> tuple[VocabList, bool]:
    """Reads a vocab file, and saves the vocab dump inside a cache folder.

    The name of the vocabulary dump file is decided by hashing the
    vocab file given. Note that if the cache folder does not exist,
    it is created.

    Parameters
    ----------
    cache_folder : Path
        The path to the cache folder.
    vocab_file_path : Path
        The path to the vocab file that is to be read.

    Returns
    -------
    (VocabList, bool)
        The vocab list, and whether it was generated from cache or not.

    Warnings
    --------
    UserWarning
        If the cache folder did not exist and had to be created.
    """
    if not cache_folder.exists():  # pragma: no cover
        cache_folder.mkdir(parents=True, exist_ok=True)
        warnings.warn(
            f"The directory {cache_folder} did not exist and has been created",
            stacklevel=2,
        )

    cache_file_name: str = _sha256sum(vocab_file_path)
    cache_path: Path = Path(cache_folder / cache_file_name)

    if cache_path.exists():
        return (read_vocab_dump(cache_path), True)

    vocab_list: VocabList = read_vocab_file(  # pragma: no cover
        vocab_file_path
    )  # sourcery skip: name-type-suffix
    save_vocab_dump(cache_path, vocab_list)  # pragma: no cover
    return (vocab_list, False)  # pragma: no cover
