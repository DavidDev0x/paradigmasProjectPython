from abc import ABC, abstractmethod


class Declaracao(ABC):
    @abstractmethod
    def elabora(self, ambiente):
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool:
        raise NotImplementedError
