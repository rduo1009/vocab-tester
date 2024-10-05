#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains representations of questions about Latin vocabulary."""

from __future__ import annotations

from dataclasses import dataclass

from .. import accido


@dataclass
class _Question[T]:
    """Generic class for questions."""

    main_answer: T
    answers: set[T]

    def check(self, response: T) -> bool:
        """Check if the response is correct.

        Parameters
        ----------
        response : T
            The response to the question.

        Returns
        -------
        bool
            True if the response is correct, False otherwise.
        """
        return response in self.answers


@dataclass
class TypeInEngToLatQuestion(_Question[str]):
    """A question that asks for the Latin translation of an English word.

    For example, "I search" (answer: "quaero")

    Attributes
    ----------
    prompt : str
        The prompt for the question (in English).
    main_answer : str
        The best answer to the question (in Latin).
    answers : set[str]
        The possible answers to the question (in Latin).
    """

    prompt: str


@dataclass
class TypeInLatToEngQuestion(_Question[str]):
    """A question that asks for the English translation of a Latin word.

    For example, "quaero" (answer: "I search")

    Attributes
    ----------
    prompt : str
        The prompt for the question (in Latin).
    main_answer : str
        The best answer to the question (in English).
    answers : set[str]
        The possible answers to the question (in English).
    """

    prompt: str


@dataclass
class ParseWordCompToLatQuestion(_Question[str]):
    """A question that asks for a Latin word given the grammatical
    components of the word.

    For example:
    present active indicative 2nd person plural of "quaero"
    (answer: "quaeratis").

    Attributes
    ----------
    prompt : str
        The prompt for the question.
    components : accido.misc.EndingComponents
        The grammatical components of the word.
    main_answer : str
        The best answer to the question.
    answers : set[str]
        The possible answers to the question.
    """  # noqa: D205

    prompt: str
    components: accido.misc.EndingComponents


@dataclass
class ParseWordLatToCompQuestion(_Question[accido.misc.EndingComponents]):
    """A question that asks for the grammatical components of a Latin
    word, given the word.

    For example:
    Parse "quaeratis" (hear: quaero, quaerere, quaesivi, quaesitus)
    (answer: "present active indicative 2nd person plural").

    Attributes
    ----------
    prompt : str
        The prompt for the question.
    dictionary_entry : str
        The dictionary entry for the word.
    main_answer : accido.misc.EndingComponents
        The best answer to the question.
    answers : set[accido.misc.EndingComponents]
        The possible answers to the question.
    """  # noqa: D205

    prompt: str
    dictionary_entry: str
