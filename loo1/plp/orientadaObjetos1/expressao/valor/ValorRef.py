from .Valor import Valor
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class ValorRef(Valor):
    VALOR_INICIAL = 0

    def __init__(self, valor: int):
        if type(valor) is not int:
            raise TypeError("A referência deve ser representada por um inteiro.")
        self._valor = max(valor, self.VALOR_INICIAL)

    def valor(self) -> int:
        return self._valor

    def avaliar(self, ambiente):
        return self

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_INTEIRO

    def checa_tipo(self, ambiente) -> bool:
        return True

    def incrementa(self) -> "ValorRef":
        self._valor += 1
        return self

    def __hash__(self) -> int:
        return hash((ValorRef, self._valor))

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, ValorRef) and self._valor == outro._valor

    def __str__(self) -> str:
        return str(self._valor)
