from __future__ import annotations
from typing import Generic, TypeVar
T = TypeVar('T')

class Lista(Generic[T]):
    def __init__(self, valor: T | None = None, lista: 'Lista[T] | None' = None) -> None:
        self.head = valor
        self.tail = lista

    def length(self) -> int:
        if self.head is None:
            return 0
        if self.tail is None:
            return 1
        return 1 + self.tail.length()

    def get_head(self) -> T | None:
        return self.head

    def get_tail(self) -> 'Lista[T] | None':
        return self.tail

    def __iter__(self):
        atual: Lista[T] | None = self
        while atual is not None and atual.head is not None:
            yield atual.head
            atual = atual.tail

    def __str__(self) -> str:
        return ' '.join(str(item) for item in self)
