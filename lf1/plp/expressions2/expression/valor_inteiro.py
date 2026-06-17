from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.expression.valor_concreto import ValorConcreto


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int) -> None:
        if type(valor) is not int:
            raise TypeError("ValorInteiro exige int puro; bool não é aceito como inteiro.")
        super().__init__(valor)

    def get_tipo(self, amb: Any) -> Tipo:
        return Tipo.TIPO_INTEIRO
