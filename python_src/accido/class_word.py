#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf13dc79b

# Compiled with Coconut version 3.1.2

"""Representation of a Latin word."""

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



from abc import ABC  #3: from abc import ABC, abstractmethod
from abc import abstractmethod  #3: from abc import ABC, abstractmethod
from functools import total_ordering  #4: from functools import total_ordering
if _coconut.typing.TYPE_CHECKING:  #5: from typing import Any
    from typing import Any  #5: from typing import Any
else:  #5: from typing import Any
    try:  #5: from typing import Any
        Any = _coconut.typing.Any  #5: from typing import Any
    except _coconut.AttributeError as _coconut_imp_err:  #5: from typing import Any
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #5: from typing import Any

from .misc import EndingComponents  #7: from .misc import EndingComponents, MultipleEndings
from .misc import MultipleEndings  #7: from .misc import EndingComponents, MultipleEndings

if TYPE_CHECKING:  #9: if TYPE_CHECKING:
    from .type_aliases import Ending  #10:     from .type_aliases import Ending, Endings
    from .type_aliases import Endings  #10:     from .type_aliases import Ending, Endings


@total_ordering  #13: @total_ordering
class _Word(ABC):  # noqa: PLW1641  #14: class _Word(ABC):  # noqa: PLW1641
    """Representation of an word.

    This class is not intended to be used by the user. Rather, all of the
    other classes inherit from this class.

    Attributes
    ----------
    endings : Ending
    _first : str
        The first principal part. Used so that the word classes can be
        alphabetically sorted.
    """  #26:     """

    def __init__(self):  #28:     def __init__(self) -> None:
# type: (...) -> None
        """Initialises _Word (and all classes that inherit from it)."""  #29:         """Initialises _Word (and all classes that inherit from it)."""
        self.endings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Endings  #30:         self.endings: Endings
        if "__annotations__" not in _coconut.locals():  #30:         self.endings: Endings
            __annotations__ = {}  # type: ignore  #30:         self.endings: Endings
        __annotations__["self.endings"] = 'Endings'  #30:         self.endings: Endings
        self._first = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #31:         self._first: str
        if "__annotations__" not in _coconut.locals():  #31:         self._first: str
            __annotations__ = {}  # type: ignore  #31:         self._first: str
        __annotations__["self._first"] = 'str'  #31:         self._first: str
        self._unique_endings = set()  # type: set[Ending]  #32:         self._unique_endings: set[Ending] = set()
        if "__annotations__" not in _coconut.locals():  #32:         self._unique_endings: set[Ending] = set()
            __annotations__ = {}  # type: ignore  #32:         self._unique_endings: set[Ending] = set()
        __annotations__["self._unique_endings"] = 'set[Ending]'  #32:         self._unique_endings: set[Ending] = set()


    def __eq__(self, other  # type: object  #34:     def __eq__(self, other: object) -> bool:
        ):  #34:     def __eq__(self, other: object) -> bool:
# type: (...) -> bool
        if not isinstance(other, _Word):  #35:         if not isinstance(other, _Word):
            return NotImplemented  #36:             return NotImplemented
        return self.endings == other.endings  #37:         return self.endings == other.endings


    def __lt__(self, other  # type: object  #39:     def __lt__(self, other: object) -> bool:
        ):  #39:     def __lt__(self, other: object) -> bool:
# type: (...) -> bool
        if not isinstance(other, _Word):  #40:         if not isinstance(other, _Word):
            return NotImplemented  #41:             return NotImplemented
        return self._first < other._first  #42:         return self._first < other._first


    def __getitem__(self, key  # type: str  #44:     def __getitem__(self, key: str) -> Ending:
        ):  #44:     def __getitem__(self, key: str) -> Ending:
# type: (...) -> Ending
        return self.endings[key]  #45:         return self.endings[key]


    def find(self, form  # type: str  #47:     def find(self, form: str) -> list[EndingComponents]:
        ):  #47:     def find(self, form: str) -> list[EndingComponents]:
# type: (...) -> list[EndingComponents]
        """Finds the accido properties that match the given form.

        Attributes
        ----------
        form : str
            The form to search for.

        Returns
        -------
        list[EndingComponents]
            The list of EndingComponents objects that represent the endings
            that match the given form.
        """  #60:         """
        return [self._create_namespace(key) for key, value in self.endings.items() if (isinstance(value, MultipleEndings) and form in value.get_all()) or (not isinstance(value, MultipleEndings) and value == form)]  #61:         return [

# Force implementation of these methods
# docstr-coverage:excused `abstract method`

    @abstractmethod  #70:     @abstractmethod
    def get(self, *args,  # type: Any  # pragma: no cover # sourcery skip: docstrings-for-functions  #71:     def get(
        **kwargs,  # type: Any  # pragma: no cover # sourcery skip: docstrings-for-functions  #71:     def get(
        ):  # pragma: no cover # sourcery skip: docstrings-for-functions  #71:     def get(
# type: (...) -> (_coconut.typing.Union[Ending, None])  # pragma: no cover # sourcery skip: docstrings-for-functions
        pass  #78:         pass


    @staticmethod  #80:     @staticmethod
    @abstractmethod  #81:     @abstractmethod
    def _create_namespace(key  # type: str  # pragma: no cover  #82:     def _create_namespace(key: str) -> EndingComponents:  # pragma: no cover
        ):  # pragma: no cover  #82:     def _create_namespace(key: str) -> EndingComponents:  # pragma: no cover
# type: (...) -> EndingComponents  # pragma: no cover
        pass  #83:         pass


_coconut_call_set_names(_Word)  #85:         pass
