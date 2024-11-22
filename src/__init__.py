"""A wrapper for the Python packages used by vocab-tester."""

import dunamai as _dunamai

from . import core

__version__ = _dunamai.get_version(
    "src", third_choice=_dunamai.Version.from_any_vcs
).serialize()
__author__ = "rduo1009"
__copyright__ = "2024, rduo1009"
__license__ = "MIT"
__all__ = ["core"]
