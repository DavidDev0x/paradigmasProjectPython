from .ExpUnaria import ExpUnaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpMenos(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao, "-")

    def avaliar(self, ambiente):
        valor = self.get_exp().avaliar(ambiente)
        if not isinstance(valor, ValorInteiro):
            raise ErroTipoException("O operador unário '-' exige inteiro.")
        return ValorInteiro(-valor.valor())

    def checa_tipo(self, ambiente) -> bool:
        return super().checa_tipo(ambiente) and self.get_exp().get_tipo(ambiente) == TipoPrimitivo.TIPO_INTEIRO

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_INTEIRO
