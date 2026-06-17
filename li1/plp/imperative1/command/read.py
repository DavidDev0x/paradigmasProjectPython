from __future__ import annotations
from li1.plp.expressions2.expression.id import Id
from .io import IO
from li1.plp.imperative1.memory.erro_tipo_entrada_exception import ErroTipoEntradaException

class Read(IO):
    def __init__(self, id: Id) -> None:
        self._id = id

    def executar(self, ambiente):
        valor_id = ambiente.get(self._id)
        valor_read = ambiente.read()
        if valor_id.get_tipo(None).e_igual(valor_read.get_tipo(None)):
            ambiente.change_valor(self._id, valor_read)
        else:
            raise ErroTipoEntradaException(f'Tipo do valor de entrada lido incompatível com tipo da variável ({self._id.get_id_name()})')
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return True
