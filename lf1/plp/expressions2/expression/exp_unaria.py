from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from lf1.plp.expressions2.expression.expressao import Expressao


class ExpUnaria(Expressao, ABC):
    def __init__(self, exp: Expressao, operador: str) -> None:
        self._exp = exp
        self._operador = operador

    def get_exp(self) -> Expressao:
        return self._exp

    def get_operador(self) -> str:
        return self._operador

    def checa_tipo(self, amb: Any) -> bool:
        return self._exp.checa_tipo(amb) and self.checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def checa_tipo_elemento_terminal(self, amb: Any) -> bool:
        raise NotImplementedError
