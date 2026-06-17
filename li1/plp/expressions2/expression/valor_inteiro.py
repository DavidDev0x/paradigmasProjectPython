from __future__ import annotations
from li1.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from .valor_concreto import ValorConcreto

class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int) -> None:
        if type(valor) is not int:
            raise TypeError(f'ValorInteiro exige int puro; recebido {type(valor).__name__}.')
        super().__init__(valor)

    def get_tipo(self, amb: object = None) -> TipoPrimitivo:
        return TipoPrimitivo.INTEIRO

    def clone(self) -> 'ValorInteiro':
        return ValorInteiro(self.valor())
