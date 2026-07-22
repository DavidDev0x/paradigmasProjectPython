from abc import ABC, abstractmethod
from .Valor import Valor


class ValorConcreto(Valor, ABC):
    @abstractmethod
    def valor(self):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, outro: object) -> bool:
        raise NotImplementedError
