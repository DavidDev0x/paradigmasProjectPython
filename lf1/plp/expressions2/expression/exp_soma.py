from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.exp_binaria import ExpBinaria
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.type_guards import ensure_inteiro
from lf1.plp.expressions2.expression.valor_inteiro import ValorInteiro


class ExpSoma(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "+")

    def avaliar(self, amb: Any) -> ValorInteiro:
        esq = ensure_inteiro(self.get_esq().avaliar(amb), "+")
        dir = ensure_inteiro(self.get_dir().avaliar(amb), "+")
        return ValorInteiro(esq.valor() + dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente: Any) -> bool:
        return self.get_esq().get_tipo(ambiente).e_inteiro() and self.get_dir().get_tipo(ambiente).e_inteiro()

    def get_tipo(self, ambiente: Any) -> Tipo:
        return Tipo.TIPO_INTEIRO
