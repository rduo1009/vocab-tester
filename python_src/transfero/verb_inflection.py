#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb2b48ae6

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



try:  #3: from typing import Literal
    _coconut_sys_0 = sys  # type: ignore  #3: from typing import Literal
except _coconut.NameError:  #3: from typing import Literal
    _coconut_sys_0 = _coconut_sentinel  #3: from typing import Literal
sys = _coconut_sys  #3: from typing import Literal
if sys.version_info >= (3, 8):  #3: from typing import Literal
    if _coconut.typing.TYPE_CHECKING:  #3: from typing import Literal
        from typing import Literal  #3: from typing import Literal
    else:  #3: from typing import Literal
        try:  #3: from typing import Literal
            Literal = _coconut.typing.Literal  #3: from typing import Literal
        except _coconut.AttributeError as _coconut_imp_err:  #3: from typing import Literal
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3: from typing import Literal
else:  #3: from typing import Literal
    from typing_extensions import Literal  #3: from typing import Literal
if _coconut_sys_0 is not _coconut_sentinel:  #3: from typing import Literal
    sys = _coconut_sys_0  #3: from typing import Literal


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


# type: ignore[return]
@_coconut_tco  # type: ignore[return]  #71: def find_verb_inflections(  # type: ignore[return]
def find_verb_inflections(verb,  # type: str  # type: ignore[return]  #71: def find_verb_inflections(  # type: ignore[return]
    components,  # type: accido.misc.EndingComponents  # type: ignore[return]  #71: def find_verb_inflections(  # type: ignore[return]
    ):  # type: ignore[return]  #71: def find_verb_inflections(  # type: ignore[return]
# type: (...) -> set[str]  # type: ignore[return]
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
    """  # noqa: D205  #100:     """  # noqa: D205
    _verify_verb_inflections(components)  #101:     _verify_verb_inflections(components)

    if components.mood == "participle":  #103:     if components.mood == "participle":
        return _coconut_tail_call(_find_participle_inflections, verb, components)  #104:         return _find_participle_inflections(verb, components)

    try:  #106:     try:
        lemma = lemminflect.getLemma(verb, "VERB")[0]  # type: str  #107:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
        if "__annotations__" not in _coconut.locals():  #107:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
            __annotations__ = {}  # type: ignore  #107:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
        __annotations__["lemma"] = 'str'  #107:         lemma: str = lemminflect.getLemma(verb, "VERB")[0]
    except KeyError as e:  #108:     except KeyError as e:
        _coconut_raise_from_0 = InvalidWordError("Word {_coconut_format_0} is not a verb".format(_coconut_format_0=(verb)))  #109:         raise InvalidWordError(f"Word {verb} is not a verb") from e
        _coconut_raise_from_0.__cause__ = e  #109:         raise InvalidWordError(f"Word {verb} is not a verb") from e
        raise _coconut_raise_from_0  #109:         raise InvalidWordError(f"Word {verb} is not a verb") from e

    _coconut_case_match_to_0 = (components.tense, components.voice, components.mood)  #111:     match (components.tense, components.voice, components.mood):
    _coconut_case_match_check_0 = False  #111:     match (components.tense, components.voice, components.mood):
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "present") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #111:     match (components.tense, components.voice, components.mood):
        _coconut_case_match_check_0 = True  #111:     match (components.tense, components.voice, components.mood):
    if _coconut_case_match_check_0:  #111:     match (components.tense, components.voice, components.mood):
        return _coconut_tail_call(_find_preactind_inflections, lemma, components.number, components.person)  #113:             return _find_preactind_inflections(

    if not _coconut_case_match_check_0:  #119:         case ("imperfect", "active", "indicative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "imperfect") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #119:         case ("imperfect", "active", "indicative"):
            _coconut_case_match_check_0 = True  #119:         case ("imperfect", "active", "indicative"):
        if _coconut_case_match_check_0:  #119:         case ("imperfect", "active", "indicative"):
            return _coconut_tail_call(_find_impactind_inflections, lemma, components.number, components.person)  #120:             return _find_impactind_inflections(

    if not _coconut_case_match_check_0:  #126:         case ("perfect", "active", "indicative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "perfect") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #126:         case ("perfect", "active", "indicative"):
            _coconut_case_match_check_0 = True  #126:         case ("perfect", "active", "indicative"):
        if _coconut_case_match_check_0:  #126:         case ("perfect", "active", "indicative"):
            return _coconut_tail_call(_find_peractind_inflections, lemma, components.number, components.person)  #127:             return _find_peractind_inflections(

    if not _coconut_case_match_check_0:  #133:         case ("pluperfect", "active", "indicative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "pluperfect") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "indicative"):  #133:         case ("pluperfect", "active", "indicative"):
            _coconut_case_match_check_0 = True  #133:         case ("pluperfect", "active", "indicative"):
        if _coconut_case_match_check_0:  #133:         case ("pluperfect", "active", "indicative"):
            return _coconut_tail_call(_find_plpactind_inflections, lemma, components.number, components.person)  #134:             return _find_plpactind_inflections(

    if not _coconut_case_match_check_0:  #140:         case ("present", "active", "infinitive"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "present") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "infinitive"):  #140:         case ("present", "active", "infinitive"):
            _coconut_case_match_check_0 = True  #140:         case ("present", "active", "infinitive"):
        if _coconut_case_match_check_0:  #140:         case ("present", "active", "infinitive"):
            return _coconut_tail_call(_find_preactinf_inflections, lemma)  #141:             return _find_preactinf_inflections(lemma)

    if not _coconut_case_match_check_0:  #143:         case ("present", "active", "imperative"):
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 3) and (_coconut_case_match_to_0[0] == "present") and (_coconut_case_match_to_0[1] == "active") and (_coconut_case_match_to_0[2] == "imperative"):  #143:         case ("present", "active", "imperative"):
            _coconut_case_match_check_0 = True  #143:         case ("present", "active", "imperative"):
        if _coconut_case_match_check_0:  #143:         case ("present", "active", "imperative"):
            return _coconut_tail_call(_find_preipe_inflections, lemma)  #144:             return _find_preipe_inflections(lemma)

    if not _coconut_case_match_check_0:  #146:         case _:
        _coconut_case_match_check_0 = True  #146:         case _:
        if _coconut_case_match_check_0:  #146:         case _:
            raise NotImplementedError("The {_coconut_format_0} {_coconut_format_1} {_coconut_format_2} has not been implemented".format(_coconut_format_0=(components.tense), _coconut_format_1=(components.voice), _coconut_format_2=(components.mood)))  #147:             raise NotImplementedError(



