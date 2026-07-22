from loo1.plp.expressions1.util.TipoPrimitivo import TipoPrimitivo
from .ValorConcreto import ValorConcreto


class ValorString(ValorConcreto):
    def __init__(self, valor: str):
        if type(valor) is not str:
            raise TypeError("ValorString aceita apenas str.")
        super().__init__(valor)

    def get_tipo(self, ambiente):
        return TipoPrimitivo.STRING

    def clone(self) -> "ValorString":
        return ValorString(self.valor())

    def __str__(self) -> str:
        return f'"{self.valor()}"'
