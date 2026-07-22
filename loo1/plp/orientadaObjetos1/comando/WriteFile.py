import pickle
from .IO import IO
from loo1.plp.orientadaObjetos1.expressao.valor.ValorRef import ValorRef
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class WriteFile(IO):
    def __init__(self, identificador, dir):
        self._id = identificador
        self._dir = dir

    def executar(self, ambiente):
        caminho = str(self._dir.avaliar(ambiente))
        referencia = self._id.avaliar(ambiente)
        if not isinstance(referencia, ValorRef):
            raise ErroTipoException("WriteFile exige uma variável de objeto.")
        objeto = ambiente.get_objeto(referencia)
        with open(caminho, "ab") as arquivo:
            pickle.dump(objeto, arquivo)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._id.checa_tipo(ambiente) and self._dir.checa_tipo(ambiente) and self._dir.get_tipo(ambiente) == TipoPrimitivo.TIPO_STRING
