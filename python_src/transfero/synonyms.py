#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Contains a function that finds synonyms of English words."""

from __future__ import annotations

from nltk.corpus import wordnet  # type: ignore[import-untyped]


def find_synonyms(word: str) -> set[str]:
    """Finds synonyms of a word.

    Parameters
    ----------
    word : str
        The word to find synonyms of.

    Returns
    -------
    set[str]
        The synonyms of the word.
    """
    synonyms: set[str] = set()

    for synset in wordnet.synsets(word):
        synonyms.update(
            lemma.name()
            for lemma in synset.lemmas()
            if lemma.name != word and "_" not in lemma.name()
        )

    return synonyms
