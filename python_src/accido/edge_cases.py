#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7e008145

# Compiled with Coconut version 3.1.2

"""Contains edge case endings."""

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



try:  #3: from typing import Final
    _coconut_sys_0 = sys  # type: ignore  #3: from typing import Final
except _coconut.NameError:  #3: from typing import Final
    _coconut_sys_0 = _coconut_sentinel  #3: from typing import Final
sys = _coconut_sys  #3: from typing import Final
if sys.version_info >= (3, 8):  #3: from typing import Final
    if _coconut.typing.TYPE_CHECKING:  #3: from typing import Final
        from typing import Final  #3: from typing import Final
    else:  #3: from typing import Final
        try:  #3: from typing import Final
            Final = _coconut.typing.Final  #3: from typing import Final
        except _coconut.AttributeError as _coconut_imp_err:  #3: from typing import Final
            raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3: from typing import Final
else:  #3: from typing import Final
    from typing_extensions import Final  #3: from typing import Final
if _coconut_sys_0 is not _coconut_sentinel:  #3: from typing import Final
    sys = _coconut_sys_0  #3: from typing import Final

from .misc import MultipleEndings  #5: from .misc import MultipleEndings

if TYPE_CHECKING:  #7: if TYPE_CHECKING:
    from .type_aliases import Endings  #8:     from .type_aliases import Endings

#  NOTE: There are deponents, but am keeping them for future
# There also may be missing verbs
"""Contains third conjugation -io verbs."""  #12: """Contains third conjugation -io verbs."""
THIRD_IO_VERBS = _coconut.set(("abicio", "adicio", "aggredior", "capio", "concutio", "confugio", "conicio", "cupio", "deicio", "diripio", "disicio", "effugio", "eicio", "eripio", "facio", "fugio", "gradior", "iacio", "illicio", "ingredior", "inicio", "mori", "obicio", "patior", "percutio", "perfugio", "profugio", "proicio", "quatere", "rapio", "refugio", "reicio", "sapio", "subicio", "traicio",))  # type: Final[set[str]]  #13: THIRD_IO_VERBS: Final[set[str]] = {
if "__annotations__" not in _coconut.locals():  #13: THIRD_IO_VERBS: Final[set[str]] = {
    __annotations__ = {}  # type: ignore  #13: THIRD_IO_VERBS: Final[set[str]] = {
__annotations__["THIRD_IO_VERBS"] = 'Final[set[str]]'  #13: THIRD_IO_VERBS: Final[set[str]] = {


@_coconut_tco  #52: def check_io_verb(present: str) -> bool:
def check_io_verb(present  # type: str  #52: def check_io_verb(present: str) -> bool:
    ):  #52: def check_io_verb(present: str) -> bool:
# type: (...) -> bool
    """Checks if the given word matches any of the third conjugation -io
    verbs in the THIRD_IO_VERBS set.

    Parameters
    ----------
    present : str
        The present form verb to check

    Returns
    -------
    bool
        If the prefix matches a third conjugation -io verb
    """  # noqa: D205  #65:     """  # noqa: D205
    return _coconut_tail_call(any, (present.endswith(io_verb) for io_verb in THIRD_IO_VERBS))  #66:     return any(present.endswith(io_verb) for io_verb in THIRD_IO_VERBS)



