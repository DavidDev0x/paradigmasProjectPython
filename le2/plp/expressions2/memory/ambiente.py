from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from le2.plp.expressions2.expression.id import Id


class Ambiente(ABC):
    @abstractmethod
    def incrementa(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def map(self, id_arg: Id, valor_id: object) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id_arg: Id) -> object:
        raise NotImplementedError
