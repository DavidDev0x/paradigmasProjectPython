from abc import ABC, abstractmethod


class Ambiente(ABC):
    @abstractmethod
    def incrementa(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def restaura(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def map(self, id_arg, valor_id) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id_arg):
        raise NotImplementedError
