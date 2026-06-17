from __future__ import annotations

from abc import abstractmethod

from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao


class ExpBinaria(Expressao):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str) -> None:
        if not isinstance(esq, Expressao):
            raise TypeError("esq deve implementar Expressao.")
        if not isinstance(dir, Expressao):
            raise TypeError("dir deve implementar Expressao.")
        if type(operador) is not str:
            raise TypeError("operador deve ser string.")
        self._esq = esq
        self._dir = dir
        self._operador = operador

    def get_esq(self) -> Expressao:
        return self._esq

    def get_dir(self) -> Expressao:
        return self._dir

    def get_operador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self._esq} {self._operador} {self._dir}"

    def checa_tipo(self, amb: AmbienteCompilacao) -> bool:
        if not self.get_esq().checa_tipo(amb) or not self.get_dir().checa_tipo(amb):
            return False
        return self.checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def checa_tipo_elemento_terminal(self, amb: AmbienteCompilacao) -> bool:
        raise NotImplementedError
