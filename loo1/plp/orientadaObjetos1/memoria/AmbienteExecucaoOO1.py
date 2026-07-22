from abc import ABC, abstractmethod
from .AmbienteOO1 import AmbienteOO1


class AmbienteExecucaoOO1(AmbienteOO1, ABC):
    @abstractmethod
    def incrementa(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def map(self, identificador, valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, identificador):
        raise NotImplementedError

    @abstractmethod
    def get_pilha(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def get_map_def_classe(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_map_objetos(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def map_objeto(self, referencia, objeto) -> None:
        raise NotImplementedError

    @abstractmethod
    def change_valor(self, identificador, valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_objeto(self, referencia):
        raise NotImplementedError

    @abstractmethod
    def get_prox_ref(self):
        raise NotImplementedError

    @abstractmethod
    def get_ref(self):
        raise NotImplementedError

    @abstractmethod
    def read(self, tipo):
        raise NotImplementedError

    @abstractmethod
    def write(self, valor):
        raise NotImplementedError

    @abstractmethod
    def get_entrada(self):
        raise NotImplementedError

    @abstractmethod
    def get_saida(self):
        raise NotImplementedError

    @abstractmethod
    def get_contexto_id_valor(self):
        raise NotImplementedError

    @abstractmethod
    def get_valor(self, identificador):
        raise NotImplementedError
