from abc import ABC, abstractmethod

from li2.plp.imperative1.memory.ambiente_execucao_imperativa import AmbienteExecucaoImperativa


class AmbienteExecucaoImperativa2(AmbienteExecucaoImperativa, ABC):
    @abstractmethod
    def map_procedimento(self, id_arg, procedimento_id) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_procedimento(self, id_arg):
        raise NotImplementedError
