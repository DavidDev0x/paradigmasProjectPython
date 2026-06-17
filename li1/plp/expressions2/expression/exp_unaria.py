from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING
from .expressao import Expressao
if TYPE_CHECKING:
    from .valor import Valor
    from li1.plp.expressions1.util.tipo import Tipo
    from li1.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from li1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao

class ExpUnaria(Expressao):
    def __init__(self, exp: Expressao, operador: str) -> None:
        self.exp = exp
        self._operador = operador

    def get_exp(self) -> Expressao:
        return self.exp

    def get_operador(self) -> str:
        return self._operador

    def checa_tipo(self, amb: 'AmbienteCompilacao') -> bool:
        return self.get_exp().checa_tipo(amb) and self.checa_tipo_elemento_terminal(amb)

    def __str__(self) -> str:
        return f'{self._operador} {self.exp}'

    @abstractmethod
    def checa_tipo_elemento_terminal(self, amb: 'AmbienteCompilacao') -> bool: ...

    def reduzir(self, ambiente: 'AmbienteExecucao') -> Expressao:
        self.exp = self.exp.reduzir(ambiente)
        return self

    @abstractmethod
    def avaliar(self, amb: 'AmbienteExecucao') -> 'Valor': ...

    @abstractmethod
    def get_tipo(self, amb: 'AmbienteCompilacao') -> 'Tipo': ...

    @abstractmethod
    def clone(self) -> 'ExpUnaria': ...
