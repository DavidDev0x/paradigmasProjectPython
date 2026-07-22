from .DecVariavel import DecVariavel
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse


class SimplesDecVariavel(DecVariavel):
    def __init__(self, tipo, identificador, expressao):
        self._tipo = tipo
        self._id = identificador
        self._expressao = expressao

    def get_tipo(self, identificador):
        if self._id == identificador:
            return self._tipo
        raise VariavelNaoDeclaradaException(identificador)

    def elabora(self, ambiente):
        ambiente.map(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        if not self._expressao.checa_tipo(ambiente):
            return False
        tipo_exp = self._expressao.get_tipo(ambiente)
        resposta = tipo_exp == self._tipo
        if isinstance(self._tipo, TipoClasse):
            resposta = resposta or tipo_exp == TipoClasse.TIPO_NULL
        if resposta:
            ambiente.map(self._id, self._tipo)
        return resposta
