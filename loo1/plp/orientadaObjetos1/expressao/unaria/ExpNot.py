from .ExpUnaria import ExpUnaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpNot(ExpUnaria):
    def __init__(self, expressao):
        super().__init__(expressao, "~")

    def avaliar(self, ambiente):
        valor = self.get_exp().avaliar(ambiente)
        if not isinstance(valor, ValorBooleano):
            raise ErroTipoException("O operador 'not' exige booleano.")
        return ValorBooleano(not valor.valor())

    def checa_tipo(self, ambiente) -> bool:
        return super().checa_tipo(ambiente) and self.get_exp().get_tipo(ambiente) == TipoPrimitivo.TIPO_BOOLEANO

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_BOOLEANO
