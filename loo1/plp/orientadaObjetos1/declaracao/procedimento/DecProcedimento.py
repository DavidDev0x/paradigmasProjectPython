from abc import ABC, abstractmethod


class DecProcedimento(ABC):
    @abstractmethod
    def get_procedimento(self, nome_procedimento):
        raise NotImplementedError

    @abstractmethod
    def checa_tipo(self, ambiente) -> bool:
        raise NotImplementedError
