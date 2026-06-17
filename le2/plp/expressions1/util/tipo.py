from __future__ import annotations

from enum import Enum, auto
from typing import Iterable


class Tipos(Enum):
    INTEIRO = auto()
    BOOLEANO = auto()
    STRING = auto()
    PID = auto()
    TUPLA = auto()


class Tipo:
    """Representa os tipos possíveis de uma expressão da linguagem LE2.

    Conversão direta da classe Java ``Tipo``. O ``EnumSet`` foi adaptado para
    ``set``/``frozenset`` nativo do Python.
    """

    def __init__(self, tipo: Iterable[Tipos] | Tipo | None = None, prox: Tipo | None = None) -> None:
        if isinstance(tipo, Tipo) and prox is None:
            prox = tipo
            tipos = set(Tipos)
        elif tipo is None:
            tipos = set(Tipos)
        else:
            tipos = set(tipo)

        for item in tipos:
            if not isinstance(item, Tipos):
                raise TypeError("Tipo aceita apenas elementos da enumeração Tipos.")

        self._tipo: frozenset[Tipos] = frozenset(tipos)
        self._prox: Tipo | None = prox

    def get(self) -> frozenset[Tipos]:
        return self._tipo

    def e_inteiro(self) -> bool:
        return Tipos.INTEIRO in self._tipo

    def e_booleano(self) -> bool:
        return Tipos.BOOLEANO in self._tipo

    def e_string(self) -> bool:
        return Tipos.STRING in self._tipo

    def e_pid(self) -> bool:
        return Tipos.PID in self._tipo

    def e_tupla(self) -> bool:
        return Tipos.TUPLA in self._tipo

    def e_void(self) -> bool:
        return len(self._tipo) == 0

    def intersecao(self, outro_tipo: Tipo) -> Tipo:
        if not isinstance(outro_tipo, Tipo):
            raise TypeError("intersecao espera outro objeto Tipo.")
        if self._tipo == outro_tipo._tipo:
            return self
        return Tipo(self._tipo.intersection(outro_tipo._tipo))

    def get_prox(self) -> Tipo | None:
        return self._prox

    def set_prox(self, novo_prox: Tipo | None) -> None:
        if novo_prox is not None and not isinstance(novo_prox, Tipo):
            raise TypeError("novo_prox deve ser Tipo ou None.")
        self._prox = novo_prox

    def e_valido(self) -> bool:
        return len(self._tipo) == 1

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, Tipo) and obj._tipo == self._tipo

    def __hash__(self) -> int:
        return hash(self._tipo)

    def __repr__(self) -> str:
        if self.e_void():
            return "Tipo({})"
        nomes = ", ".join(sorted(t.name for t in self._tipo))
        return f"Tipo({{{nomes}}})"


Tipo.TIPO_INTEIRO = Tipo({Tipos.INTEIRO})
Tipo.TIPO_BOOLEANO = Tipo({Tipos.BOOLEANO})
Tipo.TIPO_STRING = Tipo({Tipos.STRING})
Tipo.TIPO_PID = Tipo({Tipos.PID})
Tipo.TIPO_TUPLA = Tipo({Tipos.TUPLA})
Tipo.TIPO_INDEFINIDO = Tipo(set())
