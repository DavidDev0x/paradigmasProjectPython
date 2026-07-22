from abc import ABC, abstractmethod


class Comando(ABC):
    @abstractmethod
    def executar(self, ambiente):
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool:
        raise NotImplementedError
