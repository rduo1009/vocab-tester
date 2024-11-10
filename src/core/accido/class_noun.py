"""Representation of a Latin noun with endings."""

from __future__ import annotations

from functools import total_ordering
from typing import TYPE_CHECKING, overload

from .class_word import _Word
from .edge_cases import IRREGULAR_NOUNS
from .exceptions import InvalidInputError
from .misc import Case, ComponentsSubtype, EndingComponents, Gender, Number

if TYPE_CHECKING:
    from .type_aliases import Ending, Endings, Meaning, NounDeclension


@total_ordering
class Noun(_Word):
    """Representation of a Latin noun with endings.

    Attributes
    ----------
    nominative : str
    genitive : str | None
        The genitive, if applicable (only for regular nouns).
    meaning : Meaning
    declension : NounDeclension
        The declension of the noun. The value 0 represents an irregular
        declension.
    endings : Endings
    plurale_tantum : bool
        If the noun is a plurale tantum or not.
    gender : Gender | None
        The gender, if applicable (only for regular nouns).

    Examples
    --------
    >>> foo = Noun(
    ...     "ancilla",
    ...     "ancillae",
    ...     gender=Gender.FEMININE,
    ...     meaning="slavegirl",
    ... )
    >>> foo["Nnomsg"]
    'ancilla'

    Note that all arguments of Noun are keyword-only.

    >>> foo = Noun("ego", meaning="I")
    >>> foo["Nnomsg"]
    'ego'

    Notes
    -----
    Accido relies on the assumption that there are no neuter or plurale
    tantum fifth declension nouns (there doesn't seem to be any).
    """

    # fmt: off
    @overload
    def __init__(self, nominative: str, *, meaning: Meaning) -> None: ...
    @overload
    def __init__(self, nominative: str, genitive: str, *, gender: Gender, meaning: Meaning) -> None: ...
    # fmt: on

    def __init__(
        self,
        nominative: str,
        genitive: str | None = None,
        *,
        gender: Gender | None = None,
        meaning: Meaning,
    ) -> None:
        """Initialise Noun and determines the declension and endings.

        Parameters
        ----------
        nominative : str
        genitive : str | None
            The genitive, if applicable (only for regular nouns).
        gender : Gender | None
            The gender, if applicable (only for regular nouns).
        meaning : Meaning

        Raises
        ------
        InvalidInputError
            If the input is not valid (invalid gender value or genitive).
        """
        super().__init__()

        if gender:
            self.gender: Gender = gender

        self.nominative: str = nominative
        if genitive:
            self.genitive: str = genitive
        self.meaning: Meaning = meaning
        self.plurale_tantum: bool = False

        self._first: str = self.nominative
        self.declension: NounDeclension
        self._stem: str

        if self.nominative in IRREGULAR_NOUNS:
            self.endings = IRREGULAR_NOUNS[nominative]
            self.declension = 0
            return

        self._find_declension()

        self.endings = self._determine_endings()

        if self.gender == Gender.NEUTER:
            self._neuter_endings()

        if self.plurale_tantum:
            self.endings = {
                k: v for k, v in self.endings.items() if not k.endswith("sg")
            }

        # HACK: workaround for pydoclint
        if False:  # pragma: no cover # sourcery skip:remove-redundant-if
            raise InvalidInputError

    def _find_declension(self) -> None:
        # The ordering of this is strange because
        # e.g. ending -ei ends in 'i' as well as 'ei'
        # so 5th declension check must come before 2nd declension check, etc.
        if self.genitive.endswith("ei"):
            self.declension = 5
            self._stem = self.genitive[:-2]  # diei > di-
        elif self.genitive.endswith("ae"):
            self.declension = 1
            self._stem = self.genitive[:-2]  # puellae -> puell-
        elif self.genitive.endswith("i"):
            self.declension = 2
            self._stem = self.genitive[:-1]  # servi -> serv-
        elif self.genitive.endswith("is"):
            self.declension = 3
            self._stem = self.genitive[:-2]  # canis -> can-
        elif self.genitive.endswith("us"):
            self.declension = 4
            self._stem = self.genitive[:-2]  # manus -> man-

        elif self.genitive.endswith("uum"):
            self.declension = 4
            self._stem = self.genitive[:-3]  # manuum -> man-
            self.plurale_tantum = True
        elif self.genitive.endswith("arum"):
            self.declension = 1
            self._stem = self.genitive[:-4]  # puellarum -> puell-
            self.plurale_tantum = True
        elif self.genitive.endswith("orum"):
            self.declension = 2
            self._stem = self.genitive[:-4]  # servorum -> serv-
            self.plurale_tantum = True
        elif self.genitive.endswith("um"):
            self.declension = 3
            self._stem = self.genitive[:-2]  # canum -> can-
            self.plurale_tantum = True

        else:
            raise InvalidInputError(
                f"Invalid genitive form: '{self.genitive}'",
            )

    def _determine_endings(self) -> Endings:
        match self.declension:
            case 1:
                return {
                    "Nnomsg": self.nominative,  # puella
                    "Nvocsg": self.nominative,  # puella
                    "Naccsg": f"{self._stem}am",  # puellam
                    "Ngensg": self.genitive,  # puellae
                    "Ndatsg": f"{self._stem}ae",  # puellae
                    "Nablsg": f"{self._stem}a",  # puella
                    "Nnompl": f"{self._stem}ae",  # puellae
                    "Nvocpl": f"{self._stem}ae",  # puellae
                    "Naccpl": f"{self._stem}as",  # puellas
                    "Ngenpl": f"{self._stem}arum",  # puellarum
                    "Ndatpl": f"{self._stem}is",  # puellis
                    "Nablpl": f"{self._stem}is",  # puellis
                }

            case 2:
                return {
                    "Nnomsg": self.nominative,  # servus
                    "Nvocsg": (
                        self.nominative  # puer
                        if self.nominative.endswith("er")
                        else f"{self._stem}e"  # serve
                    ),
                    "Naccsg": f"{self._stem}um",  # servum
                    "Ngensg": self.genitive,  # servi
                    "Ndatsg": f"{self._stem}o",  # servo
                    "Nablsg": f"{self._stem}o",  # servo
                    "Nnompl": f"{self._stem}i",  # servi
                    "Nvocpl": f"{self._stem}i",  # servi
                    "Naccpl": f"{self._stem}os",  # servos
                    "Ngenpl": f"{self._stem}orum",  # servorum
                    "Ndatpl": f"{self._stem}is",  # servis
                    "Nablpl": f"{self._stem}is",  # servis
                }

            case 3:
                return {
                    "Nnomsg": self.nominative,  # mercator
                    "Nvocsg": self.nominative,  # mercator
                    "Naccsg": f"{self._stem}em",  # mercatorem
                    "Ngensg": self.genitive,  # mercatoris
                    "Ndatsg": f"{self._stem}i",  # mercatori
                    "Nablsg": f"{self._stem}e",  # mercatore
                    "Nnompl": f"{self._stem}es",  # mercatores
                    "Nvocpl": f"{self._stem}es",  # mercatores
                    "Naccpl": f"{self._stem}es",  # mercatores
                    "Ngenpl": f"{self._stem}um",  # mercatorum
                    "Ndatpl": f"{self._stem}ibus",  # mercatoribus
                    "Nablpl": f"{self._stem}ibus",  # mercatoribus
                }

            case 4:
                return {
                    "Nnomsg": self.nominative,  # manus
                    "Nvocsg": self.nominative,  # manus
                    "Naccsg": f"{self._stem}um",  # manum
                    "Ngensg": f"{self._stem}us",  # manus
                    "Ndatsg": f"{self._stem}ui",  # manui
                    "Nablsg": f"{self._stem}u",  # manu
                    "Nnompl": f"{self._stem}us",  # manus
                    "Nvocpl": f"{self._stem}us",  # manus
                    "Naccpl": f"{self._stem}us",  # manus
                    "Ngenpl": f"{self._stem}uum",  # manuum
                    "Ndatpl": f"{self._stem}ibus",  # manibus
                    "Nablpl": f"{self._stem}ibus",  # manibus
                }

        return {
            "Nnomsg": self.nominative,  # res
            "Nvocsg": self.nominative,  # res
            "Naccsg": f"{self._stem}em",  # rem
            "Ngensg": f"{self._stem}ei",  # rei
            "Ndatsg": f"{self._stem}ei",  # rei
            "Nablsg": f"{self._stem}e",  # re
            "Nnompl": f"{self._stem}es",  # res
            "Nvocpl": f"{self._stem}es",  # res
            "Naccpl": f"{self._stem}es",  # res
            "Ngenpl": f"{self._stem}erum",  # rerum
            "Ndatpl": f"{self._stem}ebus",  # rebus
            "Nablpl": f"{self._stem}ebus",  # rebus
        }

    def _neuter_endings(self) -> None:
        self.endings["Naccsg"] = self.nominative  # templum
        self.endings["Nvocsg"] = self.nominative  # templum

        if self.declension == 5:
            raise InvalidInputError(
                "Fifth declension nouns cannot be neuter "
                f"(noun '{self.nominative}' given)",
            )

        if self.declension == 4:
            self.endings["Nnompl"] = f"{self._stem}ua"  # cornua
            self.endings["Naccpl"] = f"{self._stem}ua"  # cornua
            self.endings["Nvocpl"] = f"{self._stem}ua"  # cornua
            self.endings["Ndatsg"] = f"{self._stem}u"  # cornu
            return

        # For the other declensions
        self.endings["Nnompl"] = f"{self._stem}a"  # templa
        self.endings["Naccpl"] = f"{self._stem}a"  # templa
        self.endings["Nvocpl"] = f"{self._stem}a"  # templa

    def get(self, *, case: Case, number: Number) -> Ending | None:
        """Return the ending of the noun.

        The function returns None if no ending is found.

        Parameters
        ----------
        case : Case
            The case of the noun.
        number : Number
            The number of the noun.

        Returns
        -------
        Ending | None
            The ending found, or None if no ending is found.

        Examples
        --------
        >>> foo = Noun(
        ...     "ancilla",
        ...     "ancillae",
        ...     gender=Gender.FEMININE,
        ...     meaning="slavegirl",
        ... )
        >>> foo.get(case=Case.NOMINATIVE, number=Number.SINGULAR)
        'ancilla'

        Note that all arguments of get are keyword-only.
        """
        short_case: str = case.shorthand
        short_number: str = number.shorthand

        return self.endings.get(f"N{short_case}{short_number}")

    def _create_components(self, key: str) -> EndingComponents:  # type: ignore[override]
        output: EndingComponents = EndingComponents(
            case=Case(key[1:4]),
            number=Number(key[4:6]),
        )
        output.string = f"{output.case.regular} {output.number.regular}"
        if self.declension == 0:
            output.subtype = ComponentsSubtype.PRONOUN
        return output

    def __repr__(self) -> str:
        return (
            f"Noun({self.nominative}, {self.genitive}, "
            f"{self.gender.regular}, {self.meaning})"
        )

    def __str__(self) -> str:
        return (
            f"{self.meaning}: {self.nominative}, "
            f"{self.genitive}, ({Gender(self.gender).shorthand})"
        )
