from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ExpressaoComplexa(ABC):
    @abstractmethod
    def avaliar(self, amb: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, amb: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_tipo(self, amb: Any) -> Any:
        raise NotImplementedError
