#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa043cad6

# Compiled with Coconut version 3.1.2

"""Contains functions that inflect English nouns."""

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
from inflect import engine  #4: from inflect import engine
if _coconut.typing.TYPE_CHECKING:  #5: from typing import no_type_check
    from typing import no_type_check  #5: from typing import no_type_check
else:  #5: from typing import no_type_check
    try:  #5: from typing import no_type_check
        no_type_check = _coconut.typing.no_type_check  #5: from typing import no_type_check
    except _coconut.AttributeError as _coconut_imp_err:  #5: from typing import no_type_check
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #5: from typing import no_type_check
from .exceptions import InvalidWordError  #6: from .exceptions import InvalidWordError

if TYPE_CHECKING:  #8: if TYPE_CHECKING:
    from .. import accido  #9:     from .. import accido

# Distinguish from the lemminflect module
pluralinflect = engine()  # sourcery skip: avoid-global-variables  #12: pluralinflect = engine()  # sourcery skip: avoid-global-variables
del engine  #13: del engine


def _get_possessive(noun  # type: str  #16: def _get_possessive(noun: str) -> str:
    ):  #16: def _get_possessive(noun: str) -> str:
# type: (...) -> str
    return "{_coconut_format_0}'".format(_coconut_format_0=(noun)) if noun.endswith("s") else "{_coconut_format_0}'s".format(_coconut_format_0=(noun))  #17:     return f"{noun}'" if noun.endswith("s") else f"{noun}'s"



@no_type_check  #20: @no_type_check
def find_noun_inflections(noun,  # type: str  #21: def find_noun_inflections(
    components,  # type: accido.misc.EndingComponents  #21: def find_noun_inflections(
    ):  #21: def find_noun_inflections(
