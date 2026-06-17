from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.type_guards import ensure_booleano
from lf1.plp.expressions2.expression.valor import Valor


class IfThenElse(Expressao):
    def __init__(self, teste: Expressao, then_expressao: Expressao, else_expressao: Expressao) -> None:
        self._condicao = teste
        self._then = then_expressao
        self._else_expressao = else_expressao

    def avaliar(self, ambiente: Any) -> Valor:
        cond = ensure_booleano(self._condicao.avaliar(ambiente), "if")
        return self._then.avaliar(ambiente) if cond.valor() else self._else_expressao.avaliar(ambiente)

    def __str__(self) -> str:
        return f"if ({self._condicao}) then ({self._then}) else ({self._else_expressao})"

    def checa_tipo(self, amb: Any) -> bool:
        return (self._condicao.checa_tipo(amb)
                and self._then.checa_tipo(amb)
                and self._else_expressao.checa_tipo(amb)
                and self._condicao.get_tipo(amb).e_booleano()
                and not self._then.get_tipo(amb).intersecao(self._else_expressao.get_tipo(amb)).e_void())

    def get_tipo(self, amb: Any) -> Tipo:
        return self._then.get_tipo(amb).intersecao(self._else_expressao.get_tipo(amb))

    def get_condicao(self) -> Expressao:
        return self._condicao

    def get_then(self) -> Expressao:
        return self._then

    def get_else_expressao(self) -> Expressao:
        return self._else_expressao
