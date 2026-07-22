from li2.plp.imperative1.util.lista import Lista


class ListaDeclaracaoParametro(Lista):
    def __init__(self, declaracao=None, lista_declaracao=None) -> None:
        if declaracao is None:
            super().__init__()
        else:
            super().__init__(declaracao, lista_declaracao)

    def checa_tipo(self, ambiente) -> bool:
        return all(declaracao.checa_tipo(ambiente) for declaracao in self)

    def elabora(self, ambiente):
        for declaracao in self:
            ambiente = declaracao.elabora(ambiente)
        return ambiente

    def get_tipos(self) -> list:
        return [declaracao.get_tipo() for declaracao in self]
