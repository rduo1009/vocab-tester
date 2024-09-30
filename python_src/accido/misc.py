#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x386fd023

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

from aenum import Enum  #6: from aenum import Enum, MultiValue
from aenum import MultiValue  #6: from aenum import Enum, MultiValue


@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #9: class Number(Enum, settings=MultiValue, init="regular shorthand"):
class Number(Enum):  #9: class Number(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the grammatical number."""  #10:     """Represents the grammatical number."""

    SINGULAR = "singular", "sg"  #12:     SINGULAR = "singular", "sg"
    PLURAL = "plural", "pl"  #13:     PLURAL = "plural", "pl"


_coconut_call_set_names(Number)  #16: class Tense(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #16: class Tense(Enum, settings=MultiValue, init="regular shorthand"):
class Tense(Enum):  #16: class Tense(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the tense of a verb."""  #17:     """Represents the tense of a verb."""

    PRESENT = "present", "pre"  #19:     PRESENT = "present", "pre"
    IMPERFECT = "imperfect", "imp"  #20:     IMPERFECT = "imperfect", "imp"
    FUTURE = "future", "fut"  #21:     FUTURE = "future", "fut"
    PERFECT = "perfect", "per"  #22:     PERFECT = "perfect", "per"
    PLUPERFECT = "pluperfect", "plp"  #23:     PLUPERFECT = "pluperfect", "plp"
# FUTURE_PERFECT = "future perfect", "fpr"


_coconut_call_set_names(Tense)  #27: class Voice(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #27: class Voice(Enum, settings=MultiValue, init="regular shorthand"):
class Voice(Enum):  #27: class Voice(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the voice of a verb."""  #28:     """Represents the voice of a verb."""

    ACTIVE = "active", "act"  #30:     ACTIVE = "active", "act"
    PASSIVE = "passive", "pas"  #31:     PASSIVE = "passive", "pas"


_coconut_call_set_names(Voice)  #34: class Mood(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #34: class Mood(Enum, settings=MultiValue, init="regular shorthand"):
class Mood(Enum):  #34: class Mood(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the mood of a verb."""  #35:     """Represents the mood of a verb."""

    INDICATIVE = "indicative", "ind"  #37:     INDICATIVE = "indicative", "ind"
    INFINITIVE = "infinitive", "inf"  #38:     INFINITIVE = "infinitive", "inf"
    IMPERATIVE = "imperative", "ipe"  #39:     IMPERATIVE = "imperative", "ipe"
    SUBJUNCTIVE = "subjunctive", "sbj"  #40:     SUBJUNCTIVE = "subjunctive", "sbj"
    PARTICIPLE = "participle", "ptc"  #41:     PARTICIPLE = "participle", "ptc"


_coconut_call_set_names(Mood)  #44: class Case(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #44: class Case(Enum, settings=MultiValue, init="regular shorthand"):
class Case(Enum):  #44: class Case(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the case of a noun."""  #45:     """Represents the case of a noun."""

    NOMINATIVE = "nominative", "nom"  #47:     NOMINATIVE = "nominative", "nom"
    VOCATIVE = "vocative", "voc"  #48:     VOCATIVE = "vocative", "voc"
    ACCUSATIVE = "accusative", "acc"  #49:     ACCUSATIVE = "accusative", "acc"
    GENITIVE = "genitive", "gen"  #50:     GENITIVE = "genitive", "gen"
    DATIVE = "dative", "dat"  #51:     DATIVE = "dative", "dat"
    ABLATIVE = "ablative", "abl"  #52:     ABLATIVE = "ablative", "abl"


_coconut_call_set_names(Case)  #55: class Gender(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #55: class Gender(Enum, settings=MultiValue, init="regular shorthand"):
class Gender(Enum):  #55: class Gender(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the gender of a noun or adjective."""  #56:     """Represents the gender of a noun or adjective."""

    MASCULINE = "masculine", "m"  #58:     MASCULINE = "masculine", "m"
    FEMININE = "feminine", "f"  #59:     FEMININE = "feminine", "f"
    NEUTER = "neuter", "n"  #60:     NEUTER = "neuter", "n"


_coconut_call_set_names(Gender)  #63: class Degree(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #63: class Degree(Enum, settings=MultiValue, init="regular shorthand"):
class Degree(Enum):  #63: class Degree(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the degree of an adjective."""  #64:     """Represents the degree of an adjective."""

    POSITIVE = "positive", "pos"  #66:     POSITIVE = "positive", "pos"
    COMPARATIVE = "comparative", "cmp"  #67:     COMPARATIVE = "comparative", "cmp"
    SUPERLATIVE = "superlative", "spr"  #68:     SUPERLATIVE = "superlative", "spr"


