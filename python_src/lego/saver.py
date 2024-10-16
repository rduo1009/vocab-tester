#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x5dfb1291

# Compiled with Coconut version 3.1.2

"""Contains a function for saving vocabulary files."""

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

import dill as pickle  #7: import dill as pickle
import lz4.frame  #8: import lz4.frame

from .exceptions import MisleadingFilenameWarning  #10: from .exceptions import MisleadingFilenameWarning
from .misc import KEY  #11: from .misc import KEY, VocabList
from .misc import VocabList  #11: from .misc import KEY, VocabList

if TYPE_CHECKING:  #13: if TYPE_CHECKING:
    from pathlib import Path  #14:     from pathlib import Path


def save_vocab_dump(file_path,  # type: Path  #17: def save_vocab_dump(
    vocab_list,  # type: VocabList  #17: def save_vocab_dump(
    compress=False  # type: bool  #17: def save_vocab_dump(
    ):  #17: def save_vocab_dump(
# type: (...) -> None
    """Saves a vocabulary dump file.

    The pickle files are signed with a HMAC signature to ensure the data
    has not been tampered with.
    The files can also be compressed using LZ4 compression. If this is the
    case, the files will be saved with the .lz4 extension, unless the user
    has put the .lz4 extension in the file path already.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the vocabulary dump file.
    vocab_list : VocabList
        The vocabulary to save.
    compress : bool, default = False
        Whether to compress the pickle file.

    Raises
    ------
    FileNotFoundError
        If the directory of the file does not exist.

    Warnings
    --------
    UserWarning
        If the file already exists and has been overwritten.
    MisleadingFilenameWarning
        If the file path does not end in .lz4 and the file is being
        compressed, or if the file path ends in .lz4 and the file is not
        being compressed.

    Examples
    --------
    >>> save_vocab_dump(
    ...     Path("path_to_file.pickle"), VocabList()
    ... )  # doctest: +SKIP
    """  #56:     """
    if not file_path.parent.exists():  #57:     if not file_path.parent.exists():
        raise FileNotFoundError("The directory '{_coconut_format_0}' does not exist".format(_coconut_format_0=(file_path.parent)))  #58:         raise FileNotFoundError(

    if file_path.exists():  #62:     if file_path.exists():
        warnings.warn("The file '{_coconut_format_0}' already exists and has been overwritten".format(_coconut_format_0=(file_path)), stacklevel=2)  #63:         warnings.warn(

    pickled_data = pickle.dumps(vocab_list)  # type: bytes  #68:     pickled_data: bytes = pickle.dumps(vocab_list)
    if "__annotations__" not in _coconut.locals():  #68:     pickled_data: bytes = pickle.dumps(vocab_list)
        __annotations__ = {}  # type: ignore  #68:     pickled_data: bytes = pickle.dumps(vocab_list)
    __annotations__["pickled_data"] = 'bytes'  #68:     pickled_data: bytes = pickle.dumps(vocab_list)
    signature = hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest()  # type: str  #69:     signature: str = hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest()
    if "__annotations__" not in _coconut.locals():  #69:     signature: str = hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest()
        __annotations__ = {}  # type: ignore  #69:     signature: str = hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest()
    __annotations__["signature"] = 'str'  #69:     signature: str = hmac.new(KEY, pickled_data, hashlib.sha256).hexdigest()

    if compress:  #71:     if compress:
# Add lz4 extension if it is not already there
        if file_path.suffix != ".lz4":  #73:         if file_path.suffix != ".lz4":
            warnings.warn("The file '{_coconut_format_0}' is being compressed, but the '.lz4' extension is not present and is being added.".format(_coconut_format_0=(file_path)), category=MisleadingFilenameWarning, stacklevel=2)  #74:             warnings.warn(
            file_path = file_path.with_suffix(file_path.suffix + ".lz4")  # type: Path  #79:             file_path: Path = file_path.with_suffix(file_path.suffix + ".lz4")
            if "__annotations__" not in _coconut.locals():  #79:             file_path: Path = file_path.with_suffix(file_path.suffix + ".lz4")
                __annotations__ = {}  # type: ignore  #79:             file_path: Path = file_path.with_suffix(file_path.suffix + ".lz4")
            __annotations__["file_path"] = 'Path'  #79:             file_path: Path = file_path.with_suffix(file_path.suffix + ".lz4")

        with lz4.frame.open(file_path, "wb") as file:  #81:         with lz4.frame.open(file_path, "wb") as file:
            file.write(pickled_data)  #82:             file.write(pickled_data)
            file.write(signature.encode())  #83:             file.write(signature.encode())
        return  #84:         return

    if file_path.suffix == ".lz4":  #86:     if file_path.suffix == ".lz4":
        warnings.warn("The file '{_coconut_format_0}' is not being compressed, but the file extension ('.lz4') suggests it is.".format(_coconut_format_0=(file_path)), category=MisleadingFilenameWarning, stacklevel=2)  #87:         warnings.warn(

    with open(file_path, "wb") as file:  #93:     with open(file_path, "wb") as file:
        file.write(pickled_data)  #94:         file.write(pickled_data)
        file.write(signature.encode())  #95:         file.write(signature.encode())