"""Contains irregular verbs."""  #69: """Contains irregular verbs."""
IRREGULAR_VERBS = _coconut.dict((("sum", _coconut.dict((("Vpreactindsg1", "sum"), ("Vpreactindsg2", "es"), ("Vpreactindsg3", "est"), ("Vpreactindpl1", "sumus"), ("Vpreactindpl2", "estis"), ("Vpreactindpl3", "sunt"), ("Vimpactindsg1", "eram"), ("Vimpactindsg2", "eras"), ("Vimpactindsg3", "erat"), ("Vimpactindpl1", "eramus"), ("Vimpactindpl2", "eratis"), ("Vimpactindpl3", "erant"), ("Vperactindsg1", "fui"), ("Vperactindsg2", "fuisti"), ("Vperactindsg3", "fuit"), ("Vperactindpl1", "fuimus"), ("Vperactindpl2", "fuistis"), ("Vperactindpl3", "fuerunt"), ("Vplpactindsg1", "fueram"), ("Vplpactindsg2", "fueras"), ("Vplpactindsg3", "fuerat"), ("Vplpactindpl1", "fueramus"), ("Vplpactindpl2", "fueratis"), ("Vplpactindpl3", "fuerant"), ("Vpreactinf   ", "esse"), ("Vimpactsbjsg1", "essem"), ("Vimpactsbjsg2", "esses"), ("Vimpactsbjsg3", "esset"), ("Vimpactsbjpl1", "essemus"), ("Vimpactsbjpl2", "essetis"), ("Vimpactsbjpl3", "essent"), ("Vplpactsbjsg1", "fuissem"), ("Vplpactsbjsg2", "fuisses"), ("Vplpactsbjsg3", "fuisset"), ("Vplpactsbjpl1", "fuissemus"), ("Vplpactsbjpl2", "fuissetis"), ("Vplpactsbjpl3", "fuissent")))), ("possum", _coconut.dict((("Vpreactindsg1", "possum"), ("Vpreactindsg2", "potes"), ("Vpreactindsg3", "potest"), ("Vpreactindpl1", "possumus"), ("Vpreactindpl2", "potestis"), ("Vpreactindpl3", "possunt"), ("Vimpactindsg1", "poteram"), ("Vimpactindsg2", "poteras"), ("Vimpactindsg3", "poterat"), ("Vimpactindpl1", "poteramus"), ("Vimpactindpl2", "poteratis"), ("Vimpactindpl3", "poterant"), ("Vperactindsg1", "potui"), ("Vperactindsg2", "potuisti"), ("Vperactindsg3", "potuit"), ("Vperactindpl1", "potuimus"), ("Vperactindpl2", "potuistis"), ("Vperactindpl3", "potuerunt"), ("Vplpactindsg1", "potueram"), ("Vplpactindsg2", "potueras"), ("Vplpactindsg3", "potuerat"), ("Vplpactindpl1", "potueramus"), ("Vplpactindpl2", "potueratis"), ("Vplpactindpl3", "potuerant"), ("Vpreactinf   ", "posse"), ("Vimpactsbjsg1", "possem"), ("Vimpactsbjsg2", "posses"), ("Vimpactsbjsg3", "posset"), ("Vimpactsbjpl1", "possemus"), ("Vimpactsbjpl2", "possetis"), ("Vimpactsbjpl3", "possent"), ("Vplpactsbjsg1", "potuissem"), ("Vplpactsbjsg2", "potuisses"), ("Vplpactsbjsg3", "potuisset"), ("Vplpactsbjpl1", "potuissemus"), ("Vplpactsbjpl2", "potuissetis"), ("Vplpactsbjpl3", "potuissent")))), ("volo", _coconut.dict((("Vpreactindsg1", "volo"), ("Vpreactindsg2", "vis"), ("Vpreactindsg3", "vult"), ("Vpreactindpl1", "volumus"), ("Vpreactindpl2", "vultis"), ("Vpreactindpl3", "volunt"), ("Vimpactindsg1", "volebam"), ("Vimpactindsg2", "volebas"), ("Vimpactindsg3", "volebat"), ("Vimpactindpl1", "volebamus"), ("Vimpactindpl2", "volebatis"), ("Vimpactindpl3", "volebant"), ("Vperactindsg1", "volui"), ("Vperactindsg2", "voluisti"), ("Vperactindsg3", "voluit"), ("Vperactindpl1", "voluimus"), ("Vperactindpl2", "voluistis"), ("Vperactindpl3", "voluerunt"), ("Vplpactindsg1", "volueram"), ("Vplpactindsg2", "volueras"), ("Vplpactindsg3", "voluerat"), ("Vplpactindpl1", "volueramus"), ("Vplpactindpl2", "volueratis"), ("Vplpactindpl3", "voluerant"), ("Vpreactinf   ", "velle"), ("Vimpactsbjsg1", "vellem"), ("Vimpactsbjsg2", "velles"), ("Vimpactsbjsg3", "vellet"), ("Vimpactsbjpl1", "vellemus"), ("Vimpactsbjpl2", "velletis"), ("Vimpactsbjpl3", "vellent"), ("Vplpactsbjsg1", "voluissem"), ("Vplpactsbjsg2", "voluisses"), ("Vplpactsbjsg3", "voluisset"), ("Vplpactsbjpl1", "voluissemus"), ("Vplpactsbjpl2", "voluissetis"), ("Vplpactsbjpl3", "voluissent")))), ("nolo", _coconut.dict((("Vpreactindsg1", "nolo"), ("Vpreactindsg2", "non vis"), ("Vpreactindsg3", "non vult"), ("Vpreactindpl1", "nolumus"), ("Vpreactindpl2", "non vultis"), ("Vpreactindpl3", "nolunt"), ("Vimpactindsg1", "nolebam"), ("Vimpactindsg2", "nolebas"), ("Vimpactindsg3", "nolebat"), ("Vimpactindpl1", "nolebamus"), ("Vimpactindpl2", "nolebatis"), ("Vimpactindpl3", "nolebant"), ("Vperactindsg1", "nolui"), ("Vperactindsg2", "noluisti"), ("Vperactindsg3", "noluit"), ("Vperactindpl1", "noluimus"), ("Vperactindpl2", "noluistis"), ("Vperactindpl3", "noluerunt"), ("Vplpactindsg1", "nolueram"), ("Vplpactindsg2", "nolueras"), ("Vplpactindsg3", "noluerat"), ("Vplpactindpl1", "nolueramus"), ("Vplpactindpl2", "nolueratis"), ("Vplpactindpl3", "noluerant"), ("Vpreactinf   ", "nolle"), ("Vimpactsbjsg1", "nollem"), ("Vimpactsbjsg2", "nolles"), ("Vimpactsbjsg3", "nollet"), ("Vimpactsbjpl1", "nollemus"), ("Vimpactsbjpl2", "nolletis"), ("Vimpactsbjpl3", "nollent"), ("Vplpactsbjsg1", "noluissem"), ("Vplpactsbjsg2", "noluisses"), ("Vplpactsbjsg3", "noluisset"), ("Vplpactsbjpl1", "noluissemus"), ("Vplpactsbjpl2", "noluissetis"), ("Vplpactsbjpl3", "noluissent")))), ("fero", _coconut.dict((("Vpreactindsg1", "fero"), ("Vpreactindsg2", "fers"), ("Vpreactindsg3", "fert"), ("Vpreactindpl1", "ferimus"), ("Vpreactindpl2", "fertis"), ("Vpreactindpl3", "ferunt"), ("Vimpactindsg1", "ferebam"), ("Vimpactindsg2", "ferebas"), ("Vimpactindsg3", "ferebat"), ("Vimpactindpl1", "ferebamus"), ("Vimpactindpl2", "ferebatis"), ("Vimpactindpl3", "ferebant"), ("Vperactindsg1", "tuli"), ("Vperactindsg2", "tulisti"), ("Vperactindsg3", "tulit"), ("Vperactindpl1", "tulimus"), ("Vperactindpl2", "tulistis"), ("Vperactindpl3", "tulerunt"), ("Vplpactindsg1", "tuleram"), ("Vplpactindsg2", "tuleras"), ("Vplpactindsg3", "tulerat"), ("Vplpactindpl1", "tuleramus"), ("Vplpactindpl2", "tuleratis"), ("Vplpactindpl3", "tulerant"), ("Vpreactinf   ", "ferre"), ("Vpreactipesg2", "fer"), ("Vpreactipepl2", "ferte"), ("Vimpactsbjsg1", "ferrem"), ("Vimpactsbjsg2", "ferres"), ("Vimpactsbjsg3", "ferret"), ("Vimpactsbjpl1", "ferremus"), ("Vimpactsbjpl2", "ferretis"), ("Vimpactsbjpl3", "ferrent"), ("Vplpactsbjsg1", "tulissem"), ("Vplpactsbjsg2", "tulisses"), ("Vplpactsbjsg3", "tulisset"), ("Vplpactsbjpl1", "tulissemus"), ("Vplpactsbjpl2", "tulissetis"), ("Vplpactsbjpl3", "tulissent")))), ("eo", _coconut.dict((("Vpreactindsg1", "eo"), ("Vpreactindsg2", "is"), ("Vpreactindsg3", "it"), ("Vpreactindpl1", "imus"), ("Vpreactindpl2", "itis"), ("Vpreactindpl3", "eunt"), ("Vimpactindsg1", "ibam"), ("Vimpactindsg2", "ibas"), ("Vimpactindsg3", "ibat"), ("Vimpactindpl1", "ibamus"), ("Vimpactindpl2", "ibatis"), ("Vimpactindpl3", "ibant"), ("Vperactindsg1", "ii"), ("Vperactindsg2", "iisti"), ("Vperactindsg3", "iit"), ("Vperactindpl1", "iimus"), ("Vperactindpl2", "iistis"), ("Vperactindpl3", "ierunt"), ("Vplpactindsg1", "ieram"), ("Vplpactindsg2", "ieras"), ("Vplpactindsg3", "ierat"), ("Vplpactindpl1", "ieramus"), ("Vplpactindpl2", "ieratis"), ("Vplpactindpl3", "ierant"), ("Vpreactinf   ", "ire"), ("Vpreactipesg2", "i"), ("Vpreactipepl2", "ite"), ("Vimpactsbjsg1", "irem"), ("Vimpactsbjsg2", "ires"), ("Vimpactsbjsg3", "iret"), ("Vimpactsbjpl1", "iremus"), ("Vimpactsbjpl2", "iretis"), ("Vimpactsbjpl3", "irent"), ("Vplpactsbjsg1", "iissem"), ("Vplpactsbjsg2", "iisses"), ("Vplpactsbjsg3", "iisset"), ("Vplpactsbjpl1", "iissemus"), ("Vplpactsbjpl2", "iissetis"), ("Vplpactsbjpl3", "iissent")))), ("absum", _coconut.dict((("Vpreactindsg1", "absum"), ("Vpreactindsg2", "abes"), ("Vpreactindsg3", "abest"), ("Vpreactindpl1", "absumus"), ("Vpreactindpl2", "abestis"), ("Vpreactindpl3", "absunt"), ("Vimpactindsg1", "aberam"), ("Vimpactindsg2", "aberas"), ("Vimpactindsg3", "aberat"), ("Vimpactindpl1", "aberamus"), ("Vimpactindpl2", "aberatis"), ("Vimpactindpl3", "aberant"), ("Vperactindsg1", "afui"), ("Vperactindsg2", "afuisti"), ("Vperactindsg3", "afuit"), ("Vperactindpl1", "afuimus"), ("Vperactindpl2", "afuistis"), ("Vperactindpl3", "afuerunt"), ("Vplpactindsg1", "afueram"), ("Vplpactindsg2", "afueras"), ("Vplpactindsg3", "afuerat"), ("Vplpactindpl1", "afueramus"), ("Vplpactindpl2", "afueratis"), ("Vplpactindpl3", "afuerant"), ("Vpreactinf   ", "abesse"), ("Vimpactsbjsg1", "abessem"), ("Vimpactsbjsg2", "abesses"), ("Vimpactsbjsg3", "abesset"), ("Vimpactsbjpl1", "abessemus"), ("Vimpactsbjpl2", "abessetis"), ("Vimpactsbjpl3", "abessent"), ("Vplpactsbjsg1", "afuissem"), ("Vplpactsbjsg2", "afuisses"), ("Vplpactsbjsg3", "afuisset"), ("Vplpactsbjpl1", "afuissemus"), ("Vplpactsbjpl2", "afuissetis"), ("Vplpactsbjpl3", "afuissent")))), ("adsum", _coconut.dict((("Vpreactindsg1", "adsum"), ("Vpreactindsg2", "ades"), ("Vpreactindsg3", "adest"), ("Vpreactindpl1", "adsumus"), ("Vpreactindpl2", "adestis"), ("Vpreactindpl3", "adsunt"), ("Vimpactindsg1", "aderam"), ("Vimpactindsg2", "aderas"), ("Vimpactindsg3", "aderat"), ("Vimpactindpl1", "aderamus"), ("Vimpactindpl2", "aderatis"), ("Vimpactindpl3", "aderant"), ("Vperactindsg1", "adfui"), ("Vperactindsg2", "adfuisti"), ("Vperactindsg3", "adfuit"), ("Vperactindpl1", "adfuimus"), ("Vperactindpl2", "adfuistis"), ("Vperactindpl3", "adfuerunt"), ("Vplpactindsg1", "adfueram"), ("Vplpactindsg2", "adfueras"), ("Vplpactindsg3", "adfuerat"), ("Vplpactindpl1", "adfueramus"), ("Vplpactindpl2", "adfueratis"), ("Vplpactindpl3", "adfuerant"), ("Vpreactinf   ", "adesse"), ("Vimpactsbjsg1", "adessem"), ("Vimpactsbjsg2", "adesses"), ("Vimpactsbjsg3", "adesset"), ("Vimpactsbjpl1", "adessemus"), ("Vimpactsbjpl2", "adessetis"), ("Vimpactsbjpl3", "adessent"), ("Vplpactsbjsg1", "adfuissem"), ("Vplpactsbjsg2", "adfuisses"), ("Vplpactsbjsg3", "adfuisset"), ("Vplpactsbjpl1", "adfuissemus"), ("Vplpactsbjpl2", "adfuissetis"), ("Vplpactsbjpl3", "adfuissent"))))))  # type: Final[dict[str, Endings]]  #70: IRREGULAR_VERBS: Final[dict[str, Endings]] = {
if "__annotations__" not in _coconut.locals():  #70: IRREGULAR_VERBS: Final[dict[str, Endings]] = {
    __annotations__ = {}  # type: ignore  #70: IRREGULAR_VERBS: Final[dict[str, Endings]] = {
