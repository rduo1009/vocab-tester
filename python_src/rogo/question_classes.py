#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains representations of questions about Latin vocabulary."""

from dataclasses import dataclass

from .. import accido


# TI = type-in
# MC = multiple choice
# PW = parse word


class _Question:
    """Base class for questions."""

    pass


@dataclass
class TI_EngtoLat_Question(_Question):
    """A question that asks for the Latin translation of an English word.
    For example, "I search" (answer: "quaero")
    """

    english: str
    answer: accido.misc.Ending

    def check(self, response: str, further_answers: list[str]) -> bool:
        """Check if the response is correct."""
        if type(self.answer) is str:
            return response == self.answer
        elif type(self.answer) is accido.misc.MultipleEndings:
            return response in self.answer.get_all()
        else:
            raise TypeError(f"Unknown type of answer: {type(self.answer)}")


@dataclass
class TI_LattoEng_Question(_Question):
    """A question that asks for the English translation of a Latin word.
    For example, "quaero" (answer: "I search")"""

    latin: str
    answer: accido.misc.Meaning

    def check(self, response: str, further_answers: list[str]) -> bool:
        """Check if the response is correct."""
        if type(self.answer) is str:
            return response == self.answer
        elif type(self.answer) is accido.misc.MultipleMeanings:
            return response in self.answer.meanings
        elif self.answer in further_answers:
            return True
        else:
            raise TypeError(f"Unknown type of answer: {type(self.answer)}")


@dataclass
class PW_ComptoLat_Question(_Question):
    """A question that asks for a Latin word given the grammatical
    components of the word.
    For example:
    present active indicative 2nd person plural of "quaero"
    (answer: "quaeratis")"""

    latin: str
    components: accido.endings.EndingComponents
    answer: str

    def check(self, response: str) -> bool:
        return response == self.answer


@dataclass
class PW_LattoComp_Question(_Question):
    """A question that asks for the grammatical components of a Latin word,
    given the word.
    For example:
    Parse "quaeratis" (hear: quaero, quaerere, quaesivi, quaesitus)
    (answer: "present active indicative 2nd person plural")"""

    dictionary_entry: str
    latin: str
    answer: accido.endings.EndingComponents

    def check(self, response: accido.endings.EndingComponents) -> bool:
        return response == self.answer
