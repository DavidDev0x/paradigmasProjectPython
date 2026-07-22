from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression.valor_concreto import ValorConcreto


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int) -> None:
        if type(valor) is not int:
            raise TypeError("ValorInteiro aceita apenas int; bool não é permitido.")
        super().__init__(valor)

    def get_tipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ValorInteiro":
        return ValorInteiro(self.valor())
