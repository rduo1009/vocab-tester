"""Contains functions for reading vocabulary files."""

from __future__ import annotations

import hashlib
import hmac
import warnings
from re import match
from typing import TYPE_CHECKING, Literal, cast

import dill as pickle
import lz4.frame  # type: ignore[import-untyped]

import src

from .. import accido
from ..accido.misc import Gender
from ..accido.type_aliases import is_termination
from .exceptions import (
    InvalidVocabDumpError,
    InvalidVocabFileFormatError,
)
from .misc import KEY, VocabList

if TYPE_CHECKING:
    from io import TextIOWrapper
    from pathlib import Path

    from ..accido.type_aliases import Meaning


def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
    word: accido.endings._Word
    new_vocab: list[accido.endings._Word] = []

    for word in vocab_list.vocab:
        if isinstance(word, accido.endings.RegularWord):
            new_vocab.append(
                accido.endings.RegularWord(
                    word.word,
                    meaning=word.meaning,
                ),
            )

        elif isinstance(word, accido.endings.Verb):
            new_vocab.append(
                accido.endings.Verb(
                    word.present,
                    word.infinitive,
                    word.perfect,
                    word.ppp,
                    meaning=word.meaning,
                ),
            )

        elif isinstance(word, accido.endings.Noun):
            new_vocab.append(
                accido.endings.Noun(
                    word.nominative,
                    word.genitive,
                    meaning=word.meaning,
                    gender=word.gender,
                ),
            )

        elif isinstance(word, accido.endings.Adjective):
            if word.declension == "212":
                new_vocab.append(
                    accido.endings.Adjective(
                        *word._principal_parts,  # noqa: SLF001
                        declension="212",
                        meaning=word.meaning,
                    ),
                )
            else:
                assert word.termination is not None

                new_vocab.append(
                    accido.endings.Adjective(
                        *word._principal_parts,  # noqa: SLF001
                        termination=word.termination,
                        declension="3",
                        meaning=word.meaning,
                    ),
                )

        elif isinstance(word, accido.endings.Pronoun):
            new_vocab.append(
                accido.endings.Pronoun(
                    word.pronoun,
                    meaning=word.meaning,
                ),
            )

    return VocabList(new_vocab)


def read_vocab_dump(filename: Path) -> VocabList:
    """Read a vocabulary dump file and returns a VocabList object.

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

    if hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest() != signature:
        raise InvalidVocabDumpError(
            "Data integrity check failed for vocab dump."
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

    raise InvalidVocabDumpError("Vocab dump is not valid.")


def _generate_meaning(meaning: str) -> Meaning:
    if "/" in meaning:
        return accido.misc.MultipleMeanings(
            tuple(x.strip() for x in meaning.split("/"))
        )
    return meaning


type _PartOfSpeech = Literal[  # pragma: no mutate
    "Verb", "Adjective", "Noun", "Regular", "Pronoun"  # pragma: no mutate
]


def _is_typeofspeech(x: str) -> bool:
    return x in {
        "Verb",
        "Adjective",
        "Noun",
        "Regular",
        "Pronoun",
    }


def read_vocab_file(file_path: Path) -> VocabList:
    """Read a vocabulary file and returns a VocabList object.

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
    InvalidVocabListError
        If the vocab list created from the file is invalid.

    Examples
    --------
    >>> read_vocab_file(Path("path_to_file.txt"))  # doctest: +SKIP
    """
    vocab: list[accido.endings._Word] = []
    file: TextIOWrapper

    with file_path.open("r") as file:
        line: str
        current: _PartOfSpeech | Literal[""] = ""

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
                            assert _is_typeofspeech(line[1:].strip())
                            current = cast(_PartOfSpeech, line[1:].strip())

                        case (
                            "Verbs"
                            | "Adjectives"
                            | "Nouns"
                            | "Regulars"
                            | "Pronouns"
                        ):
                            assert _is_typeofspeech(line[1:-1].strip())
                            current = cast(_PartOfSpeech, line[1:-1].strip())

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

                    meaning: Meaning = _generate_meaning(
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
    current: _PartOfSpeech,
    latin_parts: list[str],
    meaning: Meaning,
    line: str,
) -> accido.endings._Word:
    match current:
        case "Verb":
            if len(latin_parts) not in {3, 4}:
                raise InvalidVocabFileFormatError(
                    f"Invalid verb format: '{line}'",
                )

            # Verb with ppp
            if len(latin_parts) > 3:
                return accido.endings.Verb(
                    latin_parts[0],
                    latin_parts[1],
                    latin_parts[2],
                    latin_parts[3],
                    meaning=meaning,
                )

            # Verb without ppp
            return accido.endings.Verb(
                latin_parts[0],
                latin_parts[1],
                latin_parts[2],
                meaning=meaning,
            )

        case "Noun":
            if len(latin_parts) != 3:
                raise InvalidVocabFileFormatError(
                    f"Invalid noun format: '{line}'",
                )

            try:
                return accido.endings.Noun(
                    latin_parts[0],
                    latin_parts[1].split()[0],
                    gender=Gender(latin_parts[2].split()[-1].strip("()")),
                    meaning=meaning,
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

            # Third declension adjective
            if declension.startswith("3"):
                termination = int(declension[2])
                assert is_termination(termination)

                return accido.endings.Adjective(
                    *latin_parts[:-1],
                    termination=termination,
                    declension="3",
                    meaning=meaning,
                )

            # Second declension adjective
            return accido.endings.Adjective(
                *latin_parts[:-1],
                meaning=meaning,
                declension="212",
            )

        case "Regular":
            return accido.endings.RegularWord(
                latin_parts[0],
                meaning=meaning,
            )

    return accido.endings.Pronoun(
        latin_parts[0],
        meaning=meaning,
    )
