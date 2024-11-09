from typing import Any, Union

from lemminflect.core.Inflections import Inflections
from lemminflect.core.Lemmatizer import Lemmatizer

class _Singleton:
    def __call__(
        cls: object, *args: list[Any], **kwargs: list[Any]
    ) -> Union[Inflections, Lemmatizer]: ...

class Singleton(_Singleton):
    pass
