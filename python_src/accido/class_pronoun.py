#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc90d848f

# Compiled with Coconut version 3.1.2

"""Representation of a Latin pronoun with endings."""

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



from functools import total_ordering  #3: from functools import total_ordering

from ..utils import key_from_value  #5: from ..utils import key_from_value
from .class_word import _Word  #6: from .class_word import _Word
from .edge_cases import PRONOUNS  #7: from .edge_cases import PRONOUNS
from .exceptions import InvalidInputError  #8: from .exceptions import InvalidInputError
from .misc import CASE_SHORTHAND  #9: from .misc import (
from .misc import GENDER_SHORTHAND  #9: from .misc import (
from .misc import NUMBER_SHORTHAND  #9: from .misc import (
from .misc import EndingComponents  #9: from .misc import (

if TYPE_CHECKING:  #16: if TYPE_CHECKING:
    from .type_aliases import Ending  #17:     from .type_aliases import Ending, Meaning
    from .type_aliases import Meaning  #17:     from .type_aliases import Ending, Meaning


@total_ordering  #20: @total_ordering
class Pronoun(_Word):  #21: class Pronoun(_Word):
    """Representation of a Latin pronoun with endings.

    Attributes
    ----------
    pronoun : str
    meaning : Meaning
    endings : Endings

    Examples
    --------
    >>> foo = Pronoun(pronoun="hic", meaning="this")
    >>> foo["Pmnomsg"]
    'hic'

    Note that the arguments of Pronoun are keyword-only.
    """  #37:     """

    def __init__(self, pronoun,  # type: str  #39:     def __init__(self, pronoun: str, meaning: Meaning) -> None:
        meaning  # type: Meaning  #39:     def __init__(self, pronoun: str, meaning: Meaning) -> None:
        ):  #39:     def __init__(self, pronoun: str, meaning: Meaning) -> None:
# type: (...) -> None
        """Intialises Pronoun and determines the endings.

        Parameters
        ----------
        pronoun : str
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the pronoun entered is not in the pronoun table.

        Notes
        -----
        As pronouns in Latin have irregular endings with little pattern,
        the pronoun endings are manually written out in the edge_cases
        module.
        """  #57:         """
        __class__ = Pronoun  #58:         super().__init__()

        super().__init__()  #58:         super().__init__()
        try:  #59:         try:
            self.endings = PRONOUNS[pronoun]  #60:             self.endings = PRONOUNS[pronoun]
        except KeyError as e:  #61:         except KeyError as e:
            _coconut_raise_from_0 = InvalidInputError("Pronoun '{_coconut_format_0}' not recognised".format(_coconut_format_0=(pronoun)))  #62:             raise InvalidInputError(
            _coconut_raise_from_0.__cause__ = e  #62:             raise InvalidInputError(
            raise _coconut_raise_from_0  #62:             raise InvalidInputError(

        self.pronoun = pronoun  # type: str  #66:         self.pronoun: str = pronoun
        if "__annotations__" not in _coconut.locals():  #66:         self.pronoun: str = pronoun
            __annotations__ = {}  # type: ignore  #66:         self.pronoun: str = pronoun
        __annotations__["self.pronoun"] = 'str'  #66:         self.pronoun: str = pronoun
        self._first = self.pronoun  #67:         self._first = self.pronoun
        self.meaning = meaning  # type: Meaning  #68:         self.meaning: Meaning = meaning
        if "__annotations__" not in _coconut.locals():  #68:         self.meaning: Meaning = meaning
            __annotations__ = {}  # type: ignore  #68:         self.meaning: Meaning = meaning
        __annotations__["self.meaning"] = 'Meaning'  #68:         self.meaning: Meaning = meaning

        self._mascnom = self.endings["Pmnomsg"]  # type: Ending  #70:         self._mascnom: Ending = self.endings["Pmnomsg"]
        if "__annotations__" not in _coconut.locals():  #70:         self._mascnom: Ending = self.endings["Pmnomsg"]
            __annotations__ = {}  # type: ignore  #70:         self._mascnom: Ending = self.endings["Pmnomsg"]
        __annotations__["self._mascnom"] = 'Ending'  #70:         self._mascnom: Ending = self.endings["Pmnomsg"]
        self._femnom = self.endings["Pfnomsg"]  # type: Ending  #71:         self._femnom: Ending = self.endings["Pfnomsg"]
        if "__annotations__" not in _coconut.locals():  #71:         self._femnom: Ending = self.endings["Pfnomsg"]
            __annotations__ = {}  # type: ignore  #71:         self._femnom: Ending = self.endings["Pfnomsg"]
        __annotations__["self._femnom"] = 'Ending'  #71:         self._femnom: Ending = self.endings["Pfnomsg"]
        self._neutnom = self.endings["Pnnomsg"]  # type: Ending  #72:         self._neutnom: Ending = self.endings["Pnnomsg"]
        if "__annotations__" not in _coconut.locals():  #72:         self._neutnom: Ending = self.endings["Pnnomsg"]
            __annotations__ = {}  # type: ignore  #72:         self._neutnom: Ending = self.endings["Pnnomsg"]
        __annotations__["self._neutnom"] = 'Ending'  #72:         self._neutnom: Ending = self.endings["Pnnomsg"]


    @_coconut_tco  #74:     def get(self, gender: str, case: str, number: str) -> Ending | None:
    def get(self, gender,  # type: str  #74:     def get(self, gender: str, case: str, number: str) -> Ending | None:
        case,  # type: str  #74:     def get(self, gender: str, case: str, number: str) -> Ending | None:
        number  # type: str  #74:     def get(self, gender: str, case: str, number: str) -> Ending | None:
        ):  #74:     def get(self, gender: str, case: str, number: str) -> Ending | None:
# type: (...) -> _coconut.typing.Union[Ending, None]
        """Returns the ending of the pronoun.

        The function returns None if no ending is found.

        Parameters
        ----------
        gender, case, number : str

        Returns
        -------
        Ending
            The ending found.
        None
            If no ending is found

        Raises
        ------
        InvalidInputError
            If the input is invalid.

            If an ending cannot be found.

        Examples
        --------
        >>> foo = Pronoun(pronoun="hic", meaning="this")
        >>> foo.get(gender="masculine", case="nominative", number="singular")
        'hic'

        Note that the arguments of get are keyword-only.
        """  #104:         """
        if gender not in GENDER_SHORTHAND:  #105:         if gender not in GENDER_SHORTHAND:
            raise InvalidInputError("Invalid gender: '{_coconut_format_0}'".format(_coconut_format_0=(gender)))  #106:             raise InvalidInputError(f"Invalid gender: '{gender}'")

        if case not in CASE_SHORTHAND:  #108:         if case not in CASE_SHORTHAND:
            raise InvalidInputError("Invalid case: '{_coconut_format_0}'".format(_coconut_format_0=(case)))  #109:             raise InvalidInputError(f"Invalid case: '{case}'")

        if number not in NUMBER_SHORTHAND:  #111:         if number not in NUMBER_SHORTHAND:
            raise InvalidInputError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(number)))  #112:             raise InvalidInputError(f"Invalid number: '{number}'")

        short_gender = GENDER_SHORTHAND[gender]  # type: str  #114:         short_gender: str = GENDER_SHORTHAND[gender]
        if "__annotations__" not in _coconut.locals():  #114:         short_gender: str = GENDER_SHORTHAND[gender]
            __annotations__ = {}  # type: ignore  #114:         short_gender: str = GENDER_SHORTHAND[gender]
        __annotations__["short_gender"] = 'str'  #114:         short_gender: str = GENDER_SHORTHAND[gender]
        short_case = CASE_SHORTHAND[case]  # type: str  #115:         short_case: str = CASE_SHORTHAND[case]
        if "__annotations__" not in _coconut.locals():  #115:         short_case: str = CASE_SHORTHAND[case]
            __annotations__ = {}  # type: ignore  #115:         short_case: str = CASE_SHORTHAND[case]
        __annotations__["short_case"] = 'str'  #115:         short_case: str = CASE_SHORTHAND[case]
        short_number = NUMBER_SHORTHAND[number]  # type: str  #116:         short_number: str = NUMBER_SHORTHAND[number]
        if "__annotations__" not in _coconut.locals():  #116:         short_number: str = NUMBER_SHORTHAND[number]
            __annotations__ = {}  # type: ignore  #116:         short_number: str = NUMBER_SHORTHAND[number]
        __annotations__["short_number"] = 'str'  #116:         short_number: str = NUMBER_SHORTHAND[number]

        return _coconut_tail_call(self.endings.get, "P{_coconut_format_0}{_coconut_format_1}{_coconut_format_2}".format(_coconut_format_0=(short_gender), _coconut_format_1=(short_case), _coconut_format_2=(short_number)))  #118:         return self.endings.get(f"P{short_gender}{short_case}{short_number}")


    @staticmethod  #120:     @staticmethod
    def _create_namespace(key  # type: str  #121:     def _create_namespace(key: str) -> EndingComponents:
        ):  #121:     def _create_namespace(key: str) -> EndingComponents:
# type: (...) -> EndingComponents
        output = EndingComponents(gender=key_from_value(GENDER_SHORTHAND, key[1]), case=key_from_value(CASE_SHORTHAND, key[2:5]), number=key_from_value(NUMBER_SHORTHAND, key[5:7]))  # type: EndingComponents  #122:         output: EndingComponents = EndingComponents(
        if "__annotations__" not in _coconut.locals():  #122:         output: EndingComponents = EndingComponents(
            __annotations__ = {}  # type: ignore  #122:         output: EndingComponents = EndingComponents(
        __annotations__["output"] = 'EndingComponents'  #122:         output: EndingComponents = EndingComponents(
        output.string = "{_coconut_format_0} {_coconut_format_1} {_coconut_format_2}".format(_coconut_format_0=(output.case), _coconut_format_1=(output.number), _coconut_format_2=(output.gender))  #127:         output.string = f"{output.case} {output.number} {output.gender}"
        return output  #128:         return output


    @_coconut_tco  #130:     def __repr__(self) -> str:
    def __repr__(self):  #130:     def __repr__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("Pronoun({_coconut_format_0}, {_coconut_format_1})".format, _coconut_format_0=(self.pronoun), _coconut_format_1=(self.meaning))  #131:         return f"Pronoun({self.pronoun}, {self.meaning})"


    @_coconut_tco  #133:     def __str__(self) -> str:
    def __str__(self):  #133:     def __str__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("{_coconut_format_0}: {_coconut_format_1}, {_coconut_format_2}, {_coconut_format_3}".format, _coconut_format_0=(self.meaning), _coconut_format_1=(self._mascnom), _coconut_format_2=(self._femnom), _coconut_format_3=(self._neutnom))  #134:         return (


_coconut_call_set_names(Pronoun)  #138:         )
