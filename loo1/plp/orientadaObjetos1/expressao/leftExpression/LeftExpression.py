from abc import ABC, abstractmethod
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class LeftExpression(Expressao, ABC):
    @abstractmethod
    def get_id(self):
        raise NotImplementedError