_coconut_call_set_names(Degree)  #71: class Person(Enum, settings=MultiValue, init="regular shorthand"):
@_coconut_handle_cls_kwargs(settings=MultiValue, init="regular shorthand")  #71: class Person(Enum, settings=MultiValue, init="regular shorthand"):
class Person(Enum):  #71: class Person(Enum, settings=MultiValue, init="regular shorthand"):
    """Represents the person of a verb."""  #72:     """Represents the person of a verb."""

    FIRST = 1, "1st person"  #74:     FIRST = 1, "1st person"
    SECOND = 2, "2nd person"  #75:     SECOND = 2, "2nd person"
    THIRD = 3, "3rd person"  #76:     THIRD = 3, "3rd person"


_coconut_call_set_names(Person)  #79: class EndingComponents(SimpleNamespace):
class EndingComponents(SimpleNamespace):  #79: class EndingComponents(SimpleNamespace):
    """A container for the grammatical components of an ending.

    Examples
    --------
    >>> foo = EndingComponents(case="nominative", gender="masculine", \
                               number="singular")
    >>> foo.case
    'nominative'
    """  #88:     """


_coconut_call_set_names(EndingComponents)  #91: @dataclass(init=True)
@dataclass(init=True)  #91: @dataclass(init=True)
class MultipleMeanings(_coconut.object):  #92: class MultipleMeanings:
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
    """  #114:     """

    meanings = _coconut.typing.cast(_coconut.typing.Any, _coconut.Ellipsis)  # type: list[str]  #116:     meanings: list[str]
    if "__annotations__" not in _coconut.locals():  #116:     meanings: list[str]
        __annotations__ = {}  # type: ignore  #116:     meanings: list[str]
    __annotations__["meanings"] = 'list[str]'  #116:     meanings: list[str]

    def __str__(self):  #118:     def __str__(self) -> str:
# type: (...) -> str
        return self.meanings[0]  #119:         return self.meanings[0]


    @_coconut_tco  #121:     def __repr__(self) -> str:
    def __repr__(self):  #121:     def __repr__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("MultipleMeanings({_coconut_format_0})".format, _coconut_format_0=(', '.join(self.meanings)))  #122:         return f"MultipleMeanings({', '.join(self.meanings)})"



_coconut_call_set_names(MultipleMeanings)  #125: class MultipleEndings(SimpleNamespace):
class MultipleEndings(SimpleNamespace):  #125: class MultipleEndings(SimpleNamespace):
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
    """  # noqa: D205  #152:     """  # noqa: D205

    @_coconut_tco  #154:     def get_all(self) -> list[str]:
    def get_all(self):  #154:     def get_all(self) -> list[str]:
# type: (...) -> list[str]
        """Returns a list of all the possible endings.

        Returns
        -------
        list[str]
            The endings.
        """  #161:         """
        return _coconut_tail_call(list, self.__dict__.values())  #162:         return list(self.__dict__.values())


    @_coconut_tco  #164:     def __str__(self) -> str:
    def __str__(self):  #164:     def __str__(self) -> str:
# type: (...) -> str
        return _coconut_tail_call("/".join, self.__dict__.values())  #165:         return "/".join(self.__dict__.values())


    def __add__(self, val2  # type: str  #167:     def __add__(self, val2: str) -> str:
        ):  #167:     def __add__(self, val2: str) -> str:
# type: (...) -> str
        return self.__str__() + val2  #168:         return self.__str__() + val2

# Allows for a prefix to be added to all of the endings.
# pragma: no cover
    @_coconut_tco  # pragma: no cover  #171:     def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
    def __radd__(self, val2  # type: str  # pragma: no cover  #171:     def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
        ):  # pragma: no cover  #171:     def __radd__(self, val2: str) -> MultipleEndings:  # pragma: no cover
# type: (...) -> MultipleEndings  # pragma: no cover
        prefixed = _coconut.dict(((key), ("{_coconut_format_0}{_coconut_format_1}".format(_coconut_format_0=(val2), _coconut_format_1=(value)))) for key, value in self.__dict__.items())  #172:         prefixed = {
        return _coconut_tail_call(MultipleEndings, **prefixed)  #175:         return MultipleEndings(**prefixed)


_coconut_call_set_names(MultipleEndings)  #177:         return MultipleEndings(**prefixed)
