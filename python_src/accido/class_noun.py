#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7f12492d

# Compiled with Coconut version 3.1.2

"""Representation of a Latin noun with endings."""

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
from .edge_cases import IRREGULAR_NOUNS  #8: from .edge_cases import IRREGULAR_NOUNS
from .exceptions import InvalidInputError  #9: from .exceptions import InvalidInputError
from .misc import CASE_SHORTHAND  #10: from .misc import (
from .misc import GENDER_SHORTHAND  #10: from .misc import (
from .misc import NUMBER_SHORTHAND  #10: from .misc import (
from .misc import EndingComponents  #10: from .misc import (

if TYPE_CHECKING:  #17: if TYPE_CHECKING:
    from .type_aliases import Ending  #18:     from .type_aliases import Ending, Endings, Meaning
    from .type_aliases import Endings  #18:     from .type_aliases import Ending, Endings, Meaning
    from .type_aliases import Meaning  #18:     from .type_aliases import Ending, Endings, Meaning


@total_ordering  #21: @total_ordering
class Noun(_Word):  #22: class Noun(_Word):
    """Representation of a Latin noun with endings.

    Attributes
    ----------
    nominative, genitive : str
    meaning : Meaning
    declension : {0, 1, 2, 3, 4, 5}
        The declension of the noun. The value 0 represents an irregular
        declension.
    endings : Endings
    plurale_tantum : bool
        If the noun is a plurale tantum or not.
    gender : str

    Examples
    --------
    >>> foo = Noun(
    ...     nominative="ancilla",
    ...     genitive="ancillae",
    ...     gender="feminine",
    ...     meaning="slavegirl",
    ... )
    >>> foo["Nnomsg"]
    'ancilla'

    Note that all arguments of Noun are keyword-only.

    Notes
    -----
    Accido relies on the assumption that there are no neuter or plurale
    tantum fifth declension nouns (there doesn't seem to be any).
    """  #54:     """

    def __init__(self, nominative,  # type: str  #56:     def __init__(
        genitive,  # type: str  #56:     def __init__(
        gender,  # type: str  #56:     def __init__(
        meaning,  # type: Meaning  #56:     def __init__(
        ):  #56:     def __init__(
