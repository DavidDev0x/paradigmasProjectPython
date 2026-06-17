from __future__ import annotations
from li1.plp.expressions2.expression.valor import Valor
from li1.plp.imperative1.util.lista import Lista

class ListaValor(Lista[Valor]):
    def __init__(self, valor: Valor | None = None, lista_valor: 'ListaValor | None' = None) -> None:
        if valor is None and lista_valor is None:
            super().__init__()
        else:
            super().__init__(valor, lista_valor if lista_valor is not None else ListaValor())

    def write(self, valor: Valor) -> None:
        if self.get_head() is None:
            self.head = valor
            self.tail = ListaValor()
        else:
            tail = self.get_tail()
            if not isinstance(tail, ListaValor):
                raise TypeError('Cauda de ListaValor deve ser ListaValor.')
            tail.write(valor)
