from abc import ABC, abstractmethod

from li2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class AmbienteExecucaoImperativa(AmbienteExecucao, ABC):
    @abstractmethod
    def change_valor(self, id_arg, valor_id) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def write(self, valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_saida(self):
        raise NotImplementedError
