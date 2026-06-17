from __future__ import annotations
from li1.plp.expressions2.expression.expressao import Expressao
from li1.plp.expressions2.expression.id import Id
from .declaracao import Declaracao

class DeclaracaoVariavel(Declaracao):
    def __init__(self, id: Id, expressao: Expressao) -> None:
        self._id = id
        self._expressao = expressao

    def elabora(self, ambiente):
        ambiente.map(self.get_id(), self.get_expressao().avaliar(ambiente))
        return ambiente

    def get_expressao(self) -> Expressao:
        return self._expressao

    def get_id(self) -> Id:
        return self._id

    def checa_tipo(self, ambiente) -> bool:
        result = self.get_expressao().checa_tipo(ambiente)
        if result:
            ambiente.map(self.get_id(), self.get_expressao().get_tipo(ambiente))
        return result
