from .AcessoAtributo import AcessoAtributo
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class AcessoAtributoId(AcessoAtributo):
    def __init__(self, av, identificador):
        super().__init__(identificador)
        self._av = av

    def avaliar(self, ambiente):
        referencia = self._av.avaliar(ambiente)
        if not isinstance(referencia, ValorRef):
            raise ErroTipoException("Acesso a atributo exige uma referência de objeto.")
        return ambiente.get_objeto(referencia).get_estado().get(self.get_id())

    def get_expressao_objeto(self):
        return self._av

    def checa_tipo(self, ambiente) -> bool:
        try:
            if not self._av.checa_tipo(ambiente):
                return False
            tipo = self._av.get_tipo(ambiente)
            if not isinstance(tipo, TipoClasse):
                return False
            ambiente.get_def_classe(tipo.get_tipo()).get_tipo_atributo(self.get_id())
            return True
        except Exception:
            return False

    def get_tipo(self, ambiente):
        tipo = self._av.get_tipo(ambiente)
        if not isinstance(tipo, TipoClasse):
            raise ErroTipoException("A expressão à esquerda não possui tipo de classe.")
        return ambiente.get_def_classe(tipo.get_tipo()).get_tipo_atributo(self.get_id())

    def get_av(self):
        return self._av
