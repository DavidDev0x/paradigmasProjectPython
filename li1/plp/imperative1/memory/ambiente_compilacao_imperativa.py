from __future__ import annotations
from abc import abstractmethod
from li1.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao

class AmbienteCompilacaoImperativa(AmbienteCompilacao):
    @abstractmethod
    def get_tipo_entrada(self): ...
