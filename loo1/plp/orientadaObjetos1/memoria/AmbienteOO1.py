from abc import ABC, abstractmethod


class AmbienteOO1(ABC):
    @abstractmethod
    def map_def_classe(self, identificador, definicao) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_def_classe(self, identificador):
        raise NotImplementedError
