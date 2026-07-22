from .Contexto import Contexto
from .AmbienteExecucao import AmbienteExecucao


class ContextoExecucao(Contexto, AmbienteExecucao):
    def clone(self) -> "ContextoExecucao":
        retorno = ContextoExecucao()
        consolidado: dict = {}
        for escopo in self._pilha:
            consolidado.update(escopo)
        retorno.set_pilha([consolidado])
        return retorno
