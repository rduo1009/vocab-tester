#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x3524bfde

# Compiled with Coconut version 3.1.2

"""Contains functions that inflect English verbs."""

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



try:  #3: from typing import Literal, no_type_check
    _coconut_sys_0 = sys  # type: ignore  #3: from typing import Literal, no_type_check
except _coconut.NameError:  #3: from typing import Literal, no_type_check
    _coconut_sys_0 = _coconut_sentinel  #3: from typing import Literal, no_type_check
sys = _coconut_sys  #3: from typing import Literal, no_type_check
if sys.version_info >= (3, 8):  #3: from typing import Literal, no_type_check
    if _coconut.typing.TYPE_CHECKING:  #3: from typing import Literal, no_type_check
        from typing import Literal  #3: from typing import Literal, no_type_check
    else:  #3: from typing import Literal, no_type_check
        try:  #3: from typing import Literal, no_type_check
            Literal = _coconut.typing.Literal  #3: from typing import Literal, no_type_check
        except _coconut.AttributeError as _coconut_imp_err:  #3: from typing import Literal, no_type_check
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3: from typing import Literal, no_type_check
else:  #3: from typing import Literal, no_type_check
    from typing_extensions import Literal  #3: from typing import Literal, no_type_check
if _coconut_sys_0 is not _coconut_sentinel:  #3: from typing import Literal, no_type_check
    sys = _coconut_sys_0  #3: from typing import Literal, no_type_check
if _coconut.typing.TYPE_CHECKING:  #3: from typing import Literal, no_type_check
    from typing import no_type_check  #3: from typing import Literal, no_type_check
else:  #3: from typing import Literal, no_type_check
    try:  #3: from typing import Literal, no_type_check
        no_type_check = _coconut.typing.no_type_check  #3: from typing import Literal, no_type_check
    except _coconut.AttributeError as _coconut_imp_err:  #3: from typing import Literal, no_type_check
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3: from typing import Literal, no_type_check


import lemminflect  #6: import lemminflect

from .edge_cases import STATIVE_VERBS  #8: from .edge_cases import STATIVE_VERBS
from .exceptions import InvalidWordError  #9: from .exceptions import InvalidWordError

if TYPE_CHECKING:  #11: if TYPE_CHECKING:
    from .. import accido  #12:     from .. import accido


def _verify_verb_inflections(components  # type: accido.misc.EndingComponents  #15: def _verify_verb_inflections(components: accido.misc.EndingComponents) -> None:
    ):  #15: def _verify_verb_inflections(components: accido.misc.EndingComponents) -> None:
# type: (...) -> None
    if not hasattr(components, "tense"):  #16:     if not hasattr(components, "tense"):
        raise ValueError("Tense must be specified")  #17:         raise ValueError("Tense must be specified")

    if not hasattr(components, "voice"):  #19:     if not hasattr(components, "voice"):
        raise ValueError("Voice must be specified")  #20:         raise ValueError("Voice must be specified")

    if not hasattr(components, "mood"):  #22:     if not hasattr(components, "mood"):
        raise ValueError("Mood must be specified")  #23:         raise ValueError("Mood must be specified")

# not an infinitive
    if components.mood != "infinitive":  #26:     if components.mood != "infinitive":
        if not hasattr(components, "number"):  #27:         if not hasattr(components, "number"):
            raise ValueError("Number must be specified")  #28:             raise ValueError("Number must be specified")

        if components.number not in _coconut.set(("singular", "plural")):  #30:         if components.number not in {"singular", "plural"}:
            raise ValueError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(components.number)))  #31:             raise ValueError(f"Invalid number: '{components.number}'")

# not a participle or an infinitive
        if components.mood != "participle":  #34:         if components.mood != "participle":
            if not hasattr(components, "person"):  #35:             if not hasattr(components, "person"):
                raise ValueError("Person must be specified")  #36:                 raise ValueError("Person must be specified")

            if components.person not in _coconut.set((1, 2, 3)):  #38:             if components.person not in {1, 2, 3}:
                raise ValueError("Invalid person: '{_coconut_format_0}'".format(_coconut_format_0=(components.person)))  #39:                 raise ValueError(f"Invalid person: '{components.person}'")

        else:  #41:         else:
            if not hasattr(components, "case"):  #42:             if not hasattr(components, "case"):
                raise ValueError("Case must be specified")  #43:                 raise ValueError("Case must be specified")

            if not hasattr(components, "gender"):  #45:             if not hasattr(components, "gender"):
                raise ValueError("Gender must be specified")  #46:                 raise ValueError("Gender must be specified")

    if components.voice not in _coconut.set(("active", "passive")):  #48:     if components.voice not in {"active", "passive"}:
        raise ValueError("Invalid voice: '{_coconut_format_0}'".format(_coconut_format_0=(components.voice)))  #49:         raise ValueError(f"Invalid voice: '{components.voice}'")

    if components.mood not in _coconut.set(("indicative", "imperative", "subjunctive", "infinitive", "participle",)):  #51:     if components.mood not in {
        raise ValueError("Invalid mood: '{_coconut_format_0}'".format(_coconut_format_0=(components.mood)))  #58:         raise ValueError(f"Invalid mood: '{components.mood}'")

    if components.tense not in _coconut.set(("pluperfect", "perfect", "imperfect", "present", "future", "future perfect",)):  #60:     if components.tense not in {
        raise ValueError("Invalid tense: '{_coconut_format_0}'".format(_coconut_format_0=(components.tense)))  #68:         raise ValueError(f"Invalid tense: '{components.tense}'")



@no_type_check  #71: @no_type_check
@_coconut_tco  #72: def find_verb_inflections(
def find_verb_inflections(verb,  # type: str  #72: def find_verb_inflections(
    components,  # type: accido.misc.EndingComponents  #72: def find_verb_inflections(
    ):  #72: def find_verb_inflections(
