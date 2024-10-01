#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains representations of questions about Latin vocabulary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import accido

# TI = type-in
# MC = multiple choice
# PW = parse word


class _Question:
    """Base class for questions."""


@dataclass
class TI_EngtoLat_Question(_Question):
    """A question that asks for the Latin translation of an English word.
    For example, "I search" (answer: "quaero").
    """

    english: str
    answers: list[str]

    def check(self, response: str, further_answers: list[str]) -> bool:
        """Check if the response is correct."""
        return response in self.answers


@dataclass
class TI_LattoEng_Question(_Question):
    """A question that asks for the English translation of a Latin word.
    For example, "quaero" (answer: "I search").
    """

    latin: str
    answers: list[str]

    def check(self, response: str) -> bool:
        """Check if the response is correct."""
        return response in self.answers


@dataclass
class PW_ComptoLat_Question(_Question):
    """A question that asks for a Latin word given the grammatical
    components of the word.
    For example:
    present active indicative 2nd person plural of "quaero"
    (answer: "quaeratis").
    """

    latin: str
    components: accido.misc.EndingComponents
    answers: list[str]

    def check(self, response: str) -> bool:
        return response in self.answers


@dataclass
class PW_LattoComp_Question(_Question):
    """A question that asks for the grammatical components of a Latin word,
    given the word.
    For example:
    Parse "quaeratis" (hear: quaero, quaerere, quaesivi, quaesitus)
    (answer: "present active indicative 2nd person plural").
    """

    dictionary_entry: str
    latin: str
    answers: list[accido.misc.EndingComponents]

    def check(self, response: accido.misc.EndingComponents) -> bool:
        return response in self.answers
