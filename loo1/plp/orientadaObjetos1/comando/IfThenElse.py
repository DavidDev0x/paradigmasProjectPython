from .Comando import Comando
from loo1.plp.orientadaObjetos1.expressao.valor.ValorBooleano import ValorBooleano
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class IfThenElse(Comando):
    def __init__(self, expressao, comando_then, comando_else):
        self._expressao = expressao
        self._comando_then = comando_then
        self._comando_else = comando_else

    def executar(self, ambiente):
        condicao = self._expressao.avaliar(ambiente)
        if not isinstance(condicao, ValorBooleano):
            raise ErroTipoException("A condição do if deve ser booleana.")
        comando = self._comando_then if condicao.valor() else self._comando_else
        return comando.executar(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        return (
            self._expressao.checa_tipo(ambiente)
            and self._expressao.get_tipo(ambiente) == TipoPrimitivo.TIPO_BOOLEANO
            and self._comando_then.checa_tipo(ambiente)
            and self._comando_else.checa_tipo(ambiente)
        )
