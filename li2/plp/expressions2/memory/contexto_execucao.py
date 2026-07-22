from li2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao
from li2.plp.expressions2.memory.contexto import Contexto


class ContextoExecucao(Contexto, AmbienteExecucao):
    def clone(self) -> "ContextoExecucao":
        retorno = ContextoExecucao()
        consolidado = {}
        for bloco in self._pilha:
            consolidado.update(bloco)
        retorno.set_pilha([consolidado])
        return retorno
