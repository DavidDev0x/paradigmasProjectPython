from .ExpUnaria import ExpUnaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorString import ValorString
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpLength(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao, "length")

    def avaliar(self, ambiente):
        valor = self.get_exp().avaliar(ambiente)
        if not isinstance(valor, ValorString):
            raise ErroTipoException("O operador 'length' exige string.")
        return ValorInteiro(len(valor.valor()))

    def checa_tipo(self, ambiente) -> bool:
        return super().checa_tipo(ambiente) and self.get_exp().get_tipo(ambiente) == TipoPrimitivo.TIPO_STRING

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_INTEIRO
