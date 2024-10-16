#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf3e6eb13

# Compiled with Coconut version 3.1.2

"""Representation of a Latin verb with endings."""

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
try:  #4: from typing import Literal
    _coconut_sys_0 = sys  # type: ignore  #4: from typing import Literal
except _coconut.NameError:  #4: from typing import Literal
    _coconut_sys_0 = _coconut_sentinel  #4: from typing import Literal
sys = _coconut_sys  #4: from typing import Literal
if sys.version_info >= (3, 8):  #4: from typing import Literal
    if _coconut.typing.TYPE_CHECKING:  #4: from typing import Literal
        from typing import Literal  #4: from typing import Literal
    else:  #4: from typing import Literal
        try:  #4: from typing import Literal
            Literal = _coconut.typing.Literal  #4: from typing import Literal
        except _coconut.AttributeError as _coconut_imp_err:  #4: from typing import Literal
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #4: from typing import Literal
else:  #4: from typing import Literal
    from typing_extensions import Literal  #4: from typing import Literal
if _coconut_sys_0 is not _coconut_sentinel:  #4: from typing import Literal
    sys = _coconut_sys_0  #4: from typing import Literal

from ..utils import key_from_value  #6: from ..utils import key_from_value
from .class_word import _Word  #7: from .class_word import _Word
from .edge_cases import check_io_verb  #8: from .edge_cases import check_io_verb, find_irregular_endings
from .edge_cases import find_irregular_endings  #8: from .edge_cases import check_io_verb, find_irregular_endings
from .exceptions import InvalidInputError  #9: from .exceptions import InvalidInputError
from .misc import CASE_SHORTHAND  #10: from .misc import (
from .misc import GENDER_SHORTHAND  #10: from .misc import (
from .misc import MOOD_SHORTHAND  #10: from .misc import (
from .misc import NUMBER_SHORTHAND  #10: from .misc import (
from .misc import PERSON_SHORTHAND  #10: from .misc import (
from .misc import TENSE_SHORTHAND  #10: from .misc import (
from .misc import VOICE_SHORTHAND  #10: from .misc import (
from .misc import EndingComponents  #10: from .misc import (

if TYPE_CHECKING:  #21: if TYPE_CHECKING:
    from .type_aliases import Ending  #22:     from .type_aliases import Ending, Endings, Meaning
    from .type_aliases import Endings  #22:     from .type_aliases import Ending, Endings, Meaning
    from .type_aliases import Meaning  #22:     from .type_aliases import Ending, Endings, Meaning


@total_ordering  #25: @total_ordering
class Verb(_Word):  #26: class Verb(_Word):
    """Representation of a Latin verb with endings.

    Attributes
    ----------
    present, infinitive, perfect : str
    ppp : str
        The present perfect participle form of the verb. If the verb does
        not have participle endings, ppp is an empty string.
    meaning : Meaning
    conjugation : {0, 1, 2, 3, 4, 5}
        The conjugation of the verb. The value 5 represents the third
        declension -io verbs, and the value 0 represents an irregular
        conjugation.
    endings : Endings

    Examples
    --------
    >>> foo = Verb(
    ...     present="celo",
    ...     infinitive="celare",
    ...     perfect="celavi",
    ...     ppp="celatus",
    ...     meaning="hide",
    ... )
    >>> foo["Vpreactindsg1"]
    'celo'

    Note that all arguments of Verb are keyword-only.
    """  #55:     """

# HACK: Extra optional stuff to avoid syntax errors
    def __init__(self, present,  # type: str  #58:     def __init__(
        infinitive,  # type: str  #58:     def __init__(
        perfect,  # type: str  #58:     def __init__(
        ppp="",  # type: str  #58:     def __init__(
        meaning=None,  # type: _coconut.typing.Union[Meaning, None]  #58:     def __init__(
        ):  #58:     def __init__(
# type: (...) -> None
        """Initalises Verb and determines the conjugation and endings.

        Parameters
        ----------
        present, infinitive, perfect : str
        ppp : str, default = ""
            The ppp ending of the verb. If the verb does not have
            participle endings, ppp is an empty string.
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the input is invalid (incorrect perfect or infinitive).
        """  #80:         """
        __class__ = Verb  #81:         super().__init__()

        super().__init__()  #81:         super().__init__()

        self.present = present  # type: str  #83:         self.present: str = present
        if "__annotations__" not in _coconut.locals():  #83:         self.present: str = present
            __annotations__ = {}  # type: ignore  #83:         self.present: str = present
        __annotations__["self.present"] = 'str'  #83:         self.present: str = present
        self.infinitive = infinitive  # type: str  #84:         self.infinitive: str = infinitive
        if "__annotations__" not in _coconut.locals():  #84:         self.infinitive: str = infinitive
            __annotations__ = {}  # type: ignore  #84:         self.infinitive: str = infinitive
        __annotations__["self.infinitive"] = 'str'  #84:         self.infinitive: str = infinitive
        self.perfect = perfect  # type: str  #85:         self.perfect: str = perfect
        if "__annotations__" not in _coconut.locals():  #85:         self.perfect: str = perfect
            __annotations__ = {}  # type: ignore  #85:         self.perfect: str = perfect
        __annotations__["self.perfect"] = 'str'  #85:         self.perfect: str = perfect
        self.ppp = ppp  # type: str  #86:         self.ppp: str = ppp
        if "__annotations__" not in _coconut.locals():  #86:         self.ppp: str = ppp
            __annotations__ = {}  # type: ignore  #86:         self.ppp: str = ppp
        __annotations__["self.ppp"] = 'str'  #86:         self.ppp: str = ppp
        if meaning:  #87:         if meaning:
            self.meaning = meaning  # type: Meaning  #88:             self.meaning: Meaning = meaning
            if "__annotations__" not in _coconut.locals():  #88:             self.meaning: Meaning = meaning
                __annotations__ = {}  # type: ignore  #88:             self.meaning: Meaning = meaning
            __annotations__["self.meaning"] = 'Meaning'  #88:             self.meaning: Meaning = meaning
        else:  #89:         else:
            raise ValueError  #90:             raise ValueError

        self._first = self.present  #92:         self._first = self.present
        self.conjugation = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Literal[0, 1, 2, 3, 4, 5]  #93:         self.conjugation: Literal[0, 1, 2, 3, 4, 5]
        if "__annotations__" not in _coconut.locals():  #93:         self.conjugation: Literal[0, 1, 2, 3, 4, 5]
            __annotations__ = {}  # type: ignore  #93:         self.conjugation: Literal[0, 1, 2, 3, 4, 5]
        __annotations__["self.conjugation"] = 'Literal[0, 1, 2, 3, 4, 5]'  #93:         self.conjugation: Literal[0, 1, 2, 3, 4, 5]

        if self.present[-1:] != "o":  #95:         if self.present[-1:] != "o":
            raise InvalidInputError("Invalid present form: '{_coconut_format_0}' (must end in '-o')".format(_coconut_format_0=(self.present)))  #96:             raise InvalidInputError(

        if self.perfect[-1:] != "i":  #100:         if self.perfect[-1:] != "i":
            raise InvalidInputError("Invalid perfect form: '{_coconut_format_0}' (must end in '-i')".format(_coconut_format_0=(self.perfect)))  #101:             raise InvalidInputError(

