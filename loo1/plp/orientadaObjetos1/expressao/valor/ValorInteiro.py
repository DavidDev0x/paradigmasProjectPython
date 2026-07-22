from .ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorInteiro(ValorConcreto):
    def __init__(self, valor: int):
        if type(valor) is not int:
            raise TypeError("ValorInteiro aceita apenas int; bool não é aceito como inteiro.")
        self._valor = valor

    def valor(self) -> int:
        return self._valor

    def avaliar(self, ambiente):
        return self

    def checa_tipo(self, ambiente) -> bool:
        return True

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_INTEIRO

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, ValorInteiro) and self._valor == outro._valor

    def __hash__(self) -> int:
        return hash((ValorInteiro, self._valor))

    def __str__(self) -> str:
        return str(self._valor)
