#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe642de9b

# Compiled with Coconut version 3.1.2

"""Contains functions for reading vocabulary files."""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.2', '', True)
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

import python_src as src  #11: import python_src as src

from .. import accido  #13: from .. import accido
from .exceptions import InvalidVocabDumpError  #14: from .exceptions import InvalidVocabDumpError, InvalidVocabFileFormatError
from .exceptions import InvalidVocabFileFormatError  #14: from .exceptions import InvalidVocabDumpError, InvalidVocabFileFormatError
from .misc import KEY  #15: from .misc import KEY, VocabList
from .misc import VocabList  #15: from .misc import KEY, VocabList

if TYPE_CHECKING:  #17: if TYPE_CHECKING:
    from io import TextIOWrapper  #18:     from io import TextIOWrapper
    from pathlib import Path  #19:     from pathlib import Path

"""Mapping of gender values to their more concise abbreviated forms."""  #21: """Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND = _coconut.dict((("m", "masculine"), ("f", "feminine"), ("n", "neuter")))  # type: Final[dict[str, str]]  #22: GENDER_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #22: GENDER_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #22: GENDER_SHORTHAND: Final[dict[str, str]] = {
__annotations__["GENDER_SHORTHAND"] = 'Final[dict[str, str]]'  #22: GENDER_SHORTHAND: Final[dict[str, str]] = {


@_coconut_tco  #29: def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
def _regenerate_vocab_list(vocab_list  # type: VocabList  #29: def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
    ):  #29: def _regenerate_vocab_list(vocab_list: VocabList) -> VocabList:
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
    """  #44:     """
    word = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: accido.endings._Word  #45:     word: accido.endings._Word
    if "__annotations__" not in _coconut.locals():  #45:     word: accido.endings._Word
        __annotations__ = {}  # type: ignore  #45:     word: accido.endings._Word
    __annotations__["word"] = 'accido.endings._Word'  #45:     word: accido.endings._Word
    new_vocab = []  # type: list[accido.endings._Word]  #46:     new_vocab: list[accido.endings._Word] = []
    if "__annotations__" not in _coconut.locals():  #46:     new_vocab: list[accido.endings._Word] = []
        __annotations__ = {}  # type: ignore  #46:     new_vocab: list[accido.endings._Word] = []
    __annotations__["new_vocab"] = 'list[accido.endings._Word]'  #46:     new_vocab: list[accido.endings._Word] = []

    for word in vocab_list.vocab:  #48:     for word in vocab_list.vocab:
        if type(word) is accido.endings.RegularWord:  #49:         if type(word) is accido.endings.RegularWord:
            new_vocab.append(accido.endings.RegularWord(word=word.word, meaning=word.meaning))  #50:             new_vocab.append(
        elif type(word) is accido.endings.Verb:  #56:         elif type(word) is accido.endings.Verb:
            new_vocab.append(accido.endings.Verb(present=word.present, infinitive=word.infinitive, perfect=word.perfect, ppp=word.ppp, meaning=word.meaning))  #57:             new_vocab.append(
        elif type(word) is accido.endings.Noun:  #66:         elif type(word) is accido.endings.Noun:
            new_vocab.append(accido.endings.Noun(nominative=word.nominative, genitive=word.genitive, meaning=word.meaning, gender=word.gender))  #67:             new_vocab.append(
        elif type(word) is accido.endings.Adjective:  #75:         elif type(word) is accido.endings.Adjective:
            new_vocab.append(accido.endings.Adjective(*word._principal_parts, termination=word.termination, declension=word.declension, meaning=word.meaning))  # type: ignore[misc, arg-type]  #76:             new_vocab.append(
        elif type(word) is accido.endings.Pronoun:  #84:         elif type(word) is accido.endings.Pronoun:
            new_vocab.append(accido.endings.Pronoun(pronoun=word.pronoun, meaning=word.meaning))  #85:             new_vocab.append(
        else:  # pragma: no cover # this should never happen  #91:         else:  # pragma: no cover # this should never happen
            raise ValueError("Unknown word type: {_coconut_format_0}".format(_coconut_format_0=(type(word))))  # noqa: DOC501  #92:             raise ValueError(f"Unknown word type: {type(word)}")  # noqa: DOC501

    return _coconut_tail_call(VocabList, new_vocab)  #94:     return VocabList(new_vocab)



