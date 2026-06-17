from __future__ import annotations
from li1.plp.expressions2.expression.expressao import Expressao
from li1.plp.expressions2.expression.valor_booleano import ValorBooleano
from .comando import Comando

class IfThenElse(Comando):
    def __init__(self, expressao: Expressao, comando_then: Comando, comando_else: Comando) -> None:
        self._expressao = expressao
        self._comando_then = comando_then
        self._comando_else = comando_else

    def executar(self, ambiente):
        cond = self._expressao.avaliar(ambiente)
        if not isinstance(cond, ValorBooleano):
            raise TypeError(f'IfThenElse exige condição booleana, recebeu {type(cond).__name__}.')
        return self._comando_then.executar(ambiente) if cond.valor() else self._comando_else.executar(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        return (self._expressao.checa_tipo(ambiente)
                and self._expressao.get_tipo(ambiente).e_booleano()
                and self._comando_then.checa_tipo(ambiente)
                and self._comando_else.checa_tipo(ambiente))
