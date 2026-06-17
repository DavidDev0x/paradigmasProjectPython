from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.exp_unaria import ExpUnaria
from le1.plp.expressions1.expression.expressao import Expressao
from le1.plp.expressions1.expression.valor import Valor
from le1.plp.expressions1.expression.valor_inteiro import ValorInteiro
from le1.plp.expressions1.util.tipo import Tipo


class ExpMenos(ExpUnaria):
    def __init__(self, exp: Expressao) -> None:
        super().__init__(exp, "-")

    def avaliar(self) -> Valor:
        exp = self.get_exp().avaliar()
        if type(exp) is not ValorInteiro:  # noqa: E721
            raise ErroTipo("Operador unário - espera inteiro")
        return ValorInteiro(-exp.valor())

    def _checa_tipo_elemento_terminal(self) -> bool:
        return self.get_exp().get_tipo().e_inteiro()

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
