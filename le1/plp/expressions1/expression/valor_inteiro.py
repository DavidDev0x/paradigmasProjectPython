from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.valor_concreto import ValorConcreto
from le1.plp.expressions1.util.tipo import Tipo


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int) -> None:
        if type(valor) is not int:  # noqa: E721 - bool herda de int em Python
            raise ErroTipo("ValorInteiro espera int puro; bool não é aceito")
        super().__init__(valor)

    def valor(self) -> int:
        return self._valor

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_INTEIRO
