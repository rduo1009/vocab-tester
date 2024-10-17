#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6d08a3a

# Compiled with Coconut version 3.1.2

"""Contains functions for reading vocabulary files."""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.2', '', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------



import hashlib  #3: import hashlib
import hmac  #4: import hmac
import warnings  #5: import warnings
from re import match  #6: from re import match
try:  #7: from typing import Final
    _coconut_sys_0 = sys  # type: ignore  #7: from typing import Final
except _coconut.NameError:  #7: from typing import Final
    _coconut_sys_0 = _coconut_sentinel  #7: from typing import Final
sys = _coconut_sys  #7: from typing import Final
if sys.version_info >= (3, 8):  #7: from typing import Final
    if _coconut.typing.TYPE_CHECKING:  #7: from typing import Final
        from typing import Final  #7: from typing import Final
    else:  #7: from typing import Final
        try:  #7: from typing import Final
            Final = _coconut.typing.Final  #7: from typing import Final
        except _coconut.AttributeError as _coconut_imp_err:  #7: from typing import Final
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #7: from typing import Final
else:  #7: from typing import Final
    from typing_extensions import Final  #7: from typing import Final
if _coconut_sys_0 is not _coconut_sentinel:  #7: from typing import Final
    sys = _coconut_sys_0  #7: from typing import Final

import dill as pickle  #9: import dill as pickle
import lz4.frame  #10: import lz4.frame

import python_src as src  #12: import python_src as src

from .. import accido  #14: from .. import accido
from .exceptions import InvalidVocabDumpError  #15: from .exceptions import InvalidVocabDumpError, InvalidVocabFileFormatError
from .exceptions import InvalidVocabFileFormatError  #15: from .exceptions import InvalidVocabDumpError, InvalidVocabFileFormatError
from .misc import KEY  #16: from .misc import KEY, VocabList
from .misc import VocabList  #16: from .misc import KEY, VocabList

if TYPE_CHECKING:  #18: if TYPE_CHECKING:
    from io import TextIOWrapper  #19:     from io import TextIOWrapper
    from pathlib import Path  #20:     from pathlib import Path

"""Mapping of gender values to their more concise abbreviated forms."""  #22: """Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND = _coconut.dict((("m", "masculine"), ("f", "feminine"), ("n", "neuter")))  # type: Final[dict[str, str]]  #23: GENDER_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #23: GENDER_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #23: GENDER_SHORTHAND: Final[dict[str, str]] = {
__annotations__["GENDER_SHORTHAND"] = 'Final[dict[str, str]]'  #23: GENDER_SHORTHAND: Final[dict[str, str]] = {


@_coconut_tco  #30: def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
def _regenerate_vocab_list(vocab_list  # type: VocabList  #30: def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
    ):  #30: def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
# type: (...) -> VocabList
    """Regenerates a VocabList from a VocabList.

    This is useful for regenerating a VocabList if it was created in a
    previous version of the package.

    Parameters
    ----------
    vocab_list : VocabList
        The VocabList to regenerate.

    Returns
    -------
    VocabList
        The regenerated VocabList.
    """  #45:     """
    word = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: accido.endings._Word  #46:     word: accido.endings._Word
    if "__annotations__" not in _coconut.locals():  #46:     word: accido.endings._Word
        __annotations__ = {}  # type: ignore  #46:     word: accido.endings._Word
    __annotations__["word"] = 'accido.endings._Word'  #46:     word: accido.endings._Word
    new_vocab = []  # type: list[accido.endings._Word]  #47:     new_vocab: list[accido.endings._Word] = []
    if "__annotations__" not in _coconut.locals():  #47:     new_vocab: list[accido.endings._Word] = []
        __annotations__ = {}  # type: ignore  #47:     new_vocab: list[accido.endings._Word] = []
    __annotations__["new_vocab"] = 'list[accido.endings._Word]'  #47:     new_vocab: list[accido.endings._Word] = []

    for word in vocab_list.vocab:  #49:     for word in vocab_list.vocab:
        if type(word) is accido.endings.RegularWord:  #50:         if type(word) is accido.endings.RegularWord:
            new_vocab.append(accido.endings.RegularWord(word=word.word, meaning=word.meaning))  #51:             new_vocab.append(
        elif type(word) is accido.endings.Verb:  #57:         elif type(word) is accido.endings.Verb:
            new_vocab.append(accido.endings.Verb(present=word.present, infinitive=word.infinitive, perfect=word.perfect, ppp=word.ppp, meaning=word.meaning))  #58:             new_vocab.append(
        elif type(word) is accido.endings.Noun:  #67:         elif type(word) is accido.endings.Noun:
            new_vocab.append(accido.endings.Noun(nominative=word.nominative, genitive=word.genitive, meaning=word.meaning, gender=word.gender))  #68:             new_vocab.append(
        elif type(word) is accido.endings.Adjective:  #76:         elif type(word) is accido.endings.Adjective:
            new_vocab.append(accido.endings.Adjective(*word._principal_parts, termination=word.termination, declension=word.declension, meaning=word.meaning))  # type: ignore[misc, arg-type]  #77:             new_vocab.append(
        elif type(word) is accido.endings.Pronoun:  #85:         elif type(word) is accido.endings.Pronoun:
            new_vocab.append(accido.endings.Pronoun(pronoun=word.pronoun, meaning=word.meaning))  #86:             new_vocab.append(
        else:  # pragma: no cover # this should never happen  #92:         else:  # pragma: no cover # this should never happen
            raise ValueError("Unknown word type: {_coconut_format_0}".format(_coconut_format_0=(type(word))))  # noqa: DOC501  #93:             raise ValueError(f"Unknown word type: {type(word)}")  # noqa: DOC501

    return _coconut_tail_call(VocabList, new_vocab)  #95:     return VocabList(new_vocab)



@_coconut_tco  #98: def read_vocab_dump(filename: Path) -> VocabList:
def read_vocab_dump(filename  # type: Path  #98: def read_vocab_dump(filename: Path) -> VocabList:
    ):  #98: def read_vocab_dump(filename: Path) -> VocabList:
# type: (...) -> VocabList
    """Reads a vocabulary dump file and returns a VocabList object.

    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with. If the data is invalid, an exception is
    raised.
    If the file ends in .lz4, the file is decompressed using lz4.

    Parameters
    ----------
    filename : pathlib.Path
        The path to the vocabulary dump file.

    Returns
    -------
    VocabList
        The vocabulary from the file.

    Raises
    ------
    InvalidVocabDumpError
        If the file is not a valid vocabulary dump, or if the data has been
        tampered with.
    FileNotFoundError
        If the file does not exist.

    Examples
    --------
    >>> read_vocab_dump(Path("path_to_file.pickle"))  # doctest: +SKIP
    """  #127:     """
    if filename.suffix == ".lz4":  #128:     if filename.suffix == ".lz4":
        with lz4.frame.open(filename, "rb") as file:  #129:         with lz4.frame.open(filename, "rb") as file:
            content = file.read()  # type: bytes  #130:             content: bytes = file.read()
            if "__annotations__" not in _coconut.locals():  #130:             content: bytes = file.read()
                __annotations__ = {}  # type: ignore  #130:             content: bytes = file.read()
            __annotations__["content"] = 'bytes'  #130:             content: bytes = file.read()
            pickled_data = content[:-64]  # type: bytes  #131:             pickled_data: bytes = content[:-64]
            if "__annotations__" not in _coconut.locals():  #131:             pickled_data: bytes = content[:-64]
                __annotations__ = {}  # type: ignore  #131:             pickled_data: bytes = content[:-64]
            __annotations__["pickled_data"] = 'bytes'  #131:             pickled_data: bytes = content[:-64]
            signature = content[-64:].decode()  # type: str  #132:             signature: str = content[-64:].decode()
            if "__annotations__" not in _coconut.locals():  #132:             signature: str = content[-64:].decode()
                __annotations__ = {}  # type: ignore  #132:             signature: str = content[-64:].decode()
            __annotations__["signature"] = 'str'  #132:             signature: str = content[-64:].decode()
    else:  #133:     else:
        with open(filename, "rb") as file:  #134:         with open(filename, "rb") as file:
            content = file.read()  # type: bytes  #135:             content: bytes = file.read()
            if "__annotations__" not in _coconut.locals():  #135:             content: bytes = file.read()
                __annotations__ = {}  # type: ignore  #135:             content: bytes = file.read()
            __annotations__["content"] = 'bytes'  #135:             content: bytes = file.read()
            pickled_data = content[:-64]  # type: bytes  #136:             pickled_data: bytes = content[:-64]
            if "__annotations__" not in _coconut.locals():  #136:             pickled_data: bytes = content[:-64]
                __annotations__ = {}  # type: ignore  #136:             pickled_data: bytes = content[:-64]
            __annotations__["pickled_data"] = 'bytes'  #136:             pickled_data: bytes = content[:-64]
            signature = content[-64:].decode()  # type: str  #137:             signature: str = content[-64:].decode()
            if "__annotations__" not in _coconut.locals():  #137:             signature: str = content[-64:].decode()
                __annotations__ = {}  # type: ignore  #137:             signature: str = content[-64:].decode()
            __annotations__["signature"] = 'str'  #137:             signature: str = content[-64:].decode()

    if (hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest() != signature):  # pragma: no cover # this should never happen  #139:     if (
        raise InvalidVocabDumpError("Data integrity check failed for vocab dump.")  #142:         raise InvalidVocabDumpError(

    raw_data = pickle.loads(pickled_data)  #146:     raw_data = pickle.loads(pickled_data)
    if type(raw_data) is VocabList:  # type: ignore[comparison-overlap] # mypy cannot recognise this  #147:     if type(raw_data) is VocabList:  # type: ignore[comparison-overlap] # mypy cannot recognise this
        if raw_data.version == src.__version__:  #148:         if raw_data.version == src.__version__:
            return raw_data  #149:             return raw_data
        warnings.warn("Vocab dump is from a different version of vocab-tester.", stacklevel=2)  #150:         warnings.warn(
        return _coconut_tail_call(_regenerate_vocab_list, raw_data)  #154:         return _regenerate_vocab_list(raw_data)

    raise InvalidVocabDumpError("Vocab dump is not valid.")  # pragma: no cover # this should never happen  #156:     raise InvalidVocabDumpError(



@_coconut_tco  #161: def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
def _generate_meaning(meaning  # type: str  #161: def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
    ):  #161: def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
# type: (...) -> accido.type_aliases.Meaning
    if "/" in meaning:  #162:     if "/" in meaning:
        return _coconut_tail_call(accido.misc.MultipleMeanings, [x.strip() for x in meaning.split("/")])  #163:         return accido.misc.MultipleMeanings([
    return meaning  #166:     return meaning



@_coconut_tco  #169: def read_vocab_file(file_path: Path) -> VocabList:
def read_vocab_file(file_path  # type: Path  #169: def read_vocab_file(file_path: Path) -> VocabList:
    ):  #169: def read_vocab_file(file_path: Path) -> VocabList:
# type: (...) -> VocabList
    """Reads a vocabulary file and returns a VocabList object.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the vocabulary file.

    Returns
    -------
    VocabList
        The vocabulary from the file.

    Raises
    ------
    InvalidVocabFileFormatError
        If the file is not a valid vocabulary file, or if the formatting
        is incorrect.
    FileNotFoundError
        If the file does not exist.

    Examples
    --------
    >>> read_vocab_file(Path("path_to_file.txt"))  # doctest: +SKIP
    """  #193:     """
    vocab = []  # type: list[accido.endings._Word]  #194:     vocab: list[accido.endings._Word] = []
    if "__annotations__" not in _coconut.locals():  #194:     vocab: list[accido.endings._Word] = []
        __annotations__ = {}  # type: ignore  #194:     vocab: list[accido.endings._Word] = []
    __annotations__["vocab"] = 'list[accido.endings._Word]'  #194:     vocab: list[accido.endings._Word] = []
    file = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: TextIOWrapper  #195:     file: TextIOWrapper
    if "__annotations__" not in _coconut.locals():  #195:     file: TextIOWrapper
        __annotations__ = {}  # type: ignore  #195:     file: TextIOWrapper
    __annotations__["file"] = 'TextIOWrapper'  #195:     file: TextIOWrapper

    with file_path.open("r") as file:  #197:     with file_path.open("r") as file:
        line = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #198:         line: str
        if "__annotations__" not in _coconut.locals():  #198:         line: str
            __annotations__ = {}  # type: ignore  #198:         line: str
        __annotations__["line"] = 'str'  #198:         line: str
        current = ""  # type: str  #199:         current: str = ""
        if "__annotations__" not in _coconut.locals():  #199:         current: str = ""
            __annotations__ = {}  # type: ignore  #199:         current: str = ""
        __annotations__["current"] = 'str'  #199:         current: str = ""

        for line in (raw_line.strip() for raw_line in file.read().split("\n") if raw_line.strip()):  # remove whitespace  # but skip if the line is blank  # for line in file  #201:         for line in (
            _coconut_case_match_to_1 = line[0]  #206:             match line[0]:
            _coconut_case_match_check_1 = False  #206:             match line[0]:
            if _coconut_case_match_to_1 == "#":  #206:             match line[0]:
                _coconut_case_match_check_1 = True  #206:             match line[0]:
            if _coconut_case_match_check_1:  #206:             match line[0]:
                continue  #208:                     continue

            if not _coconut_case_match_check_1:  #210:                 case "@":
                if _coconut_case_match_to_1 == "@":  #210:                 case "@":
                    _coconut_case_match_check_1 = True  #210:                 case "@":
                if _coconut_case_match_check_1:  #210:                 case "@":
                    _coconut_case_match_to_0 = line[1:].strip()  #210:                 case "@":
                    _coconut_case_match_check_0 = False  #210:                 case "@":
                    _coconut_case_match_check_0 = True  #210:                 case "@":
                    if _coconut_case_match_check_0:  #210:                 case "@":
                        _coconut_case_match_check_0 = False  #210:                 case "@":
                        if not _coconut_case_match_check_0:  #210:                 case "@":
                            if _coconut_case_match_to_0 == "Verb":  #210:                 case "@":
                                _coconut_case_match_check_0 = True  #210:                 case "@":

                        if not _coconut_case_match_check_0:  #210:                 case "@":
                            if _coconut_case_match_to_0 == "Adjective":  #210:                 case "@":
                                _coconut_case_match_check_0 = True  #210:                 case "@":

                        if not _coconut_case_match_check_0:  #210:                 case "@":
                            if _coconut_case_match_to_0 == "Noun":  #210:                 case "@":
                                _coconut_case_match_check_0 = True  #210:                 case "@":

                        if not _coconut_case_match_check_0:  #210:                 case "@":
                            if _coconut_case_match_to_0 == "Regular":  #210:                 case "@":
                                _coconut_case_match_check_0 = True  #210:                 case "@":

                        if not _coconut_case_match_check_0:  #210:                 case "@":
                            if _coconut_case_match_to_0 == "Pronoun":  #210:                 case "@":
                                _coconut_case_match_check_0 = True  #210:                 case "@":


                    if _coconut_case_match_check_0:  #210:                 case "@":
                        current = line[1:].strip()  #219:                             current = line[1:].strip()

                    if not _coconut_case_match_check_0:  #221:                         case (
                        _coconut_case_match_check_0 = True  #221:                         case (
                        if _coconut_case_match_check_0:  #221:                         case (
                            _coconut_case_match_check_0 = False  #221:                         case (
                            if not _coconut_case_match_check_0:  #221:                         case (
                                if _coconut_case_match_to_0 == "Verbs":  #221:                         case (
                                    _coconut_case_match_check_0 = True  #221:                         case (

                            if not _coconut_case_match_check_0:  #221:                         case (
                                if _coconut_case_match_to_0 == "Adjectives":  #221:                         case (
                                    _coconut_case_match_check_0 = True  #221:                         case (

                            if not _coconut_case_match_check_0:  #221:                         case (
                                if _coconut_case_match_to_0 == "Nouns":  #221:                         case (
                                    _coconut_case_match_check_0 = True  #221:                         case (

                            if not _coconut_case_match_check_0:  #221:                         case (
                                if _coconut_case_match_to_0 == "Regulars":  #221:                         case (
                                    _coconut_case_match_check_0 = True  #221:                         case (

                            if not _coconut_case_match_check_0:  #221:                         case (
                                if _coconut_case_match_to_0 == "Pronouns":  #221:                         case (
                                    _coconut_case_match_check_0 = True  #221:                         case (


                        if _coconut_case_match_check_0:  #221:                         case (
                            current = line[1:-1].strip()  #228:                             current = line[1:-1].strip()

                    if not _coconut_case_match_check_0:  #230:                         case _:
                        _coconut_case_match_check_0 = True  #230:                         case _:
                        if _coconut_case_match_check_0:  #230:                         case _:
                            raise InvalidVocabFileFormatError("Invalid part of speech: {_coconut_format_0}".format(_coconut_format_0=(line[1:].strip())))  #231:                             raise InvalidVocabFileFormatError(

            if not _coconut_case_match_check_1:  #235:                 case _:
                _coconut_case_match_check_1 = True  #235:                 case _:
                if _coconut_case_match_check_1:  #235:                 case _:
                    parts = line.strip().split(":")  # type: list[str]  #235:                 case _:
                    if "__annotations__" not in _coconut.locals():  #235:                 case _:
                        __annotations__ = {}  # type: ignore  #235:                 case _:
                    __annotations__["parts"] = 'list[str]'  #236:                     parts: list[str] = line.strip().split(":")
                    if len(parts) != 2:  #237:                     if len(parts) != 2:
                        raise InvalidVocabFileFormatError("Invalid line format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #238:                         raise InvalidVocabFileFormatError(

                    meaning = _generate_meaning(parts[0].strip())  # type: accido.type_aliases.Meaning  #242:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                    if "__annotations__" not in _coconut.locals():  #242:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                        __annotations__ = {}  # type: ignore  #242:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                    __annotations__["meaning"] = 'accido.type_aliases.Meaning'  #242:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                    latin_parts = [raw_part.strip() for raw_part in parts[1].split(",")]  # type: list[str]  #245:                     latin_parts: list[str] = [
                    if "__annotations__" not in _coconut.locals():  #245:                     latin_parts: list[str] = [
                        __annotations__ = {}  # type: ignore  #245:                     latin_parts: list[str] = [
                    __annotations__["latin_parts"] = 'list[str]'  #245:                     latin_parts: list[str] = [

                    if not current:  #249:                     if not current:
                        raise InvalidVocabFileFormatError("Part of speech was not given")  #250:                         raise InvalidVocabFileFormatError(

                    vocab.append(_parse_line(current, latin_parts, meaning, line))  #254:                     vocab.append(
    return _coconut_tail_call(VocabList, vocab)  #257:     return VocabList(vocab)


# type: ignore[return]
@_coconut_tco  # type: ignore[return]  #260: def _parse_line(  # type: ignore[return]
def _parse_line(current,  # type: str  # type: ignore[return]  #260: def _parse_line(  # type: ignore[return]
    latin_parts,  # type: list[str]  # type: ignore[return]  #260: def _parse_line(  # type: ignore[return]
    meaning,  # type: accido.type_aliases.Meaning  # type: ignore[return]  #260: def _parse_line(  # type: ignore[return]
    line,  # type: str  # type: ignore[return]  #260: def _parse_line(  # type: ignore[return]
    ):  # type: ignore[return]  #260: def _parse_line(  # type: ignore[return]
# type: (...) -> accido.endings._Word  # type: ignore[return]
    _coconut_case_match_to_2 = current  #266:     match current:
    _coconut_case_match_check_2 = False  #266:     match current:
    if _coconut_case_match_to_2 == "Verb":  #266:     match current:
        _coconut_case_match_check_2 = True  #266:     match current:
    if _coconut_case_match_check_2:  #266:     match current:
        if len(latin_parts) not in _coconut.set((3, 4)):  #268:             if len(latin_parts) not in {3, 4}:
            raise InvalidVocabFileFormatError("Invalid verb format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #269:                 raise InvalidVocabFileFormatError(

        if len(latin_parts) > 3:  #273:             if len(latin_parts) > 3:
            return _coconut_tail_call(accido.endings.Verb, present=latin_parts[0], infinitive=latin_parts[1], perfect=latin_parts[2], ppp=latin_parts[3], meaning=meaning)  #274:                 return accido.endings.Verb(
        return _coconut_tail_call(accido.endings.Verb, present=latin_parts[0], infinitive=latin_parts[1], perfect=latin_parts[2], meaning=meaning)  #281:             return accido.endings.Verb(

    if not _coconut_case_match_check_2:  #288:         case "Noun":
        if _coconut_case_match_to_2 == "Noun":  #288:         case "Noun":
            _coconut_case_match_check_2 = True  #288:         case "Noun":
        if _coconut_case_match_check_2:  #288:         case "Noun":
            if len(latin_parts) != 3:  #289:             if len(latin_parts) != 3:
                raise InvalidVocabFileFormatError("Invalid noun format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #290:                 raise InvalidVocabFileFormatError(

            try:  #294:             try:
                return accido.endings.Noun(meaning=meaning, nominative=latin_parts[0], genitive=latin_parts[1].split()[0], gender=GENDER_SHORTHAND[latin_parts[2].split()[-1].strip("()")])  #295:                 return accido.endings.Noun(
            except KeyError as e:  #303:             except KeyError as e:
                _coconut_raise_from_0 = InvalidVocabFileFormatError("Invalid gender: " + "{_coconut_format_0}".format(_coconut_format_0=(latin_parts[2].split()[-1].strip('()'))))  #304:                 raise InvalidVocabFileFormatError(
                _coconut_raise_from_0.__cause__ = e  #304:                 raise InvalidVocabFileFormatError(
                raise _coconut_raise_from_0  #304:                 raise InvalidVocabFileFormatError(

    if not _coconut_case_match_check_2:  #309:         case "Adjective":
        if _coconut_case_match_to_2 == "Adjective":  #309:         case "Adjective":
            _coconut_case_match_check_2 = True  #309:         case "Adjective":
        if _coconut_case_match_check_2:  #309:         case "Adjective":
            if len(latin_parts) not in _coconut.set((3, 4)):  #310:             if len(latin_parts) not in {3, 4}:
                raise InvalidVocabFileFormatError("Invalid adjective format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #311:                 raise InvalidVocabFileFormatError(

            declension = latin_parts[-1].strip("()")  # type: str  #315:             declension: str = latin_parts[-1].strip("()")
            if "__annotations__" not in _coconut.locals():  #315:             declension: str = latin_parts[-1].strip("()")
                __annotations__ = {}  # type: ignore  #315:             declension: str = latin_parts[-1].strip("()")
            __annotations__["declension"] = 'str'  #315:             declension: str = latin_parts[-1].strip("()")

            if declension not in _coconut.set(("212", "2-1-2")) and not match(r"^3-.$", declension):  #317:             if declension not in {"212", "2-1-2"} and not match(
                raise InvalidVocabFileFormatError("Invalid adjective declension: {_coconut_format_0}".format(_coconut_format_0=(declension)))  #321:                 raise InvalidVocabFileFormatError(
            if declension.startswith("3"):  #324:             if declension.startswith("3"):
                return _coconut_tail_call(accido.endings.Adjective, *latin_parts[:-1], termination=int(declension[2]), declension="3", meaning=meaning)  #325:                 return accido.endings.Adjective(
            return _coconut_tail_call(accido.endings.Adjective, *latin_parts[:-1], meaning=meaning, declension="212")  #331:             return accido.endings.Adjective(
    if not _coconut_case_match_check_2:  #336:         case "Regular":
        if _coconut_case_match_to_2 == "Regular":  #336:         case "Regular":
            _coconut_case_match_check_2 = True  #336:         case "Regular":
        if _coconut_case_match_check_2:  #336:         case "Regular":
            return _coconut_tail_call(accido.endings.RegularWord, word=latin_parts[0], meaning=meaning)  #337:             return accido.endings.RegularWord(

    if not _coconut_case_match_check_2:  #342:         case "Pronoun":
        if _coconut_case_match_to_2 == "Pronoun":  #342:         case "Pronoun":
            _coconut_case_match_check_2 = True  #342:         case "Pronoun":
        if _coconut_case_match_check_2:  #342:         case "Pronoun":
            return _coconut_tail_call(accido.endings.Pronoun, meaning=meaning, pronoun=latin_parts[0])  #343:             return accido.endings.Pronoun(

    if not _coconut_case_match_check_2:  # pragma: no cover # this should never happen  #348:         case _:  # pragma: no cover # this should never happen
        _coconut_case_match_check_2 = True  # pragma: no cover # this should never happen  #348:         case _:  # pragma: no cover # this should never happen
        if _coconut_case_match_check_2:  # pragma: no cover # this should never happen  #348:         case _:  # pragma: no cover # this should never happen
            raise ValueError  #349:             raise ValueError
