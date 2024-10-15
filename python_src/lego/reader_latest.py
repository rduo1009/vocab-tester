#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions for reading vocabulary files."""

from __future__ import annotations

import sys

assert sys.version_info >= (3, 10)

from re import match
from typing import TYPE_CHECKING, Final

from .. import accido
from ..accido.misc import Gender
from ..accido.type_aliases import is_termination
from .exceptions import (
    InvalidVocabFileFormatError,
)
from .misc import VocabList

if TYPE_CHECKING:
    from io import TextIOWrapper
    from pathlib import Path

"""Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND: Final[dict[str, str]] = {
    "m": "masculine",
    "f": "feminine",
    "n": "neuter",
}


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
    file_path : pathlib.Path
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
