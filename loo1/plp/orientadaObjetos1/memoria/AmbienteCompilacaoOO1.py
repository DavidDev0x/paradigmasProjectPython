from abc import ABC, abstractmethod
from .AmbienteOO1 import AmbienteOO1


class AmbienteCompilacaoOO1(AmbienteOO1, ABC):
    @abstractmethod
    def incrementa(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def map(self, identificador, tipo) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, identificador):
        raise NotImplementedError

    @abstractmethod
    def get_tipo(self, identificador):
        raise NotImplementedError

    @abstractmethod
    def map_parametros_procedimento(self, identificador, parametros) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_parametros_procedimento(self, identificador):
        raise NotImplementedError

    @abstractmethod
    def get_tipo_entrada(self):
        raise NotImplementedError
