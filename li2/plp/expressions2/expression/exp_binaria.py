from abc import abstractmethod

from li2.plp.expressions2.expression.expressao import Expressao


class ExpBinaria(Expressao):
    def __init__(self, esq: Expressao, dir: Expressao, operador: str) -> None:
        self._esq = esq
        self._dir = dir
        self._operador = operador

    def get_esq(self) -> Expressao:
        return self._esq

    def get_dir(self) -> Expressao:
        return self._dir

    def get_operador(self) -> str:
        return self._operador

    def checa_tipo(self, ambiente) -> bool:
        return (
            self._esq.checa_tipo(ambiente)
            and self._dir.checa_tipo(ambiente)
            and self.checa_tipo_elemento_terminal(ambiente)
        )

    @abstractmethod
    def checa_tipo_elemento_terminal(self, ambiente) -> bool:
        raise NotImplementedError

    def reduzir(self, ambiente):
        self._esq = self._esq.reduzir(ambiente)
        self._dir = self._dir.reduzir(ambiente)
        return self

    def __str__(self) -> str:
        return f"{self._esq} {self._operador} {self._dir}"

    @abstractmethod
    def clone(self) -> "ExpBinaria":
        raise NotImplementedError
