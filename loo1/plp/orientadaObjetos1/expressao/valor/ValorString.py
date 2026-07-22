from .ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorString(ValorConcreto):
    def __init__(self, valor: str):
        if type(valor) is not str:
            raise TypeError("ValorString aceita apenas str.")
        self._valor = valor

    def valor(self) -> str:
        return self._valor

    def avaliar(self, ambiente):
        return self

    def checa_tipo(self, ambiente) -> bool:
        return True

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_STRING

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, ValorString) and self._valor == outro._valor

    def __hash__(self) -> int:
        return hash((ValorString, self._valor))

    def __str__(self) -> str:
        return self._valor
