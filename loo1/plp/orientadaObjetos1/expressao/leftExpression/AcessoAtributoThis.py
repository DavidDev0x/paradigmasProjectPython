from .AcessoAtributo import AcessoAtributo
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class AcessoAtributoThis(AcessoAtributo):
    def __init__(self, var_this, identificador):
        super().__init__(identificador)
        self._var_this = var_this

    def avaliar(self, ambiente):
        referencia = self._var_this.avaliar(ambiente)
        if not isinstance(referencia, ValorRef):
            raise ErroTipoException("'this' não contém uma referência de objeto.")
        return ambiente.get_objeto(referencia).get_estado().get(self.get_id())

    def get_expressao_objeto(self):
        return self._var_this

    def checa_tipo(self, ambiente) -> bool:
        try:
            tipo = self._var_this.get_tipo(ambiente)
            ambiente.get_def_classe(tipo.get_tipo()).get_tipo_atributo(self.get_id())
            return True
        except Exception:
            return False

    def get_tipo(self, ambiente):
        tipo = self._var_this.get_tipo(ambiente)
        return ambiente.get_def_classe(tipo.get_tipo()).get_tipo_atributo(self.get_id())
