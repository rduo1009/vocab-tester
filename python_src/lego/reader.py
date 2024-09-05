#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains functions for reading vocabulary files."""

from __future__ import annotations

import hashlib
import hmac
import warnings
from io import TextIOWrapper
from pathlib import Path
from re import match
from typing import Final

import dill as pickle

import python_src as src

from .. import accido
from .exceptions import InvalidVocabDump, InvalidVocabFileFormat
from .misc import KEY, VocabList

"""Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND: Final[dict[str, str]] = {
    "m": "masculine",
    "f": "feminine",
    "n": "neuter",
}


def _generate_meaning(meaning: str) -> accido.misc.Meaning:
    if "/" in meaning:
        return accido.misc.MultipleMeanings([
            x.strip() for x in meaning.split("/")
        ])
    else:
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
    InvalidVocabFileFormat
        If the file is not a valid vocabulary file, or if the formatting
        is incorrect.
    FileNotFoundError
        If the file does not exist.

    Examples
    --------
    >>> read_vocab_file(Path("path_to_file.txt"))
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
                            raise InvalidVocabFileFormat(
                                f"Invalid part of speech: {line[1:].strip()}"
                            )

                case _:
                    parts: list[str] = line.strip().split(":")
                    if len(parts) != 2:
                        raise InvalidVocabFileFormat(
                            f"Invalid line format: {line}"
                        )

                    meaning: accido.misc.Meaning = _generate_meaning(
                        parts[0].strip()
                    )
                    latin_parts: list[str] = [
                        raw_part.strip() for raw_part in parts[1].split(",")
                    ]
                    match current:
                        case "":
                            raise InvalidVocabFileFormat(
                                "Part of speech was not given"
                            )

                        case "Verb":
                            if len(latin_parts) not in {3, 4}:
                                raise InvalidVocabFileFormat(
                                    f"Invalid verb format: {line}"
                                )

                            if len(latin_parts) > 3:
                                vocab.append(
                                    accido.endings.Verb(
                                        present=latin_parts[0],
                                        infinitive=latin_parts[1],
                                        perfect=latin_parts[2],
                                        ppp=latin_parts[3],
                                        meaning=meaning,
                                    )
                                )
                            else:
                                vocab.append(
                                    accido.endings.Verb(
                                        present=latin_parts[0],
                                        infinitive=latin_parts[1],
                                        perfect=latin_parts[2],
                                        meaning=meaning,
                                    )
                                )

                        case "Noun":
                            if len(latin_parts) != 3:
                                raise InvalidVocabFileFormat(
                                    f"Invalid noun format: {line}"
                                )

                            try:
                                vocab.append(
                                    accido.endings.Noun(
                                        meaning=meaning,
                                        nominative=latin_parts[0],
                                        genitive=latin_parts[1].split()[0],
                                        gender=GENDER_SHORTHAND[
                                            latin_parts[2]
                                            .split()[-1]
                                            .strip("()")
                                        ],
                                    )
                                )
                            except KeyError:
                                raise InvalidVocabFileFormat(
                                    f"Invalid gender: {latin_parts[2].split()[-1].strip('()')}"
                                )

                        case "Adjective":
                            if len(latin_parts) not in {3, 4}:
                                raise InvalidVocabFileFormat(
                                    f"Invalid adjective format: {line}"
                                )

                            declension: str = latin_parts[-1].strip("()")

                            if declension == "212":
                                vocab.append(
                                    accido.endings.Adjective(
                                        *latin_parts[:-1],
                                        meaning=meaning,
                                        declension="212",
                                    )
                                )
                            elif declension == "2-1-2":
                                vocab.append(
                                    accido.endings.Adjective(
                                        *latin_parts[:-1],
                                        meaning=meaning,
                                        declension="212",
                                    )
                                )
                            elif declension.startswith("3"):
                                if not match(r"^.-.$", declension):
                                    raise InvalidVocabFileFormat(
                                        f"Invalid adjective declension: {declension}"
                                    )
                                vocab.append(
                                    accido.endings.Adjective(
                                        *latin_parts[:-1],
                                        termination=int(declension[2]),
                                        declension="3",
                                        meaning=meaning,
                                    )
                                )
                            else:
                                raise InvalidVocabFileFormat(
                                    f"Invalid adjective declension: {declension}"
                                )

                        case "Regular":
                            vocab.append(
                                accido.endings.RegularWord(
                                    word=latin_parts[0], meaning=meaning
                                )
                            )

                        case "Pronoun":
                            vocab.append(
                                accido.endings.Pronoun(
                                    meaning=meaning, pronoun=latin_parts[0]
                                )
                            )

                        # case _:
                        #     raise InvalidVocabFileFormat(
                        #         f"Invalid word type: {current}"
                        #     )

    return VocabList(vocab)


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
        if type(word) is accido.endings.RegularWord:
            new_vocab.append(
                accido.endings.RegularWord(
                    word=word.word,
                    meaning=word.meaning,
                )
            )
        elif type(word) is accido.endings.Verb:
            new_vocab.append(
                accido.endings.Verb(
                    present=word.present,
                    infinitive=word.infinitive,
                    perfect=word.perfect,
                    ppp=word.ppp,
                    meaning=word.meaning,
                )
            )
        elif type(word) is accido.endings.Noun:
            new_vocab.append(
                accido.endings.Noun(
                    nominative=word.nominative,
                    genitive=word.genitive,
                    meaning=word.meaning,
                    gender=word.gender,
                )
            )
        elif type(word) is accido.endings.Adjective:
            new_vocab.append(
                accido.endings.Adjective(
                    *word._principal_parts,
                    termination=word.termination,
                    declension=word.declension,
                    meaning=word.meaning,
                )
            )
        elif type(word) is accido.endings.Pronoun:
            new_vocab.append(
                accido.endings.Pronoun(
                    pronoun=word.pronoun,
                    meaning=word.meaning,
                )
            )
        else:  # pragma: no cover # this should never happen
            raise ValueError(f"Unknown word type: {type(word)}")

    return VocabList(new_vocab)


def read_vocab_dump(filename: Path) -> VocabList:
    """Reads a vocabulary dump file and returns a VocabList object.
    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with. If the data is invalid, an exception is
    raised.

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
    InvalidVocabDump
        If the file is not a valid vocabulary dump, or if the data has been
        tampered with.
    FileNotFoundError
        If the file does not exist.

    Examples
    --------
    >>> read_vocab_dump(Path("path_to_file.pickle"))
    """

    with open(filename, "rb") as file:
        content: bytes = file.read()
        pickled_data: bytes = content[:-64]
        signature: str = content[-64:].decode()

    if (
        hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest() != signature
    ):  # pragma: no cover
        raise InvalidVocabDump("Data integrity check failed for vocab dump.")

    output = pickle.loads(pickled_data)
    if type(output) is VocabList:
        if output.version == src.__version__:
            return output
        else:  # pragma: no cover
            warnings.warn(
                "Vocab dump is from a different version of vocab-tester."
            )
            return _regenerate_vocab_list(output)

    raise InvalidVocabDump("Vocab dump is not valid.")  # pragma: no cover