__annotations__["IRREGULAR_VERBS"] = 'Final[dict[str, Endings]]'  #70: IRREGULAR_VERBS: Final[dict[str, Endings]] = {


"""Contains verbs that are derived from the main irregular verbs (usually
having a prefix)."""  #391: having a prefix)."""
DERIVED_IRREGULAR_VERBS = _coconut.dict((("eo", _coconut.set(("abeo", "adeo", "ambeo", "circumeo", "coeo", "deeo", "dispereo", "exeo", "ineo", "intereo", "introeo", "nequeo", "obeo", "pereo", "praetereo", "prodeo", "queo", "redeo", "subeo", "transabeo", "transeo", "veneo",))), ("fero", _coconut.set(("affero", "aufero", "circumfero", "confero", "defero", "differo", "effero", "infero", "interfero", "introfero", "offero", "perfero", "postfero", "praefero", "profero", "refero", "suffero", "transfero",)))))  # type: Final[dict[str, set[str]]]  #392: DERIVED_IRREGULAR_VERBS: Final[dict[str, set[str]]] = {
if "__annotations__" not in _coconut.locals():  #392: DERIVED_IRREGULAR_VERBS: Final[dict[str, set[str]]] = {
    __annotations__ = {}  # type: ignore  #392: DERIVED_IRREGULAR_VERBS: Final[dict[str, set[str]]] = {