@_coconut_tco  #97: def read_vocab_dump(filename: Path) -> VocabList:
def read_vocab_dump(filename  # type: Path  #97: def read_vocab_dump(filename: Path) -> VocabList:
    ):  #97: def read_vocab_dump(filename: Path) -> VocabList:
# type: (...) -> VocabList
    """Reads a vocabulary dump file and returns a VocabList object.

    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with. If the data is invalid, an exception is
    raised.

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
    """  #125:     """
    with open(filename, "rb") as file:  #126:     with open(filename, "rb") as file:
        content = file.read()  # type: bytes  #127:         content: bytes = file.read()
        if "__annotations__" not in _coconut.locals():  #127:         content: bytes = file.read()
            __annotations__ = {}  # type: ignore  #127:         content: bytes = file.read()
        __annotations__["content"] = 'bytes'  #127:         content: bytes = file.read()
        pickled_data = content[:-64]  # type: bytes  #128:         pickled_data: bytes = content[:-64]
        if "__annotations__" not in _coconut.locals():  #128:         pickled_data: bytes = content[:-64]
            __annotations__ = {}  # type: ignore  #128:         pickled_data: bytes = content[:-64]
        __annotations__["pickled_data"] = 'bytes'  #128:         pickled_data: bytes = content[:-64]
        signature = content[-64:].decode()  # type: str  #129:         signature: str = content[-64:].decode()
        if "__annotations__" not in _coconut.locals():  #129:         signature: str = content[-64:].decode()
            __annotations__ = {}  # type: ignore  #129:         signature: str = content[-64:].decode()
        __annotations__["signature"] = 'str'  #129:         signature: str = content[-64:].decode()

    if (hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest() != signature):  # pragma: no cover # this should never happen  #131:     if (
        raise InvalidVocabDumpError("Data integrity check failed for vocab dump.")  #134:         raise InvalidVocabDumpError(

    output = pickle.loads(pickled_data)  #138:     output = pickle.loads(pickled_data)
    if type(output) is VocabList:  # type: ignore[comparison-overlap] # mypy cannot recognise this  #139:     if type(output) is VocabList:  # type: ignore[comparison-overlap] # mypy cannot recognise this
        if output.version == src.__version__:  #140:         if output.version == src.__version__:
            return output  #141:             return output
        warnings.warn("Vocab dump is from a different version of vocab-tester.", stacklevel=2)  #142:         warnings.warn(
        return _coconut_tail_call(_regenerate_vocab_list, output)  #146:         return _regenerate_vocab_list(output)

    raise InvalidVocabDumpError("Vocab dump is not valid.")  # pragma: no cover # this should never happen  #148:     raise InvalidVocabDumpError(



@_coconut_tco  #153: def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
def _generate_meaning(meaning  # type: str  #153: def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
    ):  #153: def _generate_meaning(meaning: str) -> accido.type_aliases.Meaning:
# type: (...) -> accido.type_aliases.Meaning
    if "/" in meaning:  #154:     if "/" in meaning:
        return _coconut_tail_call(accido.misc.MultipleMeanings, [x.strip() for x in meaning.split("/")])  #155:         return accido.misc.MultipleMeanings([
    return meaning  #158:     return meaning



