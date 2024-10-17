#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfd8a436f

# Compiled with Coconut version 3.1.2

"""Representation of a Latin adjective with endings."""

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
from .edge_cases import IRREGULAR_ADJECTIVES  #7: from .edge_cases import IRREGULAR_ADJECTIVES, LIS_ADJECTIVES
from .edge_cases import LIS_ADJECTIVES  #7: from .edge_cases import IRREGULAR_ADJECTIVES, LIS_ADJECTIVES
from .exceptions import InvalidInputError  #8: from .exceptions import InvalidInputError
from .misc import CASE_SHORTHAND  #9: from .misc import (
from .misc import DEGREE_SHORTHAND  #9: from .misc import (
from .misc import GENDER_SHORTHAND  #9: from .misc import (
from .misc import NUMBER_SHORTHAND  #9: from .misc import (
from .misc import EndingComponents  #9: from .misc import (

if TYPE_CHECKING:  #17: if TYPE_CHECKING:
    from .type_aliases import Ending  #18:     from .type_aliases import Ending, Endings, Meaning
    from .type_aliases import Endings  #18:     from .type_aliases import Ending, Endings, Meaning
    from .type_aliases import Meaning  #18:     from .type_aliases import Ending, Endings, Meaning


@total_ordering  #21: @total_ordering
class Adjective(_Word):  #22: class Adjective(_Word):
    """Representation of a Latin adjective with endings.

    Attributes
    ----------
    meaning : Meaning
    endings : Endings
    declension : str
        The declension of the adjective. "212" represents a 2-1-2
        adjective, while "3" represents a third declension adjective.
    termination : Optional[int]
        The termination of the adjective if applicable (only third
        declension adjectives).
    irregular_flag : bool

    Examples
    --------
    >>> foo = Adjective(
    ...     "laetus", "laeta", "laetum", declension="212", meaning="happy"
    ... )
    >>> foo["Aposmnomsg"]
    'laetus'

    Note that the declension and meaning arguments of Adjectives are
    keyword-only.

    >>> bar = Adjective(
    ...     "egens", "egentis", termination=1, declension="3", meaning="poor"
    ... )
    >>> bar["Aposmnomsg"]
    'egens'

    The same can be said with the termination argument for third declension
    adjectives.
    """  #56:     """

# HACK: Extra optional stuff to avoid syntax errors
    def __init__(self, first_principal_part,  # type: str  #59:     def __init__(
        second_principal_part,  # type: str  #59:     def __init__(
        third_principal_part=None,  # type: _coconut.typing.Union[str, None]  #59:     def __init__(
        termination=None,  # type: _coconut.typing.Union[int, None]  #59:     def __init__(
        declension=None,  # type: _coconut.typing.Union[str, None]  #59:     def __init__(
        meaning=None,  # type: _coconut.typing.Union[Meaning, None]  #59:     def __init__(
        ):  #59:     def __init__(