__annotations__["DERIVED_IRREGULAR_VERBS"] = 'Final[dict[str, set[str]]]'  #392: DERIVED_IRREGULAR_VERBS: Final[dict[str, set[str]]] = {


# NOTE: This entire thing will probably need to be reworked at some point
# Notably allowing the given perfect stem to be used so that I don't have
# to write everything manually

"""Contains the endings that are used for the derived irregular verbs."""  #444: """Contains the endings that are used for the derived irregular verbs."""
DERIVED_IRREGULAR_ENDINGS = _coconut.dict((("eo", _coconut.dict((("Vpreactindsg1", "eo"), ("Vpreactindsg2", "is"), ("Vpreactindsg3", "it"), ("Vpreactindpl1", "imus"), ("Vpreactindpl2", "itis"), ("Vpreactindpl3", "eunt"), ("Vimpactindsg1", "ibam"), ("Vimpactindsg2", "ibas"), ("Vimpactindsg3", "ibat"), ("Vimpactindpl1", "ibamus"), ("Vimpactindpl2", "ibatis"), ("Vimpactindpl3", "ibant"), ("Vperactindsg1", "ii"), ("Vperactindsg2", "isti"), ("Vperactindsg3", "iit"), ("Vperactindpl1", "iimus"), ("Vperactindpl2", "istis"), ("Vperactindpl3", "ierunt"), ("Vplpactindsg1", "ieram"), ("Vplpactindsg2", "ieras"), ("Vplpactindsg3", "ierat"), ("Vplpactindpl1", "ieramus"), ("Vplpactindpl2", "ieratis"), ("Vplpactindpl3", "ierant"), ("Vpreactinf   ", "ire"), ("Vpreactipesg2", "i"), ("Vpreactipepl2", "ite"), ("Vimpactsbjsg1", "irem"), ("Vimpactsbjsg2", "ires"), ("Vimpactsbjsg3", "iret"), ("Vimpactsbjpl1", "iremus"), ("Vimpactsbjpl2", "iretis"), ("Vimpactsbjpl3", "irent"), ("Vplpactsbjsg1", "issem"), ("Vplpactsbjsg2", "isses"), ("Vplpactsbjsg3", "isset"), ("Vplpactsbjpl1", "issemus"), ("Vplpactsbjpl2", "issetis"), ("Vplpactsbjpl3", "issent")))), ("fero", _coconut.dict((("Vpreactindsg1", "fero"), ("Vpreactindsg2", "fers"), ("Vpreactindsg3", "fert"), ("Vpreactindpl1", "ferimus"), ("Vpreactindpl2", "fertis"), ("Vpreactindpl3", "ferunt"), ("Vimpactindsg1", "ferebam"), ("Vimpactindsg2", "ferebas"), ("Vimpactindsg3", "ferebat"), ("Vimpactindpl1", "ferebamus"), ("Vimpactindpl2", "ferebatis"), ("Vimpactindpl3", "ferebant"), ("Vperactindsg1", "tuli"), ("Vperactindsg2", "tulisti"), ("Vperactindsg3", "tulit"), ("Vperactindpl1", "tulimus"), ("Vperactindpl2", "tulistis"), ("Vperactindpl3", "tulerunt"), ("Vplpactindsg1", "tuleram"), ("Vplpactindsg2", "tuleras"), ("Vplpactindsg3", "tulerat"), ("Vplpactindpl1", "tuleramus"), ("Vplpactindpl2", "tuleratis"), ("Vplpactindpl3", "tulerant"), ("Vpreactinf   ", "ferre"), ("Vpreactipesg2", "fer"), ("Vpreactipepl2", "ferte"), ("Vimpactsbjsg1", "ferrem"), ("Vimpactsbjsg2", "ferres"), ("Vimpactsbjsg3", "ferret"), ("Vimpactsbjpl1", "ferremus"), ("Vimpactsbjpl2", "ferretis"), ("Vimpactsbjpl3", "ferrent"), ("Vplpactsbjsg1", "tulissem"), ("Vplpactsbjsg2", "tulisses"), ("Vplpactsbjsg3", "tulisset"), ("Vplpactsbjpl1", "tulissemus"), ("Vplpactsbjpl2", "tulissetis"), ("Vplpactsbjpl3", "tulissent"))))))  # type: Final[dict[str, Endings]]  #445: DERIVED_IRREGULAR_ENDINGS: Final[dict[str, Endings]] = {
if "__annotations__" not in _coconut.locals():  #445: DERIVED_IRREGULAR_ENDINGS: Final[dict[str, Endings]] = {
    __annotations__ = {}  # type: ignore  #445: DERIVED_IRREGULAR_ENDINGS: Final[dict[str, Endings]] = {
