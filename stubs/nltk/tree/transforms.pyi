from _typeshed import Incomplete

__all__ = ["chomsky_normal_form", "un_chomsky_normal_form", "collapse_unary"]

def chomsky_normal_form(
    tree: Incomplete,
    factor: str = "right",
    horzMarkov: Incomplete | None = None,
    vertMarkov: int = 0,
    childChar: str = "|",
    parentChar: str = "^",
) -> None: ...
def un_chomsky_normal_form(
    tree: Incomplete,
    expandUnary: bool = True,
    childChar: str = "|",
    parentChar: str = "^",
    unaryChar: str = "+",
) -> None: ...
def collapse_unary(
    tree: Incomplete,
    collapsePOS: bool = False,
    collapseRoot: bool = False,
    joinChar: str = "+",
) -> None: ...
