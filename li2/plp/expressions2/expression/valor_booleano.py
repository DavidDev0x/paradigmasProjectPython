from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression.valor_concreto import ValorConcreto


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool) -> None:
        if type(valor) is not bool:
            raise TypeError("ValorBooleano aceita apenas bool.")
        super().__init__(valor)

    def get_tipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> "ValorBooleano":
        return ValorBooleano(self.valor())