__annotations__["DERIVED_IRREGULAR_ENDINGS"] = 'Final[dict[str, Endings]]'  #445: DERIVED_IRREGULAR_ENDINGS: Final[dict[str, Endings]] = {


def find_irregular_endings(present  # type: str  #531: def find_irregular_endings(present: str) -> Endings | None:
    ):  #531: def find_irregular_endings(present: str) -> Endings | None:
# type: (...) -> _coconut.typing.Union[Endings, None]
    """Detects if a verb is irregular (using the irregular verb dictionary)
    and returns its endings.

    Parameters
    ----------
    present : str
        The present form verb to check.

    Returns
    -------
    Endings | None
        The endings. None if the verb is not irregular.
    """  # noqa: D205  #544:     """  # noqa: D205

    @_coconut_tco  #546:     def _prefix(
    def _prefix(pre,  # type: str  #546:     def _prefix(
        endings,  # type: Endings  #546:     def _prefix(
        ):  #546:     def _prefix(
# type: (...) -> dict[str, _coconut.typing.Union[str, MultipleEndings]]
        return _coconut_tail_call(_coconut.dict, (((key), (pre + value)) for key, value in endings.items()))  #550:         return {key: pre + value for key, value in endings.items()}

# pragma: no cover
    if present in IRREGULAR_VERBS:  # pragma: no cover  #552:     if present in IRREGULAR_VERBS:  # pragma: no cover
        return IRREGULAR_VERBS[present]  #553:         return IRREGULAR_VERBS[present]

    for (irregular_suffix, suffix_list,) in DERIVED_IRREGULAR_VERBS.items():  #555:     for (
        if present in suffix_list:  #559:         if present in suffix_list:
            return _prefix(present.rstrip(irregular_suffix), DERIVED_IRREGULAR_ENDINGS[irregular_suffix])  #560:             return _prefix(

    return None  #565:     return None



