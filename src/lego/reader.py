#!/usr/bin/env python3

from io import StringIO
from re import match
from typing import Final

from .. import accido
from .custom_exceptions import InvalidVocabFileFormat

GENDER_SHORTHAND: Final[dict[str, str]] = {
    "m": "masculine",
    "f": "feminine",
    "n": "neuter",
}


def read_vocab_file(file: StringIO) -> list[accido.endings._Word]:
    line: str
    current: str = ""
    vocab: list[accido.endings._Word] = []

    for line in (
        raw_line.strip()  # remove whitespace
        for raw_line in file.read().split("\n")  # for line in file
        if raw_line.strip()  # but skip if the line is blank
    ):
        match line[0]:
            case "#":
                continue
            case "@":
                match line[1:]:
                    case "Verb" | "Adjective" | "Noun" | "Regular" | "Pronoun":
                        current = line[1:]
                    case (
                        "Verbs"
                        | "Adjectives"
                        | "Nouns"
                        | "Regulars"
                        | "Pronouns"
                    ):
                        current = line[1:-1]
                    case _:
                        raise InvalidVocabFileFormat(
                            f"Invalid part of speech: {line[1:]}"
                        )
            case _:
                parts: list[str] = line.strip().split(":")
                if len(parts) != 2:
                    raise InvalidVocabFileFormat(
                        f"Invalid line format: {line}"
                    )

                meaning: str = parts[0].strip()
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
                                accido.endings.LearningVerb(
                                    present=latin_parts[0],
                                    infinitive=latin_parts[1],
                                    perfect=latin_parts[2],
                                    ppp=latin_parts[3],
                                    meaning=meaning,
                                )
                            )
                        else:
                            vocab.append(
                                accido.endings.LearningVerb(
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
                                        latin_parts[2].split()[-1].strip("()")
                                    ],
                                )
                            )
                        except KeyError:
                            raise InvalidVocabFileFormat(
                                f"Invalid gender: {latin_parts[2].split()[-1].strip("()")}"
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
                                    declension=declension,
                                )
                            )
                        elif declension.startswith("3"):
                            if (
                                len(latin_parts) == 4
                            ):  # i.e. three principal parts
                                vocab.append(
                                    accido.endings.Adjective(
                                        *latin_parts[:-1],
                                        termination=3,
                                        declension="3",
                                        meaning=meaning,
                                    )
                                )
                            else:
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
                            accido.endings.RegularWord(latin_parts[0], meaning)
                        )
                    case "Pronoun":
                        vocab.append(
                            accido.endings.Pronoun(
                                meaning=meaning, pronoun=latin_parts[0]
                            )
                        )
                    # case _:
                    #    raise InvalidVocabFileFormat(
                    #        f"Invalid word type: {current}"
                    #    )
    return vocab
