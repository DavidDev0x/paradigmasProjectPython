from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from .ValorConcreto import ValorConcreto


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int):
        if type(valor) is not int:
            raise TypeError("ValorInteiro aceita apenas int; bool não é aceito como inteiro.")
        super().__init__(valor)

    def get_tipo(self, ambiente):
        return TipoPrimitivo.INTEIRO

    def clone(self) -> "ValorInteiro":
        return ValorInteiro(self.valor())
