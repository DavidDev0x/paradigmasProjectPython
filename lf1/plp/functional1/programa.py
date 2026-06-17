from __future__ import annotations

from lf1.plp.expressions2.expression.expressao import Expressao
from lf1.plp.expressions2.expression.valor import Valor
from lf1.plp.expressions2.memory.contexto_compilacao import ContextoCompilacao
from lf1.plp.functional1.memory.contexto_execucao_funcional import ContextoExecucaoFuncional


class Programa:
    def __init__(self, exp: Expressao) -> None:
        self._exp = exp

    def executar(self) -> Valor:
        amb_exec = ContextoExecucaoFuncional()
        return self._exp.avaliar(amb_exec)

    def checa_tipo(self) -> bool:
        amb_comp = ContextoCompilacao()
        return self._exp.checa_tipo(amb_comp)

    def get_expressao(self) -> Expressao:
        return self._exp
