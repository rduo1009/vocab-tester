#!/usr/bin/env python3
# -*- coding: future_typing -*-

"""Contains functions for reading vocabulary files."""

import hashlib
import hmac
import sys
import warnings
from pathlib import Path

import dill as pickle
import lz4.frame  # type: ignore[import-untyped]

import python_src as src

from .. import accido
from .exceptions import InvalidVocabDumpError
from .misc import KEY, VocabList

if sys.version_info >= (3, 10):
    from .reader_latest import _generate_meaning as _generate_meaning
    from .reader_latest import _parse_line as _parse_line
    from .reader_latest import read_vocab_file as read_vocab_file
else:
    from .._compat.py39.lego.reader import (
        _generate_meaning as _generate_meaning,
    )
    from .._compat.py39.lego.reader import _parse_line as _parse_line
    from .._compat.py39.lego.reader import read_vocab_file as read_vocab_file


def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
    """Regenerates a VocabList from a VocabList.

    This is useful for regenerating a VocabList if it was created in a
    previous version of the package.

    Parameters
    ----------
    vocab_list : VocabList
        The VocabList to regenerate.

    Returns
    -------
    VocabList
        The regenerated VocabList.
    """
    word: accido.endings._Word
    new_vocab: list[accido.endings._Word] = []

    for word in vocab_list.vocab:
        if isinstance(word, accido.endings.RegularWord):
            new_vocab.append(
                accido.endings.RegularWord(
                    word=word.word,
                    meaning=word.meaning,
                ),
            )
        elif isinstance(word, accido.endings.Verb):
            new_vocab.append(
                accido.endings.Verb(
                    present=word.present,
                    infinitive=word.infinitive,
                    perfect=word.perfect,
                    ppp=word.ppp,
                    meaning=word.meaning,
                ),
            )
        elif isinstance(word, accido.endings.Noun):
            new_vocab.append(
                accido.endings.Noun(
                    nominative=word.nominative,
                    genitive=word.genitive,
                    meaning=word.meaning,
                    gender=word.gender,
                ),
            )
        elif isinstance(word, accido.endings.Adjective):
            new_vocab.append(
                accido.endings.Adjective(
                    *word._principal_parts,  # noqa: SLF001
                    termination=word.termination,
                    declension=word.declension,
                    meaning=word.meaning,
                ),
            )
        elif isinstance(word, accido.endings.Pronoun):
            new_vocab.append(
                accido.endings.Pronoun(
                    pronoun=word.pronoun,
                    meaning=word.meaning,
                ),
            )
        else:  # pragma: no cover # this should never happen
            raise TypeError(f"Unknown word type: {type(word)}")  # noqa: DOC501

    return VocabList(new_vocab)


def read_vocab_dump(filename: Path) -> VocabList:
    """Reads a vocabulary dump file and returns a VocabList object.

    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with. If the data is invalid, an exception is
    raised.
    If the file ends in .lz4, the file is decompressed using lz4.

    Parameters
    ----------
    filename : pathlib.Path
        The path to the vocabulary dump file.

    Returns
    -------
    VocabList
        The vocabulary from the file.

    Raises
    ------
    InvalidVocabDumpError
        If the file is not a valid vocabulary dump, or if the data has been
        tampered with.
    FileNotFoundError
        If the file does not exist.

    Examples
    --------
    >>> read_vocab_dump(Path("path_to_file.pickle"))  # doctest: +SKIP
    """
    if filename.suffix == ".lz4":
        with lz4.frame.open(filename, "rb") as file:
            content: bytes = file.read()
            pickled_data: bytes = content[:-64]
            signature: str = content[-64:].decode()
    else:
        with open(filename, "rb") as file:
            content = file.read()
            pickled_data = content[:-64]
            signature = content[-64:].decode()

    if (
        hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest() != signature
    ):  # pragma: no cover # this should never happen
        raise InvalidVocabDumpError(
            "Data integrity check failed for vocab dump.",
        )

    raw_data = pickle.loads(pickled_data)
    if isinstance(raw_data, VocabList):
        if raw_data.version == src.__version__:
            return raw_data
        warnings.warn(
            "Vocab dump is from a different version of vocab-tester.",
            stacklevel=2,
        )
        return _regenerate_vocab_list(raw_data)

    raise InvalidVocabDumpError(
        "Vocab dump is not valid.",
    )  # pragma: no cover # this should never happen
