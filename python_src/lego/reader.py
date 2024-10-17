#!/usr/bin/env python3

"""Contains functions for reading vocabulary files."""

from __future__ import annotations

import hashlib
import hmac
import warnings
from re import match
from typing import TYPE_CHECKING

import dill as pickle
import lz4.frame  # type: ignore[import-untyped]

import python_src as src

from .. import accido
from ..accido.misc import Gender
from ..accido.type_aliases import is_termination
from .exceptions import InvalidVocabDumpError, InvalidVocabFileFormatError
from .misc import KEY, VocabList

if TYPE_CHECKING:
    from io import TextIOWrapper
    from pathlib import Path


def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
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
            raise TypeError(f"Unknown word type: {type(word)}")

    return VocabList(new_vocab)


def read_vocab_dump(filename: Path) -> VocabList:
    """Reads a vocabulary dump file and returns a VocabList object.

    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with. If the data is invalid, an exception is
    raised.
    If the file ends in .lz4, the file is decompressed using lz4.

    Parameters
    ----------
    filename : Path
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


def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
    if "/" in meaning:
        return accido.misc.MultipleMeanings([
            x.strip() for x in meaning.split("/")
        ])
    return meaning


def read_vocab_file(file_path: Path) -> VocabList:
    """Reads a vocabulary file and returns a VocabList object.

    Parameters
    ----------
    file_path : Path
        The path to the vocabulary file.

    Returns
    -------
    VocabList
        The vocabulary from the file.

    Raises
    ------
    InvalidVocabFileFormatError
        If the file is not a valid vocabulary file, or if the formatting
        is incorrect.
    FileNotFoundError
        If the file does not exist.

    Examples
    --------
    >>> read_vocab_file(Path("path_to_file.txt"))  # doctest: +SKIP
    """
    vocab: list[accido.endings._Word] = []
    file: TextIOWrapper

    with file_path.open("r") as file:
        line: str
        current: str = ""

        for line in (
            raw_line.strip()  # remove whitespace
            for raw_line in file.read().split("\n")  # for line in file
            if raw_line.strip()  # but skip if the line is blank
        ):
            match line[0]:
                case "#":
                    continue

                case "@":
                    match line[1:].strip():
                        case (
                            "Verb"
                            | "Adjective"
                            | "Noun"
                            | "Regular"
                            | "Pronoun"
                        ):
                            current = line[1:].strip()

                        case (
                            "Verbs"
                            | "Adjectives"
                            | "Nouns"
                            | "Regulars"
                            | "Pronouns"
                        ):
                            current = line[1:-1].strip()

                        case _:
                            raise InvalidVocabFileFormatError(
                                "Invalid part of speech: "
                                f"'{line[1:].strip()}'",
                            )

                case _:
                    parts: list[str] = line.strip().split(":")
                    if len(parts) != 2:
                        raise InvalidVocabFileFormatError(
                            f"Invalid line format: '{line}'",
                        )

                    meaning: accido.type_aliases.Meaning = _generate_meaning(
                        parts[0].strip(),
                    )
                    latin_parts: list[str] = [
                        raw_part.strip() for raw_part in parts[1].split(",")
                    ]

                    if not current:
                        raise InvalidVocabFileFormatError(
                            "Part of speech was not given",
                        )

                    vocab.append(
                        _parse_line(current, latin_parts, meaning, line),
                    )
    return VocabList(vocab)


def _parse_line(
    current: str,
    latin_parts: list[str],
    meaning: accido.type_aliases.Meaning,
    line: str,
) -> accido.endings._Word:
    match current:
        case "Verb":
            if len(latin_parts) not in {3, 4}:
                raise InvalidVocabFileFormatError(
                    f"Invalid verb format: '{line}'",
                )

            if len(latin_parts) > 3:
                return accido.endings.Verb(
                    present=latin_parts[0],
                    infinitive=latin_parts[1],
                    perfect=latin_parts[2],
                    ppp=latin_parts[3],
                    meaning=meaning,
                )
            return accido.endings.Verb(
                present=latin_parts[0],
                infinitive=latin_parts[1],
                perfect=latin_parts[2],
                meaning=meaning,
            )

        case "Noun":
            if len(latin_parts) != 3:
                raise InvalidVocabFileFormatError(
                    f"Invalid noun format: '{line}'",
                )

            try:
                return accido.endings.Noun(
                    meaning=meaning,
                    nominative=latin_parts[0],
                    genitive=latin_parts[1].split()[0],
                    gender=Gender(latin_parts[2].split()[-1].strip("()")),
                )
            except ValueError as e:
                raise InvalidVocabFileFormatError(
                    "Invalid gender: "
                    f"'{latin_parts[2].split()[-1].strip('()')}'",
                ) from e

        case "Adjective":
            if len(latin_parts) not in {3, 4}:
                raise InvalidVocabFileFormatError(
                    f"Invalid adjective format: '{line}'",
                )

            declension: str = latin_parts[-1].strip("()")

            if declension not in {"212", "2-1-2"} and not match(
                r"^3-.$",
                declension,
            ):
                raise InvalidVocabFileFormatError(
                    f"Invalid adjective declension: '{declension}'",
                )
            if declension.startswith("3"):
                termination = int(declension[2])
                assert is_termination(termination)

                return accido.endings.Adjective(
                    *latin_parts[:-1],
                    termination=termination,
                    declension="3",
                    meaning=meaning,
                )
            return accido.endings.Adjective(
                *latin_parts[:-1],
                meaning=meaning,
                declension="212",
            )
        case "Regular":
            return accido.endings.RegularWord(
                word=latin_parts[0],
                meaning=meaning,
            )

        case "Pronoun":
            return accido.endings.Pronoun(
                meaning=meaning,
                pronoun=latin_parts[0],
            )

        case _:  # pragma: no cover # this should never happen
            raise ValueError
