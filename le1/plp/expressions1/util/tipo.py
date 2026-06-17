from __future__ import annotations

from enum import Enum, auto
from typing import Optional, FrozenSet, Set


class Tipos(Enum):
    INTEIRO = auto()
    BOOLEANO = auto()
    STRING = auto()
    PID = auto()
    TUPLA = auto()


class Tipo:
    """Representa os tipos possíveis de uma expressão da LE1.

    A implementação preserva a ideia do Java: um Tipo guarda um conjunto de
    possibilidades e, opcionalmente, um próximo Tipo para representar funções.
    """

    TIPO_INTEIRO: "Tipo"
    TIPO_BOOLEANO: "Tipo"
    TIPO_STRING: "Tipo"
    TIPO_PID: "Tipo"
    TIPO_TUPLA: "Tipo"
    TIPO_INDEFINIDO: "Tipo"

    def __init__(self, tipo: Optional[Set[Tipos]] = None, prox: Optional["Tipo"] = None) -> None:
        self._tipo: Set[Tipos] = set(Tipos) if tipo is None else set(tipo)
        self._prox: Optional[Tipo] = prox

    def get(self) -> FrozenSet[Tipos]:
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

    def intersecao(self, outro_tipo: "Tipo") -> "Tipo":
        if not isinstance(outro_tipo, Tipo):
            raise TypeError("intersecao espera um objeto Tipo")
        if self._tipo == outro_tipo._tipo:
            return self
        return Tipo(self._tipo.intersection(outro_tipo._tipo))

    def get_prox(self) -> Optional["Tipo"]:
        return self._prox

    def set_prox(self, novo_prox: Optional["Tipo"]) -> None:
        if novo_prox is not None and not isinstance(novo_prox, Tipo):
            raise TypeError("novo_prox deve ser Tipo ou None")
        self._prox = novo_prox

    def e_valido(self) -> bool:
        return len(self._tipo) == 1

    def __eq__(self, obj: object) -> bool:
        return isinstance(obj, Tipo) and obj._tipo == self._tipo

    def __hash__(self) -> int:
        return hash(frozenset(self._tipo))

    def __str__(self) -> str:
        if self.e_void():
            return "INDEFINIDO"
        return "|".join(sorted(tipo.name for tipo in self._tipo))


Tipo.TIPO_INTEIRO = Tipo({Tipos.INTEIRO})
Tipo.TIPO_BOOLEANO = Tipo({Tipos.BOOLEANO})
Tipo.TIPO_STRING = Tipo({Tipos.STRING})
Tipo.TIPO_PID = Tipo({Tipos.PID})
Tipo.TIPO_TUPLA = Tipo({Tipos.TUPLA})
Tipo.TIPO_INDEFINIDO = Tipo(set())
