from abc import ABC, abstractmethod


class Expressao(ABC):
    @abstractmethod
    def avaliar(self, ambiente):
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_tipo(self, ambiente):
        raise NotImplementedError
