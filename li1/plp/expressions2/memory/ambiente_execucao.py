from __future__ import annotations
from abc import abstractmethod
from .ambiente import Ambiente

class AmbienteExecucao(Ambiente):
    """Interface de ambiente de execução: Id -> Valor."""

    @abstractmethod
    def clone(self) -> 'AmbienteExecucao': ...
