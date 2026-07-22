from .ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class ValorNull(ValorConcreto):
    def valor(self):
        return None

    def avaliar(self, ambiente):
        return self

    def checa_tipo(self, ambiente) -> bool:
        return True

    def get_tipo(self, ambiente):
        return TipoClasse.TIPO_NULL

    def __eq__(self, outro: object) -> bool:
        return isinstance(outro, ValorNull)

    def __hash__(self) -> int:
        return hash(ValorNull)

    def __str__(self) -> str:
        return "null"
