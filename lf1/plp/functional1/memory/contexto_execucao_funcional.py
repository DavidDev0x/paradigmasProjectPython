from __future__ import annotations

from typing import Any

from lf1.plp.expressions2.memory.contexto import Contexto
from lf1.plp.expressions2.memory.contexto_execucao import ContextoExecucao
from lf1.plp.functional1.memory.ambiente_execucao_funcional import AmbienteExecucaoFuncional


class ContextoExecucaoFuncional(AmbienteExecucaoFuncional):
    def __init__(self, pilha_funcao: list[dict[Any, Any]] | None = None,
                 pilha_id_valor: ContextoExecucao | None = None,
                 pilha_id_valor_func: Contexto | None = None) -> None:
        self._pilha_funcao = pilha_funcao if pilha_funcao is not None else []
        self._pilha_id_valor = pilha_id_valor if pilha_id_valor is not None else ContextoExecucao()
        self._pilha_id_valor_func = pilha_id_valor_func if pilha_id_valor_func is not None else Contexto(self._pilha_funcao)

    def incrementa(self) -> None:
        self._pilha_id_valor.incrementa()
        self._pilha_funcao.append({})

    def restaura(self) -> None:
        self._pilha_id_valor.restaura()
        if not self._pilha_funcao:
            raise RuntimeError("Não há escopo funcional para restaurar.")
        self._pilha_funcao.pop()

    def map_funcao(self, id_arg: Any, funcao: Any) -> None:
        self._pilha_id_valor_func.map(id_arg, funcao)

    def get_funcao(self, id_arg: Any) -> Any:
        return self._pilha_id_valor_func.get(id_arg)

    def get(self, id_arg: Any) -> Any:
        return self._pilha_id_valor.get(id_arg)

    def map(self, id_arg: Any, tipo_id: Any) -> None:
        self._pilha_id_valor.map(id_arg, tipo_id)

    def get_pilha_funcao(self) -> list[dict[Any, Any]]:
        return self._pilha_funcao

    def get_pilha_id_valor(self) -> ContextoExecucao:
        return self._pilha_id_valor

    def get_pilha_id_valor_func(self) -> Contexto:
        return self._pilha_id_valor_func
