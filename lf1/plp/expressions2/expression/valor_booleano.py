from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.valor_concreto import ValorConcreto


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool) -> None:
        if type(valor) is not bool:
            raise TypeError("ValorBooleano exige bool puro.")
        super().__init__(valor)

    def get_tipo(self, amb: Any) -> Tipo:
        return Tipo.TIPO_BOOLEANO
