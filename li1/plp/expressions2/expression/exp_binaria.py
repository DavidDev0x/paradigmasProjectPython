from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING
from .expressao import Expressao
if TYPE_CHECKING:
    from .valor import Valor
    from li1.plp.expressions1.util.tipo import Tipo
    from li1.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from li1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao

class ExpBinaria(Expressao):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str) -> None:
        self.esq = esq
        self.dir = dir
        self._operador = operador

    def get_esq(self) -> Expressao:
        return self.esq

    def get_dir(self) -> Expressao:
        return self.dir

    def get_operador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f'{self.esq} {self._operador} {self.dir}'

    def checa_tipo(self, amb: 'AmbienteCompilacao') -> bool:
        return self.get_esq().checa_tipo(amb) and self.get_dir().checa_tipo(amb) and self.checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def checa_tipo_elemento_terminal(self, amb: 'AmbienteCompilacao') -> bool: ...

    def reduzir(self, ambiente: 'AmbienteExecucao') -> Expressao:
        self.esq = self.esq.reduzir(ambiente)
        self.dir = self.dir.reduzir(ambiente)
        return self

    @abstractmethod
    def avaliar(self, amb: 'AmbienteExecucao') -> 'Valor': ...

    @abstractmethod
    def get_tipo(self, amb: 'AmbienteCompilacao') -> 'Tipo': ...

    @abstractmethod
    def clone(self) -> 'ExpBinaria': ...
