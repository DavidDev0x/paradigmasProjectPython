from abc import ABC, abstractmethod


class Tipo(ABC):
    """Interface dos tipos da linguagem de expressões."""

    @abstractmethod
    def get_nome(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def e_inteiro(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def e_booleano(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def e_string(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def e_igual(self, tipo: "Tipo") -> bool:
        raise NotImplementedError

    @abstractmethod
    def e_valido(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def intersecao(self, outro_tipo: "Tipo") -> "Tipo | None":
        raise NotImplementedError
