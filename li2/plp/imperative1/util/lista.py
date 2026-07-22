class Lista:
    def __init__(self, valor=None, lista=None) -> None:
        self._head = valor
        self._tail = lista

    def length(self) -> int:
        if self._head is None:
            return 0
        if self._tail is None:
            return 1
        return 1 + self._tail.length()

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def __iter__(self):
        atual = self
        while atual is not None and atual.get_head() is not None:
            yield atual.get_head()
            atual = atual.get_tail()

    def __str__(self) -> str:
        return " ".join(str(item) for item in self)
