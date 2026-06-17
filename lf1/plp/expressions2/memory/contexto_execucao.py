from lf1.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao
from lf1.plp.expressions2.memory.contexto import Contexto


class ContextoExecucao(Contexto, AmbienteExecucao):
    def clone(self) -> "ContextoExecucao":
        ret = ContextoExecucao()
        ret.set_pilha([dict(escopo) for escopo in self.get_pilha()])
        return ret
