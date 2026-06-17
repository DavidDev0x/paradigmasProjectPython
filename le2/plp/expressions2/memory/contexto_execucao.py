from __future__ import annotations

from le2.plp.expressions2.memory.ambiente_execucao import AmbienteExecucao
from le2.plp.expressions2.memory.contexto import Contexto


class ContextoExecucao(Contexto, AmbienteExecucao):
    def clone(self) -> ContextoExecucao:
        retorno = ContextoExecucao()
        novo_mapa: dict[object, object] = {}
        for mapa in self._pilha:
            for chave, valor in mapa.items():
                novo_mapa[chave] = valor
        retorno.set_pilha([novo_mapa])
        return retorno