"""Contains irregular nouns."""  #568: """Contains irregular nouns."""
IRREGULAR_NOUNS = _coconut.dict((("ego", _coconut.dict((("Nnomsg", "ego"), ("Nvocsg", "ego"), ("Naccsg", "me"), ("Ngensg", "mei"), ("Ndatsg", "mihi"), ("Nablsg", "me"), ("Nnompl", "nos"), ("Nvocpl", "nos"), ("Naccpl", "nos"), ("Ngenpl", MultipleEndings(regular="nostri", partitive="nostrum")), ("Ndatpl", "nobis"), ("Nablpl", "nobis")))), ("tu", _coconut.dict((("Nnomsg", "tu"), ("Nvocsg", "tu"), ("Naccsg", "te"), ("Ngensg", "tui"), ("Ndatsg", "tibi"), ("Nablsg", "te"), ("Nnompl", "vos"), ("Nvocpl", "vos"), ("Naccpl", "vos"), ("Ngenpl", MultipleEndings(regular="vestri", partitive="vestrum")), ("Ndatpl", "vobis"), ("Nablpl", "vobis")))), ("se", _coconut.dict((("Naccsg", "se"), ("Ngensg", "sui"), ("Ndatsg", "sibi"), ("Nablsg", "se"), ("Naccpl", "se"), ("Ngenpl", "sui"), ("Ndatpl", "sibi"), ("Nablpl", "se"))))))  # type: Final[dict[str, Endings]]  #569: IRREGULAR_NOUNS: Final[dict[str, Endings]] = {
if "__annotations__" not in _coconut.locals():  #569: IRREGULAR_NOUNS: Final[dict[str, Endings]] = {
    __annotations__ = {}  # type: ignore  #569: IRREGULAR_NOUNS: Final[dict[str, Endings]] = {
__annotations__["IRREGULAR_NOUNS"] = 'Final[dict[str, Endings]]'  #569: IRREGULAR_NOUNS: Final[dict[str, Endings]] = {


"""Contains adjectives that end in -lis, and thus have irregular
superlatives."""  #612: superlatives."""
LIS_ADJECTIVES = _coconut.set(("facilis", "difficilis", "similis", "dissimilis", "gracilis", "humilis",))  # type: Final[set[str]]  #613: LIS_ADJECTIVES: Final[set[str]] = {
if "__annotations__" not in _coconut.locals():  #613: LIS_ADJECTIVES: Final[set[str]] = {
    __annotations__ = {}  # type: ignore  #613: LIS_ADJECTIVES: Final[set[str]] = {
__annotations__["LIS_ADJECTIVES"] = 'Final[set[str]]'  #613: LIS_ADJECTIVES: Final[set[str]] = {


