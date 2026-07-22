from .ExpBinaria import ExpBinaria
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.expressao.valor.ValorConcreto import ValorConcreto
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ExpEquals(ExpBinaria):
    def __init__(self, esq, dir):
        super().__init__(esq, dir, "==")

    def avaliar(self, ambiente):
        esq = self.get_esq().avaliar(ambiente)
        dir = self.get_dir().avaliar(ambiente)
        tipos_iguais = type(esq) is type(dir)
        referencia_com_null = (
            isinstance(esq, ValorRef) and isinstance(dir, ValorNull)
        ) or (
            isinstance(esq, ValorNull) and isinstance(dir, ValorRef)
        )
        if not tipos_iguais and not referencia_com_null:
            raise ErroTipoException("O operador '==' exige operandos de tipos compatíveis.")
        return ValorBooleano(esq == dir)

    def checa_tipo(self, ambiente) -> bool:
        if not super().checa_tipo(ambiente):
            return False
        tipo_esq = self.get_esq().get_tipo(ambiente)
        tipo_dir = self.get_dir().get_tipo(ambiente)
        if isinstance(tipo_esq, TipoClasse):
            return tipo_dir == TipoClasse.TIPO_NULL or tipo_esq == tipo_dir
        return tipo_esq == tipo_dir

    def get_tipo(self, ambiente):
        return TipoPrimitivo.TIPO_BOOLEANO
