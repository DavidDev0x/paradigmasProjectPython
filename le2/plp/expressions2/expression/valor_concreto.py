from __future__ import annotations

from abc import ABC

from le2.plp.expressions2.expression.valor import Valor
from le2.plp.expressions2.memory.ambiente_compilacao import AmbienteCompilacao
from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao


class ValorConcreto(Valor, ABC):
    def __init__(self, valor: object) -> None:
        self._valor = valor

    def __str__(self) -> str:
        if isinstance(self._valor, bool):
            return str(self._valor).lower()
        return str(self._valor)

    def valor(self) -> object:
        return self._valor

    def is_equals(self, obj: ValorConcreto) -> bool:
        return type(self) is type(obj) and self.valor() == obj.valor()

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, ValorConcreto) and self.is_equals(obj)

    def __hash__(self) -> int:
        return hash((type(self), self._valor))

    def avaliar(self, amb: AmbienteExecucao) -> Valor:
        return self

    def checa_tipo(self, amb: AmbienteCompilacao) -> bool:
        return True
