from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from li1.plp.expressions1.util.tipo import Tipo
    from li1.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from li1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao
    from .valor import Valor

class Expressao(ABC):
    @abstractmethod
    def avaliar(self, amb: 'AmbienteExecucao') -> 'Valor': ...

    @abstractmethod
    def checa_tipo(self, amb: 'AmbienteCompilacao') -> bool: ...

    @abstractmethod
    def get_tipo(self, amb: 'AmbienteCompilacao | None') -> 'Tipo': ...

    @abstractmethod
    def reduzir(self, ambiente: 'AmbienteExecucao') -> 'Expressao': ...

    @abstractmethod
    def clone(self) -> 'Expressao': ...
