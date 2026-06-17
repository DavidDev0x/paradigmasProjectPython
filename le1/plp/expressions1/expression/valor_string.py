from __future__ import annotations

from le1.plp.expressions1.expression.erro_tipo import ErroTipo
from le1.plp.expressions1.expression.valor_concreto import ValorConcreto
from le1.plp.expressions1.util.tipo import Tipo


class ValorString(ValorConcreto):
    def __init__(self, valor: str) -> None:
        if type(valor) is not str:  # noqa: E721
            raise ErroTipo("ValorString espera str")
        super().__init__(valor)

    def valor(self) -> str:
        return self._valor

    def get_tipo(self) -> Tipo:
        return Tipo.TIPO_STRING
