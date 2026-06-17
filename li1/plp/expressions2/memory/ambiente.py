from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Ambiente(ABC):
    @abstractmethod
    def incrementa(self) -> None: ...

    @abstractmethod
    def restaura(self) -> None: ...

    @abstractmethod
    def map(self, id_arg: Any, valor_id: Any) -> None: ...

    @abstractmethod
    def get(self, id_arg: Any) -> Any: ...
