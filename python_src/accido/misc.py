#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x44b981cf

# Compiled with Coconut version 3.1.2

"""Contains miscellaneous functions, classes and constants used by accido."""

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



from dataclasses import dataclass  #3: from dataclasses import dataclass
from types import SimpleNamespace  #4: from types import SimpleNamespace
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

"""Mapping of number values to their more concise abbreviated forms."""  #7: """Mapping of number values to their more concise abbreviated forms."""
NUMBER_SHORTHAND = _coconut.dict((("singular", "sg"), ("plural", "pl")))  # type: Final[dict[str, str]]  #8: NUMBER_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #8: NUMBER_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #8: NUMBER_SHORTHAND: Final[dict[str, str]] = {
__annotations__["NUMBER_SHORTHAND"] = 'Final[dict[str, str]]'  #8: NUMBER_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of tense values to their more concise abbreviated forms."""  #13: """Mapping of tense values to their more concise abbreviated forms."""
TENSE_SHORTHAND = _coconut.dict((("present", "pre"), ("imperfect", "imp"), ("future", "fut"), ("perfect", "per"), ("pluperfect", "plp")))  # type: Final[dict[str, str]]  #14: TENSE_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #14: TENSE_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #14: TENSE_SHORTHAND: Final[dict[str, str]] = {
__annotations__["TENSE_SHORTHAND"] = 'Final[dict[str, str]]'  #14: TENSE_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of voice values to their more concise abbreviated forms."""  #23: """Mapping of voice values to their more concise abbreviated forms."""
VOICE_SHORTHAND = _coconut.dict((("active", "act"), ("passive", "pas")))  # type: Final[dict[str, str]]  #24: VOICE_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #24: VOICE_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #24: VOICE_SHORTHAND: Final[dict[str, str]] = {
__annotations__["VOICE_SHORTHAND"] = 'Final[dict[str, str]]'  #24: VOICE_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of mood values to their more concise abbreviated forms."""  #29: """Mapping of mood values to their more concise abbreviated forms."""
MOOD_SHORTHAND = _coconut.dict((("indicative", "ind"), ("infinitive", "inf"), ("imperative", "ipe"), ("subjunctive", "sbj"), ("participle", "ptc")))  # type: Final[dict[str, str]]  #30: MOOD_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #30: MOOD_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #30: MOOD_SHORTHAND: Final[dict[str, str]] = {
__annotations__["MOOD_SHORTHAND"] = 'Final[dict[str, str]]'  #30: MOOD_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of case values to their more concise abbreviated forms."""  #38: """Mapping of case values to their more concise abbreviated forms."""
CASE_SHORTHAND = _coconut.dict((("nominative", "nom"), ("vocative", "voc"), ("accusative", "acc"), ("genitive", "gen"), ("dative", "dat"), ("ablative", "abl")))  # type: Final[dict[str, str]]  #39: CASE_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #39: CASE_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #39: CASE_SHORTHAND: Final[dict[str, str]] = {
__annotations__["CASE_SHORTHAND"] = 'Final[dict[str, str]]'  #39: CASE_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of gender values to their more concise abbreviated forms."""  #48: """Mapping of gender values to their more concise abbreviated forms."""
GENDER_SHORTHAND = _coconut.dict((("masculine", "m"), ("feminine", "f"), ("neuter", "n")))  # type: Final[dict[str, str]]  #49: GENDER_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #49: GENDER_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #49: GENDER_SHORTHAND: Final[dict[str, str]] = {
__annotations__["GENDER_SHORTHAND"] = 'Final[dict[str, str]]'  #49: GENDER_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of degree values to their more concise abbreviated forms."""  #55: """Mapping of degree values to their more concise abbreviated forms."""
DEGREE_SHORTHAND = _coconut.dict((("positive", "pos"), ("comparative", "cmp"), ("superlative", "spr")))  # type: Final[dict[str, str]]  #56: DEGREE_SHORTHAND: Final[dict[str, str]] = {
if "__annotations__" not in _coconut.locals():  #56: DEGREE_SHORTHAND: Final[dict[str, str]] = {
    __annotations__ = {}  # type: ignore  #56: DEGREE_SHORTHAND: Final[dict[str, str]] = {
__annotations__["DEGREE_SHORTHAND"] = 'Final[dict[str, str]]'  #56: DEGREE_SHORTHAND: Final[dict[str, str]] = {

"""Mapping of person values to their more concise abbreviated forms."""  #62: """Mapping of person values to their more concise abbreviated forms."""
PERSON_SHORTHAND = _coconut.dict(((1, "1st person"), (2, "2nd person"), (3, "3rd person")))  # type: Final[dict[int, str]]  #63: PERSON_SHORTHAND: Final[dict[int, str]] = {
if "__annotations__" not in _coconut.locals():  #63: PERSON_SHORTHAND: Final[dict[int, str]] = {
    __annotations__ = {}  # type: ignore  #63: PERSON_SHORTHAND: Final[dict[int, str]] = {
