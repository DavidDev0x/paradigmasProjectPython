from __future__ import annotations
from .declaracao import Declaracao

class DeclaracaoComposta(Declaracao):
    def __init__(self, parametro1: Declaracao, parametro2: Declaracao) -> None:
        self._declaracao1 = parametro1
        self._declaracao2 = parametro2

    def elabora(self, ambiente):
        return self._declaracao2.elabora(self._declaracao1.elabora(ambiente))

    def checa_tipo(self, ambiente) -> bool:
        return self._declaracao1.checa_tipo(ambiente) and self._declaracao2.checa_tipo(ambiente)
