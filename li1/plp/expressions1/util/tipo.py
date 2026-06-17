from __future__ import annotations
from abc import ABC, abstractmethod

class Tipo(ABC):
    """Interface que representa os tipos de expressões da linguagem LI1."""

    @abstractmethod
    def get_nome(self) -> str: ...

    @abstractmethod
    def e_inteiro(self) -> bool: ...

    @abstractmethod
    def e_booleano(self) -> bool: ...

    @abstractmethod
    def e_string(self) -> bool: ...

    @abstractmethod
    def e_igual(self, tipo: 'Tipo') -> bool: ...

    @abstractmethod
    def e_valido(self) -> bool: ...

    @abstractmethod
    def intersecao(self, outro_tipo: 'Tipo') -> 'Tipo | None': ...