"""Contains adjectives that have irregular forms in the comparative,
superlative and adverb forms.
Note that some of these adjectives do not have adverb forms, so the adverb
forms are given a None value instead."""  #626: forms are given a None value instead."""
IRREGULAR_ADJECTIVES = _coconut.dict((("bonus", ["melior", "optim", "bene", "melius", "optime"]), ("malus", ["peior", "pessim", "male", "peius", "pessime"]), ("magnus", ["maior", "maxim", None, None, None]), ("parvus", ["minor", "minim", None, None, None]), ("multus", ["plus", "plurim", None, None, None]), ("nequam", ["nequior", "nequissim", None, None, None]), ("frugi", ["frugalior", "frugalissim", "frugaliter", "frugalius", "frugalissime"]), ("dexter", ["dexterior", "dextim", None, None, None])))  # type: Final[dict[str, list[_coconut.typing.Union[str, None]]]]  #627: IRREGULAR_ADJECTIVES: Final[dict[str, list[str | None]]] = {
if "__annotations__" not in _coconut.locals():  #627: IRREGULAR_ADJECTIVES: Final[dict[str, list[str | None]]] = {
    __annotations__ = {}  # type: ignore  #627: IRREGULAR_ADJECTIVES: Final[dict[str, list[str | None]]] = {
__annotations__["IRREGULAR_ADJECTIVES"] = 'Final[dict[str, list[_coconut.typing.Union[str, None]]]]'  #627: IRREGULAR_ADJECTIVES: Final[dict[str, list[str | None]]] = {


