from loo1.plp.imperative1.util.Lista import Lista


class ListaValor(Lista):
    def __init__(self, valor=None, lista_valor=None):
        if valor is None:
            super().__init__()
        elif lista_valor is None:
            super().__init__(valor, ListaValor())
        else:
            super().__init__(valor, lista_valor)

    def write(self, valor) -> None:
        if self.get_head() is None:
            self._head = valor
            self._tail = ListaValor()
        else:
            self.get_tail().write(valor)

    def to_list(self) -> list:
        return list(self)
