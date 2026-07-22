from enum import Enum

from li2.plp.expressions1.util.tipo import Tipo


class TipoPrimitivo(Enum):
    INTEIRO = "INTEIRO"
    BOOLEANO = "BOOLEANO"
    STRING = "STRING"

    def get_nome(self) -> str:
        return self.value

    def e_inteiro(self) -> bool:
        return self is TipoPrimitivo.INTEIRO

    def e_booleano(self) -> bool:
        return self is TipoPrimitivo.BOOLEANO

    def e_string(self) -> bool:
        return self is TipoPrimitivo.STRING

    def e_igual(self, tipo: Tipo) -> bool:
        if not isinstance(tipo, Tipo):
            return False
        if self.e_valido() and tipo.e_valido():
            return self.get_nome() == tipo.get_nome()
        return tipo.e_igual(self)

    def e_valido(self) -> bool:
        return bool(self.value)

    def intersecao(self, outro_tipo: Tipo) -> "TipoPrimitivo | None":
        return self if outro_tipo.e_igual(self) else None

    def __str__(self) -> str:
        return self.value


Tipo.register(TipoPrimitivo)
