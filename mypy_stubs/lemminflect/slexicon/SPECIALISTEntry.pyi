from typing import Any

class StandardVariant:
    vtype: Any
    isgroup: Any
    irreg: Any
    def __init__(
        self,
        vtype: Any,
        isgroup: bool = False,
        irreg: Any | None = None,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class AuxModVariant:
    inflection: Any
    form: Any
    agreements: Any
    negative: Any
    def __init__(
        self,
        inflection: Any,
        form: Any,
        agreements: Any,
        negative: Any,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class SPECIALISTEntry:
    EUI: Any
    base: Any
    category: Any
    spelling_variant: Any
    features: Any
    acronym_of: Any
    nominalization_of: Any
    nominalization: Any
    variants: Any
    def __init__(self) -> None: ...
    def getString(self) -> str: ...
