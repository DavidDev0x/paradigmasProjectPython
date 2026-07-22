from .Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class While(Comando):
    def __init__(self, expressao, comando):
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente):
        while True:
            condicao = self._expressao.avaliar(ambiente)
            if not isinstance(condicao, ValorBooleano):
                raise ErroTipoException("A condição do while deve ser booleana.")
            if not condicao.valor():
                return ambiente
            self._comando.executar(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        return (
            self._expressao.checa_tipo(ambiente)
            and self._expressao.get_tipo(ambiente) == TipoPrimitivo.TIPO_BOOLEANO
            and self._comando.checa_tipo(ambiente)
        )
