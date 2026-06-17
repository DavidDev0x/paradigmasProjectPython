from __future__ import annotations
from li1.plp.expressions2.expression.expressao import Expressao
from li1.plp.expressions2.expression.id import Id
from .comando import Comando

class Atribuicao(Comando):
    def __init__(self, id: Id, expressao: Expressao) -> None:
        self._id = id
        self._expressao = expressao

    def executar(self, ambiente):
        ambiente.change_valor(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._expressao.checa_tipo(ambiente) and self._id.get_tipo(ambiente).e_igual(self._expressao.get_tipo(ambiente))
