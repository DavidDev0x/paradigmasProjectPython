from abc import abstractmethod
from .LeftExpression import LeftExpression


class AcessoAtributo(LeftExpression):
    def __init__(self, identificador):
        self._id = identificador

    def get_id(self):
        return self._id

    @abstractmethod
    def get_expressao_objeto(self):
        raise NotImplementedError