# type: (...) -> set[str]
    """Inflect English verbs using the tense, voice, mood, number and
    person. If a participle is queried, find_participle_inflections is ran
    instead.

    Note that subjunctives are not supported as they do not have an exact
    translation in English.

    Parameters
    ----------
    verb : str
        The verb to inflect.
    components : EndingComponents
        The components of the ending.

    Returns
    -------
    set[str]
        The possible forms of the verb.

    Raises
    ------
    InvalidWordError
        If the word is not a valid English verb.
    ValueError
        If the input (other than the word itself) is invalid.
    """  # noqa: D205  #101:     """  # noqa: D205
    _verify_verb_inflections(components)  #102:     _verify_verb_inflections(components)

    if components.mood == "participle":  #104:     if components.mood == "participle":
        return _coconut_tail_call(_find_participle_inflections, verb, components)  #105:         return _find_participle_inflections(verb, components)

    try:  #107:     try:
        lemma = lemminflect.getLemma(verb, "VERB")[0]  # type: str  #108:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
        if "__annotations__" not in _coconut.locals():  #108:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
            __annotations__ = {}  # type: ignore  #108:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
        __annotations__["lemma"] = 'str'  #108:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
    except KeyError as e:  #109:     except KeyError as e:
        _coconut_raise_from_0 = InvalidWordError("Word {_coconut_format_0} is not a verb".format(_coconut_format_0=(verb)))  #110:         raise InvalidWordError(f"Word {verb} is not a verb") from e
        _coconut_raise_from_0.__cause__ = e  #110:         raise InvalidWordError(f"Word {verb} is not a verb") from e
        raise _coconut_raise_from_0  #110:         raise InvalidWordError(f"Word {verb} is not a verb") from e

    _coconut_case_match_to_0 = (components.tense, components.voice, components.mood)  #112:     match (components.tense, components.voice, components.mood):
    _coconut_case_match_check_0 = False  #112:     match (components.tense, components.voice, components.mood):
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "present") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #112:     match (components.tense, components.voice, components.mood):
        _coconut_case_match_check_0 = True  #112:     match (components.tense, components.voice, components.mood):
    if _coconut_case_match_check_0:  #112:     match (components.tense, components.voice, components.mood):
        return _coconut_tail_call(_find_preactind_inflections, lemma, components.number, components.person)  #114:             return _find_preactind_inflections(

    if not _coconut_case_match_check_0:  #120:         case ("imperfect", "active", "indicative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "imperfect") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #120:         case ("imperfect", "active", "indicative"):
            _coconut_case_match_check_0 = True  #120:         case ("imperfect", "active", "indicative"):
        if _coconut_case_match_check_0:  #120:         case ("imperfect", "active", "indicative"):
            return _coconut_tail_call(_find_impactind_inflections, lemma, components.number, components.person)  #121:             return _find_impactind_inflections(

    if not _coconut_case_match_check_0:  #127:         case ("perfect", "active", "indicative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "perfect") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #127:         case ("perfect", "active", "indicative"):
            _coconut_case_match_check_0 = True  #127:         case ("perfect", "active", "indicative"):
        if _coconut_case_match_check_0:  #127:         case ("perfect", "active", "indicative"):
            return _coconut_tail_call(_find_peractind_inflections, lemma, components.number, components.person)  #128:             return _find_peractind_inflections(

    if not _coconut_case_match_check_0:  #134:         case ("pluperfect", "active", "indicative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "pluperfect") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #134:         case ("pluperfect", "active", "indicative"):
            _coconut_case_match_check_0 = True  #134:         case ("pluperfect", "active", "indicative"):
        if _coconut_case_match_check_0:  #134:         case ("pluperfect", "active", "indicative"):
            return _coconut_tail_call(_find_plpactind_inflections, lemma, components.number, components.person)  #135:             return _find_plpactind_inflections(

    if not _coconut_case_match_check_0:  #141:         case ("present", "active", "infinitive"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "present") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "infinitive"):  #141:         case ("present", "active", "infinitive"):
            _coconut_case_match_check_0 = True  #141:         case ("present", "active", "infinitive"):
        if _coconut_case_match_check_0:  #141:         case ("present", "active", "infinitive"):
            return _coconut_tail_call(_find_preactinf_inflections, lemma)  #142:             return _find_preactinf_inflections(lemma)

    if not _coconut_case_match_check_0:  #144:         case ("present", "active", "imperative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "present") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "imperative"):  #144:         case ("present", "active", "imperative"):
            _coconut_case_match_check_0 = True  #144:         case ("present", "active", "imperative"):
        if _coconut_case_match_check_0:  #144:         case ("present", "active", "imperative"):
            return _coconut_tail_call(_find_preipe_inflections, lemma)  #145:             return _find_preipe_inflections(lemma)

    if not _coconut_case_match_check_0:  #147:         case _:
        _coconut_case_match_check_0 = True  #147:         case _:
        if _coconut_case_match_check_0:  #147:         case _:
            raise NotImplementedError("The {_coconut_format_0} {_coconut_format_1} {_coconut_format_2} has not been implemented".format(_coconut_format_0=(components.tense), _coconut_format_1=(components.voice), _coconut_format_2=(components.mood)))  #148:             raise NotImplementedError(



@_coconut_tco  #153: def _find_preactind_inflections(
def _find_preactind_inflections(lemma,  # type: str  #153: def _find_preactind_inflections(
    number,  # type: Literal["singular", "plural"]  #153: def _find_preactind_inflections(
    person,  # type: Literal[1, 2, 3]  #153: def _find_preactind_inflections(
    ):  #153: def _find_preactind_inflections(
