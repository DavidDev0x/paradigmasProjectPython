from __future__ import annotations
from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .valor_concreto import ValorConcreto

class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool) -> None:
        if type(valor) is not bool:
            raise TypeError(f'ValorBooleano exige bool; recebido {type(valor).__name__}.')
        super().__init__(valor)

    def __str__(self) -> str:
        return str(self.valor()).lower()

    def get_tipo(self, amb: object = None) -> TipoPrimitivo:
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> 'ValorBooleano':
        return ValorBooleano(self.valor())
