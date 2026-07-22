from abc import ABC, abstractmethod
from .Valor import Valor


class ValorConcreto(Valor, ABC):
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        return self._valor

    def is_equals(self, outro: "ValorConcreto") -> bool:
        return type(self) is type(outro) and self._valor == outro._valor

    def avaliar(self, ambiente):
        return self

    def checa_tipo(self, ambiente) -> bool:
        return True

    def reduzir(self, ambiente):
        return self

    def __str__(self) -> str:
        return str(self._valor)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._valor!r})"

    def __eq__(self, outro: object) -> bool:
        return type(self) is type(outro) and self._valor == outro._valor

    def __hash__(self) -> int:
        return hash((type(self), self._valor))

    @abstractmethod
    def get_tipo(self, ambiente):
        raise NotImplementedError

    @abstractmethod
    def clone(self):
        raise NotImplementedError
