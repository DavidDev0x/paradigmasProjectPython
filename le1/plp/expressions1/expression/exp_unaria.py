from __future__ import annotations

from abc import ABC, abstractmethod

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.expressao import Expressao


class ExpUnaria(Expressao, ABC):
    """Expressão unária com uma subexpressão e um operador."""

    def __init__(self, exp: Expressao, operador: str) -> None:
        if not isinstance(exp, Expressao):
            raise ErroTipo("ExpUnaria espera uma Expressao")
        if type(operador) is not str:  # noqa: E721
            raise ErroTipo("operador deve ser str")
        self._exp: Expressao = exp
        self._operador: str = operador

    def get_exp(self) -> Expressao:
        return self._exp

    def get_operador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self._operador} {self._exp}"

    def checa_tipo(self) -> bool:
        return self.get_exp().checa_tipo() and self._checa_tipo_elemento_terminal()

    @abstractmethod
    def _checa_tipo_elemento_terminal(self) -> bool:
        pass
