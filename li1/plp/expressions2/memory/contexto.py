from __future__ import annotations
from typing import Any
from .ambiente import Ambiente
from .variavel_ja_declarada_exception import VariavelJaDeclaradaException
from .variavel_nao_declarada_exception import VariavelNaoDeclaradaException

class Contexto(Ambiente):
    """Contexto em pilha: list[dict], equivalente a Stack<HashMap<Id,T>>."""

    def __init__(self) -> None:
        self._pilha: list[dict[Any, Any]] = []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError('Não há bloco de contexto para restaurar.')
        self._pilha.pop()

    def map(self, id_arg: Any, valor_id: Any) -> None:
        if not self._pilha:
            raise RuntimeError('Não há bloco de contexto ativo para mapear identificador.')
        topo = self._pilha[-1]
        if id_arg in topo:
            raise VariavelJaDeclaradaException(id_arg)
        topo[id_arg] = valor_id

    def get(self, id_arg: Any) -> Any:
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                return bloco[id_arg]
        raise VariavelNaoDeclaradaException(id_arg)

    def get_pilha(self) -> list[dict[Any, Any]]:
        return self._pilha

    def set_pilha(self, pilha: list[dict[Any, Any]]) -> None:
        self._pilha = pilha
