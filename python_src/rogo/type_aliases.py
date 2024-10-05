#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contains type aliases used by rogo."""

from typing import Mapping

from .. import accido

type Settings = Mapping[str, str | bool | int]
type Vocab = list[accido.endings._Word]  # noqa: SLF001
