from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from le2.plp.expressions1.util.tipo import Tipo
    from le2.plp.expressions2.expression.valor import Valor
    from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
    from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class ExpressaoComplexa(ABC):
    @abstractmethod
    def avaliar(self, amb: AmbienteExecucao) -> Valor:
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, amb: AmbienteCompilacao) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_tipo(self, amb: AmbienteCompilacao) -> Tipo:
        raise NotImplementedError