# Conjugation edge cases
        irregular_endings = find_irregular_endings(self.present)  # type: _coconut.typing.Union[Endings, None]  #106:         irregular_endings: Endings | None = find_irregular_endings(
        if "__annotations__" not in _coconut.locals():  #106:         irregular_endings: Endings | None = find_irregular_endings(
            __annotations__ = {}  # type: ignore  #106:         irregular_endings: Endings | None = find_irregular_endings(
        __annotations__["irregular_endings"] = '_coconut.typing.Union[Endings, None]'  #106:         irregular_endings: Endings | None = find_irregular_endings(
        if irregular_endings:  #109:         if irregular_endings:
            self.endings = irregular_endings  #110:             self.endings = irregular_endings
            self.conjugation = 0  #111:             self.conjugation = 0
            return  #112:             return
        if check_io_verb(self.present):  #113:         if check_io_verb(self.present):
            self.conjugation = 5  #114:             self.conjugation = 5

        elif self.infinitive.endswith("are"):  #116:         elif self.infinitive.endswith("are"):
            self.conjugation = 1  #117:             self.conjugation = 1
        elif self.infinitive.endswith("ire"):  #118:         elif self.infinitive.endswith("ire"):
            self.conjugation = 4  #119:             self.conjugation = 4
        elif self.infinitive.endswith("ere"):  #120:         elif self.infinitive.endswith("ere"):
            self.conjugation = 2 if self.present.endswith("eo") else 3  #121:             self.conjugation = 2 if self.present.endswith("eo") else 3
        else:  #122:         else:
            raise InvalidInputError("Invalid infinitive form: '{_coconut_format_0}'".format(_coconut_format_0=(self.infinitive)))  #123:             raise InvalidInputError(

        self._pre_stem = self.present[:-1]  # type: str  #127:         self._pre_stem: str = self.present[:-1]
        if "__annotations__" not in _coconut.locals():  #127:         self._pre_stem: str = self.present[:-1]
            __annotations__ = {}  # type: ignore  #127:         self._pre_stem: str = self.present[:-1]
        __annotations__["self._pre_stem"] = 'str'  #127:         self._pre_stem: str = self.present[:-1]
        self._inf_stem = self.infinitive[:-3]  # type: str  #128:         self._inf_stem: str = self.infinitive[:-3]
        if "__annotations__" not in _coconut.locals():  #128:         self._inf_stem: str = self.infinitive[:-3]
            __annotations__ = {}  # type: ignore  #128:         self._inf_stem: str = self.infinitive[:-3]
        __annotations__["self._inf_stem"] = 'str'  #128:         self._inf_stem: str = self.infinitive[:-3]
        self._per_stem = self.perfect[:-1]  # type: str  #129:         self._per_stem: str = self.perfect[:-1]
        if "__annotations__" not in _coconut.locals():  #129:         self._per_stem: str = self.perfect[:-1]
            __annotations__ = {}  # type: ignore  #129:         self._per_stem: str = self.perfect[:-1]
        __annotations__["self._per_stem"] = 'str'  #129:         self._per_stem: str = self.perfect[:-1]

        _coconut_case_match_to_0 = self.conjugation  #131:         match self.conjugation:
        _coconut_case_match_check_0 = False  #131:         match self.conjugation:
        if _coconut_case_match_to_0 == 1:  #131:         match self.conjugation:
            _coconut_case_match_check_0 = True  #131:         match self.conjugation:
        if _coconut_case_match_check_0:  #131:         match self.conjugation:
            self.endings = self._first_conjugation()  #133:                 self.endings = self._first_conjugation()

        if not _coconut_case_match_check_0:  #135:             case 2:
            if _coconut_case_match_to_0 == 2:  #135:             case 2:
                _coconut_case_match_check_0 = True  #135:             case 2:
            if _coconut_case_match_check_0:  #135:             case 2:
                self.endings = self._second_conjugation()  #136:                 self.endings = self._second_conjugation()

        if not _coconut_case_match_check_0:  #138:             case 3:
            if _coconut_case_match_to_0 == 3:  #138:             case 3:
                _coconut_case_match_check_0 = True  #138:             case 3:
            if _coconut_case_match_check_0:  #138:             case 3:
                self.endings = self._third_conjugation()  #139:                 self.endings = self._third_conjugation()

        if not _coconut_case_match_check_0:  #141:             case 4:
            if _coconut_case_match_to_0 == 4:  #141:             case 4:
                _coconut_case_match_check_0 = True  #141:             case 4:
            if _coconut_case_match_check_0:  #141:             case 4:
                self.endings = self._fourth_conjugation()  #142:                 self.endings = self._fourth_conjugation()

        if not _coconut_case_match_check_0:  #144:             case 5:
            if _coconut_case_match_to_0 == 5:  #144:             case 5:
                _coconut_case_match_check_0 = True  #144:             case 5:
            if _coconut_case_match_check_0:  #144:             case 5:
                self.endings = self._third_io_conjugation()  #145:                 self.endings = self._third_io_conjugation()

        if not _coconut_case_match_check_0:  # pragma: no cover  #147:             case _:  # pragma: no cover
            _coconut_case_match_check_0 = True  # pragma: no cover  #147:             case _:  # pragma: no cover
            if _coconut_case_match_check_0:  # pragma: no cover  #147:             case _:  # pragma: no cover
                raise ValueError("Conjugation {_coconut_format_0} not recognised".format(_coconut_format_0=(self.conjugation)))  # noqa: DOC501  #148:                 raise ValueError(  # noqa: DOC501

        if self.ppp:  #152:         if self.ppp:
            self.endings |= self._participles()  #153:             self.endings |= self._participles()


    @_coconut_tco  #155:     def _first_conjugation(self) -> Endings:
    def _first_conjugation(self):  #155:     def _first_conjugation(self) -> Endings:
