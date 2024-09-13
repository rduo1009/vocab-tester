#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x83e4d7a0

# Compiled with Coconut version 3.1.2

"""Representation of a Latin word that is undeclinable."""

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



from functools import total_ordering  #3: from functools import total_ordering

from .class_word import _Word  #5: from .class_word import _Word

if TYPE_CHECKING:  #7: if TYPE_CHECKING:
    from .misc import EndingComponents  #8:     from .misc import EndingComponents
    from .type_aliases import Meaning  #9:     from .type_aliases import Meaning


@total_ordering  #12: @total_ordering
class RegularWord(_Word):  #13: class RegularWord(_Word):
    """Representation of a Latin word that is undeclinable.

    Attributes
    ----------
    word : str
    meaning : Meaning

    Examples
    --------
    >>> foo = RegularWord(word="sed", meaning="but")
    >>> foo.endings
    {'': 'sed'}

    Note that the arguments of RegularWord are keyword-only.
    """  #28:     """

    def __init__(self, word,  # type: str  #30:     def __init__(self, word: str, meaning: Meaning) -> None:
        meaning  # type: Meaning  #30:     def __init__(self, word: str, meaning: Meaning) -> None:
        ):  #30:     def __init__(self, word: str, meaning: Meaning) -> None:
# type: (...) -> None
        """Initalises RegularWord.

        Parameters
        ----------
        word : str
        meaning : Meaning
        """  #37:         """
        self.word = word  # type: str  #38:         self.word: str = word
        if "__annotations__" not in _coconut.locals():  #38:         self.word: str = word
            __annotations__ = {}  # type: ignore  #38:         self.word: str = word
        __annotations__["self.word"] = 'str'  #38:         self.word: str = word
        self.meaning = meaning  # type: Meaning  #39:         self.meaning: Meaning = meaning
        if "__annotations__" not in _coconut.locals():  #39:         self.meaning: Meaning = meaning
            __annotations__ = {}  # type: ignore  #39:         self.meaning: Meaning = meaning
        __annotations__["self.meaning"] = 'Meaning'  #39:         self.meaning: Meaning = meaning
        self.endings = _coconut.dict((("", self.word),))  #40:         self.endings = {"": self.word}


    def get(self):  #42:     def get(self) -> str:
# type: (...) -> str
        """Returns the word.

        Returns
        -------
        str
            The word.

        Examples
        --------
        >>> foo = RegularWord(word="sed", meaning="but")
        >>> foo.get()
        'sed'
        """  #55:         """
        return self.word  #56:         return self.word


    @staticmethod  #58:     @staticmethod
    def _create_namespace(key,  # type: str  # pragma: no cover # this should never be ran  # noqa: ARG004  #59:     def _create_namespace(
        ):  # pragma: no cover # this should never be ran  # noqa: ARG004  #59:     def _create_namespace(
# type: (...) -> EndingComponents  # pragma: no cover # this should never be ran  # noqa: ARG004
        return NotImplemented  #62:         return NotImplemented


    @_coconut_tco  #64:     def __repr__(self) -> str:
    def __repr__(self):  #64:     def __repr__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("RegularWord({_coconut_format_0}, {_coconut_format_1})".format, _coconut_format_0=(self.word), _coconut_format_1=(self.meaning))  #65:         return f"RegularWord({self.word}, {self.meaning})"


_coconut_call_set_names(RegularWord)  #67:         return f"RegularWord({self.word}, {self.meaning})"