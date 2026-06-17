from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.exp_binaria import ExpBinaria
from le1.plp.expressions1.expression.expressao import Expressao
from le1.plp.expressions1.expression.valor import Valor
from le1.plp.expressions1.expression.valor_inteiro import ValorInteiro
from le1.plp.expressions1.util.tipo import Tipo


class ExpSoma(ExpBinaria):
    def __init__(self, esq: Expressao, dir: Expressao) -> None:
        super().__init__(esq, dir, "+")

    def avaliar(self) -> Valor:
        esq = self.get_esq().avaliar()
        dir = self.get_dir().avaliar()
        if type(esq) is not ValorInteiro or type(dir) is not ValorInteiro:  # noqa: E721
            raise ErroTipo("Operador + espera dois inteiros")
        return ValorInteiro(esq.valor() + dir.valor())

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.get_esq().get_tipo().e_inteiro() and self.get_dir().get_tipo().e_inteiro()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
