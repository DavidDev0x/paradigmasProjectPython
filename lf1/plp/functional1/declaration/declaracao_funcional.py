from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DeclaracaoFuncional(ABC):
    @abstractmethod
    def get_id(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_aridade(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_expressao(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, ambiente: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_tipo(self, amb: Any) -> Any:
        raise NotImplementedError