# type: (...) -> Endings
        return _coconut_tail_call(_coconut.dict, (("Vpreactindsg1", self.present), ("Vpreactindsg2", "{_coconut_format_0}as".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindsg3", "{_coconut_format_0}at".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl1", "{_coconut_format_0}amus".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl2", "{_coconut_format_0}atis".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl3", "{_coconut_format_0}ant".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg1", "{_coconut_format_0}abam".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg2", "{_coconut_format_0}abas".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg3", "{_coconut_format_0}abat".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl1", "{_coconut_format_0}abamus".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl2", "{_coconut_format_0}abatis".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl3", "{_coconut_format_0}abant".format(_coconut_format_0=(self._inf_stem))), ("Vperactindsg1", self.perfect), ("Vperactindsg2", "{_coconut_format_0}isti".format(_coconut_format_0=(self._per_stem))), ("Vperactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl2", "{_coconut_format_0}istis".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl3", "{_coconut_format_0}erunt".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg1", "{_coconut_format_0}eram".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg2", "{_coconut_format_0}eras".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg3", "{_coconut_format_0}erat".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl1", "{_coconut_format_0}eramus".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl2", "{_coconut_format_0}eratis".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl3", "{_coconut_format_0}erant".format(_coconut_format_0=(self._per_stem))), ("Vpreactinf   ", self.infinitive), ("Vpreactipesg2", "{_coconut_format_0}a".format(_coconut_format_0=(self._inf_stem))), ("Vpreactipepl2", "{_coconut_format_0}ate".format(_coconut_format_0=(self._inf_stem))), ("Vimpactsbjsg1", "{_coconut_format_0}m".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg2", "{_coconut_format_0}s".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg3", "{_coconut_format_0}t".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl1", "{_coconut_format_0}mus".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl2", "{_coconut_format_0}tis".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl3", "{_coconut_format_0}nt".format(_coconut_format_0=(self.infinitive))), ("Vplpactsbjsg1", "{_coconut_format_0}issem".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg2", "{_coconut_format_0}isses".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg3", "{_coconut_format_0}isset".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl1", "{_coconut_format_0}issemus".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl2", "{_coconut_format_0}issetis".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl3", "{_coconut_format_0}issent".format(_coconut_format_0=(self._per_stem)))))  # portabat  # portare  # portaveram  # portavissem  # portaretis  # portaverant  # portavistis  # portaret  # portaremus  # portas  # portavisti  # portabamus  # portavissemus  # porta  # portaveramus  # portabam  # portavissent  # portaveras  # portaverunt  # portate  # portares  # portatis  # portarem  # portavissetis  # portaveratis  # portavisses  # portavimus  # portat  # portavit  # portaverat  # portabant  # portamus  # portavisset  # portabatis  # portavi  # portabas  # portant  # portarent  # porto  #156:         return {


    @_coconut_tco  #198:     def _second_conjugation(self) -> Endings:
    def _second_conjugation(self):  #198:     def _second_conjugation(self) -> Endings:
# type: (...) -> Endings
        return _coconut_tail_call(_coconut.dict, (("Vpreactindsg1", self.present), ("Vpreactindsg2", "{_coconut_format_0}es".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindsg3", "{_coconut_format_0}et".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl1", "{_coconut_format_0}emus".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl2", "{_coconut_format_0}etis".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl3", "{_coconut_format_0}ent".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg1", "{_coconut_format_0}ebam".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg2", "{_coconut_format_0}ebas".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg3", "{_coconut_format_0}ebat".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl1", "{_coconut_format_0}ebamus".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl2", "{_coconut_format_0}ebatis".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl3", "{_coconut_format_0}ebant".format(_coconut_format_0=(self._inf_stem))), ("Vperactindsg1", self.perfect), ("Vperactindsg2", "{_coconut_format_0}isti".format(_coconut_format_0=(self._per_stem))), ("Vperactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl2", "{_coconut_format_0}istis".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl3", "{_coconut_format_0}erunt".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg1", "{_coconut_format_0}eram".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg2", "{_coconut_format_0}eras".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg3", "{_coconut_format_0}erat".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl1", "{_coconut_format_0}eramus".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl2", "{_coconut_format_0}eratis".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl3", "{_coconut_format_0}erant".format(_coconut_format_0=(self._per_stem))), ("Vpreactinf   ", self.infinitive), ("Vpreactipesg2", "{_coconut_format_0}e".format(_coconut_format_0=(self._inf_stem))), ("Vpreactipepl2", "{_coconut_format_0}ete".format(_coconut_format_0=(self._inf_stem))), ("Vimpactsbjsg1", "{_coconut_format_0}m".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg2", "{_coconut_format_0}s".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg3", "{_coconut_format_0}t".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl1", "{_coconut_format_0}mus".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl2", "{_coconut_format_0}tis".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl3", "{_coconut_format_0}nt".format(_coconut_format_0=(self.infinitive))), ("Vplpactsbjsg1", "{_coconut_format_0}issem".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg2", "{_coconut_format_0}isses".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg3", "{_coconut_format_0}isset".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl1", "{_coconut_format_0}issemus".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl2", "{_coconut_format_0}issetis".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl3", "{_coconut_format_0}issent".format(_coconut_format_0=(self._per_stem)))))  # docere  # doceremus  # docuit  # docueram  # doceo  # docuisses  # docueramus  # doceret  # docuimus  # docebam  # docuisit  # docet  # docetis  # docuerunt  # docuissent  # docuisset  # docui  # docuissetis  # docuerant  # docebamus  # docebant  # docemus  # docuissmus  # docerent  # docuistis  # docuissem  # docebas  # doce  # docete  # doceretis  # docueratis  # docent  # docuerat  # doces  # docerem  # doceres  # docueras  # docebat  # docebatis  #199:         return {


    @_coconut_tco  #241:     def _third_conjugation(self) -> Endings:
    def _third_conjugation(self):  #241:     def _third_conjugation(self) -> Endings:
# type: (...) -> Endings
        return _coconut_tail_call(_coconut.dict, (("Vpreactindsg1", self.present), ("Vpreactindsg2", "{_coconut_format_0}is".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl2", "{_coconut_format_0}itis".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl3", "{_coconut_format_0}unt".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg1", "{_coconut_format_0}ebam".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg2", "{_coconut_format_0}ebas".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg3", "{_coconut_format_0}ebat".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl1", "{_coconut_format_0}ebamus".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl2", "{_coconut_format_0}ebatis".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl3", "{_coconut_format_0}ebant".format(_coconut_format_0=(self._inf_stem))), ("Vperactindsg1", self.perfect), ("Vperactindsg2", "{_coconut_format_0}isti".format(_coconut_format_0=(self._per_stem))), ("Vperactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl2", "{_coconut_format_0}istis".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl3", "{_coconut_format_0}erunt".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg1", "{_coconut_format_0}eram".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg2", "{_coconut_format_0}eras".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg3", "{_coconut_format_0}erat".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl1", "{_coconut_format_0}eramus".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl2", "{_coconut_format_0}eratis".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl3", "{_coconut_format_0}erant".format(_coconut_format_0=(self._per_stem))), ("Vpreactinf   ", self.infinitive), ("Vpreactipesg2", "{_coconut_format_0}e".format(_coconut_format_0=(self._inf_stem))), ("Vpreactipepl2", "{_coconut_format_0}ite".format(_coconut_format_0=(self._inf_stem))), ("Vimpactsbjsg1", "{_coconut_format_0}m".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg2", "{_coconut_format_0}s".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg3", "{_coconut_format_0}t".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl1", "{_coconut_format_0}mus".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl2", "{_coconut_format_0}tis".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl3", "{_coconut_format_0}nt".format(_coconut_format_0=(self.infinitive))), ("Vplpactsbjsg1", "{_coconut_format_0}issem".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg2", "{_coconut_format_0}isses".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg3", "{_coconut_format_0}isset".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl1", "{_coconut_format_0}issemus".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl2", "{_coconut_format_0}issetis".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl3", "{_coconut_format_0}issent".format(_coconut_format_0=(self._per_stem)))))  # trahebat  # trahere  # trahit  # traxeram  # trahis  # trahe  # traho  # traxissem  # traxerant  # trahebatis  # traheret  # traxeratis  # traxissetis  # traheremus  # traximus  # traxisses  # traxisti  # traxit  # traxisset  # traxissemus  # traherem  # trahitis  # trahunt  # trahebam  # trahite  # traheres  # trahebas  # traxistis  # traxerat  # trahebamus  # trahebant  # traxeras  # traxi  # traheretis  # trahimus  # traxerunt  # traxissent  # traherent  # traxeramus  #242:         return {


    @_coconut_tco  #284:     def _fourth_conjugation(self) -> Endings:
    def _fourth_conjugation(self):  #284:     def _fourth_conjugation(self) -> Endings:
# type: (...) -> Endings
        return _coconut_tail_call(_coconut.dict, (("Vpreactindsg1", self.present), ("Vpreactindsg2", "{_coconut_format_0}is".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl2", "{_coconut_format_0}itis".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl3", "{_coconut_format_0}iunt".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg1", "{_coconut_format_0}iebam".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg2", "{_coconut_format_0}iebas".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg3", "{_coconut_format_0}iebat".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl1", "{_coconut_format_0}iebamus".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl2", "{_coconut_format_0}iebatis".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl3", "{_coconut_format_0}iebant".format(_coconut_format_0=(self._inf_stem))), ("Vperactindsg1", self.perfect), ("Vperactindsg2", "{_coconut_format_0}isti".format(_coconut_format_0=(self._per_stem))), ("Vperactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl2", "{_coconut_format_0}istis".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl3", "{_coconut_format_0}erunt".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg1", "{_coconut_format_0}eram".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg2", "{_coconut_format_0}eras".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg3", "{_coconut_format_0}erat".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl1", "{_coconut_format_0}eramus".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl2", "{_coconut_format_0}eratis".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl3", "{_coconut_format_0}erant".format(_coconut_format_0=(self._per_stem))), ("Vpreactinf   ", self.infinitive), ("Vpreactipesg2", "{_coconut_format_0}i".format(_coconut_format_0=(self._inf_stem))), ("Vpreactipepl2", "{_coconut_format_0}ite".format(_coconut_format_0=(self._inf_stem))), ("Vimpactsbjsg1", "{_coconut_format_0}m".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg2", "{_coconut_format_0}s".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg3", "{_coconut_format_0}t".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl1", "{_coconut_format_0}mus".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl2", "{_coconut_format_0}tis".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl3", "{_coconut_format_0}nt".format(_coconut_format_0=(self.infinitive))), ("Vplpactsbjsg1", "{_coconut_format_0}issem".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg2", "{_coconut_format_0}isses".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg3", "{_coconut_format_0}isset".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl1", "{_coconut_format_0}issemus".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl2", "{_coconut_format_0}issetis".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl3", "{_coconut_format_0}issent".format(_coconut_format_0=(self._per_stem)))))  # audiebas  # audiretis  # audiebant  # audivi  # audiveras  # audire  # audivimus  # audite  # audivisses  # audiret  # audivistis  # audirent  # audis  # audirem  # audiveram  # audiveramus  # audiebamus  # audi  # audiebam  # audiunt  # audiverunt  # audivissem  # audivissemus  # audiremus  # audiebat  # audivisset  # audires  # audio  # audivit  # audiebatis  # audit  # audiverat  # audiveratis  # audivissetis  # auditis  # audiverant  # audimus  # audivissent  # audivisti  #285:         return {


    @_coconut_tco  #327:     def _third_io_conjugation(self) -> Endings:
    def _third_io_conjugation(self):  #327:     def _third_io_conjugation(self) -> Endings:
# type: (...) -> Endings
        return _coconut_tail_call(_coconut.dict, (("Vpreactindsg1", self.present), ("Vpreactindsg2", "{_coconut_format_0}is".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl2", "{_coconut_format_0}itis".format(_coconut_format_0=(self._inf_stem))), ("Vpreactindpl3", "{_coconut_format_0}iunt".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg1", "{_coconut_format_0}iebam".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg2", "{_coconut_format_0}iebas".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindsg3", "{_coconut_format_0}iebat".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl1", "{_coconut_format_0}iebamus".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl2", "{_coconut_format_0}iebatis".format(_coconut_format_0=(self._inf_stem))), ("Vimpactindpl3", "{_coconut_format_0}iebant".format(_coconut_format_0=(self._inf_stem))), ("Vperactindsg1", self.perfect), ("Vperactindsg2", "{_coconut_format_0}isti".format(_coconut_format_0=(self._per_stem))), ("Vperactindsg3", "{_coconut_format_0}it".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl1", "{_coconut_format_0}imus".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl2", "{_coconut_format_0}istis".format(_coconut_format_0=(self._per_stem))), ("Vperactindpl3", "{_coconut_format_0}erunt".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg1", "{_coconut_format_0}eram".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg2", "{_coconut_format_0}eras".format(_coconut_format_0=(self._per_stem))), ("Vplpactindsg3", "{_coconut_format_0}erat".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl1", "{_coconut_format_0}eramus".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl2", "{_coconut_format_0}eratis".format(_coconut_format_0=(self._per_stem))), ("Vplpactindpl3", "{_coconut_format_0}erant".format(_coconut_format_0=(self._per_stem))), ("Vpreactinf   ", self.infinitive), ("Vpreactipesg2", "{_coconut_format_0}e".format(_coconut_format_0=(self._inf_stem))), ("Vpreactipepl2", "{_coconut_format_0}ite".format(_coconut_format_0=(self._inf_stem))), ("Vimpactsbjsg1", "{_coconut_format_0}m".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg2", "{_coconut_format_0}s".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjsg3", "{_coconut_format_0}t".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl1", "{_coconut_format_0}mus".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl2", "{_coconut_format_0}tis".format(_coconut_format_0=(self.infinitive))), ("Vimpactsbjpl3", "{_coconut_format_0}nt".format(_coconut_format_0=(self.infinitive))), ("Vplpactsbjsg1", "{_coconut_format_0}issem".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg2", "{_coconut_format_0}isses".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjsg3", "{_coconut_format_0}isset".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl1", "{_coconut_format_0}issemus".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl2", "{_coconut_format_0}issetis".format(_coconut_format_0=(self._per_stem))), ("Vplpactsbjpl3", "{_coconut_format_0}issent".format(_coconut_format_0=(self._per_stem)))))  # cepissetis  # cepissemus  # caperent  # cepit  # ceperamus  # caperemus  # capio  # cepimus  # ceperatis  # capitis  # caperet  # capere  # cepi  # capiebant  # caperes  # capiebatis  # ceperam  # cepistis  # ceperant  # capit  # cepisset  # ceperat  # ceperas  # capis  # cepissent  # capiebamus  # capiebat  # cepissem  # cape  # ceperunt  # cepisses  # capiebas  # capiebam  # capimus  # capite  # cepisti  # capiunt  # caperetis  # caperem  #328:         return {


    @_coconut_tco  #370:     def _participles(self) -> Endings:
    def _participles(self):  #370:     def _participles(self) -> Endings:
# type: (...) -> Endings
        self._preptc_stem = self.infinitive[:-2]  # type: str  #371:         self._preptc_stem: str = self.infinitive[:-2]
        if "__annotations__" not in _coconut.locals():  #371:         self._preptc_stem: str = self.infinitive[:-2]
            __annotations__ = {}  # type: ignore  #371:         self._preptc_stem: str = self.infinitive[:-2]
        __annotations__["self._preptc_stem"] = 'str'  #371:         self._preptc_stem: str = self.infinitive[:-2]
        self._ppp_stem = self.ppp[:-2]  # type: str  #372:         self._ppp_stem: str = self.ppp[:-2]
        if "__annotations__" not in _coconut.locals():  #372:         self._ppp_stem: str = self.ppp[:-2]
            __annotations__ = {}  # type: ignore  #372:         self._ppp_stem: str = self.ppp[:-2]
        __annotations__["self._ppp_stem"] = 'str'  #372:         self._ppp_stem: str = self.ppp[:-2]
        return _coconut_tail_call(_coconut.dict, (("Vpreactptcmnomsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmvocsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmaccsg", "{_coconut_format_0}ntem".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmgensg", "{_coconut_format_0}ntis".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmdatsg", "{_coconut_format_0}nti".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmablsg", "{_coconut_format_0}nte".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmnompl", "{_coconut_format_0}ntes".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmvocpl", "{_coconut_format_0}ntes".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmaccpl", "{_coconut_format_0}ntes".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmgenpl", "{_coconut_format_0}ntium".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmdatpl", "{_coconut_format_0}ntibus".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcmablpl", "{_coconut_format_0}ntibus".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfnomsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfvocsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfaccsg", "{_coconut_format_0}ntem".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfgensg", "{_coconut_format_0}ntis".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfdatsg", "{_coconut_format_0}nti".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfablsg", "{_coconut_format_0}nte".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfnompl", "{_coconut_format_0}ntes".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfvocpl", "{_coconut_format_0}ntes".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfaccpl", "{_coconut_format_0}ntes".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfgenpl", "{_coconut_format_0}ntium".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfdatpl", "{_coconut_format_0}ntibus".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcfablpl", "{_coconut_format_0}ntibus".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnnomsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnvocsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnaccsg", "{_coconut_format_0}ns".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcngensg", "{_coconut_format_0}ntis".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcndatsg", "{_coconut_format_0}nti".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnablsg", "{_coconut_format_0}nte".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnnompl", "{_coconut_format_0}ntia".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnvocpl", "{_coconut_format_0}ntia".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnaccpl", "{_coconut_format_0}ntia".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcngenpl", "{_coconut_format_0}ntium".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcndatpl", "{_coconut_format_0}ntibus".format(_coconut_format_0=(self._preptc_stem))), ("Vpreactptcnablpl", "{_coconut_format_0}ntibus".format(_coconut_format_0=(self._preptc_stem))), ("Vperpasptcmnomsg", self.ppp), ("Vperpasptcmvocsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmgensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmdatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmaccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmgenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcmablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfnomsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfvocsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfaccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfgensg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfdatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfaccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfgenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfdatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcfablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnnomsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnvocsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnaccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcngensg", "{_coconut_format_0}i".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnnompl", "{_coconut_format_0}a".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnvocpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnaccpl", "{_coconut_format_0}a".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._ppp_stem))), ("Vperpasptcnablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._ppp_stem)))))  # portatae  # portatis  # portatis  # portantes  # portanti  # portante  # portantes  # portatis  # portata  # portantes  # portanti  # portato  # portanti  # portati  # portatae  # portante  # portato  # portantem  # portantem  # portatorum  # portantium  # portantibus  # portate  # portati  # portatum  # portatis  # portata  # portantia  # portata  # portans  # portatis  # portati  # portato  # portato  # portantia  # portantibus  # portans  # portante  # portatam  # portans  # portantia  # portarum  # portatustus  # portantis  # portantibus  # portatos  # portantibus  # portata  # portatae  # portans  # portatum  # portantes  # portantibus  # portatum  # portatae  # portati  # portantium  # portantes  # portans  # portans  # portantis  # portata  # portantes  # portatis  # portata  # portantium  # portatorum  # portatas  # portantibus  # portans  # portatum  # portantis  #373:         return {

# HACK: Extra optional stuff to avoid syntax errors

    @_coconut_tco  #449:     def get(
    def get(self, person=None,  # type: _coconut.typing.Union[int, None]  #449:     def get(
        number=None,  # type: _coconut.typing.Union[str, None]  #449:     def get(
        tense=None,  # type: _coconut.typing.Union[str, None]  #449:     def get(
        voice=None,  # type: _coconut.typing.Union[str, None]  #449:     def get(
        mood=None,  # type: _coconut.typing.Union[str, None]  #449:     def get(
        participle_gender=None,  # type: _coconut.typing.Union[str, None]  #449:     def get(
        participle_case=None,  # type: _coconut.typing.Union[str, None]  #449:     def get(
        ):  #449:     def get(
# type: (...) -> _coconut.typing.Union[Ending, None]
        """Returns the ending of the verb.

        The function returns None if no ending is found.

        Parameters
        ----------
        person : Optional[int], default = None
            The person of the ending, if applicable (not participle).
        number : Optional[str], default = None
            The number of the ending, if applicable (not participle).
        tense, voice, mood : str
            The tense, voice and mood of the ending.
        participle_gender, participle_case : Optional[str], default = None
            The case and gender of the ending, if applicable (participle).

        Returns
        -------
        Ending
            The ending found
        None
            If no ending is found

        Raises
        ------
        InvalidInputError
            If the inputs are not valid. Note that the inputs must be the
            full words, e.g. 'singular', 'plural', 'masculine', 'feminine'.

            If the ending cannot be found.


        Examples
        --------
        >>> foo = Verb(
        ...     present="celo",
        ...     infinitive="celare",
        ...     perfect="celavi",
        ...     ppp="celatus",
        ...     meaning="hide",
        ... )
        >>> foo.get(
        ...     person=1,
        ...     number="singular",
        ...     tense="present",
        ...     voice="active",
        ...     mood="indicative",
        ... )
        'celo'

        Note that all arguments of get are keyword-only.

        >>> foo.get(
        ...     number="singular",
        ...     tense="perfect",
        ...     voice="passive",
        ...     mood="participle",
        ...     participle_gender="masculine",
        ...     participle_case="nominative",
        ... )
        'celatus'

        Similar with participle endings.
        """  #521:         """
        short_tense = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #522:         short_tense: str
        if "__annotations__" not in _coconut.locals():  #522:         short_tense: str
            __annotations__ = {}  # type: ignore  #522:         short_tense: str
        __annotations__["short_tense"] = 'str'  #522:         short_tense: str
        short_voice = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #523:         short_voice: str
        if "__annotations__" not in _coconut.locals():  #523:         short_voice: str
            __annotations__ = {}  # type: ignore  #523:         short_voice: str
        __annotations__["short_voice"] = 'str'  #523:         short_voice: str
        short_mood = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #524:         short_mood: str
        if "__annotations__" not in _coconut.locals():  #524:         short_mood: str
            __annotations__ = {}  # type: ignore  #524:         short_mood: str
        __annotations__["short_mood"] = 'str'  #524:         short_mood: str
        short_number = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #525:         short_number: str
        if "__annotations__" not in _coconut.locals():  #525:         short_number: str
            __annotations__ = {}  # type: ignore  #525:         short_number: str
        __annotations__["short_number"] = 'str'  #525:         short_number: str

        if tense not in TENSE_SHORTHAND:  #527:         if tense not in TENSE_SHORTHAND:
            raise InvalidInputError("Invalid tense: '{_coconut_format_0}'".format(_coconut_format_0=(tense)))  #528:             raise InvalidInputError(f"Invalid tense: '{tense}'")

        if voice not in VOICE_SHORTHAND:  #530:         if voice not in VOICE_SHORTHAND:
            raise InvalidInputError("Invalid voice: '{_coconut_format_0}'".format(_coconut_format_0=(voice)))  #531:             raise InvalidInputError(f"Invalid voice: '{voice}'")

        if mood == "participle":  #533:         if mood == "participle":
            if person:  #534:             if person:
                raise InvalidInputError("Participle cannot have a person (person '{_coconut_format_0}')".format(_coconut_format_0=(person)))  #535:                 raise InvalidInputError(

            if not participle_case:  #539:             if not participle_case:
                raise InvalidInputError("Case not given")  #540:                 raise InvalidInputError("Case not given")

            if not participle_gender:  #542:             if not participle_gender:
                raise InvalidInputError("Gender not given")  #543:                 raise InvalidInputError("Gender not given")

            if not number:  #545:             if not number:
                raise InvalidInputError("Number not given")  #546:                 raise InvalidInputError("Number not given")

            return _coconut_tail_call(self._get_partciple, tense=tense, voice=voice, number=number, participle_gender=participle_gender, participle_case=participle_case)  #548:             return self._get_partciple(

        if mood not in MOOD_SHORTHAND:  #556:         if mood not in MOOD_SHORTHAND:
            raise InvalidInputError("Invalid mood: '{_coconut_format_0}'".format(_coconut_format_0=(mood)))  #557:             raise InvalidInputError(f"Invalid mood: '{mood}'")

        if number and number not in NUMBER_SHORTHAND:  #559:         if number and number not in NUMBER_SHORTHAND:
            raise InvalidInputError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(number)))  #560:             raise InvalidInputError(f"Invalid number: '{number}'")

        if person and person not in _coconut.set((1, 2, 3)):  #562:         if person and person not in {1, 2, 3}:
            raise InvalidInputError("Invalid person: '{_coconut_format_0}'".format(_coconut_format_0=(person)))  #563:             raise InvalidInputError(f"Invalid person: '{person}'")

        short_tense = TENSE_SHORTHAND[tense]  #565:         short_tense = TENSE_SHORTHAND[tense]
        short_voice = VOICE_SHORTHAND[voice]  #566:         short_voice = VOICE_SHORTHAND[voice]
        short_mood = MOOD_SHORTHAND[mood]  #567:         short_mood = MOOD_SHORTHAND[mood]
        if number:  #568:         if number:
            short_number = NUMBER_SHORTHAND[number]  #569:             short_number = NUMBER_SHORTHAND[number]

        if mood == "infinitive":  #571:         if mood == "infinitive":
            return _coconut_tail_call(self.endings.get, "V{_coconut_format_0}{_coconut_format_1}inf   ".format(_coconut_format_0=(short_tense), _coconut_format_1=(short_voice)))  #572:             return self.endings.get(f"V{short_tense}{short_voice}inf   ")
        return _coconut_tail_call(self.endings.get, "V{_coconut_format_0}{_coconut_format_1}{_coconut_format_2}{_coconut_format_3}{_coconut_format_4}".format(_coconut_format_0=(short_tense), _coconut_format_1=(short_voice), _coconut_format_2=(short_mood), _coconut_format_3=(short_number), _coconut_format_4=(person)))  #573:         return self.endings.get(


    @_coconut_tco  #577:     def _get_partciple(
    def _get_partciple(self, tense,  # type: str  #577:     def _get_partciple(
        voice,  # type: str  #577:     def _get_partciple(
        number,  # type: str  #577:     def _get_partciple(
        participle_gender,  # type: str  #577:     def _get_partciple(
        participle_case,  # type: str  #577:     def _get_partciple(
        ):  #577:     def _get_partciple(
# type: (...) -> _coconut.typing.Union[Ending, None]
        if participle_case not in CASE_SHORTHAND:  #585:         if participle_case not in CASE_SHORTHAND:
            raise InvalidInputError("Invalid case: '{_coconut_format_0}'".format(_coconut_format_0=(participle_case)))  #586:             raise InvalidInputError(f"Invalid case: '{participle_case}'")

        if participle_gender not in GENDER_SHORTHAND:  #588:         if participle_gender not in GENDER_SHORTHAND:
            raise InvalidInputError("Invalid gender: '{_coconut_format_0}'".format(_coconut_format_0=(participle_gender)))  #589:             raise InvalidInputError(f"Invalid gender: '{participle_gender}'")

        if number not in NUMBER_SHORTHAND:  #591:         if number not in NUMBER_SHORTHAND:
            raise InvalidInputError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(number)))  #592:             raise InvalidInputError(f"Invalid number: '{number}'")

        short_tense = TENSE_SHORTHAND[tense]  #594:         short_tense = TENSE_SHORTHAND[tense]
        short_voice = VOICE_SHORTHAND[voice]  #595:         short_voice = VOICE_SHORTHAND[voice]
        short_number = NUMBER_SHORTHAND[number]  #596:         short_number = NUMBER_SHORTHAND[number]
        short_gender = GENDER_SHORTHAND[participle_gender]  # type: str  #597:         short_gender: str = GENDER_SHORTHAND[participle_gender]
        if "__annotations__" not in _coconut.locals():  #597:         short_gender: str = GENDER_SHORTHAND[participle_gender]
            __annotations__ = {}  # type: ignore  #597:         short_gender: str = GENDER_SHORTHAND[participle_gender]
        __annotations__["short_gender"] = 'str'  #597:         short_gender: str = GENDER_SHORTHAND[participle_gender]
        short_case = CASE_SHORTHAND[participle_case]  # type: str  #598:         short_case: str = CASE_SHORTHAND[participle_case]
        if "__annotations__" not in _coconut.locals():  #598:         short_case: str = CASE_SHORTHAND[participle_case]
            __annotations__ = {}  # type: ignore  #598:         short_case: str = CASE_SHORTHAND[participle_case]
        __annotations__["short_case"] = 'str'  #598:         short_case: str = CASE_SHORTHAND[participle_case]

        return _coconut_tail_call(self.endings.get, "V{_coconut_format_0}{_coconut_format_1}ptc{_coconut_format_2}{_coconut_format_3}{_coconut_format_4}".format(_coconut_format_0=(short_tense), _coconut_format_1=(short_voice), _coconut_format_2=(short_gender), _coconut_format_3=(short_case), _coconut_format_4=(short_number)))  #600:         return self.endings.get(


    @staticmethod  #604:     @staticmethod
    def _create_namespace(key  # type: str  #605:     def _create_namespace(key: str) -> EndingComponents:
        ):  #605:     def _create_namespace(key: str) -> EndingComponents:
# type: (...) -> EndingComponents
        output = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: EndingComponents  #606:         output: EndingComponents
        if "__annotations__" not in _coconut.locals():  #606:         output: EndingComponents
            __annotations__ = {}  # type: ignore  #606:         output: EndingComponents
        __annotations__["output"] = 'EndingComponents'  #606:         output: EndingComponents
        if len(key) == 13:  #607:         if len(key) == 13:
            output = EndingComponents(tense=key_from_value(TENSE_SHORTHAND, key[1:4]), voice=key_from_value(VOICE_SHORTHAND, key[4:7]), mood=key_from_value(MOOD_SHORTHAND, key[7:10]), number=key_from_value(NUMBER_SHORTHAND, key[10:12]), person=PERSON_SHORTHAND[int(key[12])])  #608:             output = EndingComponents(
            output.string = "{_coconut_format_0} {_coconut_format_1} {_coconut_format_2} {_coconut_format_3} {_coconut_format_4}".format(_coconut_format_0=(output.tense), _coconut_format_1=(output.voice), _coconut_format_2=(output.mood), _coconut_format_3=(output.number), _coconut_format_4=(output.person))  #615:             output.string = f"{output.tense} {output.voice} {output.mood} {output.number} {output.person}"
            return output  #616:             return output
        if len(key) == 16 and key[7:10] == "ptc":  #617:         if len(key) == 16 and key[7:10] == "ptc":
            output = EndingComponents(tense=key_from_value(TENSE_SHORTHAND, key[1:4]), voice=key_from_value(VOICE_SHORTHAND, key[4:7]), mood="participle", gender=key_from_value(GENDER_SHORTHAND, key[10]), case=key_from_value(CASE_SHORTHAND, key[11:14]), number=key_from_value(NUMBER_SHORTHAND, key[14:16]))  #618:             output = EndingComponents(
            output.string = "{_coconut_format_0} {_coconut_format_1} participle {_coconut_format_2} {_coconut_format_3} {_coconut_format_4}".format(_coconut_format_0=(output.tense), _coconut_format_1=(output.voice), _coconut_format_2=(output.gender), _coconut_format_3=(output.case), _coconut_format_4=(output.number))  #626:             output.string = f"{output.tense} {output.voice} participle {output.gender} {output.case} {output.number}"
            return output  #627:             return output

        raise InvalidInputError("Key '{_coconut_format_0}' is invalid".format(_coconut_format_0=(key)))  # pragma: no cover # this should never happen  #629:         raise InvalidInputError(


    @_coconut_tco  #633:     def __repr__(self) -> str:
    def __repr__(self):  #633:     def __repr__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("Verb({_coconut_format_0}, {_coconut_format_1}, {_coconut_format_2}, {_coconut_format_3}, {_coconut_format_4})".format, _coconut_format_0=(self.present), _coconut_format_1=(self.infinitive), _coconut_format_2=(self.perfect), _coconut_format_3=(self.ppp), _coconut_format_4=(self.meaning))  #634:         return f"Verb({self.present}, {self.infinitive}, {self.perfect}, {self.ppp}, {self.meaning})"


    @_coconut_tco  #636:     def __str__(self) -> str:
    def __str__(self):  #636:     def __str__(self) -> str:
# type: (...) -> str
        if self.ppp:  #637:         if self.ppp:
            return _coconut_tail_call("{_coconut_format_0}: {_coconut_format_1}, {_coconut_format_2}, {_coconut_format_3}, {_coconut_format_4}".format, _coconut_format_0=(self.meaning), _coconut_format_1=(self.present), _coconut_format_2=(self.infinitive), _coconut_format_3=(self.perfect), _coconut_format_4=(self.ppp))  #638:             return f"{self.meaning}: {self.present}, {self.infinitive}, {self.perfect}, {self.ppp}"
        return _coconut_tail_call("{_coconut_format_0}: {_coconut_format_1}, {_coconut_format_2}, {_coconut_format_3}".format, _coconut_format_0=(self.meaning), _coconut_format_1=(self.present), _coconut_format_2=(self.infinitive), _coconut_format_3=(self.perfect))  #639:         return f"{self.meaning}: {self.present}, {self.infinitive}, {self.perfect}"


_coconut_call_set_names(Verb)  #641:         return f"{self.meaning}: {self.present}, {self.infinitive}, {self.perfect}"
