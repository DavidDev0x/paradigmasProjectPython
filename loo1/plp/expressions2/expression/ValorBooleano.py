from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from .ValorConcreto import ValorConcreto


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool):
        if type(valor) is not bool:
            raise TypeError("ValorBooleano aceita apenas bool.")
        super().__init__(valor)

    def get_tipo(self, ambiente):
        return TipoPrimitivo.BOOLEANO

    def clone(self) -> "ValorBooleano":
        return ValorBooleano(self.valor())

    def __str__(self) -> str:
        return "true" if self.valor() else "false"
