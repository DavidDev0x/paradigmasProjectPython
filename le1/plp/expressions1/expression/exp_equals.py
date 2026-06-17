from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.exp_binaria import ExpBinaria
from le1.plp.expressions1.expression.expressao import Expressao
from le1.plp.expressions1.expression.valor import Valor
from le1.plp.expressions1.expression.valor_booleano import ValorBooleano
from le1.plp.expressions1.expression.valor_concreto import ValorConcreto
from le1.plp.expressions1.util.tipo import Tipo


class ExpEquals(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "==")

    def avaliar(self) -> Valor:
        esq = self.get_esq().avaliar()
        dir = self.get_dir().avaliar()
        if not isinstance(esq, ValorConcreto) or not isinstance(dir, ValorConcreto):
            raise ErroTipo("Operador == espera valores concretos")
        if type(esq) is not type(dir):
            raise ErroTipo("Operador == espera operandos do mesmo tipo")
        return ValorBooleano(esq == dir)

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.get_esq().get_tipo() == self.get_dir().get_tipo()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO
