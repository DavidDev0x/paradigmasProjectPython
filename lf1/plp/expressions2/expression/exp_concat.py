from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.exp_binaria import ExpBinaria
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.type_guards import ensure_string
from lf1.plp.expressions2.expression.valor_string import ValorString


class ExpConcat(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "++")

    def avaliar(self, amb: Any) -> ValorString:
        esq = ensure_string(self.get_esq().avaliar(amb), "++")
        dir = ensure_string(self.get_dir().avaliar(amb), "++")
        return ValorString(esq.valor() + dir.valor())

    def checa_tipo_elemento_terminal(self, ambiente: Any) -> bool:
        return self.get_esq().get_tipo(ambiente).e_string() and self.get_dir().get_tipo(ambiente).e_string()

    def get_tipo(self, ambiente: Any) -> Tipo:
        return Tipo.TIPO_STRING
