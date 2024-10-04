from _typeshed import Incomplete

__all__ = ["TreePrettyPrinter"]

class TreePrettyPrinter:
    def __init__(
        self,
        tree: Incomplete,
        sentence: Incomplete | None = None,
        highlight: Incomplete = (),
    ) -> None: ...
    @staticmethod
    def nodecoords(
        tree: Incomplete, sentence: Incomplete, highlight: Incomplete
    ) -> Incomplete: ...
    def text(
        self,
        nodedist: int = 1,
        unicodelines: bool = False,
        html: bool = False,
        ansi: bool = False,
        nodecolor: str = "blue",
        leafcolor: str = "red",
        funccolor: str = "green",
        abbreviate: Incomplete | None = None,
        maxwidth: int = 16,
    ) -> Incomplete: ...
    def svg(
        self,
        nodecolor: str = "blue",
        leafcolor: str = "red",
        funccolor: str = "green",
    ) -> Incomplete: ...