@_coconut_tco  #161: def read_vocab_file(file_path: Path) -> VocabList:
def read_vocab_file(file_path  # type: Path  #161: def read_vocab_file(file_path: Path) -> VocabList:
    ):  #161: def read_vocab_file(file_path: Path) -> VocabList:
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
    """  #185:     """
    vocab = []  # type: list[accido.endings._Word]  #186:     vocab: list[accido.endings._Word] = []
    if "__annotations__" not in _coconut.locals():  #186:     vocab: list[accido.endings._Word] = []
        __annotations__ = {}  # type: ignore  #186:     vocab: list[accido.endings._Word] = []
    __annotations__["vocab"] = 'list[accido.endings._Word]'  #186:     vocab: list[accido.endings._Word] = []
    file = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: TextIOWrapper  #187:     file: TextIOWrapper
    if "__annotations__" not in _coconut.locals():  #187:     file: TextIOWrapper
        __annotations__ = {}  # type: ignore  #187:     file: TextIOWrapper
    __annotations__["file"] = 'TextIOWrapper'  #187:     file: TextIOWrapper

    with file_path.open("r") as file:  #189:     with file_path.open("r") as file:
        line = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #190:         line: str
        if "__annotations__" not in _coconut.locals():  #190:         line: str
            __annotations__ = {}  # type: ignore  #190:         line: str
        __annotations__["line"] = 'str'  #190:         line: str
        current = ""  # type: str  #191:         current: str = ""
        if "__annotations__" not in _coconut.locals():  #191:         current: str = ""
            __annotations__ = {}  # type: ignore  #191:         current: str = ""
        __annotations__["current"] = 'str'  #191:         current: str = ""

        for line in (raw_line.strip() for raw_line in file.read().split("\n") if raw_line.strip()):  # for line in file  # remove whitespace  # but skip if the line is blank  #193:         for line in (
            _coconut_case_match_to_1 = line[0]  #198:             match line[0]:
            _coconut_case_match_check_1 = False  #198:             match line[0]:
            if _coconut_case_match_to_1 == "#":  #198:             match line[0]:
                _coconut_case_match_check_1 = True  #198:             match line[0]:
            if _coconut_case_match_check_1:  #198:             match line[0]:
                continue  #200:                     continue

            if not _coconut_case_match_check_1:  #202:                 case "@":
                if _coconut_case_match_to_1 == "@":  #202:                 case "@":
                    _coconut_case_match_check_1 = True  #202:                 case "@":
                if _coconut_case_match_check_1:  #202:                 case "@":
                    _coconut_case_match_to_0 = line[1:].strip()  #202:                 case "@":
                    _coconut_case_match_check_0 = False  #202:                 case "@":
                    _coconut_case_match_check_0 = True  #202:                 case "@":
                    if _coconut_case_match_check_0:  #202:                 case "@":
                        _coconut_case_match_check_0 = False  #202:                 case "@":
                        if not _coconut_case_match_check_0:  #202:                 case "@":
                            if _coconut_case_match_to_0 == "Verb":  #202:                 case "@":
                                _coconut_case_match_check_0 = True  #202:                 case "@":

                        if not _coconut_case_match_check_0:  #202:                 case "@":
                            if _coconut_case_match_to_0 == "Adjective":  #202:                 case "@":
                                _coconut_case_match_check_0 = True  #202:                 case "@":

                        if not _coconut_case_match_check_0:  #202:                 case "@":
                            if _coconut_case_match_to_0 == "Noun":  #202:                 case "@":
                                _coconut_case_match_check_0 = True  #202:                 case "@":

                        if not _coconut_case_match_check_0:  #202:                 case "@":
                            if _coconut_case_match_to_0 == "Regular":  #202:                 case "@":
                                _coconut_case_match_check_0 = True  #202:                 case "@":

                        if not _coconut_case_match_check_0:  #202:                 case "@":
                            if _coconut_case_match_to_0 == "Pronoun":  #202:                 case "@":
                                _coconut_case_match_check_0 = True  #202:                 case "@":


                    if _coconut_case_match_check_0:  #202:                 case "@":
                        current = line[1:].strip()  #211:                             current = line[1:].strip()

                    if not _coconut_case_match_check_0:  #213:                         case (
                        _coconut_case_match_check_0 = True  #213:                         case (
                        if _coconut_case_match_check_0:  #213:                         case (
                            _coconut_case_match_check_0 = False  #213:                         case (
                            if not _coconut_case_match_check_0:  #213:                         case (
                                if _coconut_case_match_to_0 == "Verbs":  #213:                         case (
                                    _coconut_case_match_check_0 = True  #213:                         case (

                            if not _coconut_case_match_check_0:  #213:                         case (
                                if _coconut_case_match_to_0 == "Adjectives":  #213:                         case (
                                    _coconut_case_match_check_0 = True  #213:                         case (

                            if not _coconut_case_match_check_0:  #213:                         case (
                                if _coconut_case_match_to_0 == "Nouns":  #213:                         case (
                                    _coconut_case_match_check_0 = True  #213:                         case (

                            if not _coconut_case_match_check_0:  #213:                         case (
                                if _coconut_case_match_to_0 == "Regulars":  #213:                         case (
                                    _coconut_case_match_check_0 = True  #213:                         case (

                            if not _coconut_case_match_check_0:  #213:                         case (
                                if _coconut_case_match_to_0 == "Pronouns":  #213:                         case (
                                    _coconut_case_match_check_0 = True  #213:                         case (


                        if _coconut_case_match_check_0:  #213:                         case (
                            current = line[1:-1].strip()  #220:                             current = line[1:-1].strip()

                    if not _coconut_case_match_check_0:  #222:                         case _:
                        _coconut_case_match_check_0 = True  #222:                         case _:
                        if _coconut_case_match_check_0:  #222:                         case _:
                            raise InvalidVocabFileFormatError("Invalid part of speech: {_coconut_format_0}".format(_coconut_format_0=(line[1:].strip())))  #223:                             raise InvalidVocabFileFormatError(

            if not _coconut_case_match_check_1:  #227:                 case _:
                _coconut_case_match_check_1 = True  #227:                 case _:
                if _coconut_case_match_check_1:  #227:                 case _:
                    parts = line.strip().split(":")  # type: list[str]  #227:                 case _:
                    if "__annotations__" not in _coconut.locals():  #227:                 case _:
                        __annotations__ = {}  # type: ignore  #227:                 case _:
                    __annotations__["parts"] = 'list[str]'  #228:                     parts: list[str] = line.strip().split(":")
                    if len(parts) != 2:  #229:                     if len(parts) != 2:
                        raise InvalidVocabFileFormatError("Invalid line format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #230:                         raise InvalidVocabFileFormatError(

                    meaning = _generate_meaning(parts[0].strip())  # type: accido.type_aliases.Meaning  #234:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                    if "__annotations__" not in _coconut.locals():  #234:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                        __annotations__ = {}  # type: ignore  #234:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                    __annotations__["meaning"] = 'accido.type_aliases.Meaning'  #234:                     meaning: accido.type_aliases.Meaning = _generate_meaning(
                    latin_parts = [raw_part.strip() for raw_part in parts[1].split(",")]  # type: list[str]  #237:                     latin_parts: list[str] = [
                    if "__annotations__" not in _coconut.locals():  #237:                     latin_parts: list[str] = [
                        __annotations__ = {}  # type: ignore  #237:                     latin_parts: list[str] = [
                    __annotations__["latin_parts"] = 'list[str]'  #237:                     latin_parts: list[str] = [

                    if not current:  #241:                     if not current:
                        raise InvalidVocabFileFormatError("Part of speech was not given")  #242:                         raise InvalidVocabFileFormatError(

                    vocab.append(_parse_line(current, latin_parts, meaning, line))  #246:                     vocab.append(
    return _coconut_tail_call(VocabList, vocab)  #249:     return VocabList(vocab)


# type: ignore[return]
@_coconut_tco  # type: ignore[return]  #252: def _parse_line(  # type: ignore[return]
def _parse_line(current,  # type: str  # type: ignore[return]  #252: def _parse_line(  # type: ignore[return]
    latin_parts,  # type: list[str]  # type: ignore[return]  #252: def _parse_line(  # type: ignore[return]
    meaning,  # type: accido.type_aliases.Meaning  # type: ignore[return]  #252: def _parse_line(  # type: ignore[return]
    line,  # type: str  # type: ignore[return]  #252: def _parse_line(  # type: ignore[return]
    ):  # type: ignore[return]  #252: def _parse_line(  # type: ignore[return]
# type: (...) -> accido.endings._Word  # type: ignore[return]
    _coconut_case_match_to_2 = current  #258:     match current:
    _coconut_case_match_check_2 = False  #258:     match current:
    if _coconut_case_match_to_2 == "Verb":  #258:     match current:
        _coconut_case_match_check_2 = True  #258:     match current:
    if _coconut_case_match_check_2:  #258:     match current:
        if len(latin_parts) not in _coconut.set((3, 4)):  #260:             if len(latin_parts) not in {3, 4}:
            raise InvalidVocabFileFormatError("Invalid verb format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #261:                 raise InvalidVocabFileFormatError(

        if len(latin_parts) > 3:  #265:             if len(latin_parts) > 3:
            return _coconut_tail_call(accido.endings.Verb, present=latin_parts[0], infinitive=latin_parts[1], perfect=latin_parts[2], ppp=latin_parts[3], meaning=meaning)  #266:                 return accido.endings.Verb(
        return _coconut_tail_call(accido.endings.Verb, present=latin_parts[0], infinitive=latin_parts[1], perfect=latin_parts[2], meaning=meaning)  #273:             return accido.endings.Verb(

    if not _coconut_case_match_check_2:  #280:         case "Noun":
        if _coconut_case_match_to_2 == "Noun":  #280:         case "Noun":
            _coconut_case_match_check_2 = True  #280:         case "Noun":
        if _coconut_case_match_check_2:  #280:         case "Noun":
            if len(latin_parts) != 3:  #281:             if len(latin_parts) != 3:
                raise InvalidVocabFileFormatError("Invalid noun format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #282:                 raise InvalidVocabFileFormatError(

            try:  #286:             try:
                return accido.endings.Noun(meaning=meaning, nominative=latin_parts[0], genitive=latin_parts[1].split()[0], gender=GENDER_SHORTHAND[latin_parts[2].split()[-1].strip("()")])  #287:                 return accido.endings.Noun(
            except KeyError as e:  #295:             except KeyError as e:
                _coconut_raise_from_0 = InvalidVocabFileFormatError("Invalid gender: {_coconut_format_0}".format(_coconut_format_0=(latin_parts[2].split()[-1].strip('()'))))  #296:                 raise InvalidVocabFileFormatError(
                _coconut_raise_from_0.__cause__ = e  #296:                 raise InvalidVocabFileFormatError(
                raise _coconut_raise_from_0  #296:                 raise InvalidVocabFileFormatError(

    if not _coconut_case_match_check_2:  #300:         case "Adjective":
        if _coconut_case_match_to_2 == "Adjective":  #300:         case "Adjective":
            _coconut_case_match_check_2 = True  #300:         case "Adjective":
        if _coconut_case_match_check_2:  #300:         case "Adjective":
            if len(latin_parts) not in _coconut.set((3, 4)):  #301:             if len(latin_parts) not in {3, 4}:
                raise InvalidVocabFileFormatError("Invalid adjective format: {_coconut_format_0}".format(_coconut_format_0=(line)))  #302:                 raise InvalidVocabFileFormatError(

            declension = latin_parts[-1].strip("()")  # type: str  #306:             declension: str = latin_parts[-1].strip("()")
            if "__annotations__" not in _coconut.locals():  #306:             declension: str = latin_parts[-1].strip("()")
                __annotations__ = {}  # type: ignore  #306:             declension: str = latin_parts[-1].strip("()")
            __annotations__["declension"] = 'str'  #306:             declension: str = latin_parts[-1].strip("()")

            if declension not in _coconut.set(("212", "2-1-2")) and not match(r"^3-.$", declension):  #308:             if declension not in {"212", "2-1-2"} and not match(
                raise InvalidVocabFileFormatError("Invalid adjective declension: {_coconut_format_0}".format(_coconut_format_0=(declension)))  #312:                 raise InvalidVocabFileFormatError(
            if declension.startswith("3"):  #315:             if declension.startswith("3"):
                return _coconut_tail_call(accido.endings.Adjective, *latin_parts[:-1], termination=int(declension[2]), declension="3", meaning=meaning)  #316:                 return accido.endings.Adjective(
            return _coconut_tail_call(accido.endings.Adjective, *latin_parts[:-1], meaning=meaning, declension="212")  #322:             return accido.endings.Adjective(
    if not _coconut_case_match_check_2:  #327:         case "Regular":
        if _coconut_case_match_to_2 == "Regular":  #327:         case "Regular":
            _coconut_case_match_check_2 = True  #327:         case "Regular":
        if _coconut_case_match_check_2:  #327:         case "Regular":
            return _coconut_tail_call(accido.endings.RegularWord, word=latin_parts[0], meaning=meaning)  #328:             return accido.endings.RegularWord(

    if not _coconut_case_match_check_2:  #333:         case "Pronoun":
        if _coconut_case_match_to_2 == "Pronoun":  #333:         case "Pronoun":
            _coconut_case_match_check_2 = True  #333:         case "Pronoun":
        if _coconut_case_match_check_2:  #333:         case "Pronoun":
            return _coconut_tail_call(accido.endings.Pronoun, meaning=meaning, pronoun=latin_parts[0])  #334:             return accido.endings.Pronoun(

    if not _coconut_case_match_check_2:  # pragma: no cover # this should never happen  #339:         case _:  # pragma: no cover # this should never happen
        _coconut_case_match_check_2 = True  # pragma: no cover # this should never happen  #339:         case _:  # pragma: no cover # this should never happen
        if _coconut_case_match_check_2:  # pragma: no cover # this should never happen  #339:         case _:  # pragma: no cover # this should never happen
            raise ValueError  #340:             raise ValueError