# type: (...) -> None
        """Initialises Noun and determines the declension and endings.

        Parameters
        ----------
        nominative, genitive : str
        gender : str
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the input is not valid (invalid gender value or genitive).
        """  #75:         """
        __class__ = Noun  #76:         super().__init__()

        super().__init__()  #76:         super().__init__()

        if gender:  #78:         if gender:
            if gender not in GENDER_SHORTHAND:  #79:             if gender not in GENDER_SHORTHAND:
                raise InvalidInputError("Invalid gender: '{_coconut_format_0}'".format(_coconut_format_0=(gender)))  #80:                 raise InvalidInputError(f"Invalid gender: '{gender}'")

            self.gender = gender  # type: str  #82:             self.gender: str = gender
            if "__annotations__" not in _coconut.locals():  #82:             self.gender: str = gender
                __annotations__ = {}  # type: ignore  #82:             self.gender: str = gender
            __annotations__["self.gender"] = 'str'  #82:             self.gender: str = gender

        self.nominative = nominative  # type: str  #84:         self.nominative: str = nominative
        if "__annotations__" not in _coconut.locals():  #84:         self.nominative: str = nominative
            __annotations__ = {}  # type: ignore  #84:         self.nominative: str = nominative
        __annotations__["self.nominative"] = 'str'  #84:         self.nominative: str = nominative
        if genitive:  #85:         if genitive:
            self.genitive = genitive  # type: str  #86:             self.genitive: str = genitive
            if "__annotations__" not in _coconut.locals():  #86:             self.genitive: str = genitive
                __annotations__ = {}  # type: ignore  #86:             self.genitive: str = genitive
            __annotations__["self.genitive"] = 'str'  #86:             self.genitive: str = genitive
        self.meaning = meaning  # type: Meaning  #87:         self.meaning: Meaning = meaning
        if "__annotations__" not in _coconut.locals():  #87:         self.meaning: Meaning = meaning
            __annotations__ = {}  # type: ignore  #87:         self.meaning: Meaning = meaning
        __annotations__["self.meaning"] = 'Meaning'  #87:         self.meaning: Meaning = meaning
        self.plurale_tantum = False  # type: bool  #88:         self.plurale_tantum: bool = False
        if "__annotations__" not in _coconut.locals():  #88:         self.plurale_tantum: bool = False
            __annotations__ = {}  # type: ignore  #88:         self.plurale_tantum: bool = False
        __annotations__["self.plurale_tantum"] = 'bool'  #88:         self.plurale_tantum: bool = False

        self._first = self.nominative  # type: str  #90:         self._first: str = self.nominative
        if "__annotations__" not in _coconut.locals():  #90:         self._first: str = self.nominative
            __annotations__ = {}  # type: ignore  #90:         self._first: str = self.nominative
        __annotations__["self._first"] = 'str'  #90:         self._first: str = self.nominative
        self.declension = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: Literal[0, 1, 2, 3, 4, 5]  #91:         self.declension: Literal[0, 1, 2, 3, 4, 5]
        if "__annotations__" not in _coconut.locals():  #91:         self.declension: Literal[0, 1, 2, 3, 4, 5]
            __annotations__ = {}  # type: ignore  #91:         self.declension: Literal[0, 1, 2, 3, 4, 5]
        __annotations__["self.declension"] = 'Literal[0, 1, 2, 3, 4, 5]'  #91:         self.declension: Literal[0, 1, 2, 3, 4, 5]
        self._stem = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: str  #92:         self._stem: str
        if "__annotations__" not in _coconut.locals():  #92:         self._stem: str
            __annotations__ = {}  # type: ignore  #92:         self._stem: str
        __annotations__["self._stem"] = 'str'  #92:         self._stem: str

        if self.nominative in IRREGULAR_NOUNS:  #94:         if self.nominative in IRREGULAR_NOUNS:
            self.endings = IRREGULAR_NOUNS[nominative]  #95:             self.endings = IRREGULAR_NOUNS[nominative]
            self.declension = 0  #96:             self.declension = 0
            return  #97:             return

        self._find_declension()  #99:         self._find_declension()

        self.endings = self._determine_endings()  #101:         self.endings = self._determine_endings()

        if self.gender == "neuter":  #103:         if self.gender == "neuter":
            self._neuter_endings()  #104:             self._neuter_endings()

        if self.plurale_tantum:  #106:         if self.plurale_tantum:
            self.endings = _coconut.dict(((k), (v)) for k, v in self.endings.items() if not k.endswith("sg"))  #107:             self.endings = {


    def _find_declension(self):  #111:     def _find_declension(self) -> None:
# type: (...) -> None
# The ordering of this is strange because
# e.g. ending -ei ends in 'i' as well as 'ei'
# so 5th declension check must come before 2nd declension check, etc.
        if self.genitive[-2:] == "ei":  #115:         if self.genitive[-2:] == "ei":
            self.declension = 5  #116:             self.declension = 5
            self._stem = self.genitive[:-2]  # diei > di-  #117:             self._stem = self.genitive[:-2]  # diei > di-
        elif self.genitive[-2:] == "ae":  #118:         elif self.genitive[-2:] == "ae":
            self.declension = 1  #119:             self.declension = 1
            self._stem = self.genitive[:-2]  # puellae -> puell-  #120:             self._stem = self.genitive[:-2]  # puellae -> puell-
        elif self.genitive[-1:] == "i":  #121:         elif self.genitive[-1:] == "i":
            self.declension = 2  #122:             self.declension = 2
            self._stem = self.genitive[:-1]  # servi -> serv-  #123:             self._stem = self.genitive[:-1]  # servi -> serv-
        elif self.genitive[-2:] == "is":  #124:         elif self.genitive[-2:] == "is":
            self.declension = 3  #125:             self.declension = 3
            self._stem = self.genitive[:-2]  # canis -> can-  #126:             self._stem = self.genitive[:-2]  # canis -> can-
        elif self.genitive[-2:] == "us":  #127:         elif self.genitive[-2:] == "us":
            self.declension = 4  #128:             self.declension = 4
            self._stem = self.genitive[:-2]  # manus -> man-  #129:             self._stem = self.genitive[:-2]  # manus -> man-

        elif self.genitive[-3:] == "uum":  #131:         elif self.genitive[-3:] == "uum":
            self.declension = 4  #132:             self.declension = 4
            self._stem = self.genitive[:-3]  # manuum -> man-  #133:             self._stem = self.genitive[:-3]  # manuum -> man-
            self.plurale_tantum = True  #134:             self.plurale_tantum = True
        elif self.genitive[-4:] == "arum":  #135:         elif self.genitive[-4:] == "arum":
            self.declension = 1  #136:             self.declension = 1
            self._stem = self.genitive[:-4]  # puellarum -> puell-  #137:             self._stem = self.genitive[:-4]  # puellarum -> puell-
            self.plurale_tantum = True  #138:             self.plurale_tantum = True
        elif self.genitive[-4:] == "orum":  #139:         elif self.genitive[-4:] == "orum":
            self.declension = 2  #140:             self.declension = 2
            self._stem = self.genitive[:-4]  # servorum -> serv-  #141:             self._stem = self.genitive[:-4]  # servorum -> serv-
            self.plurale_tantum = True  #142:             self.plurale_tantum = True
