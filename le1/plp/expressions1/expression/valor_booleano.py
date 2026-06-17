from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.valor_concreto import ValorConcreto
from le1.plp.expressions1.util.tipo import Tipo


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool) -> None:
        if type(valor) is not bool:  # noqa: E721
            raise ErroTipo("ValorBooleano espera bool")
        super().__init__(valor)

    def valor(self) -> bool:
        return self._valor

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_BOOLEANO

    def __str__(self) -> str:
        return "true" if self._valor else "false"
