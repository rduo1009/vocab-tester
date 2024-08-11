#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Contains representations of questions about Latin vocabulary."""

from .. import accido
from dataclasses import dataclass


# TI = type-in
# MC = multiple choice
# PW = parse word


@dataclass
class _Question:
    question: str


@dataclass
class TI_EngtoLat_Question(_Question):
    """A question that asks for the Latin translation of an English word."""

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
    """A question that asks for the English translation of a Latin word."""

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
