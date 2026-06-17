from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.exp_binaria import ExpBinaria
from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.type_guards import ensure_concreto
from lf1.plp.expressions2.expression.valor_booleano import ValorBooleano


class ExpEquals(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "==")

    def avaliar(self, amb: Any) -> ValorBooleano:
        esq = ensure_concreto(self.get_esq().avaliar(amb), "==")
        dir = ensure_concreto(self.get_dir().avaliar(amb), "==")
        return ValorBooleano(esq.is_equals(dir))

    def checa_tipo_elemento_terminal(self, ambiente: Any) -> bool:
        return not self.get_esq().get_tipo(ambiente).intersecao(self.get_dir().get_tipo(ambiente)).e_void()

    def get_tipo(self, ambiente: Any) -> Tipo:
        return Tipo.TIPO_BOOLEANO
