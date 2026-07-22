from abc import ABC, abstractmethod


class Tipo(ABC):
    @abstractmethod
    def get_tipo(self):
        raise NotImplementedError

    @abstractmethod
    def e_valido(self, ambiente) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, outro: object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError
