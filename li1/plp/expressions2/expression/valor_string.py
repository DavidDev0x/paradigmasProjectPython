from __future__ import annotations
from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .valor_concreto import ValorConcreto

class ValorString(ValorConcreto):
    def __init__(self, valor: str) -> None:
        if type(valor) is not str:
            raise TypeError(f'ValorString exige str; recebido {type(valor).__name__}.')
        super().__init__(valor)

    def get_tipo(self, amb: object = None) -> TipoPrimitivo:
        return TipoPrimitivo.STRING

    def __str__(self) -> str:
        return f'"{super().__str__()}"'

    def clone(self) -> 'ValorString':
        return ValorString(self.valor())
