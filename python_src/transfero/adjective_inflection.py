#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xeaaacfd4

# Compiled with Coconut version 3.1.2

"""Contains functions that inflect English adjectives."""

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

from .exceptions import InvalidWordError  #5: from .exceptions import InvalidWordError
if _coconut.typing.TYPE_CHECKING:  #6: from typing import no_type_check
    from typing import no_type_check  #6: from typing import no_type_check
else:  #6: from typing import no_type_check
    try:  #6: from typing import no_type_check
        no_type_check = _coconut.typing.no_type_check  #6: from typing import no_type_check
    except _coconut.AttributeError as _coconut_imp_err:  #6: from typing import no_type_check
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #6: from typing import no_type_check

if TYPE_CHECKING:  #8: if TYPE_CHECKING:
    from .. import accido  #9:     from .. import accido


@no_type_check  #12: @no_type_check
@_coconut_tco  #13: def find_adjective_inflections(
def find_adjective_inflections(adjective,  # type: str  #13: def find_adjective_inflections(
    components,  # type: accido.misc.EndingComponents  #13: def find_adjective_inflections(
    ):  #13: def find_adjective_inflections(
# type: (...) -> set[str]
    """Inflect English adjectives using the degree.

    Parameters
    ----------
    adjective : str
        The adjective to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the adjective.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English adjective.
    ValueError
        If the input (other than the word itself) is invalid.
    """  #37:     """
# Most of these are not necessary, but it helps to catch errors earlier
    if not hasattr(components, "gender"):  #39:     if not hasattr(components, "gender"):
        raise ValueError("Gender must be specified")  #40:         raise ValueError("Gender must be specified")

    if not hasattr(components, "case"):  #42:     if not hasattr(components, "case"):
        raise ValueError("Case must be specified")  #43:         raise ValueError("Case must be specified")

    if not hasattr(components, "number"):  #45:     if not hasattr(components, "number"):
        raise ValueError("Number must be specified")  #46:         raise ValueError("Number must be specified")

    if not hasattr(components, "degree"):  #48:     if not hasattr(components, "degree"):
        raise ValueError("Degree must be specified")  #49:         raise ValueError("Degree must be specified")

    if components.gender not in _coconut.set(("masculine", "feminine", "neuter")):  #51:     if components.gender not in {"masculine", "feminine", "neuter"}:
        raise ValueError("Invalid gender: '{_coconut_format_0}'".format(_coconut_format_0=(components.gender)))  #52:         raise ValueError(f"Invalid gender: '{components.gender}'")

    if components.case not in _coconut.set(("nominative", "vocative", "accusative", "genitive", "dative", "ablative",)):  #54:     if components.case not in {
        raise ValueError("Invalid case: '{_coconut_format_0}'".format(_coconut_format_0=(components.case)))  #62:         raise ValueError(f"Invalid case: '{components.case}'")

    if components.number not in _coconut.set(("singular", "plural")):  #64:     if components.number not in {"singular", "plural"}:
        raise ValueError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(components.number)))  #65:         raise ValueError(f"Invalid number: '{components.number}'")

    try:  #67:     try:
        lemma = lemminflect.getLemma(adjective, "ADJ")[0]  # type: str  #68:         lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]
        if "__annotations__" not in _coconut.locals():  #68:         lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]
            __annotations__ = {}  # type: ignore  #68:         lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]
        __annotations__["lemma"] = 'str'  #68:         lemma: str = lemminflect.getLemma(adjective, "ADJ")[0]
    except KeyError as e:  #69:     except KeyError as e:
        _coconut_raise_from_0 = InvalidWordError("Word '{_coconut_format_0}' is not an adjective".format(_coconut_format_0=(adjective)))  #70:         raise InvalidWordError(
        _coconut_raise_from_0.__cause__ = e  #70:         raise InvalidWordError(
        raise _coconut_raise_from_0  #70:         raise InvalidWordError(

    _coconut_case_match_to_0 = components.degree  #74:     match components.degree:
    _coconut_case_match_check_0 = False  #74:     match components.degree:
    if _coconut_case_match_to_0 == "positive":  #74:     match components.degree:
        _coconut_case_match_check_0 = True  #74:     match components.degree:
    if _coconut_case_match_check_0:  #74:     match components.degree:
        return _coconut_tail_call(_coconut.set, (lemma,))  #76:             return {lemma}

    if not _coconut_case_match_check_0:  #78:         case "comparative":
        if _coconut_case_match_to_0 == "comparative":  #78:         case "comparative":
            _coconut_case_match_check_0 = True  #78:         case "comparative":
        if _coconut_case_match_check_0:  #78:         case "comparative":
            comparative = lemminflect.getInflection(lemma, "RBR")[0]  # type: str  #78:         case "comparative":
            if "__annotations__" not in _coconut.locals():  #78:         case "comparative":
                __annotations__ = {}  # type: ignore  #78:         case "comparative":
            __annotations__["comparative"] = 'str'  #79:             comparative: str = lemminflect.getInflection(lemma, "RBR")[0]

            return _coconut_tail_call(_coconut.set, (comparative, "more {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #81:             return {comparative, f"more {lemma}"}

    if not _coconut_case_match_check_0:  #83:         case "superlative":
        if _coconut_case_match_to_0 == "superlative":  #83:         case "superlative":
            _coconut_case_match_check_0 = True  #83:         case "superlative":
        if _coconut_case_match_check_0:  #83:         case "superlative":
            superlative = lemminflect.getInflection(lemma, "RBS")[0]  # type: str  #83:         case "superlative":
            if "__annotations__" not in _coconut.locals():  #83:         case "superlative":
                __annotations__ = {}  # type: ignore  #83:         case "superlative":
            __annotations__["superlative"] = 'str'  #84:             superlative: str = lemminflect.getInflection(lemma, "RBS")[0]

            return _coconut_tail_call(_coconut.set, (superlative, "most {_coconut_format_0}".format(_coconut_format_0=(lemma)), "very {_coconut_format_0}".format(_coconut_format_0=(lemma)), "extremely {_coconut_format_0}".format(_coconut_format_0=(lemma)), "rather {_coconut_format_0}".format(_coconut_format_0=(lemma)), "too {_coconut_format_0}".format(_coconut_format_0=(lemma)), "quite {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #86:             return {

    if not _coconut_case_match_check_0:  #96:         case _:
        _coconut_case_match_check_0 = True  #96:         case _:
        if _coconut_case_match_check_0:  #96:         case _:
            raise ValueError("Invalid degree: '{_coconut_format_0}'".format(_coconut_format_0=(components.degree)))  #97:             raise ValueError(f"Invalid degree: '{components.degree}'")