# type: (...) -> None
        """Initialises Adjective and determines the endings.

        Parameters
        ----------
        *principal_parts : str
            The principal parts of the adjective.
        termination : Optional[int], default = None
            The termination of the adjective if applicable (only third
            declension adjectives).
        declension : str
            The declension of the adjective. "212" represents a 2-1-2
            adjective, while "3" represents a third declension adjective.
        meaning: Meaning

        Raises
        ------
        InvalidInputError
            If the input is invalid.
        """  #86:         """
        __class__ = Adjective  #87:         super().__init__()

        super().__init__()  #87:         super().__init__()
        self._principal_parts = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: tuple[str, ...]  #88:         self._principal_parts: tuple[str, ...]
        if "__annotations__" not in _coconut.locals():  #88:         self._principal_parts: tuple[str, ...]
            __annotations__ = {}  # type: ignore  #88:         self._principal_parts: tuple[str, ...]
        __annotations__["self._principal_parts"] = 'tuple[str, ...]'  #88:         self._principal_parts: tuple[str, ...]
        if third_principal_part:  #89:         if third_principal_part:
            self._principal_parts = (first_principal_part, second_principal_part, third_principal_part)  #90:             self._principal_parts = (
        else:  #95:         else:
            self._principal_parts = (first_principal_part, second_principal_part)  #96:             self._principal_parts = (
        self._mascnom = self._principal_parts[0]  # type: str  #100:         self._mascnom: str = self._principal_parts[0]
        if "__annotations__" not in _coconut.locals():  #100:         self._mascnom: str = self._principal_parts[0]
            __annotations__ = {}  # type: ignore  #100:         self._mascnom: str = self._principal_parts[0]
        __annotations__["self._mascnom"] = 'str'  #100:         self._mascnom: str = self._principal_parts[0]
        self._femnom = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #101:         self._femnom: str
        if "__annotations__" not in _coconut.locals():  #101:         self._femnom: str
            __annotations__ = {}  # type: ignore  #101:         self._femnom: str
        __annotations__["self._femnom"] = 'str'  #101:         self._femnom: str
        self._neutnom = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #102:         self._neutnom: str
        if "__annotations__" not in _coconut.locals():  #102:         self._neutnom: str
            __annotations__ = {}  # type: ignore  #102:         self._neutnom: str
        __annotations__["self._neutnom"] = 'str'  #102:         self._neutnom: str

        self._first = self._principal_parts[0]  #104:         self._first = self._principal_parts[0]
        if meaning:  #105:         if meaning:
            self.meaning = meaning  # type: Meaning  #106:             self.meaning: Meaning = meaning
            if "__annotations__" not in _coconut.locals():  #106:             self.meaning: Meaning = meaning
                __annotations__ = {}  # type: ignore  #106:             self.meaning: Meaning = meaning
            __annotations__["self.meaning"] = 'Meaning'  #106:             self.meaning: Meaning = meaning
        else:  #107:         else:
            raise ValueError  #108:             raise ValueError
        if declension:  #109:         if declension:
            self.declension = declension  # type: str  #110:             self.declension: str = declension
            if "__annotations__" not in _coconut.locals():  #110:             self.declension: str = declension
                __annotations__ = {}  # type: ignore  #110:             self.declension: str = declension
            __annotations__["self.declension"] = 'str'  #110:             self.declension: str = declension
        else:  #111:         else:
            raise ValueError  #112:             raise ValueError
        self.termination = termination  # type: _coconut.typing.Union[int, None]  #113:         self.termination: int | None = termination
        if "__annotations__" not in _coconut.locals():  #113:         self.termination: int | None = termination
            __annotations__ = {}  # type: ignore  #113:         self.termination: int | None = termination
        __annotations__["self.termination"] = '_coconut.typing.Union[int, None]'  #113:         self.termination: int | None = termination
        self.irregular_flag = False  # type: bool  #114:         self.irregular_flag: bool = False
        if "__annotations__" not in _coconut.locals():  #114:         self.irregular_flag: bool = False
            __annotations__ = {}  # type: ignore  #114:         self.irregular_flag: bool = False
        __annotations__["self.irregular_flag"] = 'bool'  #114:         self.irregular_flag: bool = False
        self.adverb_flag = True  # type: bool  #115:         self.adverb_flag: bool = True
        if "__annotations__" not in _coconut.locals():  #115:         self.adverb_flag: bool = True
            __annotations__ = {}  # type: ignore  #115:         self.adverb_flag: bool = True
        __annotations__["self.adverb_flag"] = 'bool'  #115:         self.adverb_flag: bool = True

        self._pos_stem = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #117:         self._pos_stem: str
        if "__annotations__" not in _coconut.locals():  #117:         self._pos_stem: str
            __annotations__ = {}  # type: ignore  #117:         self._pos_stem: str
        __annotations__["self._pos_stem"] = 'str'  #117:         self._pos_stem: str
        self._cmp_stem = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #118:         self._cmp_stem: str
        if "__annotations__" not in _coconut.locals():  #118:         self._cmp_stem: str
            __annotations__ = {}  # type: ignore  #118:         self._cmp_stem: str
        __annotations__["self._cmp_stem"] = 'str'  #118:         self._cmp_stem: str
        self._spr_stem = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #119:         self._spr_stem: str
        if "__annotations__" not in _coconut.locals():  #119:         self._spr_stem: str
            __annotations__ = {}  # type: ignore  #119:         self._spr_stem: str
        __annotations__["self._spr_stem"] = 'str'  #119:         self._spr_stem: str

        if self._mascnom in IRREGULAR_ADJECTIVES:  #121:         if self._mascnom in IRREGULAR_ADJECTIVES:
            self.irregular_flag = True  #122:             self.irregular_flag = True
            irregular_data = IRREGULAR_ADJECTIVES[self._mascnom]  #123:             irregular_data = IRREGULAR_ADJECTIVES[self._mascnom]

            assert irregular_data[0] is not None  #125:             assert irregular_data[0] is not None
            assert irregular_data[1] is not None  #126:             assert irregular_data[1] is not None

            self._cmp_stem = irregular_data[0]  #128:             self._cmp_stem = irregular_data[0]
            self._spr_stem = irregular_data[1]  #129:             self._spr_stem = irregular_data[1]

            if None not in irregular_data[2:]:  #131:             if None not in irregular_data[2:]:
                assert irregular_data[2] is not None  #132:                 assert irregular_data[2] is not None
                assert irregular_data[3] is not None  #133:                 assert irregular_data[3] is not None
                assert irregular_data[4] is not None  #134:                 assert irregular_data[4] is not None

                self._irregular_posadv = irregular_data[2]  # type: str  #136:                 self._irregular_posadv: str = irregular_data[2]
                if "__annotations__" not in _coconut.locals():  #136:                 self._irregular_posadv: str = irregular_data[2]
                    __annotations__ = {}  # type: ignore  #136:                 self._irregular_posadv: str = irregular_data[2]
                __annotations__["self._irregular_posadv"] = 'str'  #136:                 self._irregular_posadv: str = irregular_data[2]
                self._irregular_cmpadv = irregular_data[3]  # type: str  #137:                 self._irregular_cmpadv: str = irregular_data[3]
                if "__annotations__" not in _coconut.locals():  #137:                 self._irregular_cmpadv: str = irregular_data[3]
                    __annotations__ = {}  # type: ignore  #137:                 self._irregular_cmpadv: str = irregular_data[3]
                __annotations__["self._irregular_cmpadv"] = 'str'  #137:                 self._irregular_cmpadv: str = irregular_data[3]
                self._irregular_spradv = irregular_data[4]  # type: str  #138:                 self._irregular_spradv: str = irregular_data[4]
                if "__annotations__" not in _coconut.locals():  #138:                 self._irregular_spradv: str = irregular_data[4]
                    __annotations__ = {}  # type: ignore  #138:                 self._irregular_spradv: str = irregular_data[4]
                __annotations__["self._irregular_spradv"] = 'str'  #138:                 self._irregular_spradv: str = irregular_data[4]
            else:  #139:             else:
                self.adverb_flag = False  #140:                 self.adverb_flag = False

        _coconut_case_match_to_1 = self.declension  #142:         match self.declension:
        _coconut_case_match_check_1 = False  #142:         match self.declension:
        if _coconut_case_match_to_1 == "212":  #142:         match self.declension:
            _coconut_case_match_check_1 = True  #142:         match self.declension:
        if _coconut_case_match_check_1:  #142:         match self.declension:
            self.endings = self._212_endings()  #144:                 self.endings = self._212_endings()

        if not _coconut_case_match_check_1:  #146:             case "3":
            if _coconut_case_match_to_1 == "3":  #146:             case "3":
                _coconut_case_match_check_1 = True  #146:             case "3":
            if _coconut_case_match_check_1:  #146:             case "3":
                _coconut_case_match_to_0 = self.termination  #146:             case "3":
                _coconut_case_match_check_0 = False  #146:             case "3":
                if _coconut_case_match_to_0 == 1:  #146:             case "3":
                    _coconut_case_match_check_0 = True  #146:             case "3":
                if _coconut_case_match_check_0:  #146:             case "3":
                    self.endings = self._31_endings()  #149:                         self.endings = self._31_endings()

                if not _coconut_case_match_check_0:  #151:                     case 2:
                    if _coconut_case_match_to_0 == 2:  #151:                     case 2:
                        _coconut_case_match_check_0 = True  #151:                     case 2:
                    if _coconut_case_match_check_0:  #151:                     case 2:
                        self.endings = self._32_endings()  #152:                         self.endings = self._32_endings()

                if not _coconut_case_match_check_0:  #154:                     case 3:
                    if _coconut_case_match_to_0 == 3:  #154:                     case 3:
                        _coconut_case_match_check_0 = True  #154:                     case 3:
                    if _coconut_case_match_check_0:  #154:                     case 3:
                        self.endings = self._33_endings()  #155:                         self.endings = self._33_endings()

                if not _coconut_case_match_check_0:  #157:                     case _:
                    _coconut_case_match_check_0 = True  #157:                     case _:
                    if _coconut_case_match_check_0:  #157:                     case _:
                        raise InvalidInputError("Termination must be 1, 2 or 3 " + "(given '{_coconut_format_0}')".format(_coconut_format_0=(self.termination)))  #158:                         raise InvalidInputError(

        if not _coconut_case_match_check_1:  #163:             case _:
            _coconut_case_match_check_1 = True  #163:             case _:
            if _coconut_case_match_check_1:  #163:             case _:
                raise InvalidInputError("Invalid declension: '{_coconut_format_0}'".format(_coconut_format_0=(self.declension)))  #164:                 raise InvalidInputError(


    def _212_endings(self):  #168:     def _212_endings(self) -> Endings:
# type: (...) -> Endings
        if self.termination:  #169:         if self.termination:
            raise InvalidInputError("2-1-2 adjectives cannot have a termination " + "(termination '{_coconut_format_0}' given)".format(_coconut_format_0=(self.termination)))  #170:             raise InvalidInputError(

        if len(self._principal_parts) != 3:  #175:         if len(self._principal_parts) != 3:
            raise InvalidInputError("2-1-2 adjectives must have 3 principal parts " + "(adjective '{_coconut_format_0}' given)".format(_coconut_format_0=(self._first)))  #176:             raise InvalidInputError(

        self._femnom = self._principal_parts[1]  #181:         self._femnom = self._principal_parts[1]
        self._neutnom = self._principal_parts[2]  #182:         self._neutnom = self._principal_parts[2]

        self._pos_stem = self._femnom[:-1]  # cara -> car-  #184:         self._pos_stem = self._femnom[:-1]  # cara -> car-

        if self._mascnom not in IRREGULAR_ADJECTIVES:  #186:         if self._mascnom not in IRREGULAR_ADJECTIVES:
            self._cmp_stem = "{_coconut_format_0}ior".format(_coconut_format_0=(self._pos_stem))  # car- -> carior-  #187:             self._cmp_stem = f"{self._pos_stem}ior"  # car- -> carior-
            if self._mascnom.endswith("er"):  # pragma: no cover  #188:             if self._mascnom.endswith(
                self._spr_stem = "{_coconut_format_0}rim".format(_coconut_format_0=(self._mascnom))  # miser- -> miserrim-  #191:                 self._spr_stem = f"{self._mascnom}rim"  # miser- -> miserrim-
            elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover  #192:             elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                self._spr_stem = "{_coconut_format_0}lim".format(_coconut_format_0=(self._pos_stem))  # facil- -> facillim-  #193:                 self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:  #194:             else:
                self._spr_stem = "{_coconut_format_0}issim".format(_coconut_format_0=(self._pos_stem))  # car- -> carissim-  #195:                 self._spr_stem = f"{self._pos_stem}issim"  # car- -> carissim-

        endings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Endings  #197:         endings: Endings
        if "__annotations__" not in _coconut.locals():  #197:         endings: Endings
            __annotations__ = {}  # type: ignore  #197:         endings: Endings
        __annotations__["endings"] = 'Endings'  #197:         endings: Endings
        endings = _coconut.dict((("Aposmnomsg", self._mascnom), ("Aposmvocsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._pos_stem))), ("Aposmaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._pos_stem))), ("Aposmgensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._pos_stem))), ("Aposmablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._pos_stem))), ("Aposmnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmaccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._pos_stem))), ("Aposmgenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposmablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposfnomsg", self._femnom), ("Aposfvocsg", self._femnom), ("Aposfaccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._pos_stem))), ("Aposfgensg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._pos_stem))), ("Aposfablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._pos_stem))), ("Aposfnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._pos_stem))), ("Aposfvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._pos_stem))), ("Aposfaccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._pos_stem))), ("Aposfgenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposfablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposnnomsg", self._neutnom), ("Aposnvocsg", self._neutnom), ("Aposnaccsg", self._neutnom), ("Aposngensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._pos_stem))), ("Aposnablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._pos_stem))), ("Aposnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._pos_stem))), ("Aposnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._pos_stem))), ("Aposnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._pos_stem))), ("Aposngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._pos_stem))), ("Aposndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposnablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Acmpmnomsg", self._cmp_stem), ("Acmpmvocsg", self._cmp_stem), ("Acmpmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnomsg", self._cmp_stem), ("Acmpfvocsg", self._cmp_stem), ("Acmpfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnomsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnvocsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnaccsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpngensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpngenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Asprmnomsg", "{_coconut_format_0}us".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprmgensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._spr_stem))), ("Asprmgenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprmablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfnomsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._spr_stem))), ("Asprfgensg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._spr_stem))), ("Asprfgenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnnomsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprngensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem)))))  # carioribus  # caro  # caras  # carae  # carum  # carrissimus  # cariore  # carrissimi  # carius  # caris  # carrissimo  # cariores  # caro  # carrissimum  # carum  # carrissima  # caris  # carrissima  # carorum  # cariorum  # caro  # cariori  # carrissimas  # cara  # carorum  # cari  # cari  # carior  # cara  # carrissimo  # caris  # carrissimum  # carae  # carrissimi  # caro  # cariorem  # carrissimis  # cariori  # carrissimos  # cariora  # cariores  # caram  # cariorum  # carrissimis  # carrissima  # carius  # cariori  # care  # cariora  # cariores  # cariores  # cariores  # carrissima  # carioris  # cari  # carioribus  # crrissimae  # caris  # cararum  # cara  # carrissimi  # cara  # cariore  # carior  # cariorum  # cara  # carae  # cariorem  # carrissima  # carrissimo  # caris  # carrissimis  # carum  # carrissimae  # caros  # carioris  # carrissimis  # carrissimorum  # carrissimarum  # carior  # carioribus  # carius  # carus  # carrissimorum  # carrissimum  # carrissime  # cariora  # cara  # carae  # carrissimis  # caris  # carrissimae  # cari  # carum  # carrissimum  # carioribus  # cariores  # carior  # carrissimo  # carioribus  # carrissimis  # carrissimae  # carioribus  # carrissimi  # carrissima  # carioris  # cariore  # carrissimam  #198:         endings = {

        if self.adverb_flag:  #309:         if self.adverb_flag:
            endings |= _coconut.dict((("Dpos", (self._irregular_posadv if self.irregular_flag else "{_coconut_format_0}e".format(_coconut_format_0=(self._pos_stem)))), ("Dcmp", (self._irregular_cmpadv if self.irregular_flag else "{_coconut_format_0}ius".format(_coconut_format_0=(self._pos_stem)))), ("Dspr", (self._irregular_spradv if self.irregular_flag else "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))))))  # laete  # laetius  # laetissime  #310:             endings |= {

        return endings  #328:         return endings


    def _31_endings(self):  #330:     def _31_endings(self) -> Endings:
# type: (...) -> Endings
        if len(self._principal_parts) != 2:  #331:         if len(self._principal_parts) != 2:
            raise InvalidInputError("First-termination adjectives must have 2 principal parts " + "(adjective '{_coconut_format_0}' given)".format(_coconut_format_0=(self._first)))  #332:             raise InvalidInputError(

        self._mascgen = self._principal_parts[1]  # type: str  #337:         self._mascgen: str = self._principal_parts[1]
        if "__annotations__" not in _coconut.locals():  #337:         self._mascgen: str = self._principal_parts[1]
            __annotations__ = {}  # type: ignore  #337:         self._mascgen: str = self._principal_parts[1]
        __annotations__["self._mascgen"] = 'str'  #337:         self._mascgen: str = self._principal_parts[1]

        if self._mascgen[-2:] != "is":  #339:         if self._mascgen[-2:] != "is":
            raise InvalidInputError("Invalid genitive form: '{_coconut_format_0}' ".format(_coconut_format_0=(self._mascgen)) + "(must end in '-is')")  #340:             raise InvalidInputError(

        self._pos_stem = self._mascgen[:-2]  # ingentis -> ingent-  #345:         self._pos_stem = self._mascgen[:-2]  # ingentis -> ingent-

        if not self.irregular_flag:  #347:         if not self.irregular_flag:
            self._cmp_stem = "{_coconut_format_0}ior".format(_coconut_format_0=(self._pos_stem))  # ingent- > ingentior-  #348:             self._cmp_stem = f"{self._pos_stem}ior"  # ingent- > ingentior-
            if self._mascnom.endswith("er"):  #349:             if self._mascnom.endswith("er"):
                self._spr_stem = "{_coconut_format_0}rim".format(_coconut_format_0=(self._mascnom))  # miser- -> miserrim-  #350:                 self._spr_stem = f"{self._mascnom}rim"  # miser- -> miserrim-
            elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover  #351:             elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                self._spr_stem = "{_coconut_format_0}lim".format(_coconut_format_0=(self._pos_stem))  # facil- -> facillim-  #352:                 self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:  #353:             else:
                self._spr_stem = ("{_coconut_format_0}issim".format(_coconut_format_0=(self._pos_stem)))  # ingent- -> ingentissim-  #354:                 self._spr_stem = (

        endings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Endings  #358:         endings: Endings
        if "__annotations__" not in _coconut.locals():  #358:         endings: Endings
            __annotations__ = {}  # type: ignore  #358:         endings: Endings
        __annotations__["endings"] = 'Endings'  #358:         endings: Endings
        endings = _coconut.dict((("Aposmnomsg", self._mascnom), ("Aposmvocsg", self._mascnom), ("Aposmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._pos_stem))), ("Aposmgensg", self._mascgen), ("Aposmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmgenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposfnomsg", self._mascnom), ("Aposfvocsg", self._mascnom), ("Aposfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._pos_stem))), ("Aposfgensg", self._mascgen), ("Aposfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposfablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfgenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposnnomsg", self._mascnom), ("Aposnvocsg", self._mascnom), ("Aposnaccsg", self._mascnom), ("Aposngensg", self._mascgen), ("Aposndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposnablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposnnompl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposnvocpl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposnaccpl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposngenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Acmpmnomsg", self._cmp_stem), ("Acmpmvocsg", self._cmp_stem), ("Acmpmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnomsg", self._cmp_stem), ("Acmpfvocsg", self._cmp_stem), ("Acmpfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnomsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnvocsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnaccsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpngensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpngenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Asprmnomsg", "{_coconut_format_0}us".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprmgensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._spr_stem))), ("Asprmgenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprmablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfnomsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._spr_stem))), ("Asprfgensg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._spr_stem))), ("Asprfgenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnnomsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprngensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem)))))  # ingentiore  # ingentium  # ingens  # ingentius  # ingentissimis  # ingentiori  # ingentiore  # ingentes  # ingentissimi  # ingens  # ingentiores  # ingentissima  # ingentiorem  # ingentibus  # ingentem  # ingentissima  # ingentiore  # ingentissimorum  # ingens  # ingentissimae  # ingentioris  # ingentibus  # ingentioribus  # ingens  # ingentium  # ingentior  # ingentissimas  # ingens  # ingentem  # ingentibus  # ingentes  # ingentissima  # ingentissima  # ingentiori  # ingentissimis  # ingentes  # ingentior  # ingentis  # ingentiora  # ingentissimam  # ingentiores  # ingentioribus  # ingenti  # ingenti  # ingentius  # ingentiores  # ingentibus  # ingentiora  # ingentes  # ingentissimae  # ingentissimis  # ingentissima  # ingentioris  # ingenti  # ingentia  # ingentiorum  # ingentissimis  # ingentioribus  # ingentissimo  # ingentiora  # ingentioribus  # ingentissimo  # ingentissima  # ingentissimorum  # ingenti  # ingentissimo  # ingentiori  # ingentes  # ingentissimum  # ingentioris  # ingentissimus  # ingens  # ingentissimarum  # ingentius  # ingentissimum  # ingentiorem  # ingentia  # ingentissimos  # ingentes  # ingentissimo  # ingentissime  # ingentibus  # ingentissimi  # ingentior  # ingentioribus  # ingentissimi  # ingentissimum  # ingentium  # ingentis  # ingens  # ingentibus  # ingenti  # ingentiores  # ingentissimum  # ingentis  # ingentiores  # ingentissimi  # ingentia  # ingentiorum  # ingentissimis  # ingentissimae  # ingentiores  # ingentior  # ingenti  # ingentissimis  # ingentissimae  # ingentiorum  # ingentioribus  #359:         endings = {

        if self.adverb_flag:  #470:         if self.adverb_flag:
            endings |= _coconut.dict((("Dpos", (self._irregular_posadv if self.irregular_flag else "{_coconut_format_0}er".format(_coconut_format_0=(self._pos_stem)))), ("Dcmp", (self._irregular_cmpadv if self.irregular_flag else "{_coconut_format_0}ius".format(_coconut_format_0=(self._pos_stem)))), ("Dspr", (self._irregular_spradv if self.irregular_flag else "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))))))  # atrocius  # atrociter  # atrocissime  #471:             endings |= {

        return endings  #489:         return endings


    def _32_endings(self):  #491:     def _32_endings(self) -> Endings:
# type: (...) -> Endings
        if len(self._principal_parts) != 2:  #492:         if len(self._principal_parts) != 2:
            raise InvalidInputError("Second-termination adjectives must have 2 principal parts " + "(adjective '{_coconut_format_0}' given)".format(_coconut_format_0=(self._first)))  #493:             raise InvalidInputError(

        self._neutnom = self._principal_parts[1]  #498:         self._neutnom = self._principal_parts[1]

        self._pos_stem = self._mascnom[:-2]  # fortis -> fort-  #500:         self._pos_stem = self._mascnom[:-2]  # fortis -> fort-
        if not self.irregular_flag:  #501:         if not self.irregular_flag:
            self._cmp_stem = "{_coconut_format_0}ior".format(_coconut_format_0=(self._pos_stem))  # fort- -> fortior-  #502:             self._cmp_stem = f"{self._pos_stem}ior"  # fort- -> fortior-
            if self._mascnom[-2:] == "er":  # pragma: no cover  #503:             if self._mascnom[-2:] == "er":  # pragma: no cover
                self._spr_stem = "{_coconut_format_0}rim".format(_coconut_format_0=(self._mascnom))  # miser- -> miserrim-  #504:                 self._spr_stem = f"{self._mascnom}rim"  # miser- -> miserrim-
            elif self._mascnom in LIS_ADJECTIVES:  #505:             elif self._mascnom in LIS_ADJECTIVES:
                self._spr_stem = "{_coconut_format_0}lim".format(_coconut_format_0=(self._pos_stem))  # facil- -> facillim-  #506:                 self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:  #507:             else:
                self._spr_stem = ("{_coconut_format_0}issim".format(_coconut_format_0=(self._pos_stem)))  # fort- -> fortissim-  #508:                 self._spr_stem = (

        endings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Endings  #512:         endings: Endings
        if "__annotations__" not in _coconut.locals():  #512:         endings: Endings
            __annotations__ = {}  # type: ignore  #512:         endings: Endings
        __annotations__["endings"] = 'Endings'  #512:         endings: Endings
        endings = _coconut.dict((("Aposmnomsg", self._mascnom), ("Aposmvocsg", self._mascnom), ("Aposmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._pos_stem))), ("Aposmgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmgenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposfnomsg", self._mascnom), ("Aposfvocsg", self._mascnom), ("Aposfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._pos_stem))), ("Aposfgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposfablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfgenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposnnomsg", self._neutnom), ("Aposnvocsg", self._neutnom), ("Aposnaccsg", self._neutnom), ("Aposngensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposnablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposnnompl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposnvocpl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposnaccpl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposngenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Acmpmnomsg", self._cmp_stem), ("Acmpmvocsg", self._cmp_stem), ("Acmpmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnomsg", self._cmp_stem), ("Acmpfvocsg", self._cmp_stem), ("Acmpfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnomsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnvocsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnaccsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpngensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpngenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Asprmnomsg", "{_coconut_format_0}us".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprmgensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._spr_stem))), ("Asprmgenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprmablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfnomsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._spr_stem))), ("Asprfgensg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._spr_stem))), ("Asprfgenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnnomsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprngensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem)))))  # fortes  # fortior  # fortissima  # fortiora  # fortibus  # fortes  # fortioris  # fortissimum  # forti  # fortes  # fortioribus  # fortiorum  # fortiori  # fortissima  # forti  # fortissimo  # fortibus  # fortem  # fortia  # fortissimas  # fortes  # fortissima  # fortius  # fortissimam  # fortissimis  # fortissimi  # fortissime  # fortis  # fortia  # fortiorem  # fortibus  # fortissimae  # fortioris  # fortissimorum  # fortium  # fortioribus  # fortibus  # fortis  # fortis  # fortissima  # crrissimae  # fortior  # fortibus  # fortiores  # fortissimis  # fortius  # fortiore  # fortius  # fortiorum  # fortissimum  # fortioribus  # forti  # fortissimum  # fortissima  # fortioris  # forte  # forti  # fortis  # fortissimae  # forte  # fortes  # fortem  # fortissimi  # fortiorum  # fortes  # fortia  # fortiora  # fortioribus  # fortior  # fortissimorum  # fortis  # fortissimi  # fortium  # fortiorem  # fortiore  # fortior  # fortissimis  # forte  # fortissimis  # fortiori  # fortissima  # fortissimus  # fortiores  # fortissimo  # fortiores  # fortiores  # fortium  # fortiore  # fortissimi  # fortissimum  # fortioribus  # fortis  # fortibus  # fortissimarum  # fortiora  # fortissimae  # fortis  # fortissimis  # fortibus  # fortissimis  # fortioribus  # fortissimo  # fortissimo  # fortiores  # fortiori  # fortibus  # fortissimi  # fortiores  #513:         endings = {

        if self.adverb_flag:  #624:         if self.adverb_flag:
            endings |= _coconut.dict((("Dpos", (self._irregular_posadv if self.irregular_flag else "{_coconut_format_0}iter".format(_coconut_format_0=(self._pos_stem)))), ("Dcmp", (self._irregular_cmpadv if self.irregular_flag else "{_coconut_format_0}ius".format(_coconut_format_0=(self._pos_stem)))), ("Dspr", (self._irregular_spradv if self.irregular_flag else "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))))))  # fortius  # fortissime  # fortiter  #625:             endings |= {

        return endings  #643:         return endings


    def _33_endings(self):  #645:     def _33_endings(self) -> Endings:
# type: (...) -> Endings
        if len(self._principal_parts) != 3:  #646:         if len(self._principal_parts) != 3:
            raise InvalidInputError("Third-termination adjectives must have 3 principal parts " + "(adjective '{_coconut_format_0}' given)".format(_coconut_format_0=(self._first)))  #647:             raise InvalidInputError(

        self._mascnom = self._principal_parts[0]  #652:         self._mascnom = self._principal_parts[0]
        self._femnom = self._principal_parts[1]  #653:         self._femnom = self._principal_parts[1]
        self._neutnom = self._principal_parts[2]  #654:         self._neutnom = self._principal_parts[2]

        self._pos_stem = self._femnom[:-2]  # acris -> acr-  #656:         self._pos_stem = self._femnom[:-2]  # acris -> acr-
        if not self.irregular_flag:  #657:         if not self.irregular_flag:
            self._cmp_stem = "{_coconut_format_0}ior".format(_coconut_format_0=(self._pos_stem))  # acr- -> acrior-  #658:             self._cmp_stem = f"{self._pos_stem}ior"  # acr- -> acrior-
            if self._mascnom[-2:] == "er":  #659:             if self._mascnom[-2:] == "er":
                self._spr_stem = "{_coconut_format_0}rim".format(_coconut_format_0=(self._mascnom))  # cer- -> acerrim-  #660:                 self._spr_stem = f"{self._mascnom}rim"  # cer- -> acerrim-
            elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover  #661:             elif self._mascnom in LIS_ADJECTIVES:  # pragma: no cover
                self._spr_stem = "{_coconut_format_0}lim".format(_coconut_format_0=(self._pos_stem))  # facil- -> facillim-  #662:                 self._spr_stem = f"{self._pos_stem}lim"  # facil- -> facillim-
            else:  # pragma: no cover  #663:             else:  # pragma: no cover
                self._spr_stem = "{_coconut_format_0}issim".format(_coconut_format_0=(self._pos_stem))  # levis -> levissim-  #664:                 self._spr_stem = f"{self._pos_stem}issim"  # levis -> levissim-

        endings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Endings  #666:         endings: Endings
        if "__annotations__" not in _coconut.locals():  #666:         endings: Endings
            __annotations__ = {}  # type: ignore  #666:         endings: Endings
        __annotations__["endings"] = 'Endings'  #666:         endings: Endings
        endings = _coconut.dict((("Aposmnomsg", self._mascnom), ("Aposmvocsg", self._mascnom), ("Aposmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._pos_stem))), ("Aposmgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposmgenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposfnomsg", self._femnom), ("Aposfvocsg", self._femnom), ("Aposfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._pos_stem))), ("Aposfgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposfablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._pos_stem))), ("Aposfgenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposnnomsg", self._neutnom), ("Aposnvocsg", self._neutnom), ("Aposnaccsg", self._neutnom), ("Aposngensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._pos_stem))), ("Aposndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposnablsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._pos_stem))), ("Aposnnompl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposnvocpl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposnaccpl", "{_coconut_format_0}ia".format(_coconut_format_0=(self._pos_stem))), ("Aposngenpl", "{_coconut_format_0}ium".format(_coconut_format_0=(self._pos_stem))), ("Aposndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Aposnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._pos_stem))), ("Acmpmnomsg", self._cmp_stem), ("Acmpmvocsg", self._cmp_stem), ("Acmpmaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpmablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnomsg", self._cmp_stem), ("Acmpfvocsg", self._cmp_stem), ("Acmpfaccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfaccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfgenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfdatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpfablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnomsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnvocsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpnaccsg", "{_coconut_format_0}ius".format(_coconut_format_0=(self._cmp_stem[:-3]))), ("Acmpngensg", "{_coconut_format_0}is".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._cmp_stem))), ("Acmpngenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._cmp_stem))), ("Acmpndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Acmpnablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._cmp_stem))), ("Asprmnomsg", "{_coconut_format_0}us".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprmgensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprmnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprmaccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._spr_stem))), ("Asprmgenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprmdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprmablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfnomsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._spr_stem))), ("Asprfgensg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprfnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._spr_stem))), ("Asprfaccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._spr_stem))), ("Asprfgenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._spr_stem))), ("Asprfdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprfablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnnomsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._spr_stem))), ("Asprngensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._spr_stem))), ("Asprndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._spr_stem))), ("Asprnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._spr_stem))), ("Asprngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._spr_stem))), ("Asprndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem))), ("Asprnablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._spr_stem)))))  # acria  # acriorum  # acrior  # acrioribus  # acriorem  # acerrimus  # acriores  # acre  # acrioribus  # acerrimi  # acri  # acribus  # acerrimo  # acerrima  # acrium  # acriorem  # acriores  # acribus  # acerrimorum  # acrium  # acrioribus  # acrioribus  # acriori  # acrior  # acris  # acerrimarum  # acres  # acer  # acris  # acrium  # acerrima  # acribus  # acerrima  # acriores  # acerrimis  # acris  # acriorum  # acres  # acerrimo  # acri  # acriore  # acribus  # acriore  # acriore  # acerrimo  # acerrimum  # acrior  # acriori  # acerrimi  # acrius  # acri  # acri  # acerrimis  # acris  # acrioris  # acerrimis  # acri  # acriorum  # acerrimum  # acriora  # acerrimi  # acria  # acerrimorum  # acriores  # acer  # acrioris  # acrius  # acre  # acrioribus  # acre  # acres  # acerrima  # acrem  # acriores  # acerrimis  # acerrima  # acria  # acerrimae  # acerrime  # acrioribus  # acriora  # acerrima  # acribus  # acrem  # acerrimum  # acribus  # acrioris  # acriori  # acerrimae  # acerrimis  # acerrimae  # acres  # acerrimi  # acerrimum  # acerrimo  # acres  # crrissimae  # acerrimos  # acrius  # acerrimis  # acris  # acres  # acri  # acerrimas  # acriores  # acerrimam  # acrior  # acriora  #667:         endings = {

        if self.adverb_flag:  #778:         if self.adverb_flag:
            endings |= _coconut.dict((("Dpos", (self._irregular_posadv if self.irregular_flag else "{_coconut_format_0}iter".format(_coconut_format_0=(self._pos_stem)))), ("Dcmp", (self._irregular_cmpadv if self.irregular_flag else "{_coconut_format_0}ius".format(_coconut_format_0=(self._pos_stem)))), ("Dspr", (self._irregular_spradv if self.irregular_flag else "{_coconut_format_0}e".format(_coconut_format_0=(self._spr_stem))))))  # acerrime  # acriter  # acrius  #779:             endings |= {

        return endings  #797:         return endings


    @_coconut_tco  #799:     def get(
    def get(self, degree,  # type: str  #799:     def get(
        gender=None,  # type: _coconut.typing.Union[str, None]  #799:     def get(
        case=None,  # type: _coconut.typing.Union[str, None]  #799:     def get(
        number=None,  # type: _coconut.typing.Union[str, None]  #799:     def get(
        adverb=False,  # type: bool  #799:     def get(
        ):  #799:     def get(
# type: (...) -> _coconut.typing.Union[Ending, None]
        """Returns the ending of the adjective.

        The function returns None if no ending is found.

        Parameters
        ----------
        degree : str
        gender, case, number : Optional[str], default = None
            The gender, case and number of the ending, if applicable (not
            an adverb).
        adverb : bool, default = False
            Whether the queried ending is an adverb or not.

        Returns
        -------
        Ending
            The ending found.
        None
            If no ending is found.

        Raises
        ------
        InvalidInputError
            If the input is invalid.

        Examples
        --------
        >>> foo = Adjective(
        ...     "egens", "egentis", termination=1, declension="3", meaning="poor"
        ... )
        >>> foo.get(
        ...     degree="positive",
        ...     gender="masculine",
        ...     case="nominative",
        ...     number="singular",
        ... )
        'egens'

        Note that the arguments of get are keyword-only.
        """  # noqa: E501  #846:         """  # noqa: E501
        short_degree = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #847:         short_degree: str
        if "__annotations__" not in _coconut.locals():  #847:         short_degree: str
            __annotations__ = {}  # type: ignore  #847:         short_degree: str
        __annotations__["short_degree"] = 'str'  #847:         short_degree: str

        if adverb:  #849:         if adverb:
            if gender or case or number:  #850:             if gender or case or number:
                raise InvalidInputError("Adverbs do not have gender, case or number " + "(given '{_coconut_format_0}', '{_coconut_format_1}' and '{_coconut_format_2}')".format(_coconut_format_0=(gender), _coconut_format_1=(case), _coconut_format_2=(number)))  #851:                 raise InvalidInputError(
            try:  #855:             try:
                short_degree = DEGREE_SHORTHAND[degree]  #856:                 short_degree = DEGREE_SHORTHAND[degree]
            except KeyError as e:  #857:             except KeyError as e:
                _coconut_raise_from_0 = InvalidInputError("Invalid degree: '{_coconut_format_0}'".format(_coconut_format_0=(degree)))  #858:                 raise InvalidInputError(f"Invalid degree: '{degree}'") from e
                _coconut_raise_from_0.__cause__ = e  #858:                 raise InvalidInputError(f"Invalid degree: '{degree}'") from e
                raise _coconut_raise_from_0  #858:                 raise InvalidInputError(f"Invalid degree: '{degree}'") from e

            return _coconut_tail_call(self.endings.get, "D{_coconut_format_0}".format(_coconut_format_0=(short_degree)))  #860:             return self.endings.get(f"D{short_degree}")

        if gender not in GENDER_SHORTHAND:  #862:         if gender not in GENDER_SHORTHAND:
            raise InvalidInputError("Invalid gender: '{_coconut_format_0}'".format(_coconut_format_0=(gender)))  #863:             raise InvalidInputError(f"Invalid gender: '{gender}'")

        if case not in CASE_SHORTHAND:  #865:         if case not in CASE_SHORTHAND:
            raise InvalidInputError("Invalid case: '{_coconut_format_0}'".format(_coconut_format_0=(case)))  #866:             raise InvalidInputError(f"Invalid case: '{case}'")

        if number not in NUMBER_SHORTHAND:  #868:         if number not in NUMBER_SHORTHAND:
            raise InvalidInputError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(number)))  #869:             raise InvalidInputError(f"Invalid number: '{number}'")

        if degree not in DEGREE_SHORTHAND:  #871:         if degree not in DEGREE_SHORTHAND:
            raise InvalidInputError("Invalid degree: '{_coconut_format_0}'".format(_coconut_format_0=(degree)))  #872:             raise InvalidInputError(f"Invalid degree: '{degree}'")

        short_degree = DEGREE_SHORTHAND[degree]  #874:         short_degree = DEGREE_SHORTHAND[degree]
        short_gender = GENDER_SHORTHAND[gender]  # type: str  #875:         short_gender: str = GENDER_SHORTHAND[gender]
        if "__annotations__" not in _coconut.locals():  #875:         short_gender: str = GENDER_SHORTHAND[gender]
            __annotations__ = {}  # type: ignore  #875:         short_gender: str = GENDER_SHORTHAND[gender]
        __annotations__["short_gender"] = 'str'  #875:         short_gender: str = GENDER_SHORTHAND[gender]
        short_case = CASE_SHORTHAND[case]  # type: str  #876:         short_case: str = CASE_SHORTHAND[case]
        if "__annotations__" not in _coconut.locals():  #876:         short_case: str = CASE_SHORTHAND[case]
            __annotations__ = {}  # type: ignore  #876:         short_case: str = CASE_SHORTHAND[case]
        __annotations__["short_case"] = 'str'  #876:         short_case: str = CASE_SHORTHAND[case]
        short_number = NUMBER_SHORTHAND[number]  # type: str  #877:         short_number: str = NUMBER_SHORTHAND[number]
        if "__annotations__" not in _coconut.locals():  #877:         short_number: str = NUMBER_SHORTHAND[number]
            __annotations__ = {}  # type: ignore  #877:         short_number: str = NUMBER_SHORTHAND[number]
        __annotations__["short_number"] = 'str'  #877:         short_number: str = NUMBER_SHORTHAND[number]

        return _coconut_tail_call(self.endings.get, "A{_coconut_format_0}{_coconut_format_1}{_coconut_format_2}{_coconut_format_3}".format(_coconut_format_0=(short_degree), _coconut_format_1=(short_gender), _coconut_format_2=(short_case), _coconut_format_3=(short_number)))  #879:         return self.endings.get(


    @staticmethod  #883:     @staticmethod
    def _create_namespace(key  # type: str  #884:     def _create_namespace(key: str) -> EndingComponents:
        ):  #884:     def _create_namespace(key: str) -> EndingComponents:
