from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.exp_binaria import ExpBinaria
from le1.plp.expressions1.expression.expressao import Expressao
from le1.plp.expressions1.expression.valor import Valor
from le1.plp.expressions1.expression.valor_booleano import ValorBooleano
from le1.plp.expressions1.util.tipo import Tipo


class ExpAnd(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "and")

    def avaliar(self) -> Valor:
        esq = self.get_esq().avaliar()
        dir = self.get_dir().avaliar()
        if type(esq) is not ValorBooleano or type(dir) is not ValorBooleano:  # noqa: E721
            raise ErroTipo("Operador and espera dois booleanos")
        return ValorBooleano(esq.valor() and dir.valor())

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.get_esq().get_tipo().e_booleano() and self.get_dir().get_tipo().e_booleano()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO
