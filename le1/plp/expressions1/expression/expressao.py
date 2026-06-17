from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from le1.plp.expressions1.util.tipo import Tipo

if TYPE_CHECKING:
    from le1.plp.expressions1.expression.valor import Valor


class Expressao(ABC):
    """Unidade básica da Linguagem de Expressões."""

    @abstractmethod
    def avaliar(self) -> "Valor":
        pass

    @abstractmethod
    def checa_tipo(self) -> bool:
        pass

    @abstractmethod
    def get_tipo(self) -> Tipo:
        pass