# type: (...) -> set[str]
    present_nonthird = lemminflect.getInflection(lemma, "VBP")[0]  # type: str  #158:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    if "__annotations__" not in _coconut.locals():  #158:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
        __annotations__ = {}  # type: ignore  #158:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    __annotations__["present_nonthird"] = 'str'  #158:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    present_third = lemminflect.getInflection(lemma, "VBZ")[0]  # type: str  #159:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    if "__annotations__" not in _coconut.locals():  #159:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
        __annotations__ = {}  # type: ignore  #159:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    __annotations__["present_third"] = 'str'  #159:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    present_participle = lemminflect.getInflection(lemma, "VBG")[0]  # type: str  #160:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    if "__annotations__" not in _coconut.locals():  #160:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
        __annotations__ = {}  # type: ignore  #160:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    __annotations__["present_participle"] = 'str'  #160:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    _coconut_case_match_to_1 = (number, person)  #162:     match (number, person):
    _coconut_case_match_check_1 = False  #162:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "singular") and (_coconut_case_match_to_1[1] == 1):  #162:     match (number, person):
        _coconut_case_match_check_1 = True  #162:     match (number, person):
    if _coconut_case_match_check_1:  #162:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "I am {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #164:             return {

    if not _coconut_case_match_check_1:  #169:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "plural") and (_coconut_case_match_to_1[1] == 1):  #169:         case ("plural", 1):
            _coconut_case_match_check_1 = True  #169:         case ("plural", 1):
        if _coconut_case_match_check_1:  #169:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "we are {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #170:             return {

    if not _coconut_case_match_check_1:  #175:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_1 = True  #175:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_1:  #175:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_1 = False  #175:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_1:  #175:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "singular") and (_coconut_case_match_to_1[1] == 2):  #175:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_1 = True  #175:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_1:  #175:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "plural") and (_coconut_case_match_to_1[1] == 2):  #175:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_1 = True  #175:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_1:  #175:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "you are {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #176:             return {

    if not _coconut_case_match_check_1:  #181:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "singular") and (_coconut_case_match_to_1[1] == 3):  #181:         case ("singular", 3):
            _coconut_case_match_check_1 = True  #181:         case ("singular", 3):
        if _coconut_case_match_check_1:  #181:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he {_coconut_format_0}".format(_coconut_format_0=(present_third)), "he is {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "she {_coconut_format_0}".format(_coconut_format_0=(present_third)), "she is {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "it {_coconut_format_0}".format(_coconut_format_0=(present_third)), "it is {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #182:             return {

    if not _coconut_case_match_check_1:  #191:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "plural") and (_coconut_case_match_to_1[1] == 3):  #191:         case ("plural", 3):
            _coconut_case_match_check_1 = True  #191:         case ("plural", 3):
        if _coconut_case_match_check_1:  #191:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "they are {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #192:             return {

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #197:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@_coconut_tco  #200: def _find_impactind_inflections(
def _find_impactind_inflections(lemma,  # type: str  #200: def _find_impactind_inflections(
    number,  # type: Literal["singular", "plural"]  #200: def _find_impactind_inflections(
    person,  # type: Literal[1, 2, 3]  #200: def _find_impactind_inflections(
    ):  #200: def _find_impactind_inflections(
