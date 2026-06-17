from __future__ import annotations

from le2.plp.expressions2.expression.id import Id
from le2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from le2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException


class Contexto:
    """Contexto de execução/compilação baseado em pilha de dicionários.

    Adaptação de ``Stack<HashMap<Id,T>>`` para ``list[dict[Id, object]]``.
    """

    def __init__(self) -> None:
        self._pilha: list[dict[Id, object]] = []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError("Não há bloco de contexto para restaurar.")
        self._pilha.pop()

    def map(self, id_arg: Id, valor_id: object) -> None:
        if not isinstance(id_arg, Id):
            raise TypeError("id_arg deve ser Id.")
        if not self._pilha:
            self.incrementa()
        topo = self._pilha[-1]
        if id_arg in topo:
            raise VariavelJaDeclaradaException(id_arg)
        topo[id_arg] = valor_id

    def get(self, id_arg: Id) -> object:
        if not isinstance(id_arg, Id):
            raise TypeError("id_arg deve ser Id.")
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                return bloco[id_arg]
        raise VariavelNaoDeclaradaException(id_arg)

    def get_pilha(self) -> list[dict[Id, object]]:
        return self._pilha

    def set_pilha(self, pilha: list[dict[Id, object]]) -> None:
        self._pilha = pilha
