from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression.valor_concreto import ValorConcreto


class ValorString(ValorConcreto):
    def __init__(self, valor: str) -> None:
        if type(valor) is not str:
            raise TypeError("ValorString aceita apenas str.")
        super().__init__(valor)

    def get_tipo(self, ambiente):
        return TipoPrimitivo.STRING

    def __str__(self) -> str:
        return f'"{self.valor()}"'

    def clone(self) -> "ValorString":
        return ValorString(self.valor())
