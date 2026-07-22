from abc import ABC
from loo1.plp.orientadaObjetos1.expressao.Expressao import Expressao


class ExpUnaria(Expressao, ABC):
    def __init__(self, exp: Expressao, operador: str):
        self._exp = exp
        self._operador = operador

    def get_exp(self) -> Expressao:
        return self._exp

    def get_operador(self) -> str:
        return self._operador

    def checa_tipo(self, ambiente) -> bool:
        return self._exp.checa_tipo(ambiente)
