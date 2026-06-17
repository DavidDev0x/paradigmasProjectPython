from __future__ import annotations
from abc import ABC, abstractmethod

class Declaracao(ABC):
    @abstractmethod
    def elabora(self, ambiente): ...

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool: ...
