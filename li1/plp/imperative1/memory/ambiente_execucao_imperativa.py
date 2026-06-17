from __future__ import annotations
from abc import abstractmethod
from li1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao

class AmbienteExecucaoImperativa(AmbienteExecucao):
    @abstractmethod
    def change_valor(self, id_arg, valor_id) -> None: ...

    @abstractmethod
    def read(self): ...

    @abstractmethod
    def write(self, v) -> None: ...

    @abstractmethod
    def get_saida(self): ...
