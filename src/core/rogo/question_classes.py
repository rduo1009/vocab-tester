"""Contains representations of questions about Latin vocabulary."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Protocol

from .. import accido


class QuestionClasses(Enum):
    """The classes of questions that can be asked."""

    TYPEIN_ENGTOLAT = "TypeInEngtoLatQuestion"
    TYPEIN_LATTOENG = "TypeInLattoEngQuestion"
    PARSEWORD_LATTOCOMP = "ParseWordLattoCompQuestion"
    PARSEWORD_COMPTOLAT = "ParseWordComptoLatQuestion"
    PRINCIPAL_PARTS = "PrincipalPartsQuestion"
    MULTIPLECHOICE_ENGTOLAT = "MultipleChoiceEngtoLatQuestion"
    MULTIPLECHOICE_LATTOENG = "MultipleChoiceLatToEngQuestion"


class Question(Protocol):
    """A protocol for questions."""

    prompt: Any

    def check(self, response: Any) -> bool:
        """Check if the response is correct."""


@dataclass
class _MultiAnswerQuestion[T]:
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
class _MultipleChoiceQuestion:
    """Generic class for multiple choice questions."""

    prompt: str
    answer: str
    choices: tuple[str, ...]

    def check(self, response: str) -> bool:
        """Check if the given answer is correct.

        Parameters
        ----------
        response : str
            The answer to check.

        Returns
        -------
        bool
            True if the given answer is correct, False otherwise.
        """
        return response == self.answer


@dataclass
class TypeInEngToLatQuestion(_MultiAnswerQuestion[str]):
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
class TypeInLatToEngQuestion(_MultiAnswerQuestion[str]):
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
class ParseWordCompToLatQuestion(_MultiAnswerQuestion[str]):
    """A question that asks for a Latin word given the grammatical
    components of the word.

    For example:
    present active indicative 2nd person plural of "quaero"
    (answer: "quaeratis").

    Attributes
    ----------
    prompt : str
        The prompt for the question (the dictionary entry).
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
class ParseWordLatToCompQuestion(
    _MultiAnswerQuestion[accido.misc.EndingComponents]
):
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


@dataclass
class PrincipalPartsQuestion:
    """A question that asks for the principal parts of a Latin verb.

    Attributes
    ----------
    prompt : str
        The prompt of the question.
    principal_parts : tuple[str, ...]
        The answer of the question (the principal parts).
    """

    prompt: str
    principal_parts: tuple[str, ...]

    def check(self, response: tuple[str, ...]) -> bool:
        """Check if the given principal parts are correct.

        Parameters
        ----------
        response : tuple[str, ...]
            The principal parts to check.

        Returns
        -------
        bool
            True if the given principal parts are correct, False otherwise.
        """
        return response == self.principal_parts


@dataclass
class MultipleChoiceEngToLatQuestion(_MultipleChoiceQuestion):
    """An English to Latin multiple choice question.

    Attributes
    ----------
    prompt : str
        The prompt of the question (in English).
    answer : str
        The answer of the question (in Latin).
    choices : tuple[str, ...]
        The choices of the question (including the answer).
    """


@dataclass
class MultipleChoiceLatToEngQuestion(_MultipleChoiceQuestion):
    """A Latin to English multiple choice question.

    Attributes
    ----------
    prompt : str
        The prompt of the question (in Latin).
    answer : str
        The answer of the question (in English).
    choices : tuple[str, ...]
        The choices of the question (including the answer).
    """
