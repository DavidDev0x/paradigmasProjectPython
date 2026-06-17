from __future__ import annotations
from li1.plp.expressions2.expression.expressao import Expressao
from li1.plp.expressions2.expression.valor_booleano import ValorBooleano
from .comando import Comando

class While(Comando):
    def __init__(self, expressao: Expressao, comando: Comando) -> None:
        self._expressao = expressao
        self._comando = comando

    def executar(self, ambiente):
        while True:
            cond = self._expressao.avaliar(ambiente)
            if not isinstance(cond, ValorBooleano):
                raise TypeError(f'While exige condição booleana, recebeu {type(cond).__name__}.')
            if not cond.valor():
                break
            ambiente = self._comando.executar(ambiente)
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._expressao.checa_tipo(ambiente) and self._expressao.get_tipo(ambiente).e_booleano() and self._comando.checa_tipo(ambiente)
