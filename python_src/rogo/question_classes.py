#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains representations of questions about Latin vocabulary."""

from __future__ import annotations

from dataclasses import dataclass

from .. import accido


@dataclass
class _Question[T]:
    """Generic class for questions."""

    prompt: T
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


TypeInEngToLatQuestion = _Question[str]
TypeInLatToEngQuestion = _Question[str]


@dataclass
class ParseWordCompToLatQuestion(_Question[str]):
    """A question that asks for a Latin word given the grammatical
    components of the word.

    For example:
    present active indicative 2nd person plural of "quaero"
    (answer: "quaeratis").
    """  # noqa: D205

    components: accido.misc.EndingComponents


@dataclass
class ParseWordLatToCompQuestion(_Question[accido.misc.EndingComponents]):
    """A question that asks for the grammatical components of a Latin
    word, given the word.

    For example:
    Parse "quaeratis" (hear: quaero, quaerere, quaesivi, quaesitus)
    (answer: "present active indicative 2nd person plural").
    """  # noqa: D205

    prompt: str  # overriding the parent class's prompt
    dictionary_entry: str
