from __future__ import annotations

from abc import abstractmethod

from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao


class ExpUnaria(Expressao):
    def __init__(self, exp: Expressao, operador: str) -> None:
        if not isinstance(exp, Expressao):
            raise TypeError("exp deve implementar Expressao.")
        if type(operador) is not str:
            raise TypeError("operador deve ser string.")
        self._exp = exp
        self._operador = operador

    def get_exp(self) -> Expressao:
        return self._exp

    def get_operador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        if self._operador == "length":
            return f"length({self._exp})"
        return f"{self._operador}{self._exp}"

    def checa_tipo(self, amb: AmbienteCompilacao) -> bool:
        return self.get_exp().checa_tipo(amb) and self.checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def checa_tipo_elemento_terminal(self, amb: AmbienteCompilacao) -> bool:
        raise NotImplementedError
