from le2.plp.expressions2.expression.expressao import Expressao
from le2.plp.expressions2.expression.valor import Valor
from le2.plp.expressions2.memory.contexto_compilacao import ContextoCompilacao
from le2.plp.expressions2.memory.contexto_execucao import ContextoExecucao


class Programa:
    def __init__(self, exp: Expressao) -> None:
        if not isinstance(exp, Expressao):
            raise TypeError("Programa exige uma Expressao.")
        self._exp = exp

    def executar(self) -> Valor:
        amb_exec = ContextoExecucao()
        return self._exp.avaliar(amb_exec)

    def checa_tipo(self) -> bool:
        amb_comp = ContextoCompilacao()
        return self._exp.checa_tipo(amb_comp)

    def get_expressao(self) -> Expressao:
        return self._exp