# type: (...) -> set[str]
    present_participle = lemminflect.getInflection(lemma, "VBG")[0]  # type: str  #205:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    if "__annotations__" not in _coconut.locals():  #205:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
        __annotations__ = {}  # type: ignore  #205:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    __annotations__["present_participle"] = 'str'  #205:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    if lemma in STATIVE_VERBS:  #207:     if lemma in STATIVE_VERBS:
        past = lemminflect.getInflection(lemma, "VBD")[0]  # type: str  #208:         past: str = lemminflect.getInflection(lemma, "VBD")[0]
        if "__annotations__" not in _coconut.locals():  #208:         past: str = lemminflect.getInflection(lemma, "VBD")[0]
            __annotations__ = {}  # type: ignore  #208:         past: str = lemminflect.getInflection(lemma, "VBD")[0]
        __annotations__["past"] = 'str'  #208:         past: str = lemminflect.getInflection(lemma, "VBD")[0]

        _coconut_case_match_to_2 = (number, person)  #210:         match (number, person):
        _coconut_case_match_check_2 = False  #210:         match (number, person):
        if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "singular") and (_coconut_case_match_to_2[1] == 1):  #210:         match (number, person):
            _coconut_case_match_check_2 = True  #210:         match (number, person):
        if _coconut_case_match_check_2:  #210:         match (number, person):
            return _coconut_tail_call(_coconut.set, ("I {_coconut_format_0}".format(_coconut_format_0=(past)), "I was {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #212:                 return {f"I {past}", f"I was {present_participle}"}

        if not _coconut_case_match_check_2:  #214:             case ("plural", 1):
            if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "plural") and (_coconut_case_match_to_2[1] == 1):  #214:             case ("plural", 1):
                _coconut_case_match_check_2 = True  #214:             case ("plural", 1):
            if _coconut_case_match_check_2:  #214:             case ("plural", 1):
                return _coconut_tail_call(_coconut.set, ("we {_coconut_format_0}".format(_coconut_format_0=(past)), "we were {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #215:                 return {f"we {past}", f"we were {present_participle}"}

        if not _coconut_case_match_check_2:  #217:             case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_2 = True  #217:             case ("singular", 2) | ("plural", 2):
            if _coconut_case_match_check_2:  #217:             case ("singular", 2) | ("plural", 2):
                _coconut_case_match_check_2 = False  #217:             case ("singular", 2) | ("plural", 2):
                if not _coconut_case_match_check_2:  #217:             case ("singular", 2) | ("plural", 2):
                    if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "singular") and (_coconut_case_match_to_2[1] == 2):  #217:             case ("singular", 2) | ("plural", 2):
                        _coconut_case_match_check_2 = True  #217:             case ("singular", 2) | ("plural", 2):

                if not _coconut_case_match_check_2:  #217:             case ("singular", 2) | ("plural", 2):
                    if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "plural") and (_coconut_case_match_to_2[1] == 2):  #217:             case ("singular", 2) | ("plural", 2):
                        _coconut_case_match_check_2 = True  #217:             case ("singular", 2) | ("plural", 2):


            if _coconut_case_match_check_2:  #217:             case ("singular", 2) | ("plural", 2):
                return _coconut_tail_call(_coconut.set, ("you {_coconut_format_0}".format(_coconut_format_0=(past)), "you were {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #218:                 return {f"you {past}", f"you were {present_participle}"}

        if not _coconut_case_match_check_2:  #220:             case ("singular", 3):
            if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "singular") and (_coconut_case_match_to_2[1] == 3):  #220:             case ("singular", 3):
                _coconut_case_match_check_2 = True  #220:             case ("singular", 3):
            if _coconut_case_match_check_2:  #220:             case ("singular", 3):
                return _coconut_tail_call(_coconut.set, ("he {_coconut_format_0}".format(_coconut_format_0=(past)), "he was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "she {_coconut_format_0}".format(_coconut_format_0=(past)), "she was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "it {_coconut_format_0}".format(_coconut_format_0=(past)), "it was {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #221:                 return {

        if not _coconut_case_match_check_2:  #230:             case ("plural", 3):
            if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "plural") and (_coconut_case_match_to_2[1] == 3):  #230:             case ("plural", 3):
                _coconut_case_match_check_2 = True  #230:             case ("plural", 3):
            if _coconut_case_match_check_2:  #230:             case ("plural", 3):
                return _coconut_tail_call(_coconut.set, ("they {_coconut_format_0}".format(_coconut_format_0=(past)), "they were {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #231:                 return {f"they {past}", f"they were {present_participle}"}

# case _:
#     raise ValueError(
#         f"Invalid number and person: '{number}' '{person}'"
#     )

    _coconut_case_match_to_3 = (number, person)  #238:     match (number, person):
    _coconut_case_match_check_3 = False  #238:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "singular") and (_coconut_case_match_to_3[1] == 1):  #238:     match (number, person):
        _coconut_case_match_check_3 = True  #238:     match (number, person):
    if _coconut_case_match_check_3:  #238:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I was {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #240:             return {f"I was {present_participle}"}

    if not _coconut_case_match_check_3:  #242:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "plural") and (_coconut_case_match_to_3[1] == 1):  #242:         case ("plural", 1):
            _coconut_case_match_check_3 = True  #242:         case ("plural", 1):
        if _coconut_case_match_check_3:  #242:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we were {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #243:             return {f"we were {present_participle}"}

    if not _coconut_case_match_check_3:  #245:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_3 = True  #245:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_3:  #245:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_3 = False  #245:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_3:  #245:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "singular") and (_coconut_case_match_to_3[1] == 2):  #245:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_3 = True  #245:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_3:  #245:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "plural") and (_coconut_case_match_to_3[1] == 2):  #245:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_3 = True  #245:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_3:  #245:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you were {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #246:             return {f"you were {present_participle}"}

    if not _coconut_case_match_check_3:  #248:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "singular") and (_coconut_case_match_to_3[1] == 3):  #248:         case ("singular", 3):
            _coconut_case_match_check_3 = True  #248:         case ("singular", 3):
        if _coconut_case_match_check_3:  #248:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "she was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "it was {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #249:             return {

    if not _coconut_case_match_check_3:  #255:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "plural") and (_coconut_case_match_to_3[1] == 3):  #255:         case ("plural", 3):
            _coconut_case_match_check_3 = True  #255:         case ("plural", 3):
        if _coconut_case_match_check_3:  #255:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they were {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #256:             return {f"they were {present_participle}"}

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #258:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@_coconut_tco  #261: def _find_peractind_inflections(
def _find_peractind_inflections(lemma,  # type: str  #261: def _find_peractind_inflections(
    number,  # type: Literal["singular", "plural"]  #261: def _find_peractind_inflections(
    person,  # type: Literal[1, 2, 3]  #261: def _find_peractind_inflections(
    ):  #261: def _find_peractind_inflections(
# type: (...) -> set[str]
    past = lemminflect.getInflection(lemma, "VBD")[0]  #266:     past = lemminflect.getInflection(lemma, "VBD")[0]

    _coconut_case_match_to_4 = (number, person)  #268:     match (number, person):
    _coconut_case_match_check_4 = False  #268:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "singular") and (_coconut_case_match_to_4[1] == 1):  #268:     match (number, person):
        _coconut_case_match_check_4 = True  #268:     match (number, person):
    if _coconut_case_match_check_4:  #268:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I {_coconut_format_0}".format(_coconut_format_0=(past)), "I have {_coconut_format_0}".format(_coconut_format_0=(past)), "I did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #270:             return {f"I {past}", f"I have {past}", f"I did {lemma}"}

    if not _coconut_case_match_check_4:  #272:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "plural") and (_coconut_case_match_to_4[1] == 1):  #272:         case ("plural", 1):
            _coconut_case_match_check_4 = True  #272:         case ("plural", 1):
        if _coconut_case_match_check_4:  #272:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we {_coconut_format_0}".format(_coconut_format_0=(past)), "we have {_coconut_format_0}".format(_coconut_format_0=(past)), "we did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #273:             return {f"we {past}", f"we have {past}", f"we did {lemma}"}

    if not _coconut_case_match_check_4:  #275:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_4 = True  #275:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_4:  #275:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_4 = False  #275:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_4:  #275:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "singular") and (_coconut_case_match_to_4[1] == 2):  #275:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_4 = True  #275:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_4:  #275:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "plural") and (_coconut_case_match_to_4[1] == 2):  #275:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_4 = True  #275:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_4:  #275:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you {_coconut_format_0}".format(_coconut_format_0=(past)), "you have {_coconut_format_0}".format(_coconut_format_0=(past)), "you did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #276:             return {f"you {past}", f"you have {past}", f"you did {lemma}"}

    if not _coconut_case_match_check_4:  #278:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "singular") and (_coconut_case_match_to_4[1] == 3):  #278:         case ("singular", 3):
            _coconut_case_match_check_4 = True  #278:         case ("singular", 3):
        if _coconut_case_match_check_4:  #278:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he {_coconut_format_0}".format(_coconut_format_0=(past)), "he has {_coconut_format_0}".format(_coconut_format_0=(past)), "he did {_coconut_format_0}".format(_coconut_format_0=(lemma)), "she {_coconut_format_0}".format(_coconut_format_0=(past)), "she has {_coconut_format_0}".format(_coconut_format_0=(past)), "she did {_coconut_format_0}".format(_coconut_format_0=(lemma)), "it {_coconut_format_0}".format(_coconut_format_0=(past)), "it has {_coconut_format_0}".format(_coconut_format_0=(past)), "it did {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #279:             return {

    if not _coconut_case_match_check_4:  #291:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "plural") and (_coconut_case_match_to_4[1] == 3):  #291:         case ("plural", 3):
            _coconut_case_match_check_4 = True  #291:         case ("plural", 3):
        if _coconut_case_match_check_4:  #291:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they {_coconut_format_0}".format(_coconut_format_0=(past)), "they have {_coconut_format_0}".format(_coconut_format_0=(past)), "they did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #292:             return {f"they {past}", f"they have {past}", f"they did {lemma}"}

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #294:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@_coconut_tco  #297: def _find_plpactind_inflections(
def _find_plpactind_inflections(lemma,  # type: str  #297: def _find_plpactind_inflections(
    number,  # type: Literal["singular", "plural"]  #297: def _find_plpactind_inflections(
    person,  # type: Literal[1, 2, 3]  #297: def _find_plpactind_inflections(
    ):  #297: def _find_plpactind_inflections(
# type: (...) -> set[str]
    past_participle = lemminflect.getInflection(lemma, "VBN")[0]  # type: str  #302:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
    if "__annotations__" not in _coconut.locals():  #302:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
        __annotations__ = {}  # type: ignore  #302:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
    __annotations__["past_participle"] = 'str'  #302:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]

    _coconut_case_match_to_5 = (number, person)  #304:     match (number, person):
    _coconut_case_match_check_5 = False  #304:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "singular") and (_coconut_case_match_to_5[1] == 1):  #304:     match (number, person):
        _coconut_case_match_check_5 = True  #304:     match (number, person):
    if _coconut_case_match_check_5:  #304:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #306:             return {f"I had {past_participle}"}

    if not _coconut_case_match_check_5:  #308:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "plural") and (_coconut_case_match_to_5[1] == 1):  #308:         case ("plural", 1):
            _coconut_case_match_check_5 = True  #308:         case ("plural", 1):
        if _coconut_case_match_check_5:  #308:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #309:             return {f"we had {past_participle}"}

    if not _coconut_case_match_check_5:  #311:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_5 = True  #311:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_5:  #311:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_5 = False  #311:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_5:  #311:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "singular") and (_coconut_case_match_to_5[1] == 2):  #311:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_5 = True  #311:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_5:  #311:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "plural") and (_coconut_case_match_to_5[1] == 2):  #311:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_5 = True  #311:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_5:  #311:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #312:             return {f"you had {past_participle}"}

    if not _coconut_case_match_check_5:  #314:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "singular") and (_coconut_case_match_to_5[1] == 3):  #314:         case ("singular", 3):
            _coconut_case_match_check_5 = True  #314:         case ("singular", 3):
        if _coconut_case_match_check_5:  #314:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he had {_coconut_format_0}".format(_coconut_format_0=(past_participle)), "she had {_coconut_format_0}".format(_coconut_format_0=(past_participle)), "it had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #315:             return {

    if not _coconut_case_match_check_5:  #321:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "plural") and (_coconut_case_match_to_5[1] == 3):  #321:         case ("plural", 3):
            _coconut_case_match_check_5 = True  #321:         case ("plural", 3):
        if _coconut_case_match_check_5:  #321:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #322:             return {f"they had {past_participle}"}

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #324:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@no_type_check  #327: @no_type_check
@_coconut_tco  #328: def _find_participle_inflections(
def _find_participle_inflections(verb,  # type: str  #328: def _find_participle_inflections(
    components,  # type: accido.misc.EndingComponents  #328: def _find_participle_inflections(
    ):  #328: def _find_participle_inflections(
# type: (...) -> set[str]
    lemma = lemminflect.getLemma(verb, "NOUN")[0]  # type: str  #332:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]
    if "__annotations__" not in _coconut.locals():  #332:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]
        __annotations__ = {}  # type: ignore  #332:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]
    __annotations__["lemma"] = 'str'  #332:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]

    _coconut_case_match_to_6 = (components.tense, components.voice)  #334:     match (components.tense, components.voice):
    _coconut_case_match_check_6 = False  #334:     match (components.tense, components.voice):
    if (_coconut.isinstance(_coconut_case_match_to_6, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_6) == 2) and (_coconut_case_match_to_6[0] == "perfect") and (_coconut_case_match_to_6[1] == "passive"):  #334:     match (components.tense, components.voice):
        _coconut_case_match_check_6 = True  #334:     match (components.tense, components.voice):
    if _coconut_case_match_check_6:  #334:     match (components.tense, components.voice):
        past_participle = lemminflect.getInflection(lemma, "VBN")[0]  # type: str  #334:     match (components.tense, components.voice):
        if "__annotations__" not in _coconut.locals():  #334:     match (components.tense, components.voice):
            __annotations__ = {}  # type: ignore  #334:     match (components.tense, components.voice):
        __annotations__["past_participle"] = 'str'  #336:             past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
        return _coconut_tail_call(_coconut.set, ("having been {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #337:             return {f"having been {past_participle}"}

    if not _coconut_case_match_check_6:  #339:         case ("present", "active"):
        if (_coconut.isinstance(_coconut_case_match_to_6, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_6) == 2) and (_coconut_case_match_to_6[0] == "present") and (_coconut_case_match_to_6[1] == "active"):  #339:         case ("present", "active"):
            _coconut_case_match_check_6 = True  #339:         case ("present", "active"):
        if _coconut_case_match_check_6:  #339:         case ("present", "active"):
            present_participle = lemminflect.getInflection(lemma, "VBG")[0]  # type: str  #339:         case ("present", "active"):
            if "__annotations__" not in _coconut.locals():  #339:         case ("present", "active"):
                __annotations__ = {}  # type: ignore  #339:         case ("present", "active"):
            __annotations__["present_participle"] = 'str'  #340:             present_participle: str = lemminflect.getInflection(lemma, "VBG")[
            return _coconut_tail_call(_coconut.set, (present_participle,))  #343:             return {present_participle}

    if not _coconut_case_match_check_6:  #345:         case _:
        _coconut_case_match_check_6 = True  #345:         case _:
        if _coconut_case_match_check_6:  #345:         case _:
            raise NotImplementedError("The {_coconut_format_0} {_coconut_format_1} participle has not been implemented".format(_coconut_format_0=(components.tense), _coconut_format_1=(components.voice)))  #346:             raise NotImplementedError(



@_coconut_tco  #351: def _find_preactinf_inflections(lemma: str) -> set[str]:
def _find_preactinf_inflections(lemma  # type: str  #351: def _find_preactinf_inflections(lemma: str) -> set[str]:
    ):  #351: def _find_preactinf_inflections(lemma: str) -> set[str]:
# type: (...) -> set[str]
    return _coconut_tail_call(_coconut.set, ("to {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #352:     return {f"to {lemma}"}



@_coconut_tco  #355: def _find_preipe_inflections(lemma: str) -> set[str]:
def _find_preipe_inflections(lemma  # type: str  #355: def _find_preipe_inflections(lemma: str) -> set[str]:
    ):  #355: def _find_preipe_inflections(lemma: str) -> set[str]:
# type: (...) -> set[str]
    return _coconut_tail_call(_coconut.set, ("{_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #356:     return {f"{lemma}"}
