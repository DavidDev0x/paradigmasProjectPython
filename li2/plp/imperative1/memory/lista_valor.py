from li2.plp.imperative1.util.lista import Lista


class ListaValor(Lista):
    def __init__(self, valor=None, lista_valor=None) -> None:
        if valor is None:
            super().__init__()
        elif lista_valor is None:
            super().__init__(valor, ListaValor())
        else:
            super().__init__(valor, lista_valor)

    def write(self, valor) -> None:
        if self._head is None:
            self._head = valor
            self._tail = ListaValor()
        else:
            if self._tail is None:
                self._tail = ListaValor()
            self._tail.write(valor)

    @classmethod
    def from_iterable(cls, valores):
        resultado = cls()
        for valor in valores:
            resultado.write(valor)
        return resultado

    def to_list(self) -> list:
        return list(self)
