from li2.plp.expressions2.expression._type_checks import exigir_tipo
from li2.plp.expressions2.expression.valor_booleano import ValorBooleano
from li2.plp.imperative1.command.comando import Comando


class IfThenElse(Comando):
    def __init__(self, expressao, comando_then, comando_else) -> None:
        self._expressao = expressao
        self._comando_then = comando_then
        self._comando_else = comando_else

    def executar(self, ambiente):
        condicao = exigir_tipo(self._expressao.avaliar(ambiente), ValorBooleano, "if")
        if condicao.valor():
            return self._comando_then.executar(ambiente)
        return self._comando_else.executar(ambiente)

    def checa_tipo(self, ambiente) -> bool:
        return (
            self._expressao.checa_tipo(ambiente)
            and self._expressao.get_tipo(ambiente).e_booleano()
            and self._comando_then.checa_tipo(ambiente)
            and self._comando_else.checa_tipo(ambiente)
        )
