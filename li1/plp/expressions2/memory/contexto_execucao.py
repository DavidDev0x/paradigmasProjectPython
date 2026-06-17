from __future__ import annotations
from .ambiente_execucao import AmbienteExecucao
from .contexto import Contexto

class ContextoExecucao(Contexto, AmbienteExecucao):
    """Contexto de execução: armazena valores."""

    def clone(self) -> 'ContextoExecucao':
        retorno = ContextoExecucao()
        novo_mapa: dict[object, object] = {}
        for bloco in self.get_pilha():
            novo_mapa.update(bloco)
        retorno.set_pilha([novo_mapa])
        return retorno
