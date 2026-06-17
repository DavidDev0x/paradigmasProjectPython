from __future__ import annotations

from abc import ABC
from typing import Any

from lf1.plp.expressions2.expression.valor import Valor


class ValorConcreto(Valor, ABC):
    def __init__(self, valor: Any) -> None:
        self._valor = valor

    def __str__(self) -> str:
        if type(self._valor) is bool:
            return str(self._valor).lower()
        return str(self._valor)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._valor!r})"

    def valor(self) -> Any:
        return self._valor

    def is_equals(self, obj: "ValorConcreto") -> bool:
        if not isinstance(obj, ValorConcreto):
            return False
        return type(self.valor()) is type(obj.valor()) and self.valor() == obj.valor()

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, ValorConcreto) and self.is_equals(obj)

    def __hash__(self) -> int:
        return hash((type(self._valor), self._valor))

    def avaliar(self, amb: Any) -> "ValorConcreto":
        return self

    def checa_tipo(self, amb: Any) -> bool:
        return True
