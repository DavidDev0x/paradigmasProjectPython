from li2.plp.imperative1.declaration.declaracao import Declaracao


class DeclaracaoComposta(Declaracao):
    def __init__(self, declaracao1, declaracao2) -> None:
        self._declaracao1 = declaracao1
        self._declaracao2 = declaracao2

    def elabora(self, ambiente):
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checa_tipo(self, ambiente) -> bool:
        return self._declaracao1.checa_tipo(ambiente) and self._declaracao2.checa_tipo(ambiente)
