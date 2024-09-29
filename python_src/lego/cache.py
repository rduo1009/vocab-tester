#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc3c980c

# Compiled with Coconut version 3.1.2

"""Contains a function for caching vocabulary files in a cache folder."""

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



import warnings  #3: import warnings
from pathlib import Path  #4: from pathlib import Path

from .reader import read_vocab_dump  #6: from .reader import read_vocab_dump, read_vocab_file
from .reader import read_vocab_file  #6: from .reader import read_vocab_dump, read_vocab_file
from .saver import save_vocab_dump  #7: from .saver import save_vocab_dump

if TYPE_CHECKING:  #9: if TYPE_CHECKING:
    from .misc import VocabList  #10:     from .misc import VocabList
import hashlib  #11: import hashlib


@_coconut_tco  #14: def _sha256sum(filename: Path) -> str:
def _sha256sum(filename  # type: Path  #14: def _sha256sum(filename: Path) -> str:
    ):  #14: def _sha256sum(filename: Path) -> str:
# type: (...) -> str
    """Hashes a file.

    Parameters
    ----------
    filename : Path
        The file to hash.

    Returns
    -------
    str
        The hash as a string.

    Notes
    -----
    Code taken from https://stackoverflow.com/a/44873382
    """  #30:     """
    h = hashlib.sha256()  #31:     h = hashlib.sha256()
    b = bytearray(128 * 1024)  #32:     b = bytearray(128 * 1024)
    mv = memoryview(b)  #33:     mv = memoryview(b)
    with open(filename, "rb", buffering=0) as f:  #34:     with open(filename, "rb", buffering=0) as f:
        for n in iter(lambda _=None: f.readinto(mv), 0):  # type: ignore[misc]  #35:         for n in iter(=> f.readinto(mv), 0): # type: ignore[misc]
            h.update(mv[:n])  #36:             h.update(mv[:n])
    return _coconut_tail_call(h.hexdigest)  #37:     return h.hexdigest()



def cache_vocab_file(cache_folder,  # type: Path  #40: def cache_vocab_file(
    vocab_file_path  # type: Path  #40: def cache_vocab_file(
    ):  #40: def cache_vocab_file(
# type: (...) -> tuple[VocabList, bool]
    """Reads a vocab file, and saves the vocab dump inside a cache folder.

    The name of the vocabulary dump file is decided by hashing the
    vocab file given. Note that if the cache folder does not exist,
    it is created.

    Parameters
    ----------
    cache_folder : Path
        The path to the cache folder.
    vocab_list : VocabList
        The vocabulary to save.

    Returns
    -------
    (VocabList, bool)
        The vocab list, and whether it was generated from cache or not.

    Warnings
    --------
    UserWarning
        If the cache folder did not exist and had to be created.
    """  #65:     """
    if not cache_folder.exists():  #66:     if not cache_folder.exists():
        cache_folder.mkdir(parents=True, exist_ok=True)  #67:         cache_folder.mkdir(parents=True, exist_ok=True)
        warnings.warn("The directory {_coconut_format_0} did not exist and has been created".format(_coconut_format_0=(cache_folder)), stacklevel=2)  #68:         warnings.warn(

    cache_file_name = _sha256sum(vocab_file_path)  # type: str  #73:     cache_file_name: str = _sha256sum(vocab_file_path)
    if "__annotations__" not in _coconut.locals():  #73:     cache_file_name: str = _sha256sum(vocab_file_path)
        __annotations__ = {}  # type: ignore  #73:     cache_file_name: str = _sha256sum(vocab_file_path)
    __annotations__["cache_file_name"] = 'str'  #73:     cache_file_name: str = _sha256sum(vocab_file_path)
    cache_path = Path(cache_folder / cache_file_name)  # type: Path  #74:     cache_path: Path = Path(cache_folder / cache_file_name)
    if "__annotations__" not in _coconut.locals():  #74:     cache_path: Path = Path(cache_folder / cache_file_name)
        __annotations__ = {}  # type: ignore  #74:     cache_path: Path = Path(cache_folder / cache_file_name)
    __annotations__["cache_path"] = 'Path'  #74:     cache_path: Path = Path(cache_folder / cache_file_name)

    if cache_path.exists():  #76:     if cache_path.exists():
        return (read_vocab_dump(cache_path), True)  #77:         return (read_vocab_dump(cache_path), True)

    vocab_list = read_vocab_file(vocab_file_path)  # type: VocabList  #79:     vocab_list: VocabList = read_vocab_file(vocab_file_path)
    if "__annotations__" not in _coconut.locals():  #79:     vocab_list: VocabList = read_vocab_file(vocab_file_path)
        __annotations__ = {}  # type: ignore  #79:     vocab_list: VocabList = read_vocab_file(vocab_file_path)
    __annotations__["vocab_list"] = 'VocabList'  #79:     vocab_list: VocabList = read_vocab_file(vocab_file_path)
    save_vocab_dump(cache_path, vocab_list)  #80:     save_vocab_dump(cache_path, vocab_list)
    return (vocab_list, False)  #81:     return (vocab_list, False)