__annotations__["PERSON_SHORTHAND"] = 'Final[dict[int, str]]'  #63: PERSON_SHORTHAND: Final[dict[int, str]] = {


class EndingComponents(SimpleNamespace):  #70: class EndingComponents(SimpleNamespace):
    """A container for the grammatical components of an ending.

    Examples
    --------
    >>> foo = EndingComponents(case="nominative", gender="masculine", \
                               number="singular")
    >>> foo.case
    'nominative'
    """  #79:     """


_coconut_call_set_names(EndingComponents)  #82: @dataclass(init=True)
@dataclass(init=True)  #82: @dataclass(init=True)
class MultipleMeanings(_coconut.object):  #83: class MultipleMeanings:
    """Represents multiple meanings, with a main meaning and other meanings.

    Attributes
    ----------
    meanings : list[str]
        The meanings.

    Notes
    -----
    This class allows for there to be several English definitions of one
    Latin word. This means for translating-to-English questions, synonyms
    can be accepted, but not vice versa.

    Examples
    --------
    >>> foo = MultipleMeanings(["hide", "conceal"])
    >>> foo.meanings
    ['hide', 'conceal']

    >>> foo.__str__()
    'hide'
    """  #105:     """

    meanings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: list[str]  #107:     meanings: list[str]
    if "__annotations__" not in _coconut.locals():  #107:     meanings: list[str]
        __annotations__ = {}  # type: ignore  #107:     meanings: list[str]
    __annotations__["meanings"] = 'list[str]'  #107:     meanings: list[str]

    def __str__(self):  #109:     def __str__(self) -> str:
# type: (...) -> str
        return self.meanings[0]  #110:         return self.meanings[0]


    @_coconut_tco  #112:     def __repr__(self) -> str:
    def __repr__(self):  #112:     def __repr__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("MultipleMeanings({_coconut_format_0})".format, _coconut_format_0=(', '.join(self.meanings)))  #113:         return f"MultipleMeanings({', '.join(self.meanings)})"



_coconut_call_set_names(MultipleMeanings)  #116: class MultipleEndings(SimpleNamespace):
class MultipleEndings(SimpleNamespace):  #116: class MultipleEndings(SimpleNamespace):
    """Represents multiple endings for a word, where each ending is a
    separate string.

    The fact that the attribute names can be customised means that this
    class can be used for many use cases.
    e.g. MultipleEndings(regular="nostri", partitive="nostrum")
    would allow for nostrum being the partitive genitive, while nostri
    for the rest of the genitive uses.

    Attributes
    ----------
    value : str

    etc.

    Examples
    --------
    >>> foo = MultipleEndings(regular="nostri", partitive="nostrum")
    >>> foo.regular
    'nostri'

    >>> foo.__str__()
    'nostri/nostrum'

    >>> foo.get_all()
    ['nostri', 'nostrum']
    """  # noqa: D205  #143:     """  # noqa: D205

    @_coconut_tco  #145:     def get_all(self) -> list[str]:
    def get_all(self):  #145:     def get_all(self) -> list[str]:
# type: (...) -> list[str]
        """Returns a list of all the possible endings.

        Returns
        -------
        list[str]
            The endings.
        """  #152:         """
        return _coconut_tail_call(list, self.__dict__.values())  #153:         return list(self.__dict__.values())


    @_coconut_tco  #155:     def __str__(self) -> str:
    def __str__(self):  #155:     def __str__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("/".join, self.__dict__.values())  #156:         return "/".join(self.__dict__.values())


    def __add__(self, val2  # type: str  #158:     def __add__(self, val2: str) -> str:
        ):  #158:     def __add__(self, val2: str) -> str:
# type: (...) -> str
        return self.__str__() + val2  #159:         return self.__str__() + val2

# Allows for a prefix to be added to all of the endings.
# pragma: no cover
    @_coconut_tco  # pragma: no cover  #162:     def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
    def __radd__(self, val2  # type: str  # pragma: no cover  #162:     def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
        ):  # pragma: no cover  #162:     def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
# type: (...) -> MultipleEndings  # pragma: no cover
        prefixed = _coconut.dict(((key), ("{_coconut_format_0}{_coconut_format_1}".format(_coconut_format_0=(val2), _coconut_format_1=(value)))) for key, value in self.__dict__.items())  #163:         prefixed = {
        return _coconut_tail_call(MultipleEndings, **prefixed)  #166:         return MultipleEndings(**prefixed)


_coconut_call_set_names(MultipleEndings)  #168:         return MultipleEndings(**prefixed)
