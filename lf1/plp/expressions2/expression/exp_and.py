from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.exp_binaria import ExpBinaria
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.type_guards import ensure_booleano
from lf1.plp.expressions2.expression.valor_booleano import ValorBooleano


class ExpAnd(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "and")

    def avaliar(self, amb: Any) -> ValorBooleano:
        esq = ensure_booleano(self.get_esq().avaliar(amb), "and")
        dir = ensure_booleano(self.get_dir().avaliar(amb), "and")
        return ValorBooleano(esq.valor() and dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente: Any) -> bool:
        return self.get_esq().get_tipo(ambiente).e_booleano() and self.get_dir().get_tipo(ambiente).e_booleano()

    def get_tipo(self, ambiente: Any) -> Tipo:
        return Tipo.TIPO_BOOLEANO
