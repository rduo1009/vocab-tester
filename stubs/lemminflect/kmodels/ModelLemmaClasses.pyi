# Auto-generated by stubgen

from _typeshed import Incomplete

class ModelLemmaClasses:
    rules: list[str]
    rules_dict: dict[str, int]
    def __init__(self, fn: Incomplete | None = None) -> None: ...
    def getRuleIndex(
        self, rule: tuple[Incomplete, Incomplete, Incomplete] | str
    ) -> int: ...
    @staticmethod
    def computeSuffixRule(
        infl: Incomplete, lemma: str
    ) -> tuple[Incomplete, Incomplete, Incomplete]: ...
    @classmethod
    def saveFromRuleTuples(
        cls: object,
        fn: Incomplete,
        rules: set[tuple[Incomplete, Incomplete, Incomplete]],
    ) -> None: ...