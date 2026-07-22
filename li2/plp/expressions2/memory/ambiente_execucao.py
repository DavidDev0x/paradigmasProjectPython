from abc import ABC, abstractmethod

from li2.plp.expressions2.memory.ambiente import Ambiente


class AmbienteExecucao(Ambiente, ABC):
    @abstractmethod
    def clone(self) -> "AmbienteExecucao":
        raise NotImplementedError
