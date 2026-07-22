from abc import ABC, abstractmethod
from .Ambiente import Ambiente


class AmbienteExecucao(Ambiente, ABC):
    @abstractmethod
    def clone(self):
        raise NotImplementedError
