from __future__ import annotations

from typing import Any

from lf1.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from lf1.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException


class Contexto:
    """Pilha de escopos implementada como list[dict], preservando o Stack<HashMap> Java."""

    def __init__(self, pilha: list[dict[Any, Any]] | None = None) -> None:
        self._pilha: list[dict[Any, Any]] = pilha if pilha is not None else []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError("Não há escopo para restaurar.")
        self._pilha.pop()

    def map(self, id_arg: Any, valor_id: Any) -> None:
        if not self._pilha:
            raise RuntimeError("Não há escopo ativo para mapear identificador.")
        topo = self._pilha[-1]
        if id_arg in topo:
            raise VariavelJaDeclaradaException(id_arg)
        topo[id_arg] = valor_id

    def get(self, id_arg: Any) -> Any:
        for escopo in reversed(self._pilha):
            if id_arg in escopo:
                return escopo[id_arg]
        raise VariavelNaoDeclaradaException(id_arg)

    def get_pilha(self) -> list[dict[Any, Any]]:
        return self._pilha

    def set_pilha(self, pilha: list[dict[Any, Any]]) -> None:
        self._pilha = pilha

    def clone(self) -> "Contexto":
        return Contexto([dict(escopo) for escopo in self._pilha])
