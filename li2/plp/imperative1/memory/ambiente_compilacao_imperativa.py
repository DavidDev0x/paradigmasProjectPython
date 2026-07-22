from abc import ABC, abstractmethod

from li2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao


class AmbienteCompilacaoImperativa(AmbienteCompilacao, ABC):
    @abstractmethod
    def get_tipo_entrada(self):
        raise NotImplementedError
