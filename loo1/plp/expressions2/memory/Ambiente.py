from abc import ABC, abstractmethod


class Ambiente(ABC):
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
