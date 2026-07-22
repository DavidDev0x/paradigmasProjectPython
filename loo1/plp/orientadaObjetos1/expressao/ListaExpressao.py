from loo1.plp.imperative1.util.Lista import Lista
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.util.ListaTipo import ListaTipo


class ListaExpressao(Lista):
    def __init__(self, expressao=None, lista_expressao=None):
        if expressao is None:
            super().__init__()
        elif lista_expressao is None:
            super().__init__(expressao, ListaExpressao())
        else:
            super().__init__(expressao, lista_expressao)

    def avaliar(self, ambiente) -> ListaValor:
        if self.length() >= 2:
            return ListaValor(self.get_head().avaliar(ambiente), self.get_tail().avaliar(ambiente))
        if self.length() == 1:
            return ListaValor(self.get_head().avaliar(ambiente))
        return ListaValor()

    def get_tipos(self, ambiente) -> ListaTipo:
        if self.length() >= 2:
            return ListaTipo(self.get_head().get_tipo(ambiente), self.get_tail().get_tipos(ambiente))
        if self.length() == 1:
            return ListaTipo(self.get_head().get_tipo(ambiente))
        return ListaTipo()