@_coconut_tco  #152: def _find_preactind_inflections(
def _find_preactind_inflections(lemma,  # type: str  #152: def _find_preactind_inflections(
    number,  # type: Literal["singular", "plural"]  #152: def _find_preactind_inflections(
    person,  # type: Literal[1, 2, 3]  #152: def _find_preactind_inflections(
    ):  #152: def _find_preactind_inflections(
# type: (...) -> set[str]
    present_nonthird = lemminflect.getInflection(lemma, "VBP")[0]  # type: str  #157:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    if "__annotations__" not in _coconut.locals():  #157:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
        __annotations__ = {}  # type: ignore  #157:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    __annotations__["present_nonthird"] = 'str'  #157:     present_nonthird: str = lemminflect.getInflection(lemma, "VBP")[0]
    present_third = lemminflect.getInflection(lemma, "VBZ")[0]  # type: str  #158:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    if "__annotations__" not in _coconut.locals():  #158:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
        __annotations__ = {}  # type: ignore  #158:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    __annotations__["present_third"] = 'str'  #158:     present_third: str = lemminflect.getInflection(lemma, "VBZ")[0]
    present_participle = lemminflect.getInflection(lemma, "VBG")[0]  # type: str  #159:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    if "__annotations__" not in _coconut.locals():  #159:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
        __annotations__ = {}  # type: ignore  #159:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    __annotations__["present_participle"] = 'str'  #159:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    _coconut_case_match_to_1 = (number, person)  #161:     match (number, person):
    _coconut_case_match_check_1 = False  #161:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "singular") and (_coconut_case_match_to_1[1] == 1):  #161:     match (number, person):
        _coconut_case_match_check_1 = True  #161:     match (number, person):
    if _coconut_case_match_check_1:  #161:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "I am {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #163:             return {

    if not _coconut_case_match_check_1:  #168:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "plural") and (_coconut_case_match_to_1[1] == 1):  #168:         case ("plural", 1):
            _coconut_case_match_check_1 = True  #168:         case ("plural", 1):
        if _coconut_case_match_check_1:  #168:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "we are {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #169:             return {

    if not _coconut_case_match_check_1:  #174:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_1 = True  #174:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_1:  #174:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_1 = False  #174:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_1:  #174:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "singular") and (_coconut_case_match_to_1[1] == 2):  #174:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_1 = True  #174:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_1:  #174:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "plural") and (_coconut_case_match_to_1[1] == 2):  #174:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_1 = True  #174:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_1:  #174:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "you are {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #175:             return {

    if not _coconut_case_match_check_1:  #180:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "singular") and (_coconut_case_match_to_1[1] == 3):  #180:         case ("singular", 3):
            _coconut_case_match_check_1 = True  #180:         case ("singular", 3):
        if _coconut_case_match_check_1:  #180:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he {_coconut_format_0}".format(_coconut_format_0=(present_third)), "he is {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "she {_coconut_format_0}".format(_coconut_format_0=(present_third)), "she is {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "it {_coconut_format_0}".format(_coconut_format_0=(present_third)), "it is {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #181:             return {

    if not _coconut_case_match_check_1:  #190:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_1) == 2) and (_coconut_case_match_to_1[0] == "plural") and (_coconut_case_match_to_1[1] == 3):  #190:         case ("plural", 3):
            _coconut_case_match_check_1 = True  #190:         case ("plural", 3):
        if _coconut_case_match_check_1:  #190:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they {_coconut_format_0}".format(_coconut_format_0=(present_nonthird)), "they are {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #191:             return {

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #196:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@_coconut_tco  #199: def _find_impactind_inflections(
def _find_impactind_inflections(lemma,  # type: str  #199: def _find_impactind_inflections(
    number,  # type: Literal["singular", "plural"]  #199: def _find_impactind_inflections(
    person,  # type: Literal[1, 2, 3]  #199: def _find_impactind_inflections(
    ):  #199: def _find_impactind_inflections(
