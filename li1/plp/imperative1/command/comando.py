from __future__ import annotations
from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, ambiente): ...

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool: ...