# elif self.genitive[-4:] == "erum":
#     self.declension = 5
#     self._stem = self.genitive[:-4]  # dierum > di-
#     self.plurale_tantum = True
        elif self.genitive[-2:] == "um":  #147:         elif self.genitive[-2:] == "um":
            self.declension = 3  #148:             self.declension = 3
            self._stem = self.genitive[:-2]  # canum -> can-  #149:             self._stem = self.genitive[:-2]  # canum -> can-
            self.plurale_tantum = True  #150:             self.plurale_tantum = True

        else:  #152:         else:
            raise InvalidInputError("Invalid genitive form: '{_coconut_format_0}'".format(_coconut_format_0=(self.genitive)))  #153:             raise InvalidInputError(

# type: ignore[return]
    @_coconut_tco  # type: ignore[return]  #157:     def _determine_endings(self) -> Endings:  # type: ignore[return]
    def _determine_endings(self):  # type: ignore[return]  #157:     def _determine_endings(self) -> Endings:  # type: ignore[return]
# type: (...) -> Endings  # type: ignore[return]
        _coconut_case_match_to_0 = self.declension  #158:         match self.declension:
        _coconut_case_match_check_0 = False  #158:         match self.declension:
        if _coconut_case_match_to_0 == 1:  #158:         match self.declension:
            _coconut_case_match_check_0 = True  #158:         match self.declension:
        if _coconut_case_match_check_0:  #158:         match self.declension:
            return _coconut_tail_call(_coconut.dict, (("Nnomsg", self.nominative), ("Nvocsg", self.nominative), ("Naccsg", "{_coconut_format_0}am".format(_coconut_format_0=(self._stem))), ("Ngensg", self.genitive), ("Ndatsg", "{_coconut_format_0}ae".format(_coconut_format_0=(self._stem))), ("Nablsg", "{_coconut_format_0}a".format(_coconut_format_0=(self._stem))), ("Nnompl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._stem))), ("Nvocpl", "{_coconut_format_0}ae".format(_coconut_format_0=(self._stem))), ("Naccpl", "{_coconut_format_0}as".format(_coconut_format_0=(self._stem))), ("Ngenpl", "{_coconut_format_0}arum".format(_coconut_format_0=(self._stem))), ("Ndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._stem))), ("Nablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._stem)))))  # puella  # puellis  # puella  # puellae  # puellarum  # puellas  # puellis  # puellae  # puella  # puellam  # puellae  # puellae  #160:                 return {

        if not _coconut_case_match_check_0:  #175:             case 2:
            if _coconut_case_match_to_0 == 2:  #175:             case 2:
                _coconut_case_match_check_0 = True  #175:             case 2:
            if _coconut_case_match_check_0:  #175:             case 2:
                return _coconut_tail_call(_coconut.dict, (("Nnomsg", self.nominative), ("Nvocsg", (self.nominative if self.nominative.endswith("er") else "{_coconut_format_0}e".format(_coconut_format_0=(self._stem)))), ("Naccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._stem))), ("Ngensg", self.genitive), ("Ndatsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._stem))), ("Nablsg", "{_coconut_format_0}o".format(_coconut_format_0=(self._stem))), ("Nnompl", "{_coconut_format_0}i".format(_coconut_format_0=(self._stem))), ("Nvocpl", "{_coconut_format_0}i".format(_coconut_format_0=(self._stem))), ("Naccpl", "{_coconut_format_0}os".format(_coconut_format_0=(self._stem))), ("Ngenpl", "{_coconut_format_0}orum".format(_coconut_format_0=(self._stem))), ("Ndatpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._stem))), ("Nablpl", "{_coconut_format_0}is".format(_coconut_format_0=(self._stem)))))  # servum  # servi  # servis  # servorum  # puer  # servos  # servi  # servus  # servis  # servo  # servi  # servo  # serve  #176:                 return {

        if not _coconut_case_match_check_0:  #195:             case 3:
            if _coconut_case_match_to_0 == 3:  #195:             case 3:
                _coconut_case_match_check_0 = True  #195:             case 3:
            if _coconut_case_match_check_0:  #195:             case 3:
                return _coconut_tail_call(_coconut.dict, (("Nnomsg", self.nominative), ("Nvocsg", self.nominative), ("Naccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._stem))), ("Ngensg", self.genitive), ("Ndatsg", "{_coconut_format_0}i".format(_coconut_format_0=(self._stem))), ("Nablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._stem))), ("Nnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._stem))), ("Nvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._stem))), ("Naccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._stem))), ("Ngenpl", "{_coconut_format_0}um".format(_coconut_format_0=(self._stem))), ("Ndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._stem))), ("Nablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._stem)))))  # mercatori  # mercatores  # mercatorum  # mercatoribus  # mercator  # mercatores  # mercatoribus  # mercator  # mercatore  # mercatorem  # mercatoris  # mercatores  #196:                 return {

        if not _coconut_case_match_check_0:  #211:             case 4:
            if _coconut_case_match_to_0 == 4:  #211:             case 4:
                _coconut_case_match_check_0 = True  #211:             case 4:
            if _coconut_case_match_check_0:  #211:             case 4:
                return _coconut_tail_call(_coconut.dict, (("Nnomsg", self.nominative), ("Nvocsg", self.nominative), ("Naccsg", "{_coconut_format_0}um".format(_coconut_format_0=(self._stem))), ("Ngensg", "{_coconut_format_0}us".format(_coconut_format_0=(self._stem))), ("Ndatsg", "{_coconut_format_0}ui".format(_coconut_format_0=(self._stem))), ("Nablsg", "{_coconut_format_0}u".format(_coconut_format_0=(self._stem))), ("Nnompl", "{_coconut_format_0}us".format(_coconut_format_0=(self._stem))), ("Nvocpl", "{_coconut_format_0}us".format(_coconut_format_0=(self._stem))), ("Naccpl", "{_coconut_format_0}us".format(_coconut_format_0=(self._stem))), ("Ngenpl", "{_coconut_format_0}uum".format(_coconut_format_0=(self._stem))), ("Ndatpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._stem))), ("Nablpl", "{_coconut_format_0}ibus".format(_coconut_format_0=(self._stem)))))  # manuum  # manus  # manibus  # manus  # manus  # manus  # manui  # manibus  # manu  # manus  # manum  # manus  #212:                 return {

        if not _coconut_case_match_check_0:  #227:             case 5:
            if _coconut_case_match_to_0 == 5:  #227:             case 5:
                _coconut_case_match_check_0 = True  #227:             case 5:
            if _coconut_case_match_check_0:  #227:             case 5:
                return _coconut_tail_call(_coconut.dict, (("Nnomsg", self.nominative), ("Nvocsg", self.nominative), ("Naccsg", "{_coconut_format_0}em".format(_coconut_format_0=(self._stem))), ("Ngensg", "{_coconut_format_0}ei".format(_coconut_format_0=(self._stem))), ("Ndatsg", "{_coconut_format_0}ei".format(_coconut_format_0=(self._stem))), ("Nablsg", "{_coconut_format_0}e".format(_coconut_format_0=(self._stem))), ("Nnompl", "{_coconut_format_0}es".format(_coconut_format_0=(self._stem))), ("Nvocpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._stem))), ("Naccpl", "{_coconut_format_0}es".format(_coconut_format_0=(self._stem))), ("Ngenpl", "{_coconut_format_0}erum".format(_coconut_format_0=(self._stem))), ("Ndatpl", "{_coconut_format_0}ebus".format(_coconut_format_0=(self._stem))), ("Nablpl", "{_coconut_format_0}ebus".format(_coconut_format_0=(self._stem)))))  # res  # re  # rerum  # res  # rem  # res  # rei  # rei  # res  # rebus  # res  # rebus  #228:                 return {

        if not _coconut_case_match_check_0:  # pragma: no cover # this should never happen  #243:             case _:  # pragma: no cover # this should never happen
            _coconut_case_match_check_0 = True  # pragma: no cover # this should never happen  #243:             case _:  # pragma: no cover # this should never happen
            if _coconut_case_match_check_0:  # pragma: no cover # this should never happen  #243:             case _:  # pragma: no cover # this should never happen
                raise ValueError("Declension {_coconut_format_0} not recognised".format(_coconut_format_0=(self.declension)))  #244:                 raise ValueError(


    def _neuter_endings(self):  #248:     def _neuter_endings(self) -> None:
# type: (...) -> None
        self.endings["Naccsg"] = self.nominative  # templum  #249:         self.endings["Naccsg"] = self.nominative  # templum
        self.endings["Nvocsg"] = self.nominative  # templum  #250:         self.endings["Nvocsg"] = self.nominative  # templum

        if self.declension == 5:  #252:         if self.declension == 5:
            raise InvalidInputError("Fifth declension nouns cannot be neuter " + "(noun '{_coconut_format_0}' given)".format(_coconut_format_0=(self.nominative)))  #253:             raise InvalidInputError(

        if self.declension == 4:  #258:         if self.declension == 4:
            self.endings["Nnompl"] = "{_coconut_format_0}ua".format(_coconut_format_0=(self._stem))  # cornua  #259:             self.endings["Nnompl"] = f"{self._stem}ua"  # cornua
            self.endings["Naccpl"] = "{_coconut_format_0}ua".format(_coconut_format_0=(self._stem))  # cornua  #260:             self.endings["Naccpl"] = f"{self._stem}ua"  # cornua
            self.endings["Nvocpl"] = "{_coconut_format_0}ua".format(_coconut_format_0=(self._stem))  # cornua  #261:             self.endings["Nvocpl"] = f"{self._stem}ua"  # cornua
            self.endings["Ndatsg"] = "{_coconut_format_0}u".format(_coconut_format_0=(self._stem))  # cornu  #262:             self.endings["Ndatsg"] = f"{self._stem}u"  # cornu

        else:  #264:         else:
# For the other declensions
            self.endings["Nnompl"] = "{_coconut_format_0}a".format(_coconut_format_0=(self._stem))  # templa  #266:             self.endings["Nnompl"] = f"{self._stem}a"  # templa
            self.endings["Naccpl"] = "{_coconut_format_0}a".format(_coconut_format_0=(self._stem))  # templa  #267:             self.endings["Naccpl"] = f"{self._stem}a"  # templa
            self.endings["Nvocpl"] = "{_coconut_format_0}a".format(_coconut_format_0=(self._stem))  # templa  #268:             self.endings["Nvocpl"] = f"{self._stem}a"  # templa


    @_coconut_tco  #270:     def get(self, case: str, number: str) -> Ending | None:
    def get(self, case,  # type: str  #270:     def get(self, case: str, number: str) -> Ending | None:
        number  # type: str  #270:     def get(self, case: str, number: str) -> Ending | None:
        ):  #270:     def get(self, case: str, number: str) -> Ending | None:
# type: (...) -> _coconut.typing.Union[Ending, None]
        """Returns the ending of the noun.

        The function returns None if no ending is found.

        Parameters
        ----------
        case, number : str

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
        >>> foo = Noun(
        ...     nominative="ancilla",
        ...     genitive="ancillae",
        ...     gender="feminine",
        ...     meaning="slavegirl",
        ... )
        >>> foo.get(case="nominative", number="singular")
        'ancilla'

        Note that all arguments of get are keyword-only.
        """  #303:         """
        if case not in CASE_SHORTHAND:  #304:         if case not in CASE_SHORTHAND:
            raise InvalidInputError("Invalid case: '{_coconut_format_0}'".format(_coconut_format_0=(case)))  #305:             raise InvalidInputError(f"Invalid case: '{case}'")

        if number not in NUMBER_SHORTHAND:  #307:         if number not in NUMBER_SHORTHAND:
            raise InvalidInputError("Invalid number: '{_coconut_format_0}'".format(_coconut_format_0=(number)))  #308:             raise InvalidInputError(f"Invalid number: '{number}'")

        short_case = CASE_SHORTHAND[case]  # type: str  #310:         short_case: str = CASE_SHORTHAND[case]
        if "__annotations__" not in _coconut.locals():  #310:         short_case: str = CASE_SHORTHAND[case]
            __annotations__ = {}  # type: ignore  #310:         short_case: str = CASE_SHORTHAND[case]
        __annotations__["short_case"] = 'str'  #310:         short_case: str = CASE_SHORTHAND[case]
        short_number = NUMBER_SHORTHAND[number]  # type: str  #311:         short_number: str = NUMBER_SHORTHAND[number]
        if "__annotations__" not in _coconut.locals():  #311:         short_number: str = NUMBER_SHORTHAND[number]
            __annotations__ = {}  # type: ignore  #311:         short_number: str = NUMBER_SHORTHAND[number]
        __annotations__["short_number"] = 'str'  #311:         short_number: str = NUMBER_SHORTHAND[number]

        return _coconut_tail_call(self.endings.get, "N{_coconut_format_0}{_coconut_format_1}".format(_coconut_format_0=(short_case), _coconut_format_1=(short_number)))  #313:         return self.endings.get(f"N{short_case}{short_number}")


    @staticmethod  #315:     @staticmethod
    def _create_namespace(key  # type: str  #316:     def _create_namespace(key: str) -> EndingComponents:
        ):  #316:     def _create_namespace(key: str) -> EndingComponents:
# type: (...) -> EndingComponents
        output = EndingComponents(case=key_from_value(CASE_SHORTHAND, key[1:4]), number=key_from_value(NUMBER_SHORTHAND, key[4:6]))  # type: EndingComponents  #317:         output: EndingComponents = EndingComponents(
        if "__annotations__" not in _coconut.locals():  #317:         output: EndingComponents = EndingComponents(
            __annotations__ = {}  # type: ignore  #317:         output: EndingComponents = EndingComponents(
        __annotations__["output"] = 'EndingComponents'  #317:         output: EndingComponents = EndingComponents(
        output.string = "{_coconut_format_0} {_coconut_format_1}".format(_coconut_format_0=(output.case), _coconut_format_1=(output.number))  #321:         output.string = f"{output.case} {output.number}"
        return output  #322:         return output


    def __repr__(self):  #324:     def __repr__(self) -> str:
# type: (...) -> str
        return ("Noun({_coconut_format_0}, {_coconut_format_1}, ".format(_coconut_format_0=(self.nominative), _coconut_format_1=(self.genitive)) + "{_coconut_format_0}, {_coconut_format_1})".format(_coconut_format_0=(self.gender), _coconut_format_1=(self.meaning)))  #325:         return (


    def __str__(self):  #330:     def __str__(self) -> str:
# type: (...) -> str
        if self.gender in GENDER_SHORTHAND:  #331:         if self.gender in GENDER_SHORTHAND:
            return ("{_coconut_format_0}: {_coconut_format_1}, ".format(_coconut_format_0=(self.meaning), _coconut_format_1=(self.nominative)) + "{_coconut_format_0}, ({_coconut_format_1})".format(_coconut_format_0=(self.genitive), _coconut_format_1=(GENDER_SHORTHAND[self.gender])))  #332:             return (

        raise ValueError("Gender {_coconut_format_0} not recognised".format(_coconut_format_0=(self.gender)))  # pragma: no cover # this should never occur  #337:         raise ValueError(


_coconut_call_set_names(Noun)  #341:         )  # pragma: no cover # this should never occur
