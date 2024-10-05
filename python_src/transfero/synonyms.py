#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Contains a function that finds synonyms of English words."""

from __future__ import annotations

import warnings
from pathlib import Path

from nltk import download
from nltk.corpus import wordnet
from nltk.data import find, path

project_root: Path = Path(__file__).parent.parent.parent
nltk_data_path: Path = project_root / "nltk_data"
nltk_data_path.mkdir(parents=True, exist_ok=True)
path.append(str(nltk_data_path))

if not nltk_data_path.exists():  # pragma: no cover
    nltk_data_path.mkdir(parents=True, exist_ok=True)
    warnings.warn(
        f"The directory {nltk_data_path} did not exist and has been created",
        stacklevel=2,
    )

try:
    find("corpora/wordnet.zip")
except LookupError:
    download("wordnet", download_dir=str(nltk_data_path))
    warnings.warn(
        f"The wordnet dataset was not found in {nltk_data_path} and has "
        "been downloaded",
        stacklevel=2,
    )

del find, download, path


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
            if lemma.name() != word and "_" not in lemma.name()
        )

    return synonyms
