from __future__ import annotations

from abc import ABC, abstractmethod

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.expressao import Expressao


class ExpBinaria(Expressao, ABC):
    """Expressão binária com duas subexpressões e um operador."""

    def __init__(self, esq: Expressao, dir: Expressao, operador: str) -> None:
        if not isinstance(esq, Expressao) or not isinstance(dir, Expressao):
            raise ErroTipo("ExpBinaria espera duas Expressao")
        if type(operador) is not str:  # noqa: E721
            raise ErroTipo("operador deve ser str")
        self._esq: Expressao = esq
        self._dir: Expressao = dir
        self._operador: str = operador

    def get_esq(self) -> Expressao:
        return self._esq

    def get_dir(self) -> Expressao:
        return self._dir

    def get_operador(self) -> str:
        return self._operador

    def __str__(self) -> str:
        return f"{self._esq} {self._operador} {self._dir}"

    def checa_tipo(self) -> bool:
        if not self.get_esq().checa_tipo() or not self.get_dir().checa_tipo():
            return False
        return self._checa_tipo_elemento_terminal()

    @abstractmethod
    def _checa_tipo_elemento_terminal(self) -> bool:
        pass
