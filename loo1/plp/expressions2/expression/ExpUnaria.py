from abc import abstractmethod
from .Expressao import Expressao


class ExpUnaria(Expressao):
    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def get_exp(self) -> Expressao:
        return self._exp

    def get_operador(self) -> str:
        return self._operador

    def checa_tipo(self, ambiente) -> bool:
        return self._exp.checa_tipo(ambiente) and self._checa_tipo_elemento_terminal(ambiente)

    @abstractmethod
    def _checa_tipo_elemento_terminal(self, ambiente) -> bool:
        raise NotImplementedError

    def reduzir(self, ambiente):
        self._exp = self._exp.reduzir(ambiente)
        return self

    def __str__(self) -> str:
        return f"{self._operador} {self._exp}"

    @abstractmethod
    def clone(self):
        raise NotImplementedError
