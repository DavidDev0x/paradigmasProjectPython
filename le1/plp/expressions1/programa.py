from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.expressao import Expressao
from le1.plp.expressions1.expression.valor import Valor


class Programa:
    def __init__(self, exp: Expressao) -> None:
        if not isinstance(exp, Expressao):
            raise ErroTipo("Programa espera uma Expressao")
        self._exp: Expressao = exp

    def executar(self) -> Valor:
        result = self._exp.avaliar()
        print(result)
        return result

    def checa_tipo(self) -> bool:
        return self._exp.checa_tipo()

    def get_expressao(self) -> Expressao:
        return self._exp
