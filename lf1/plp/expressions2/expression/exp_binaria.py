from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from lf1.plp.expressions2.expression.expressao import Expressao


class ExpBinaria(Expressao, ABC):
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

    def __str__(self) -> str:
        return f"{self._esq} {self._operador} {self._dir}"

    def checa_tipo(self, amb: Any) -> bool:
        return self._esq.checa_tipo(amb) and self._dir.checa_tipo(amb) and self.checa_tipo_elemento_terminal(amb)

    @abstractmethod
    def checa_tipo_elemento_terminal(self, amb: Any) -> bool:
        raise NotImplementedError
