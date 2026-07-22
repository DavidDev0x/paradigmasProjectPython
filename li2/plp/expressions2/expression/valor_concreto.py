from abc import abstractmethod

from li2.plp.expressions2.expression.valor import Valor


class ValorConcreto(Valor):
    def __init__(self, valor) -> None:
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
        if type(self._valor) is bool:
            return str(self._valor).lower()
        return str(self._valor)

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, ValorConcreto) and self.is_equals(outro)

    def __hash__(self) -> int:
        return hash((type(self), self._valor))

    @abstractmethod
    def clone(self) -> "ValorConcreto":
        raise NotImplementedError
