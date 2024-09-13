#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcbea2ffe

# Compiled with Coconut version 3.1.2

"""Contains functions that inflect English adverbs."""

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



import lemminflect  #3: import lemminflect
if _coconut.typing.TYPE_CHECKING:  #4: from typing import no_type_check
    from typing import no_type_check  #4: from typing import no_type_check
else:  #4: from typing import no_type_check
    try:  #4: from typing import no_type_check
        no_type_check = _coconut.typing.no_type_check  #4: from typing import no_type_check
    except _coconut.AttributeError as _coconut_imp_err:  #4: from typing import no_type_check
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #4: from typing import no_type_check

from .exceptions import InvalidWordError  #6: from .exceptions import InvalidWordError

if TYPE_CHECKING:  #8: if TYPE_CHECKING:
    from .. import accido  #9:     from .. import accido


@no_type_check  #12: @no_type_check
@_coconut_tco  #13: def find_adverb_inflections(
def find_adverb_inflections(adverb,  # type: str  #13: def find_adverb_inflections(
    components,  # type: accido.misc.EndingComponents  #13: def find_adverb_inflections(
    ):  #13: def find_adverb_inflections(
# type: (...) -> set[str]
    """Inflect English adverbs using the degree.

    Parameters
    ----------
    adverb : str
        The adverb to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the adverb.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English adverb.
    ValueError
        If the input (other than the word itself) is invalid.
    """  #37:     """
    if not hasattr(components, "degree"):  #38:     if not hasattr(components, "degree"):
        raise ValueError("Degree must be specified")  #39:         raise ValueError("Degree must be specified")

    try:  #41:     try:
        lemma = lemminflect.getLemma(adverb, "ADV")[0]  # type: str  #42:         lemma: str = lemminflect.getLemma(adverb, "ADV")[0]
        if "__annotations__" not in _coconut.locals():  #42:         lemma: str = lemminflect.getLemma(adverb, "ADV")[0]
            __annotations__ = {}  # type: ignore  #42:         lemma: str = lemminflect.getLemma(adverb, "ADV")[0]
        __annotations__["lemma"] = 'str'  #42:         lemma: str = lemminflect.getLemma(adverb, "ADV")[0]
    except KeyError as e:  #43:     except KeyError as e:
        _coconut_raise_from_0 = InvalidWordError("Word {_coconut_format_0} is not an adverb".format(_coconut_format_0=(adverb)))  #44:         raise InvalidWordError(f"Word {adverb} is not an adverb") from e
        _coconut_raise_from_0.__cause__ = e  #44:         raise InvalidWordError(f"Word {adverb} is not an adverb") from e
        raise _coconut_raise_from_0  #44:         raise InvalidWordError(f"Word {adverb} is not an adverb") from e

    _coconut_case_match_to_0 = components.degree  #46:     match components.degree:
    _coconut_case_match_check_0 = False  #46:     match components.degree:
    if _coconut_case_match_to_0 == "positive":  #46:     match components.degree:
        _coconut_case_match_check_0 = True  #46:     match components.degree:
    if _coconut_case_match_check_0:  #46:     match components.degree:
        return _coconut_tail_call(_coconut.set, (lemma,))  #48:             return {lemma}

    if not _coconut_case_match_check_0:  #50:         case "comparative":
        if _coconut_case_match_to_0 == "comparative":  #50:         case "comparative":
            _coconut_case_match_check_0 = True  #50:         case "comparative":
        if _coconut_case_match_check_0:  #50:         case "comparative":
            return _coconut_tail_call(_coconut.set, ("more {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #51:             return {f"more {lemma}"}

    if not _coconut_case_match_check_0:  #53:         case "superlative":
        if _coconut_case_match_to_0 == "superlative":  #53:         case "superlative":
            _coconut_case_match_check_0 = True  #53:         case "superlative":
        if _coconut_case_match_check_0:  #53:         case "superlative":
            return _coconut_tail_call(_coconut.set, ("most {_coconut_format_0}".format(_coconut_format_0=(lemma)), "very {_coconut_format_0}".format(_coconut_format_0=(lemma)), "extremely {_coconut_format_0}".format(_coconut_format_0=(lemma)), "rather {_coconut_format_0}".format(_coconut_format_0=(lemma)), "too {_coconut_format_0}".format(_coconut_format_0=(lemma)), "quite {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #54:             return {

    if not _coconut_case_match_check_0:  #63:         case _:
        _coconut_case_match_check_0 = True  #63:         case _:
        if _coconut_case_match_check_0:  #63:         case _:
            raise ValueError("Invalid degree: '{_coconut_format_0}'".format(_coconut_format_0=(components.degree)))  #64:             raise ValueError(f"Invalid degree: '{components.degree}'")
