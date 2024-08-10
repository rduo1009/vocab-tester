#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import hmac
from pathlib import Path
from warnings import warn

import dill as pickle  # type: ignore

from .misc import VocabList, key


def save_vocab_dump(file_path: Path, vocab_list: VocabList) -> None:
    file_path = Path(file_path)

    if not file_path.parent.exists():
        raise FileNotFoundError(
            f"The directory {file_path.parent} does not exist."
        )

    if file_path.exists():
        warn(f"The file {file_path} already exists and has been overwritten.")

    pickled_data: bytes = pickle.dumps(vocab_list)

    signature = hmac.new(key, pickled_data, hashlib.sha256).hexdigest()

    with open(file_path, "wb") as file:
        file.write(pickled_data)
        file.write(signature.encode())
