from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.exp_unaria import ExpUnaria
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.type_guards import ensure_inteiro
from lf1.plp.expressions2.expression.valor_inteiro import ValorInteiro


class ExpMenos(ExpUnaria):
    def __init__(self, exp: Expressao) -> None:
        super().__init__(exp, "-")

    def avaliar(self, amb: Any) -> ValorInteiro:
        exp = ensure_inteiro(self.get_exp().avaliar(amb), "- unário")
        return ValorInteiro(-exp.valor())

    def checa_tipo_elemento_terminal(self, amb: Any) -> bool:
        return self.get_exp().get_tipo(amb).e_inteiro()

    def get_tipo(self, amb: Any) -> Tipo:
        return Tipo.TIPO_INTEIRO
