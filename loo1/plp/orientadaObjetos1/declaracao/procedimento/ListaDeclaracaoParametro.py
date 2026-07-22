from loo1.plp.imperative1.util.Lista import Lista


class ListaDeclaracaoParametro(Lista):
    def __init__(self, declaracao=None, lista_declaracao=None):
        if declaracao is None:
            super().__init__()
        elif lista_declaracao is None:
            super().__init__(declaracao, None)
        else:
            super().__init__(declaracao, lista_declaracao)

    def elabora(self, ambiente):
        if self.get_head() is None:
            return ambiente
        ambiente = self.get_head().elabora(ambiente)
        return self.get_tail().elabora(ambiente) if self.get_tail() is not None else ambiente

    def checa_tipo(self, ambiente) -> bool:
        if self.get_head() is None:
            return True
        atual = self.get_head().checa_tipo(ambiente)
        return atual and (self.get_tail().checa_tipo(ambiente) if self.get_tail() is not None else True)

    def declara_parametro(self, ambiente):
        if self.get_head() is None:
            return ambiente
        ambiente = self.get_head().declara_parametro(ambiente)
        return self.get_tail().declara_parametro(ambiente) if self.get_tail() is not None else ambiente
