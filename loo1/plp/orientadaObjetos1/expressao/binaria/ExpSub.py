from .ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpSub(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "-")

    def avaliar(self, ambiente):
        esq = self.get_esq().avaliar(ambiente)
        dir = self.get_dir().avaliar(ambiente)
        if not isinstance(esq, ValorInteiro) or not isinstance(dir, ValorInteiro):
            raise ErroTipoException("O operador '-' aceita apenas inteiros.")
        return ValorInteiro(esq.valor() - dir.valor())

    def checa_tipo(self, ambiente) -> bool:
        return (
            super().checa_tipo(ambiente)
            and self.get_esq().get_tipo(ambiente) == TipoPrimitivo.TIPO_INTEIRO
            and self.get_dir().get_tipo(ambiente) == TipoPrimitivo.TIPO_INTEIRO
        )

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_INTEIRO