# type: (...) -> EndingComponents
        output = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: EndingComponents  #885:         output: EndingComponents
        if "__annotations__" not in _coconut.locals():  #885:         output: EndingComponents
            __annotations__ = {}  # type: ignore  #885:         output: EndingComponents
        __annotations__["output"] = 'EndingComponents'  #885:         output: EndingComponents

        if key[0] == "A":  #887:         if key[0] == "A":
            output = EndingComponents(degree=key_from_value(DEGREE_SHORTHAND, key[1:4]), gender=key_from_value(GENDER_SHORTHAND, key[4]), case=key_from_value(CASE_SHORTHAND, key[5:8]), number=key_from_value(NUMBER_SHORTHAND, key[8:10]))  #888:             output = EndingComponents(
            output.string = ("{_coconut_format_0} {_coconut_format_1} ".format(_coconut_format_0=(output.degree), _coconut_format_1=(output.case)) + "{_coconut_format_0} {_coconut_format_1}".format(_coconut_format_0=(output.number), _coconut_format_1=(output.gender)))  #894:             output.string = (

        else:  #899:         else:
            output = EndingComponents(degree=key_from_value(DEGREE_SHORTHAND, key[1:4]))  #900:             output = EndingComponents(
            output.string = output.degree  #903:             output.string = output.degree

        return output  #905:         return output


    @_coconut_tco  #907:     def __str__(self) -> str:
    def __str__(self):  #907:     def __str__(self) -> str:
# type: (...) -> str
        if self.declension == "3":  #908:         if self.declension == "3":
            return ("{_coconut_format_0}: {_coconut_format_1}, ".format(_coconut_format_0=(self.meaning), _coconut_format_1=(', '.join(self._principal_parts))) + "({_coconut_format_0}-{_coconut_format_1})".format(_coconut_format_0=(self.declension), _coconut_format_1=(self.termination)))  #909:             return (
        return _coconut_tail_call("{_coconut_format_0}: {_coconut_format_1}, (2-1-2)".format, _coconut_format_0=(self.meaning), _coconut_format_1=(', '.join(self._principal_parts)))  #913:         return f"{self.meaning}: {', '.join(self._principal_parts)}, (2-1-2)"


    def __repr__(self):  #915:     def __repr__(self) -> str:
# type: (...) -> str
        return ("Adjective({_coconut_format_0}, ".format(_coconut_format_0=(', '.join(self._principal_parts))) + "{_coconut_format_0}, {_coconut_format_1}, {_coconut_format_2})".format(_coconut_format_0=(self.termination), _coconut_format_1=(self.declension), _coconut_format_2=(self.meaning)))  #916:         return (


_coconut_call_set_names(Adjective)  #921:         )
