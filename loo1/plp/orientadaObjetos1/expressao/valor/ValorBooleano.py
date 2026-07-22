from .ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorBooleano(ValorConcreto):
    def __init__(self, valor: bool):
        if type(valor) is not bool:
            raise TypeError("ValorBooleano aceita apenas bool.")
        self._valor = valor

    def valor(self) -> bool:
        return self._valor

    def avaliar(self, ambiente):
        return self

    def checa_tipo(self, ambiente) -> bool:
        return True

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_BOOLEANO

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, ValorBooleano) and self._valor == outro._valor

    def __hash__(self) -> int:
        return hash((ValorBooleano, self._valor))

    def __str__(self) -> str:
        return "true" if self._valor else "false"
