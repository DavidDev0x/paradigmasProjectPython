import pickle
from .IO import IO
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo
from loo1.plp.expressions1.excecao.ErroTipoException import ErroTipoException


class ReadFile(IO):
    def __init__(self, identificador, dir, index):
        self._id = identificador
        self._dir = dir
        self._index = index
        self._tipo_id = None

    def executar(self, ambiente):
        caminho = str(self._dir.avaliar(ambiente))
        indice = self._index.avaliar(ambiente)
        if not isinstance(indice, ValorInteiro):
            raise ErroTipoException("O índice de ReadFile deve ser inteiro.")
        objetos = []
        with open(caminho, "rb") as arquivo:
            while True:
                try:
                    objetos.append(pickle.load(arquivo))
                except EOFError:
                    break
        objeto = objetos[indice.valor()]
        referencia = ambiente.get_prox_ref()
        ambiente.map_objeto(referencia, objeto)
        ambiente.change_valor(self._id, referencia)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        self._tipo_id = self._id.get_tipo(ambiente)
        return (
            self._id.checa_tipo(ambiente)
            and self._dir.checa_tipo(ambiente)
            and self._dir.get_tipo(ambiente) == TipoPrimitivo.TIPO_STRING
            and self._index.checa_tipo(ambiente)
            and self._index.get_tipo(ambiente) == TipoPrimitivo.TIPO_INTEIRO
        )
