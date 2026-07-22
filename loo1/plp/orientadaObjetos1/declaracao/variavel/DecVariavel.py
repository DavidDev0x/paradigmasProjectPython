from abc import abstractmethod
from loo1.plp.orientadaObjetos1.declaracao.Declaracao import Declaracao


class DecVariavel(Declaracao):
    @abstractmethod
    def get_tipo(self, identificador):
        raise NotImplementedError
