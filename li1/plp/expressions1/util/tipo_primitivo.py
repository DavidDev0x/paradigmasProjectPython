from __future__ import annotations
from enum import Enum
from .tipo import Tipo

class TipoPrimitivo(Enum):
    INTEIRO = 'INTEIRO'
    BOOLEANO = 'BOOLEANO'
    STRING = 'STRING'

    def get_nome(self) -> str:
        return self.value

    def e_inteiro(self) -> bool:
        return self.e_igual(TipoPrimitivo.INTEIRO)

    def e_booleano(self) -> bool:
        return self.e_igual(TipoPrimitivo.BOOLEANO)

    def e_string(self) -> bool:
        return self.e_igual(TipoPrimitivo.STRING)

    def e_igual(self, tipo: Tipo) -> bool:
        if self.e_valido():
            if tipo.e_valido():
                return self.get_nome() == tipo.get_nome()
            return tipo.e_igual(self)
        return False

    def e_valido(self) -> bool:
        return bool(self.value)

    def intersecao(self, outro_tipo: Tipo) -> 'TipoPrimitivo | None':
        return self if outro_tipo.e_igual(self) else None

    def __str__(self) -> str:
        return self.value
