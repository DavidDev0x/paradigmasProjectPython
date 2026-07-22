class ListaTipo:
    def __init__(self, tipo=None, lista_tipo=None):
        self._tipo = tipo
        self._lista_tipo = None if tipo is None else (lista_tipo if lista_tipo is not None else ListaTipo())

    def length(self) -> int:
        return 0 if self._lista_tipo is None else 1 + self._lista_tipo.length()

    def head(self):
        return self._tipo

    def tail(self):
        return self._lista_tipo

    def __iter__(self):
        atual = self
        while atual is not None and atual.head() is not None:
            yield atual.head()
            atual = atual.tail()

    def __str__(self) -> str:
        return " ".join(str(tipo) for tipo in reversed(list(self))) + (" " if self.length() else "")
