from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete

class StemmerI(metaclass=ABCMeta):
    @abstractmethod
    def stem(self, token: Incomplete) -> Incomplete: ...
