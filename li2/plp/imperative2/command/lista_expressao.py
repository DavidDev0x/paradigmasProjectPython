from li2.plp.imperative1.memory.lista_valor import ListaValor
from li2.plp.imperative1.util.lista import Lista


class ListaExpressao(Lista):
    def __init__(self, expressao=None, lista_expressao=None) -> None:
        if expressao is None:
            super().__init__()
        elif lista_expressao is None:
            super().__init__(expressao, ListaExpressao())
        else:
            super().__init__(expressao, lista_expressao)

    def avaliar(self, ambiente) -> ListaValor:
        return ListaValor.from_iterable(expressao.avaliar(ambiente) for expressao in self)

    def get_tipos(self, ambiente) -> list:
        return [expressao.get_tipo(ambiente) for expressao in self]
