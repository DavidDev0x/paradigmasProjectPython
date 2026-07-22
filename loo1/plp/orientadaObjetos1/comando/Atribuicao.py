from .Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributo import AcessoAtributo
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class Atribuicao(Comando):
    def __init__(self, av, expressao):
        self._av = av
        self._expressao = expressao

    def executar(self, ambiente):
        valor = self._expressao.avaliar(ambiente)
        if isinstance(self._av, AcessoAtributo):
            referencia = self._av.get_expressao_objeto().avaliar(ambiente)
            if not isinstance(referencia, ValorRef):
                raise ErroTipoException("Atribuição de atributo exige referência de objeto.")
            ambiente.get_objeto(referencia).change_atributo(self._av.get_id(), valor)
        else:
            ambiente.change_valor(self._av.get_id(), valor)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        if not self._expressao.checa_tipo(ambiente):
            return False
        tipo_destino = self._av.get_tipo(ambiente)
        tipo_origem = self._expressao.get_tipo(ambiente)
        return tipo_destino == tipo_origem or tipo_origem == TipoClasse.TIPO_NULL