# type: (...) -> set[str]
    present_participle = lemminflect.getInflection(lemma, "VBG")[0]  # type: str  #204:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    if "__annotations__" not in _coconut.locals():  #204:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
        __annotations__ = {}  # type: ignore  #204:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]
    __annotations__["present_participle"] = 'str'  #204:     present_participle: str = lemminflect.getInflection(lemma, "VBG")[0]

    if lemma in STATIVE_VERBS:  #206:     if lemma in STATIVE_VERBS:
        past = lemminflect.getInflection(lemma, "VBD")[0]  # type: str  #207:         past: str = lemminflect.getInflection(lemma, "VBD")[0]
        if "__annotations__" not in _coconut.locals():  #207:         past: str = lemminflect.getInflection(lemma, "VBD")[0]
            __annotations__ = {}  # type: ignore  #207:         past: str = lemminflect.getInflection(lemma, "VBD")[0]
        __annotations__["past"] = 'str'  #207:         past: str = lemminflect.getInflection(lemma, "VBD")[0]

        _coconut_case_match_to_2 = (number, person)  #209:         match (number, person):
        _coconut_case_match_check_2 = False  #209:         match (number, person):
        if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "singular") and (_coconut_case_match_to_2[1] == 1):  #209:         match (number, person):
            _coconut_case_match_check_2 = True  #209:         match (number, person):
        if _coconut_case_match_check_2:  #209:         match (number, person):
            return _coconut_tail_call(_coconut.set, ("I {_coconut_format_0}".format(_coconut_format_0=(past)), "I was {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #211:                 return {f"I {past}", f"I was {present_participle}"}

        if not _coconut_case_match_check_2:  #213:             case ("plural", 1):
            if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "plural") and (_coconut_case_match_to_2[1] == 1):  #213:             case ("plural", 1):
                _coconut_case_match_check_2 = True  #213:             case ("plural", 1):
            if _coconut_case_match_check_2:  #213:             case ("plural", 1):
                return _coconut_tail_call(_coconut.set, ("we {_coconut_format_0}".format(_coconut_format_0=(past)), "we were {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #214:                 return {f"we {past}", f"we were {present_participle}"}

        if not _coconut_case_match_check_2:  #216:             case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_2 = True  #216:             case ("singular", 2) | ("plural", 2):
            if _coconut_case_match_check_2:  #216:             case ("singular", 2) | ("plural", 2):
                _coconut_case_match_check_2 = False  #216:             case ("singular", 2) | ("plural", 2):
                if not _coconut_case_match_check_2:  #216:             case ("singular", 2) | ("plural", 2):
                    if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "singular") and (_coconut_case_match_to_2[1] == 2):  #216:             case ("singular", 2) | ("plural", 2):
                        _coconut_case_match_check_2 = True  #216:             case ("singular", 2) | ("plural", 2):

                if not _coconut_case_match_check_2:  #216:             case ("singular", 2) | ("plural", 2):
                    if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "plural") and (_coconut_case_match_to_2[1] == 2):  #216:             case ("singular", 2) | ("plural", 2):
                        _coconut_case_match_check_2 = True  #216:             case ("singular", 2) | ("plural", 2):


            if _coconut_case_match_check_2:  #216:             case ("singular", 2) | ("plural", 2):
                return _coconut_tail_call(_coconut.set, ("you {_coconut_format_0}".format(_coconut_format_0=(past)), "you were {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #217:                 return {f"you {past}", f"you were {present_participle}"}

        if not _coconut_case_match_check_2:  #219:             case ("singular", 3):
            if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "singular") and (_coconut_case_match_to_2[1] == 3):  #219:             case ("singular", 3):
                _coconut_case_match_check_2 = True  #219:             case ("singular", 3):
            if _coconut_case_match_check_2:  #219:             case ("singular", 3):
                return _coconut_tail_call(_coconut.set, ("he {_coconut_format_0}".format(_coconut_format_0=(past)), "he was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "she {_coconut_format_0}".format(_coconut_format_0=(past)), "she was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "it {_coconut_format_0}".format(_coconut_format_0=(past)), "it was {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #220:                 return {

        if not _coconut_case_match_check_2:  #229:             case ("plural", 3):
            if (_coconut.isinstance(_coconut_case_match_to_2, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_2) == 2) and (_coconut_case_match_to_2[0] == "plural") and (_coconut_case_match_to_2[1] == 3):  #229:             case ("plural", 3):
                _coconut_case_match_check_2 = True  #229:             case ("plural", 3):
            if _coconut_case_match_check_2:  #229:             case ("plural", 3):
                return _coconut_tail_call(_coconut.set, ("they {_coconut_format_0}".format(_coconut_format_0=(past)), "they were {_coconut_format_0}".format(_coconut_format_0=(present_participle))))  #230:                 return {f"they {past}", f"they were {present_participle}"}

# case _:
#     raise ValueError(
#         f"Invalid number and person: '{number}' '{person}'"
#     )

    _coconut_case_match_to_3 = (number, person)  #237:     match (number, person):
    _coconut_case_match_check_3 = False  #237:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "singular") and (_coconut_case_match_to_3[1] == 1):  #237:     match (number, person):
        _coconut_case_match_check_3 = True  #237:     match (number, person):
    if _coconut_case_match_check_3:  #237:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I was {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #239:             return {f"I was {present_participle}"}

    if not _coconut_case_match_check_3:  #241:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "plural") and (_coconut_case_match_to_3[1] == 1):  #241:         case ("plural", 1):
            _coconut_case_match_check_3 = True  #241:         case ("plural", 1):
        if _coconut_case_match_check_3:  #241:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we were {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #242:             return {f"we were {present_participle}"}

    if not _coconut_case_match_check_3:  #244:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_3 = True  #244:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_3:  #244:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_3 = False  #244:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_3:  #244:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "singular") and (_coconut_case_match_to_3[1] == 2):  #244:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_3 = True  #244:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_3:  #244:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "plural") and (_coconut_case_match_to_3[1] == 2):  #244:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_3 = True  #244:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_3:  #244:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you were {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #245:             return {f"you were {present_participle}"}

    if not _coconut_case_match_check_3:  #247:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "singular") and (_coconut_case_match_to_3[1] == 3):  #247:         case ("singular", 3):
            _coconut_case_match_check_3 = True  #247:         case ("singular", 3):
        if _coconut_case_match_check_3:  #247:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "she was {_coconut_format_0}".format(_coconut_format_0=(present_participle)), "it was {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #248:             return {

    if not _coconut_case_match_check_3:  #254:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_3, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_3) == 2) and (_coconut_case_match_to_3[0] == "plural") and (_coconut_case_match_to_3[1] == 3):  #254:         case ("plural", 3):
            _coconut_case_match_check_3 = True  #254:         case ("plural", 3):
        if _coconut_case_match_check_3:  #254:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they were {_coconut_format_0}".format(_coconut_format_0=(present_participle)),))  #255:             return {f"they were {present_participle}"}

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #257:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@_coconut_tco  #260: def _find_peractind_inflections(
def _find_peractind_inflections(lemma,  # type: str  #260: def _find_peractind_inflections(
    number,  # type: Literal["singular", "plural"]  #260: def _find_peractind_inflections(
    person,  # type: Literal[1, 2, 3]  #260: def _find_peractind_inflections(
    ):  #260: def _find_peractind_inflections(
# type: (...) -> set[str]
    past = lemminflect.getInflection(lemma, "VBD")[0]  #265:     past = lemminflect.getInflection(lemma, "VBD")[0]

    _coconut_case_match_to_4 = (number, person)  #267:     match (number, person):
    _coconut_case_match_check_4 = False  #267:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "singular") and (_coconut_case_match_to_4[1] == 1):  #267:     match (number, person):
        _coconut_case_match_check_4 = True  #267:     match (number, person):
    if _coconut_case_match_check_4:  #267:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I {_coconut_format_0}".format(_coconut_format_0=(past)), "I have {_coconut_format_0}".format(_coconut_format_0=(past)), "I did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #269:             return {f"I {past}", f"I have {past}", f"I did {lemma}"}

    if not _coconut_case_match_check_4:  #271:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "plural") and (_coconut_case_match_to_4[1] == 1):  #271:         case ("plural", 1):
            _coconut_case_match_check_4 = True  #271:         case ("plural", 1):
        if _coconut_case_match_check_4:  #271:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we {_coconut_format_0}".format(_coconut_format_0=(past)), "we have {_coconut_format_0}".format(_coconut_format_0=(past)), "we did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #272:             return {f"we {past}", f"we have {past}", f"we did {lemma}"}

    if not _coconut_case_match_check_4:  #274:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_4 = True  #274:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_4:  #274:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_4 = False  #274:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_4:  #274:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "singular") and (_coconut_case_match_to_4[1] == 2):  #274:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_4 = True  #274:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_4:  #274:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "plural") and (_coconut_case_match_to_4[1] == 2):  #274:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_4 = True  #274:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_4:  #274:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you {_coconut_format_0}".format(_coconut_format_0=(past)), "you have {_coconut_format_0}".format(_coconut_format_0=(past)), "you did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #275:             return {f"you {past}", f"you have {past}", f"you did {lemma}"}

    if not _coconut_case_match_check_4:  #277:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "singular") and (_coconut_case_match_to_4[1] == 3):  #277:         case ("singular", 3):
            _coconut_case_match_check_4 = True  #277:         case ("singular", 3):
        if _coconut_case_match_check_4:  #277:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he {_coconut_format_0}".format(_coconut_format_0=(past)), "he has {_coconut_format_0}".format(_coconut_format_0=(past)), "he did {_coconut_format_0}".format(_coconut_format_0=(lemma)), "she {_coconut_format_0}".format(_coconut_format_0=(past)), "she has {_coconut_format_0}".format(_coconut_format_0=(past)), "she did {_coconut_format_0}".format(_coconut_format_0=(lemma)), "it {_coconut_format_0}".format(_coconut_format_0=(past)), "it has {_coconut_format_0}".format(_coconut_format_0=(past)), "it did {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #278:             return {

    if not _coconut_case_match_check_4:  #290:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_4, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_4) == 2) and (_coconut_case_match_to_4[0] == "plural") and (_coconut_case_match_to_4[1] == 3):  #290:         case ("plural", 3):
            _coconut_case_match_check_4 = True  #290:         case ("plural", 3):
        if _coconut_case_match_check_4:  #290:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they {_coconut_format_0}".format(_coconut_format_0=(past)), "they have {_coconut_format_0}".format(_coconut_format_0=(past)), "they did {_coconut_format_0}".format(_coconut_format_0=(lemma))))  #291:             return {f"they {past}", f"they have {past}", f"they did {lemma}"}

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #293:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")



@_coconut_tco  #296: def _find_plpactind_inflections(
def _find_plpactind_inflections(lemma,  # type: str  #296: def _find_plpactind_inflections(
    number,  # type: Literal["singular", "plural"]  #296: def _find_plpactind_inflections(
    person,  # type: Literal[1, 2, 3]  #296: def _find_plpactind_inflections(
    ):  #296: def _find_plpactind_inflections(
# type: (...) -> set[str]
    past_participle = lemminflect.getInflection(lemma, "VBN")[0]  # type: str  #301:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
    if "__annotations__" not in _coconut.locals():  #301:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
        __annotations__ = {}  # type: ignore  #301:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
    __annotations__["past_participle"] = 'str'  #301:     past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]

    _coconut_case_match_to_5 = (number, person)  #303:     match (number, person):
    _coconut_case_match_check_5 = False  #303:     match (number, person):
    if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "singular") and (_coconut_case_match_to_5[1] == 1):  #303:     match (number, person):
        _coconut_case_match_check_5 = True  #303:     match (number, person):
    if _coconut_case_match_check_5:  #303:     match (number, person):
        return _coconut_tail_call(_coconut.set, ("I had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #305:             return {f"I had {past_participle}"}

    if not _coconut_case_match_check_5:  #307:         case ("plural", 1):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "plural") and (_coconut_case_match_to_5[1] == 1):  #307:         case ("plural", 1):
            _coconut_case_match_check_5 = True  #307:         case ("plural", 1):
        if _coconut_case_match_check_5:  #307:         case ("plural", 1):
            return _coconut_tail_call(_coconut.set, ("we had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #308:             return {f"we had {past_participle}"}

    if not _coconut_case_match_check_5:  #310:         case ("singular", 2) | ("plural", 2):
        _coconut_case_match_check_5 = True  #310:         case ("singular", 2) | ("plural", 2):
        if _coconut_case_match_check_5:  #310:         case ("singular", 2) | ("plural", 2):
            _coconut_case_match_check_5 = False  #310:         case ("singular", 2) | ("plural", 2):
            if not _coconut_case_match_check_5:  #310:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "singular") and (_coconut_case_match_to_5[1] == 2):  #310:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_5 = True  #310:         case ("singular", 2) | ("plural", 2):

            if not _coconut_case_match_check_5:  #310:         case ("singular", 2) | ("plural", 2):
                if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "plural") and (_coconut_case_match_to_5[1] == 2):  #310:         case ("singular", 2) | ("plural", 2):
                    _coconut_case_match_check_5 = True  #310:         case ("singular", 2) | ("plural", 2):


        if _coconut_case_match_check_5:  #310:         case ("singular", 2) | ("plural", 2):
            return _coconut_tail_call(_coconut.set, ("you had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #311:             return {f"you had {past_participle}"}

    if not _coconut_case_match_check_5:  #313:         case ("singular", 3):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "singular") and (_coconut_case_match_to_5[1] == 3):  #313:         case ("singular", 3):
            _coconut_case_match_check_5 = True  #313:         case ("singular", 3):
        if _coconut_case_match_check_5:  #313:         case ("singular", 3):
            return _coconut_tail_call(_coconut.set, ("he had {_coconut_format_0}".format(_coconut_format_0=(past_participle)), "she had {_coconut_format_0}".format(_coconut_format_0=(past_participle)), "it had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #314:             return {

    if not _coconut_case_match_check_5:  #320:         case ("plural", 3):
        if (_coconut.isinstance(_coconut_case_match_to_5, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_5) == 2) and (_coconut_case_match_to_5[0] == "plural") and (_coconut_case_match_to_5[1] == 3):  #320:         case ("plural", 3):
            _coconut_case_match_check_5 = True  #320:         case ("plural", 3):
        if _coconut_case_match_check_5:  #320:         case ("plural", 3):
            return _coconut_tail_call(_coconut.set, ("they had {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #321:             return {f"they had {past_participle}"}

    raise ValueError("Invalid number and person: '{_coconut_format_0}' '{_coconut_format_1}'".format(_coconut_format_0=(number), _coconut_format_1=(person)))  #323:     raise ValueError(f"Invalid number and person: '{number}' '{person}'")


# type: ignore[return]
@_coconut_tco  # type: ignore[return]  #326: def _find_participle_inflections(  # type: ignore[return]
def _find_participle_inflections(verb,  # type: str  # type: ignore[return]  #326: def _find_participle_inflections(  # type: ignore[return]
    components,  # type: accido.misc.EndingComponents  # type: ignore[return]  #326: def _find_participle_inflections(  # type: ignore[return]
    ):  # type: ignore[return]  #326: def _find_participle_inflections(  # type: ignore[return]
# type: (...) -> set[str]  # type: ignore[return]
    lemma = lemminflect.getLemma(verb, "NOUN")[0]  # type: str  #330:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]
    if "__annotations__" not in _coconut.locals():  #330:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]
        __annotations__ = {}  # type: ignore  #330:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]
    __annotations__["lemma"] = 'str'  #330:     lemma: str = lemminflect.getLemma(verb, "NOUN")[0]

    _coconut_case_match_to_6 = (components.tense, components.voice)  #332:     match (components.tense, components.voice):
    _coconut_case_match_check_6 = False  #332:     match (components.tense, components.voice):
    if (_coconut.isinstance(_coconut_case_match_to_6, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_6) == 2) and (_coconut_case_match_to_6[0] == "perfect") and (_coconut_case_match_to_6[1] == "passive"):  #332:     match (components.tense, components.voice):
        _coconut_case_match_check_6 = True  #332:     match (components.tense, components.voice):
    if _coconut_case_match_check_6:  #332:     match (components.tense, components.voice):
        past_participle = lemminflect.getInflection(lemma, "VBN")[0]  # type: str  #332:     match (components.tense, components.voice):
        if "__annotations__" not in _coconut.locals():  #332:     match (components.tense, components.voice):
            __annotations__ = {}  # type: ignore  #332:     match (components.tense, components.voice):
        __annotations__["past_participle"] = 'str'  #334:             past_participle: str = lemminflect.getInflection(lemma, "VBN")[0]
        return _coconut_tail_call(_coconut.set, ("having been {_coconut_format_0}".format(_coconut_format_0=(past_participle)),))  #335:             return {f"having been {past_participle}"}

    if not _coconut_case_match_check_6:  #337:         case ("present", "active"):
        if (_coconut.isinstance(_coconut_case_match_to_6, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_6) == 2) and (_coconut_case_match_to_6[0] == "present") and (_coconut_case_match_to_6[1] == "active"):  #337:         case ("present", "active"):
            _coconut_case_match_check_6 = True  #337:         case ("present", "active"):
        if _coconut_case_match_check_6:  #337:         case ("present", "active"):
            present_participle = lemminflect.getInflection(lemma, "VBG")[0]  # type: str  #337:         case ("present", "active"):
            if "__annotations__" not in _coconut.locals():  #337:         case ("present", "active"):
                __annotations__ = {}  # type: ignore  #337:         case ("present", "active"):
            __annotations__["present_participle"] = 'str'  #338:             present_participle: str = lemminflect.getInflection(lemma, "VBG")[
            return _coconut_tail_call(_coconut.set, (present_participle,))  #341:             return {present_participle}

    if not _coconut_case_match_check_6:  #343:         case _:
        _coconut_case_match_check_6 = True  #343:         case _:
        if _coconut_case_match_check_6:  #343:         case _:
            raise NotImplementedError("The {_coconut_format_0} {_coconut_format_1} participle has not been implemented".format(_coconut_format_0=(components.tense), _coconut_format_1=(components.voice)))  #344:             raise NotImplementedError(



@_coconut_tco  #349: def _find_preactinf_inflections(lemma: str) -> set[str]:
def _find_preactinf_inflections(lemma  # type: str  #349: def _find_preactinf_inflections(lemma: str) -> set[str]:
    ):  #349: def _find_preactinf_inflections(lemma: str) -> set[str]:
# type: (...) -> set[str]
    return _coconut_tail_call(_coconut.set, ("to {_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #350:     return {f"to {lemma}"}



@_coconut_tco  #353: def _find_preipe_inflections(lemma: str) -> set[str]:
def _find_preipe_inflections(lemma  # type: str  #353: def _find_preipe_inflections(lemma: str) -> set[str]:
    ):  #353: def _find_preipe_inflections(lemma: str) -> set[str]:
# type: (...) -> set[str]
    return _coconut_tail_call(_coconut.set, ("{_coconut_format_0}".format(_coconut_format_0=(lemma)),))  #354:     return {f"{lemma}"}
