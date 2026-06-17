from __future__ import annotations

from abc import ABC
from typing import Any

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.valor import Valor


class ValorConcreto(Valor, ABC):
    """Classe base para valores primitivos concretos da LE1."""

    def __init__(self, valor: Any) -> None:
        self._valor: Any = valor

    def valor(self) -> Any:
        return self._valor

    def is_equals(self, obj: "ValorConcreto") -> bool:
        if not isinstance(obj, ValorConcreto):
            raise ErroTipo("is_equals espera um ValorConcreto")
        return self.valor() == obj.valor()

    def avaliar(self) -> Valor:
        return self

    def checa_tipo(self) -> bool:
        return True

    def __eq__(self, obj: object) -> bool:
        return type(obj) is type(self) and self.valor() == obj.valor()  # noqa: E721

    def __hash__(self) -> int:
        return hash((type(self), self.valor()))

    def __str__(self) -> str:
        return str(self._valor)