"""Contains pronouns, which all have irregular endings."""  #647: """Contains pronouns, which all have irregular endings."""
PRONOUNS = _coconut.dict((("hic", _coconut.dict((("Pmnomsg", "hic"), ("Pmaccsg", "hunc"), ("Pmgensg", "huius"), ("Pmdatsg", "huic"), ("Pmablsg", "hoc"), ("Pmnompl", "hi"), ("Pmaccpl", "hos"), ("Pmgenpl", "horum"), ("Pmdatpl", "his"), ("Pmablpl", "his"), ("Pfnomsg", "haec"), ("Pfaccsg", "hanc"), ("Pfgensg", "huius"), ("Pfdatsg", "huic"), ("Pfablsg", "hac"), ("Pfnompl", "hae"), ("Pfaccpl", "has"), ("Pfgenpl", "harum"), ("Pfdatpl", "his"), ("Pfablpl", "his"), ("Pnnomsg", "hoc"), ("Pnaccsg", "hoc"), ("Pngensg", "huius"), ("Pndatsg", "huic"), ("Pnablsg", "hoc"), ("Pnnompl", "haec"), ("Pnaccpl", "haec"), ("Pngenpl", "horum"), ("Pndatpl", "his"), ("Pnablpl", "his")))), ("ille", _coconut.dict((("Pmnomsg", "ille"), ("Pmaccsg", "illum"), ("Pmgensg", "illius"), ("Pmdatsg", "illi"), ("Pmablsg", "illo"), ("Pmnompl", "illi"), ("Pmaccpl", "illos"), ("Pmgenpl", "illorum"), ("Pmdatpl", "illis"), ("Pmablpl", "illis"), ("Pfnomsg", "illa"), ("Pfaccsg", "illam"), ("Pfgensg", "illius"), ("Pfdatsg", "illi"), ("Pfablsg", "illa"), ("Pfnompl", "illae"), ("Pfaccpl", "illas"), ("Pfgenpl", "illarum"), ("Pfdatpl", "illis"), ("Pfablpl", "illis"), ("Pnnomsg", "illud"), ("Pnaccsg", "illud"), ("Pngensg", "illius"), ("Pndatsg", "illi"), ("Pnablsg", "illo"), ("Pnnompl", "illa"), ("Pnaccpl", "illa"), ("Pngenpl", "illorum"), ("Pndatpl", "illis"), ("Pnablpl", "illis")))), ("is", _coconut.dict((("Pmnomsg", "is"), ("Pmaccsg", "eum"), ("Pmgensg", "eius"), ("Pmdatsg", "ei"), ("Pmablsg", "eo"), ("Pmnompl", "ei"), ("Pmaccpl", "eos"), ("Pmgenpl", "eorum"), ("Pmdatpl", "eis"), ("Pmablpl", "eis"), ("Pfnomsg", "ea"), ("Pfaccsg", "eam"), ("Pfgensg", "eius"), ("Pfdatsg", "ei"), ("Pfablsg", "ea"), ("Pfnompl", "eae"), ("Pfaccpl", "eas"), ("Pfgenpl", "earum"), ("Pfdatpl", "eis"), ("Pfablpl", "eis"), ("Pnnomsg", "id"), ("Pnaccsg", "id"), ("Pngensg", "eius"), ("Pndatsg", "ei"), ("Pnablsg", "eo"), ("Pnnompl", "ea"), ("Pnaccpl", "ea"), ("Pngenpl", "eorum"), ("Pndatpl", "eis"), ("Pnablpl", "eis")))), ("ipse", _coconut.dict((("Pmnomsg", "ipse"), ("Pmaccsg", "ipsum"), ("Pmgensg", "ipsius"), ("Pmdatsg", "ipsi"), ("Pmablsg", "ipso"), ("Pmnompl", "ipsi"), ("Pmaccpl", "ipsos"), ("Pmgenpl", "ipsorum"), ("Pmdatpl", "ipsis"), ("Pmablpl", "ipsis"), ("Pfnomsg", "ipsa"), ("Pfaccsg", "ipsam"), ("Pfgensg", "ipsius"), ("Pfdatsg", "ipsi"), ("Pfablsg", "ipsa"), ("Pfnompl", "ipsae"), ("Pfaccpl", "ipsas"), ("Pfgenpl", "ipsarum"), ("Pfdatpl", "ipsis"), ("Pfablpl", "ipsis"), ("Pnnomsg", "ipsum"), ("Pnaccsg", "ipsum"), ("Pngensg", "ipsius"), ("Pndatsg", "ipsi"), ("Pnablsg", "ipso"), ("Pnnompl", "ipsa"), ("Pnaccpl", "ipsa"), ("Pngenpl", "ipsorum"), ("Pndatpl", "ipsis"), ("Pnablpl", "ipsis")))), ("idem", _coconut.dict((("Pmnomsg", "idem"), ("Pmaccsg", "eundem"), ("Pmgensg", "eiusdem"), ("Pmdatsg", "eidem"), ("Pmablsg", "eodem"), ("Pmnompl", "eidem"), ("Pmaccpl", "eosdem"), ("Pmgenpl", "eorundem"), ("Pmdatpl", "eisdem"), ("Pmablpl", "eisdem"), ("Pfnomsg", "eadem"), ("Pfaccsg", "eandem"), ("Pfgensg", "eiusdem"), ("Pfdatsg", "eidem"), ("Pfablsg", "eadem"), ("Pfnompl", "eaedem"), ("Pfaccpl", "easdem"), ("Pfgenpl", "earundem"), ("Pfdatpl", "eisdem"), ("Pfablpl", "eisdem"), ("Pnnomsg", "idem"), ("Pnaccsg", "idem"), ("Pngensg", "eiusdem"), ("Pndatsg", "eidem"), ("Pnablsg", "eodem"), ("Pnnompl", "eadem"), ("Pnaccpl", "eadem"), ("Pngenpl", "eorundem"), ("Pndatpl", "eisdem"), ("Pnablpl", "eisdem")))), ("qui", _coconut.dict((("Pmnomsg", "qui"), ("Pmaccsg", "quem"), ("Pmgensg", "cuius"), ("Pmdatsg", "cui"), ("Pmablsg", "quo"), ("Pmnompl", "qui"), ("Pmaccpl", "quos"), ("Pmgenpl", "quorum"), ("Pmdatpl", "quibus"), ("Pmablpl", "quibus"), ("Pfnomsg", "quae"), ("Pfaccsg", "quam"), ("Pfgensg", "cuius"), ("Pfdatsg", "cui"), ("Pfablsg", "qua"), ("Pfnompl", "quae"), ("Pfaccpl", "quas"), ("Pfgenpl", "quarum"), ("Pfdatpl", "quibus"), ("Pfablpl", "quibus"), ("Pnnomsg", "quod"), ("Pnaccsg", "quod"), ("Pngensg", "cuius"), ("Pndatsg", "cui"), ("Pnablsg", "quo"), ("Pnnompl", "quae"), ("Pnaccpl", "quae"), ("Pngenpl", "quorum"), ("Pndatpl", "quibus"), ("Pnablpl", "quibus")))), ("quidam", _coconut.dict((("Pmnomsg", "quidam"), ("Pmaccsg", "quendam"), ("Pmgensg", "cuiusdam"), ("Pmdatsg", "cuidam"), ("Pmablsg", "quodam"), ("Pmnompl", "quidam"), ("Pmaccpl", "quosdam"), ("Pmgenpl", "quorundam"), ("Pmdatpl", "quibusdam"), ("Pmablpl", "quibusdam"), ("Pfnomsg", "quaedam"), ("Pfaccsg", "quandam"), ("Pfgensg", "cuiusdam"), ("Pfdatsg", "cuidam"), ("Pfablsg", "quadam"), ("Pfnompl", "quaedam"), ("Pfaccpl", "quasdam"), ("Pfgenpl", "quarundam"), ("Pfdatpl", "quibusdam"), ("Pfablpl", "quibusdam"), ("Pnnomsg", "quoddam"), ("Pnaccsg", "quoddam"), ("Pngensg", "cuiusdam"), ("Pndatsg", "cuidam"), ("Pnablsg", "quodam"), ("Pnnompl", "quaedam"), ("Pnaccpl", "quaedam"), ("Pngenpl", "quorundam"), ("Pndatpl", "quibusdam"), ("Pnablpl", "quibusdam"))))))  # type: Final[dict[str, Endings]]  #648: PRONOUNS: Final[dict[str, Endings]] = {
if "__annotations__" not in _coconut.locals():  #648: PRONOUNS: Final[dict[str, Endings]] = {
    __annotations__ = {}  # type: ignore  #648: PRONOUNS: Final[dict[str, Endings]] = {
__annotations__["PRONOUNS"] = 'Final[dict[str, Endings]]'  #648: PRONOUNS: Final[dict[str, Endings]] = {
