from .ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorString import ValorString
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpConcat(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "++")

    def avaliar(self, ambiente):
        esq = self.get_esq().avaliar(ambiente)
        dir = self.get_dir().avaliar(ambiente)
        if not isinstance(esq, ValorString) and not isinstance(dir, ValorString):
            raise ErroTipoException("O operador '++' exige ao menos uma string.")
        return ValorString(str(esq) + str(dir))

    def checa_tipo(self, ambiente) -> bool:
        if not super().checa_tipo(ambiente):
            return False
        return (
            self.get_esq().get_tipo(ambiente) == TipoPrimitivo.TIPO_STRING
            or self.get_dir().get_tipo(ambiente) == TipoPrimitivo.TIPO_STRING
        )

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_STRING
