from abc import ABC, abstractmethod
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class Valor(Expressao, ABC):
    @abstractmethod
    def get_tipo(self, ambiente):
        raise NotImplementedError
