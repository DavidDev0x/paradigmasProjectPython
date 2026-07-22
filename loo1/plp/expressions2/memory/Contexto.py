from copy import copy
from .VariavelJaDeclaradaException import VariavelJaDeclaradaException
from .VariavelNaoDeclaradaException import VariavelNaoDeclaradaException


class Contexto:
    def __init__(self):
        self._pilha: list[dict] = []

    def incrementa(self) -> None:
        self._pilha.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError("Não há escopo para restaurar.")
        self._pilha.pop()

    def map(self, identificador, valor) -> None:
        if not self._pilha:
            raise RuntimeError("É necessário criar um escopo antes de mapear.")
        atual = self._pilha[-1]
        if identificador in atual:
            raise VariavelJaDeclaradaException(identificador)
        atual[identificador] = valor

    def get(self, identificador):
        for escopo in reversed(self._pilha):
            if identificador in escopo and escopo[identificador] is not None:
                return escopo[identificador]
        raise VariavelNaoDeclaradaException(identificador)

    def get_pilha(self) -> list[dict]:
        return self._pilha

    def set_pilha(self, pilha: list[dict]) -> None:
        self._pilha = pilha
