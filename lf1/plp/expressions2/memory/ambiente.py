from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Ambiente(ABC):
    @abstractmethod
    def incrementa(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def map(self, id_arg: Any, tipo_id: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id_arg: Any) -> Any:
        raise NotImplementedError
