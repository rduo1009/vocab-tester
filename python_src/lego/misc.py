#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xbe6f4d61

# Compiled with Coconut version 3.1.2

"""Contains miscellaneous constants and classes used by lego."""

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



import ctypes  #3: import ctypes
from dataclasses import dataclass  #4: from dataclasses import dataclass
try:  #5: from typing import Final
    _coconut_sys_0 = sys  # type: ignore  #5: from typing import Final
except _coconut.NameError:  #5: from typing import Final
    _coconut_sys_0 = _coconut_sentinel  #5: from typing import Final
sys = _coconut_sys  #5: from typing import Final
if sys.version_info >= (3, 8):  #5: from typing import Final
    if _coconut.typing.TYPE_CHECKING:  #5: from typing import Final
        from typing import Final  #5: from typing import Final
    else:  #5: from typing import Final
        try:  #5: from typing import Final
            Final = _coconut.typing.Final  #5: from typing import Final
        except _coconut.AttributeError as _coconut_imp_err:  #5: from typing import Final
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #5: from typing import Final
else:  #5: from typing import Final
    from typing_extensions import Final  #5: from typing import Final
if _coconut_sys_0 is not _coconut_sentinel:  #5: from typing import Final
    sys = _coconut_sys_0  #5: from typing import Final

import python_src as src  #7: import python_src as src

if TYPE_CHECKING:  #9: if TYPE_CHECKING:
    from .. import accido  #10:     from .. import accido


@dataclass  #13: @dataclass
class VocabList(_coconut.object):  #14: class VocabList:
    """Represents a list of Latin vocabulary.

    Each piece of vocabulary is represented by the classes in the accido
    package.

    Attributes
    ----------
    vocab : list[accido.endings._Word]
        The vocabulary in the list.
    version : str
        The version of the package. Used to regenerate the endings if the
        version of the package is different (e.g. if the package is updated).

    Examples
    --------
    >>> foo = VocabList([
    ...     Noun(
    ...         nominative="ancilla",
    ...         genitive="ancillae",
    ...         gender="feminine",
    ...         meaning="slavegirl",
    ...     )
    ... ])  # doctest: +SKIP
    This will create a VocabList with a single Noun object in it.
    """  #39:     """

    vocab = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: list[accido.endings._Word]  #41:     vocab: list[accido.endings._Word]
    if "__annotations__" not in _coconut.locals():  #41:     vocab: list[accido.endings._Word]
        __annotations__ = {}  # type: ignore  #41:     vocab: list[accido.endings._Word]
    __annotations__["vocab"] = 'list[accido.endings._Word]'  #41:     vocab: list[accido.endings._Word]

    def __post_init__(self):  #43:     def __post_init__(self) -> None:
# type: (...) -> None
# Set the version using the package version.
        self.version = src.__version__  # type: str  #45:         self.version: str = src.__version__
        if "__annotations__" not in _coconut.locals():  #45:         self.version: str = src.__version__
            __annotations__ = {}  # type: ignore  #45:         self.version: str = src.__version__
        __annotations__["self.version"] = 'str'  #45:         self.version: str = src.__version__


    @_coconut_tco  #47:     def __repr__(self) -> str:
    def __repr__(self):  #47:     def __repr__(self) -> str:
# type: (...) -> str
        object_reprs = ", ".join((repr(word) for word in self.vocab))  # type: str  #48:         object_reprs: str = ", ".join(repr(word) for word in self.vocab)
        if "__annotations__" not in _coconut.locals():  #48:         object_reprs: str = ", ".join(repr(word) for word in self.vocab)
            __annotations__ = {}  # type: ignore  #48:         object_reprs: str = ", ".join(repr(word) for word in self.vocab)
        __annotations__["object_reprs"] = 'str'  #48:         object_reprs: str = ", ".join(repr(word) for word in self.vocab)
        return _coconut_tail_call("VocabList([{_coconut_format_0}], version={_coconut_format_1})".format, _coconut_format_0=(object_reprs), _coconut_format_1=(self.version))  #49:         return f"VocabList([{object_reprs}], version={self.version})"



_coconut_call_set_names(VocabList)  #52: LIBKEY: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
LIBKEY = ctypes.CDLL("python_src/lego/libkey.so")  # type: ctypes.CDLL  #52: LIBKEY: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
if "__annotations__" not in _coconut.locals():  #52: LIBKEY: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
    __annotations__ = {}  # type: ignore  #52: LIBKEY: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
__annotations__["LIBKEY"] = 'ctypes.CDLL'  #52: LIBKEY: ctypes.CDLL = ctypes.CDLL("python_src/lego/libkey.so")
LIBKEY.get_key.restype = ctypes.c_char_p  #53: LIBKEY.get_key.restype = ctypes.c_char_p

"""The key used to sign vocabulary pickle files."""  #55: """The key used to sign vocabulary pickle files."""
KEY = LIBKEY.get_key()  # type: Final[bytes]  #56: KEY: Final[bytes] = LIBKEY.get_key()
if "__annotations__" not in _coconut.locals():  #56: KEY: Final[bytes] = LIBKEY.get_key()
    __annotations__ = {}  # type: ignore  #56: KEY: Final[bytes] = LIBKEY.get_key()
__annotations__["KEY"] = 'Final[bytes]'  #56: KEY: Final[bytes] = LIBKEY.get_key()
