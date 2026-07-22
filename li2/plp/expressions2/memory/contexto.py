from li2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from li2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException


class Contexto:
    """Contexto léxico/dinâmico implementado como list[dict]."""

    def __init__(self) -> None:
        self._pilha: list[dict] = []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError("Não existe bloco de contexto para restaurar.")
        self._pilha.pop()

    def map(self, id_arg, valor_id) -> None:
        if not self._pilha:
            raise RuntimeError("Não existe bloco ativo para realizar o mapeamento.")
        bloco_atual = self._pilha[-1]
        if id_arg in bloco_atual:
            raise VariavelJaDeclaradaException(id_arg)
        bloco_atual[id_arg] = valor_id

    def get(self, id_arg):
        for bloco in reversed(self._pilha):
            if id_arg in bloco:
                return bloco[id_arg]
        raise VariavelNaoDeclaradaException(id_arg)

    def get_pilha(self) -> list[dict]:
        return self._pilha

    def set_pilha(self, pilha: list[dict]) -> None:
        self._pilha = pilha
