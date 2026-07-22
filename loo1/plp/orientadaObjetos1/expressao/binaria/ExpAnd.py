from .ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpAnd(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "and")

    def avaliar(self, ambiente):
        esq = self.get_esq().avaliar(ambiente)
        dir = self.get_dir().avaliar(ambiente)
        if not isinstance(esq, ValorBooleano) or not isinstance(dir, ValorBooleano):
            raise ErroTipoException("O operador 'and' aceita apenas booleanos.")
        return ValorBooleano(esq.valor() and dir.valor())

    def checa_tipo(self, ambiente) -> bool:
        return (
            super().checa_tipo(ambiente)
            and self.get_esq().get_tipo(ambiente) == TipoPrimitivo.TIPO_BOOLEANO
            and self.get_dir().get_tipo(ambiente) == TipoPrimitivo.TIPO_BOOLEANO
        )

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_BOOLEANO
