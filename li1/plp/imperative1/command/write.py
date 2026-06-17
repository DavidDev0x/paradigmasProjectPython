from __future__ import annotations
from li1.plp.expressions2.expression.expressao import Expressao
from .io import IO

class Write(IO):
    def __init__(self, expressao: Expressao) -> None:
        self._expressao = expressao

    def executar(self, ambiente):
        ambiente.write(self._expressao.avaliar(ambiente))
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._expressao.checa_tipo(ambiente)
