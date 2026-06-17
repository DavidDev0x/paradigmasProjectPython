from __future__ import annotations

from enum import Enum, auto
from typing import Optional


class Tipos(Enum):
    INTEIRO = auto()
    BOOLEANO = auto()
    STRING = auto()
    PID = auto()
    TUPLA = auto()


class Tipo:
    """Representa tipos primitivos e tipos funcionais em cadeia.

    A cadeia segue a ideia do Java: um tipo de função Int -> Bool é um
    objeto Tipo(INTEIRO, prox=Tipo(BOOLEANO)).
    """

    TIPO_INTEIRO: "Tipo"
    TIPO_BOOLEANO: "Tipo"
    TIPO_STRING: "Tipo"
    TIPO_PID: "Tipo"
    TIPO_TUPLA: "Tipo"
    TIPO_INDEFINIDO: "Tipo"

    def __init__(self, tipo: Optional[set[Tipos] | frozenset[Tipos] | "Tipo"] = None,
                 prox: Optional["Tipo"] = None) -> None:
        if isinstance(tipo, Tipo) and prox is None:
            # Equivalente ao construtor Java Tipo(Tipo prox).
            self._tipo: set[Tipos] = set(Tipos)
            self._prox: Optional[Tipo] = tipo
        else:
            self._tipo = set(Tipos) if tipo is None else set(tipo)
            self._prox = prox

    def get(self) -> frozenset[Tipos]:
        return frozenset(self._tipo)

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

    def e_valido(self) -> bool:
        return len(self._tipo) == 1

    def intersecao(self, outro_tipo: "Tipo") -> "Tipo":
        if not isinstance(outro_tipo, Tipo):
            raise TypeError("intersecao espera um objeto Tipo")
        return Tipo(self._tipo.intersection(outro_tipo._tipo), self._prox)

    def get_prox(self) -> Optional["Tipo"]:
        return self._prox

    def set_prox(self, novo_prox: Optional["Tipo"]) -> None:
        self._prox = novo_prox

    def clone(self) -> "Tipo":
        return Tipo(set(self._tipo), self._prox.clone() if self._prox is not None else None)

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, Tipo) and obj._tipo == self._tipo and obj._prox == self._prox

    def __hash__(self) -> int:
        return hash((frozenset(self._tipo), self._prox))

    def __str__(self) -> str:
        if self.e_void():
            atual = "Void"
        elif self._tipo == set(Tipos):
            atual = "Any"
        else:
            atual = "|".join(sorted(t.name.title() for t in self._tipo))
        return atual if self._prox is None else f"{atual} -> {self._prox}"

    def __repr__(self) -> str:
        return f"Tipo({str(self)})"


Tipo.TIPO_INTEIRO = Tipo({Tipos.INTEIRO})
Tipo.TIPO_BOOLEANO = Tipo({Tipos.BOOLEANO})
Tipo.TIPO_STRING = Tipo({Tipos.STRING})
Tipo.TIPO_PID = Tipo({Tipos.PID})
Tipo.TIPO_TUPLA = Tipo({Tipos.TUPLA})
Tipo.TIPO_INDEFINIDO = Tipo(set())