# type: (...) -> set[str]
    """Inflect English nouns using the case and number.

    Parameters
    ----------
    noun : str
        The noun to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the noun.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English noun.
    ValueError
        If the input (other than the word itself) is invalid.
    """  #45:     """
    if not hasattr(components, "case"):  #46:     if not hasattr(components, "case"):
        raise ValueError("Case must be specified")  #47:         raise ValueError("Case must be specified")

    if not hasattr(components, "number"):  #49:     if not hasattr(components, "number"):
        raise ValueError("Number must be specified")  #50:         raise ValueError("Number must be specified")

    try:  #52:     try:
        lemma = lemminflect.getLemma(noun, "NOUN")[0]  # type: str  #53:         lemma: str = lemminflect.getLemma(noun, "NOUN")[0]
        if "__annotations__" not in _coconut.locals():  #53:         lemma: str = lemminflect.getLemma(noun, "NOUN")[0]
            __annotations__ = {}  # type: ignore  #53:         lemma: str = lemminflect.getLemma(noun, "NOUN")[0]
        __annotations__["lemma"] = 'str'  #53:         lemma: str = lemminflect.getLemma(noun, "NOUN")[0]
    except KeyError as e:  #54:     except KeyError as e:
        _coconut_raise_from_0 = InvalidWordError("Word {_coconut_format_0} is not a noun".format(_coconut_format_0=(noun)))  #55:         raise InvalidWordError(f"Word {noun} is not a noun") from e
        _coconut_raise_from_0.__cause__ = e  #55:         raise InvalidWordError(f"Word {noun} is not a noun") from e
        raise _coconut_raise_from_0  #55:         raise InvalidWordError(f"Word {noun} is not a noun") from e

    base_forms = set()  # type: set[str]  #57:     base_forms: set[str] = set()
    if "__annotations__" not in _coconut.locals():  #57:     base_forms: set[str] = set()
        __annotations__ = {}  # type: ignore  #57:     base_forms: set[str] = set()
    __annotations__["base_forms"] = 'set[str]'  #57:     base_forms: set[str] = set()

    _coconut_case_match_to_0 = components.number  #59:     match components.number:
    _coconut_case_match_check_0 = False  #59:     match components.number:
    if _coconut_case_match_to_0 == "singular":  #59:     match components.number:
        _coconut_case_match_check_0 = True  #59:     match components.number:
    if _coconut_case_match_check_0:  #59:     match components.number:
        base_forms = _coconut.set((lemminflect.getInflection(lemma, "NN")[0],))  #61:             base_forms = {lemminflect.getInflection(lemma, "NN")[0]}

    if not _coconut_case_match_check_0:  #63:         case "plural":
        if _coconut_case_match_to_0 == "plural":  #63:         case "plural":
            _coconut_case_match_check_0 = True  #63:         case "plural":
        if _coconut_case_match_check_0:  #63:         case "plural":
            base_forms.add(pluralinflect.plural_noun(lemma))  #64:             base_forms.add(pluralinflect.plural_noun(lemma))
            pluralinflect.classical(all=True)  #65:             pluralinflect.classical(all=True)
            base_forms.add(pluralinflect.plural_noun(lemma))  #66:             base_forms.add(pluralinflect.plural_noun(lemma))
            pluralinflect.classical(all=False)  #67:             pluralinflect.classical(all=False)

    if not _coconut_case_match_check_0:  #69:         case _:
        _coconut_case_match_check_0 = True  #69:         case _:
        if _coconut_case_match_check_0:  #69:         case _:
            raise ValueError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(components.number)))  #70:             raise ValueError(f"Invalid number: '{components.number}'")

    _coconut_case_match_to_1 = components.case  #72:     match components.case:
    _coconut_case_match_check_1 = False  #72:     match components.case:
    _coconut_case_match_check_1 = True  #72:     match components.case:
    if _coconut_case_match_check_1:  #72:     match components.case:
        _coconut_case_match_check_1 = False  #72:     match components.case:
        if not _coconut_case_match_check_1:  #72:     match components.case:
            if _coconut_case_match_to_1 == "nominative":  #72:     match components.case:
                _coconut_case_match_check_1 = True  #72:     match components.case:

        if not _coconut_case_match_check_1:  #72:     match components.case:
            if _coconut_case_match_to_1 == "vocative":  #72:     match components.case:
                _coconut_case_match_check_1 = True  #72:     match components.case:

        if not _coconut_case_match_check_1:  #72:     match components.case:
            if _coconut_case_match_to_1 == "accusative":  #72:     match components.case:
                _coconut_case_match_check_1 = True  #72:     match components.case:


    if _coconut_case_match_check_1:  #72:     match components.case:
        return base_forms  #74:             return base_forms

    if not _coconut_case_match_check_1:  #76:         case "genitive":
        if _coconut_case_match_to_1 == "genitive":  #76:         case "genitive":
            _coconut_case_match_check_1 = True  #76:         case "genitive":
        if _coconut_case_match_check_1:  #76:         case "genitive":
            possessive_genitive = _coconut.set((_get_possessive(base_form) for base_form in base_forms))  # type: set[str]  #76:         case "genitive":
            if "__annotations__" not in _coconut.locals():  #76:         case "genitive":
                __annotations__ = {}  # type: ignore  #76:         case "genitive":
            __annotations__["possessive_genitive"] = 'set[str]'  #77:             possessive_genitive: set[str] = {

            if components.number == "singular":  #81:             if components.number == "singular":
                return (possessive_genitive | _coconut.set(("of the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set((pluralinflect.inflect("of a('{_coconut_format_0}')".format(_coconut_format_0=(base_form))) for base_form in base_forms)))  #82:                 return (

            return possessive_genitive | _coconut.set(("of the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms))  #91:             return possessive_genitive | {

    if not _coconut_case_match_check_1:  #95:         case "dative":
        if _coconut_case_match_to_1 == "dative":  #95:         case "dative":
            _coconut_case_match_check_1 = True  #95:         case "dative":
        if _coconut_case_match_check_1:  #95:         case "dative":
            if components.number == "singular":  #96:             if components.number == "singular":
                return (_coconut.set(("for the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set((pluralinflect.inflect("for a('{_coconut_format_0}')".format(_coconut_format_0=(base_form))) for base_form in base_forms)) | _coconut.set(("to the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set((pluralinflect.inflect("to a('{_coconut_format_0}')".format(_coconut_format_0=(base_form))) for base_form in base_forms)))  #97:                 return (

            return (_coconut.set(("for the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set(("for {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set(("to the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set(("to {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)))  #110:             return (

    if not _coconut_case_match_check_1:  #117:         case "ablative":
        if _coconut_case_match_to_1 == "ablative":  #117:         case "ablative":
            _coconut_case_match_check_1 = True  #117:         case "ablative":
        if _coconut_case_match_check_1:  #117:         case "ablative":
            if components.number == "singular":  #118:             if components.number == "singular":
                return (base_forms | _coconut.set(("with the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set((pluralinflect.inflect("with a('{_coconut_format_0}')".format(_coconut_format_0=(base_form))) for base_form in base_forms)) | _coconut.set(("by the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set((pluralinflect.inflect("by a('{_coconut_format_0}')".format(_coconut_format_0=(base_form))) for base_form in base_forms)) | _coconut.set(("by means of the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set((pluralinflect.inflect("by means of a('{_coconut_format_0}')".format(_coconut_format_0=(base_form))) for base_form in base_forms)))  #119:                 return (

            return (base_forms | _coconut.set(("with the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set(("by the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)) | _coconut.set(("by means of the {_coconut_format_0}".format(_coconut_format_0=(base_form)) for base_form in base_forms)))  #141:             return (

    if not _coconut_case_match_check_1:  #148:         case _:
        _coconut_case_match_check_1 = True  #148:         case _:
        if _coconut_case_match_check_1:  #148:         case _:
            raise ValueError("Invalid case: '{_coconut_format_0}'".format(_coconut_format_0=(components.case)))  #149:             raise ValueError(f"Invalid case: '{components.case}'")
